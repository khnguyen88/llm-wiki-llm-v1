# Document Processing Pipeline — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a three-agent document processing pipeline (pdf-processor, markdown-chunker, document-processor) with docling-serve conversion, cascading OCR, element-level sidecar metadata, auto-remediation, and approval-gated wiki ingestion.

**Architecture:** Two new agents (pdf-processor, markdown-chunker) handle conversion and segmentation independently or chained. The existing document-processor agent is extended to orchestrate the full pipeline. State passes between agents via a sidecar JSON file (`{name}.elements.json`) that tracks every table, image, and equation at element-level. Configuration uses a hybrid approach: non-sensitive settings in `scripts/config.py`, secrets in `.env`.

**Tech Stack:** Python 3.x (scripts/config.py, scripts/sidecar.py, scripts/lint.py), docling-serve (Docker REST API), arrase/OCR (CLI via Ollama + deepseek-ocr), OpenRouter API (vision model fallback), pypdf (PDF splitting), docx2pdf (DOCX normalization)

---

### Task 1: Extend config.py with tool endpoints and thresholds

**Files:**
- Modify: `scripts/config.py`

- [ ] **Step 1: Add new config keys after the existing imports and directory definitions**

Read `scripts/config.py` to find the insertion point after existing path definitions, then add:

```python
# ── Document processing pipeline ────────────────────────────────────────

# Tool endpoints (from .env or defaults)
DOCLING_URL = os.getenv("DOCLING_SERVE_URL", "http://localhost:8000")
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", None)

# Pre-processing
PDF_SPLIT_PAGE_SIZE = int(os.getenv("PDF_SPLIT_PAGE_SIZE", "25"))

# Chunking thresholds
CHUNK_MAX_WORDS = int(os.getenv("CHUNK_MAX_WORDS", "3000"))
CHUNK_TARGET_WORDS = int(os.getenv("CHUNK_TARGET_WORDS", "1500"))

# OCR cascade thresholds
DOCLING_CONFIDENCE_THRESHOLD = float(os.getenv("DOCLING_CONFIDENCE_THRESHOLD", "0.8"))
ARRASE_CONFIDENCE_FLOOR = float(os.getenv("ARRASE_CONFIDENCE_FLOOR", "0.7"))
LLM_OCR_CONFIDENCE_FLOOR = float(os.getenv("LLM_OCR_CONFIDENCE_FLOOR", "0.5"))

# Auto-remediation
MAX_AUTO_ATTEMPTS = int(os.getenv("MAX_AUTO_ATTEMPTS", "3"))
WEBSEARCH_CONFIDENCE_FLOOR = float(os.getenv("WEBSEARCH_CONFIDENCE_FLOOR", "0.6"))

# New directory
RAW_MARKDOWN_DIR = ROOT_DIR / "raw-markdown"
```

Note: `ROOT_DIR` is already defined in config.py. The `os.getenv` calls need `import os` which should already be present.

- [ ] **Step 2: Verify import of os exists**

Check that `import os` is at the top of `scripts/config.py`. If not, add it.

Run: `python -c "from scripts.config import DOCLING_URL, PDF_SPLIT_PAGE_SIZE, RAW_MARKDOWN_DIR; print(f'DOCLING_URL={DOCLING_URL}, PDF_SPLIT_PAGE_SIZE={PDF_SPLIT_PAGE_SIZE}, RAW_MARKDOWN_DIR={RAW_MARKDOWN_DIR}')"`

Expected output: `DOCLING_URL=http://localhost:8000, PDF_SPLIT_PAGE_SIZE=25, RAW_MARKDOWN_DIR=<project>\raw-markdown`

- [ ] **Step 3: Commit**

```bash
git add scripts/config.py
git commit -m "feat: add document processing pipeline config keys"
```

---

### Task 2: Create sidecar.py — element tracking contract

**Files:**
- Create: `scripts/sidecar.py`

- [ ] **Step 1: Write the sidecar module**

```python
"""
Element-level sidecar JSON for the document processing pipeline.

The sidecar is the contract between pdf-processor, markdown-chunker, and
document-processor agents. Each agent reads what the previous wrote, adds its
layer, and writes back.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from config import RAW_MARKDOWN_DIR


# ── Constants ────────────────────────────────────────────────────────────

VALID_ELEMENT_TYPES = {"table", "image", "equation", "diagram"}
VALID_ELEMENT_STATUSES = {"pending", "auto_resolved", "needs_review", "resolved_human", "error"}
VALID_PIPELINE_STAGES = {"converting", "chunking", "remediating", "review", "approved"}
VALID_OCR_METHODS = {"docling", "arrase-deepseek", "openrouter-claude", "openrouter-gemini"}
VALID_REVIEW_REASONS = {"low_confidence", "ocr_unavailable", "ambiguous", "complex_layout", "conversion_failed"}
VALID_RESOLVED_BY = {"docling_high_confidence", "llm_knowledge", "websearch", "human"}


# ── Create sidecar ───────────────────────────────────────────────────────

def create_sidecar(
    document_path: str,
    total_pages: int,
    output_dir: str | None = None,
) -> dict[str, Any]:
    """Create a new empty sidecar for a document."""
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    return {
        "document": document_path,
        "processed_date": now,
        "total_pages": total_pages,
        "elements": [],
        "pipeline_state": {
            "stage": "converting",
            "total_elements": 0,
            "resolved": 0,
            "needs_review": 0,
            "unresolved_blockers": 0,
        },
    }


# ── Sidecar path helper ──────────────────────────────────────────────────

def sidecar_path(document_path: str | Path) -> Path:
    """Derive the sidecar path from a document path.

    raw/document/my-paper.pdf → raw-markdown/my-paper.elements.json
    """
    doc = Path(document_path)
    name = doc.stem  # filename without extension
    return RAW_MARKDOWN_DIR / f"{name}.elements.json"


# ── Read / write ─────────────────────────────────────────────────────────

def load_sidecar(document_path: str | Path) -> dict[str, Any]:
    """Load an existing sidecar JSON file."""
    sp = sidecar_path(document_path)
    if not sp.exists():
        raise FileNotFoundError(f"Sidecar not found: {sp}")
    return json.loads(sp.read_text(encoding="utf-8"))


def save_sidecar(sidecar: dict[str, Any]) -> Path:
    """Save a sidecar dictionary to its JSON file."""
    doc_path = sidecar["document"]
    sp = sidecar_path(doc_path)
    RAW_MARKDOWN_DIR.mkdir(parents=True, exist_ok=True)
    sp.write_text(json.dumps(sidecar, indent=2, ensure_ascii=False), encoding="utf-8")
    return sp


# ── Element operations ───────────────────────────────────────────────────

def add_element(
    sidecar: dict[str, Any],
    type_: str,
    page: int,
    ocr_method: str,
    ocr_confidence: float,
    markdown_representation: str,
    bbox: list[int] | None = None,
) -> str:
    """Add an element to the sidecar. Returns the element ID."""
    if type_ not in VALID_ELEMENT_TYPES:
        raise ValueError(f"Invalid element type: {type_}. Must be one of {VALID_ELEMENT_TYPES}")
    if ocr_method not in VALID_OCR_METHODS:
        raise ValueError(f"Invalid OCR method: {ocr_method}. Must be one of {VALID_OCR_METHODS}")

    elem_id = f"elem-{len(sidecar['elements']) + 1:03d}"

    # Determine initial status
    if ocr_confidence >= 0.8:
        status = "auto_resolved"
        resolved_by = "docling_high_confidence"
        review_reason = None
    elif ocr_confidence >= 0.5:
        status = "pending"
        resolved_by = None
        review_reason = "low_confidence"
    else:
        status = "needs_review"
        resolved_by = None
        review_reason = "low_confidence"

    element = {
        "id": elem_id,
        "type": type_,
        "page": page,
        "ocr_method": ocr_method,
        "ocr_confidence": round(ocr_confidence, 4),
        "status": status,
        "review_reason": review_reason,
        "resolved_by": resolved_by,
        "owning_chunk": None,
        "markdown_representation": markdown_representation,
        "source_coordinates": {
            "bbox": bbox or [0, 0, 0, 0],
            "page": page,
        },
        "attempts": [],
    }
    sidecar["elements"].append(element)
    _recalc_pipeline_state(sidecar)
    return elem_id


def update_element_status(
    sidecar: dict[str, Any],
    elem_id: str,
    status: str,
    resolved_by: str | None = None,
    review_reason: str | None = None,
    markdown_representation: str | None = None,
) -> None:
    """Update an element's status and optionally its resolved_by, review_reason, and markdown."""
    if status not in VALID_ELEMENT_STATUSES:
        raise ValueError(f"Invalid status: {status}. Must be one of {VALID_ELEMENT_STATUSES}")

    for elem in sidecar["elements"]:
        if elem["id"] == elem_id:
            elem["status"] = status
            if resolved_by is not None:
                if resolved_by not in VALID_RESOLVED_BY:
                    raise ValueError(f"Invalid resolved_by: {resolved_by}. Must be one of {VALID_RESOLVED_BY}")
                elem["resolved_by"] = resolved_by
            if review_reason is not None:
                if review_reason not in VALID_REVIEW_REASONS:
                    raise ValueError(f"Invalid review_reason: {review_reason}. Must be one of {VALID_REVIEW_REASONS}")
                elem["review_reason"] = review_reason
            if markdown_representation is not None:
                elem["markdown_representation"] = markdown_representation
            _recalc_pipeline_state(sidecar)
            return
    raise ValueError(f"Element not found: {elem_id}")


def record_attempt(
    sidecar: dict[str, Any],
    elem_id: str,
    method: str,
    query: str,
    result: str,
) -> None:
    """Record a remediation attempt on an element."""
    for elem in sidecar["elements"]:
        if elem["id"] == elem_id:
            now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
            elem["attempts"].append({
                "method": method,
                "timestamp": now,
                "query": query,
                "result": result,
            })
            return
    raise ValueError(f"Element not found: {elem_id}")


def assign_elements_to_chunks(
    sidecar: dict[str, Any],
    chunk_assignments: dict[str, str],
) -> None:
    """Assign elements to their owning chunks.

    chunk_assignments maps element_id → chunk_file_path.
    """
    for elem in sidecar["elements"]:
        if elem["id"] in chunk_assignments:
            elem["owning_chunk"] = chunk_assignments[elem["id"]]
    _recalc_pipeline_state(sidecar)


def set_pipeline_stage(sidecar: dict[str, Any], stage: str) -> None:
    """Update the pipeline stage."""
    if stage not in VALID_PIPELINE_STAGES:
        raise ValueError(f"Invalid stage: {stage}. Must be one of {VALID_PIPELINE_STAGES}")
    sidecar["pipeline_state"]["stage"] = stage


def get_pending_elements(sidecar: dict[str, Any]) -> list[dict[str, Any]]:
    """Return all elements with status 'pending'."""
    return [e for e in sidecar["elements"] if e["status"] == "pending"]


def get_review_elements(sidecar: dict[str, Any]) -> list[dict[str, Any]]:
    """Return all elements needing human review."""
    return [e for e in sidecar["elements"] if e["status"] == "needs_review"]


def get_unresolved_blockers(sidecar: dict[str, Any]) -> int:
    """Count elements preventing pipeline completion."""
    return sum(1 for e in sidecar["elements"] if e["status"] in ("pending", "needs_review"))


# ── Internal helpers ─────────────────────────────────────────────────────

def _recalc_pipeline_state(sidecar: dict[str, Any]) -> None:
    """Recalculate pipeline state counts from element statuses."""
    ps = sidecar["pipeline_state"]
    elements = sidecar["elements"]
    ps["total_elements"] = len(elements)
    ps["resolved"] = sum(1 for e in elements if e["status"] in ("auto_resolved", "resolved_human"))
    ps["needs_review"] = sum(1 for e in elements if e["status"] == "needs_review")
    ps["unresolved_blockers"] = sum(1 for e in elements if e["status"] in ("pending", "needs_review", "error"))

    # If all resolved with no blockers, stage can advance past review
    if ps["unresolved_blockers"] == 0 and ps["stage"] in ("remediating", "review"):
        ps["stage"] = "approved"


# ── Validation ───────────────────────────────────────────────────────────

def validate_sidecar(sidecar: dict[str, Any]) -> list[str]:
    """Validate a sidecar structure. Returns list of error messages (empty = valid)."""
    errors = []

    # Top-level required fields
    for field in ("document", "processed_date", "total_pages", "elements", "pipeline_state"):
        if field not in sidecar:
            errors.append(f"Missing required field: {field}")

    # Pipeline state
    ps = sidecar.get("pipeline_state", {})
    if ps.get("stage") not in VALID_PIPELINE_STAGES:
        errors.append(f"Invalid pipeline stage: {ps.get('stage')}")

    # Elements
    for i, elem in enumerate(sidecar.get("elements", [])):
        prefix = f"elements[{i}]"
        if elem.get("id") is None:
            errors.append(f"{prefix}: missing id")
        if elem.get("type") not in VALID_ELEMENT_TYPES:
            errors.append(f"{prefix}: invalid type '{elem.get('type')}'")
        if elem.get("status") not in VALID_ELEMENT_STATUSES:
            errors.append(f"{prefix}: invalid status '{elem.get('status')}'")
        if elem.get("ocr_method") not in VALID_OCR_METHODS:
            errors.append(f"{prefix}: invalid ocr_method '{elem.get('ocr_method')}'")
        if not isinstance(elem.get("ocr_confidence"), (int, float)):
            errors.append(f"{prefix}: ocr_confidence must be a number")
        if elem.get("page") is None:
            errors.append(f"{prefix}: missing page")

    return errors
```

- [ ] **Step 2: Verify the module imports correctly**

Run: `python -c "from scripts.sidecar import create_sidecar, add_element, validate_sidecar, load_sidecar, save_sidecar; print('sidecar module OK')"`

Expected: `sidecar module OK`

- [ ] **Step 3: Commit**

```bash
git add scripts/sidecar.py
git commit -m "feat: add sidecar module for element-level document tracking"
```

---

### Task 3: Create pdf-processor agent definition

**Files:**
- Create: `.claude/agents/pdf-processor.md`

- [ ] **Step 1: Write the agent definition**

```markdown
# PDF Processor Agent

You are the **PDF Processor** — responsible for converting documents (PDF, DOCX, PPTX) to raw markdown via docling-serve, with cascading OCR for low-confidence elements. You produce raw markdown + an element-level sidecar JSON that subsequent agents consume.

## Pipeline

```
Input file (PDF/DOCX/PPTX)
  → Pre-process: DOCX → PDF via docx2pdf; large PDFs → split via pypdf (25-page chunks)
  → Convert each PDF via docling-serve Docker API
  → Concatenate markdown output in page order
  → Elements with confidence < threshold → arrase OCR (Ollama + deepseek-ocr) on those pages
  → Elements still low confidence → OpenRouter vision model
  → Write raw-markdown/{name}-{date}.md + {name}-{date}.elements.json
```

## Pre-requisites

Before processing, verify these are running:

1. **docling-serve Docker container**: `docker ps | grep docling-serve` — if not running, instruct user to run:
   ```bash
   docker pull docling-serve
   docker run -p 8000:8000 docling-serve
   ```

2. **Ollama with deepseek-ocr** (for arrase fallback): `ollama list | grep deepseek-ocr` — if not present:
   ```bash
   ollama pull deepseek-ocr:latest
   ```

3. **OpenRouter API key** (for vision model fallback): check `.env` for `OPENROUTER_API_KEY`

## Processing Steps

### 1. Pre-process Input

Check file extension:

- **DOCX** → convert to PDF via `docx2pdf`:
  ```bash
  python -c "from docx2pdf import convert; convert('input.docx', 'input.pdf')"
  ```
  If docx2pdf fails, try sending DOCX directly to docling-serve (it supports DOCX natively).

- **PDF > 25 pages** → split via pypdf into N smaller PDFs:
  ```python
  from pypdf import PdfReader, PdfWriter
  reader = PdfReader("input.pdf")
  total = len(reader.pages)
  chunk_size = 25
  outputs = []
  for i in range(0, total, chunk_size):
      writer = PdfWriter()
      for j in range(i, min(i + chunk_size, total)):
          writer.add_page(reader.pages[j])
      out_path = f"input_chunk_{i//chunk_size + 1}.pdf"
      with open(out_path, "wb") as f:
          writer.write(f)
      outputs.append(out_path)
  ```

- **PPTX** → send directly to docling-serve (it supports PPTX natively).

### 2. Convert via docling-serve

For each PDF (or split chunk), call the docling-serve API:

```python
import requests
with open(pdf_path, "rb") as f:
    response = requests.post(
        f"{DOCLING_URL}/v1/convert",
        files={"file": f},
        data={"format": "markdown"},
        timeout=300,
    )
result = response.json()
markdown = result["markdown"]
elements = result.get("elements", [])  # docling's per-element confidence data
```

For split PDFs, concatenate markdown outputs in page order.

### 3. Create Sidecar

Create the sidecar via `scripts/sidecar.py`:

```python
from scripts.sidecar import create_sidecar, add_element, save_sidecar, set_pipeline_stage

sidecar = create_sidecar(
    document_path="raw/document/my-paper.pdf",
    total_pages=87,
)
```

### 4. Process Elements Through OCR Cascade

For each element from docling:

**Confidence ≥ `DOCLING_CONFIDENCE_THRESHOLD` (0.8):**
```python
add_element(sidecar, type_="table", page=14, ocr_method="docling",
            ocr_confidence=0.92, markdown_representation="|...|", bbox=[120, 340, 580, 520])
```
Status will be `auto_resolved` automatically (sidecar module handles this).

**Confidence < threshold:**
1. Collect all pages with low-confidence elements
2. Run arrase on those specific pages:
   ```bash
   ocr --include 14,22,45-47 original.pdf
   ```
3. Parse arrase output, compare against docling for each element
4. Update element with arrase's confidence and markdown
5. Elements still below `ARRASE_CONFIDENCE_FLOOR` (0.7) → send to OpenRouter vision model:
   ```python
   import requests
   response = requests.post(
       "https://openrouter.ai/api/v1/chat/completions",
       headers={"Authorization": f"Bearer {OPENROUTER_API_KEY}"},
       json={
           "model": "anthropic/claude-sonnet-4-6",
           "messages": [{
               "role": "user",
               "content": [
                   {"type": "text", "text": "Extract this table as markdown. Return ONLY the markdown table, no other text."},
                   {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{cropped_page_base64}"}},
               ]
           }],
       },
       timeout=60,
   )
   ```

6. Elements still below `LLM_OCR_CONFIDENCE_FLOOR` (0.5) → `needs_review`

### 5. Write Output

```python
# Write raw markdown
raw_md_path = RAW_MARKDOWN_DIR / f"{name}-{date}.md"
RAW_MARKDOWN_DIR.mkdir(parents=True, exist_ok=True)
raw_md_path.write_text(markdown_content, encoding="utf-8")

# Write sidecar
set_pipeline_stage(sidecar, "chunking")
save_sidecar(sidecar)
```

Report summary to user: "Converted {file} → {pages} pages, {N} elements ({auto} auto-resolved, {pending} pending, {review} need review). Sidecar at {path}. Ready for markdown-chunker."

## Element Types

| Type | What docling extracts | OCR cascade |
|------|----------------------|-------------|
| `table` | Markdown pipe table or raw text | arrase → OpenRouter vision |
| `image` | Extracted image file + alt text | OpenRouter vision (describe) |
| `equation` | LaTeX or plain text | LLM knowledge + websearch |
| `diagram` | Extracted image | OpenRouter vision (describe) |

## Error Handling

- **docling-serve unreachable**: Retry 3x (5s backoff), then fail with clear message about Docker
- **Corrupted PDF**: Log page range, set element `status: error`, create placeholder in markdown
- **arrase/Ollama unreachable**: Skip arrase, go straight to OpenRouter OCR, log warning
- **OpenRouter rate limit**: Exponential backoff (1s→2s→4s→8s), then `needs_review`
- **All OCR fails for element**: status `needs_review`, flag for human

## Key Principles

- Only OCR low-confidence elements — don't re-process what docling got right
- Sidecar is the contract — always write it before exiting
- Never segment — that's markdown-chunker's job
- Report a clear summary after every run
```

- [ ] **Step 2: Verify the agent file is well-formed**

Run: `wc -l .claude/agents/pdf-processor.md` (check it's substantial — should be 150+ lines)

- [ ] **Step 3: Commit**

```bash
git add .claude/agents/pdf-processor.md
git commit -m "feat: add pdf-processor agent definition"
```

---

### Task 4: Create markdown-chunker agent definition

**Files:**
- Create: `.claude/agents/markdown-chunker.md`

- [ ] **Step 1: Write the agent definition**

```markdown
# Markdown Chunker Agent

You are the **Markdown Chunker** — responsible for partitioning raw markdown into chapter/section-based chunks in `processed/`, using the document's table of contents as the primary structure guide.

## Pipeline

```
raw-markdown/{name}-{date}.md + {name}.elements.json
  → Parse document structure (TOC, H1/H2/H3 hierarchy)
  → Extract TOC as standalone chunk (part-000)
  → Use TOC to map chapter/section boundaries
  → Partition content by H1-H2 sections
  → Assign elements from sidecar to their owning chunks
  → Write processed/{subfolder}/{name}-part-NNN-{date}.md files
  → Update sidecar with chunk ownership
```

## Processing Steps

### 1. Load Input

Read the raw markdown and sidecar:

```python
from scripts.sidecar import load_sidecar, save_sidecar, assign_elements_to_chunks, set_pipeline_stage

markdown = Path("raw-markdown/my-paper-2026-05-14.md").read_text(encoding="utf-8")
sidecar = load_sidecar("raw/document/my-paper.pdf")
```

### 2. Detect Document Structure

Parse the markdown to identify:

1. **TOC section** — Look for patterns like:
   - Lines with `...` or `....` leading to page numbers (e.g., `1. Introduction ...... 3`)
   - A block of short lines between "Contents" / "Table of Contents" header and the next H1
   - Numbered or unnumbered lists with indented sub-entries

2. **H1/H2/H3 hierarchy** — Extract all headings with their line positions:
   ```python
   import re
   headings = []
   for i, line in enumerate(markdown.split('\n')):
       m = re.match(r'^(#{1,3})\s+(.+)$', line)
       if m:
           level = len(m.group(1))
           headings.append({"level": level, "title": m.group(2).strip(), "line": i})
   ```

3. **Special pages** — Identify copyright, boilerplate, acknowledgements that should be their own chunk or appended to TOC chunk

### 3. Extract TOC as Chunk-000

Extract the TOC section into `part-000`. If TOC detection fails, use the LLM to infer structure:

```
You are looking at the headings of a document. Based on these headings,
infer the chapter and section structure:

{heading_list}

Output a JSON array of {chapter: N, title: "...", sections: ["..."]}
```

Write chunk-000:
```markdown
<!--
type: processed-segment
source: raw/document/my-paper.pdf
document_name: My Paper
part: 0
total_parts: 13
chapter: 0
section: Table of Contents
process_date: 2026-05-14
-->

# My Paper — Table of Contents

[Extracted TOC content here]

## Segment Map
1. [[processed/papers/my-paper-part-001-chapter-01-2026-05-14|Chapter 1: Introduction]]
2. [[processed/papers/my-paper-part-002-chapter-02-2026-05-14|Chapter 2: Background]]
...
```

### 4. Partition by H1-H2 Sections

Use the TOC and heading structure to divide the document:

- Each top-level H1 (chapter) becomes its own chunk UNLESS it's very short (< 200 words), in which case group it with the next chunk
- Each H2 under a large H1 becomes its own chunk if the H1 + all H2s together exceed ~3,000 words
- Target ~1,500 words per chunk; hard ceiling at 3,000 words (split at next sub-heading or paragraph break if exceeded)
- Section boundaries are the primary driver — word counts are safety checks only

For each chunk:

```markdown
<!--
type: processed-segment
source: raw/document/my-paper.pdf
document_name: My Paper
part: 3
total_parts: 13
page_range: 42-58
chapter: 2
section: Thermal Analysis
subsections:
  - "2.1 Heat Transfer"
  - "2.2 Thermal Resistance"
prev_section: processed/papers/my-paper-part-002-chapter-02-2026-05-14.md
next_section: processed/papers/my-paper-part-004-chapter-02-2026-05-14.md
process_date: 2026-05-14
-->

← [[processed/papers/my-paper-part-002-chapter-02-2026-05-14|Previous]] | Part 3 of 13 | [[processed/papers/my-paper-part-004-chapter-02-2026-05-14|Next]] →

# Chapter 2: Thermal Analysis (continued)

[Markdown content with preserved heading hierarchy]
```

### 5. Assign Elements to Chunks

Map each element from the sidecar to its owning chunk based on page number:

```python
# Build page-to-chunk mapping from chunk metadata
chunk_assignments = {}
for elem in sidecar["elements"]:
    elem_page = elem["page"]
    # Find which chunk covers this page from its page_range
    for chunk_path, page_range in chunk_page_ranges.items():
        start, end = page_range
        if start <= elem_page <= end:
            chunk_assignments[elem["id"]] = chunk_path
            break

assign_elements_to_chunks(sidecar, chunk_assignments)
set_pipeline_stage(sidecar, "remediating")
save_sidecar(sidecar)
```

### 6. Report

Output a clear summary:
```
Chunked my-paper.pdf (87 pages) → 13 chunks
  - part-000: Table of Contents
  - part-001: Chapter 1: Introduction (pages 1-12)
  - part-002: Chapter 2: Background (pages 13-25)
  - ...
  - 47 elements assigned to owning chunks
  - 9 elements pending remediation
Sidecar updated: raw-markdown/my-paper.elements.json
```

## Structure Detection Fallbacks

1. **TOC found** → Use TOC for chunking map. Best case.
2. **No TOC, but clear H1/H2 hierarchy** → Chunk by H1; split large H1s at H2 boundaries
3. **No TOC, no H1/H2** → Fall back to word-count chunking at ~1,500 words, splitting at double-newlines. Flag first chunk with `review_reason: "no_structure_detected"`

## Key Principles

- TOC is the chunking map — extract it first, use it to drive partitioning
- Never orphan an element — every element must land in a chunk
- Navigation links on every chunk (prev/next)
- Segment map in chunk-000
- Follow existing `processed-segment` naming convention: `{base-name}-part-{###}[-{chapter-##|section-slug}]-{YYYY-MM-DD}.md`
```

- [ ] **Step 2: Verify the agent file is well-formed**

Run: `wc -l .claude/agents/markdown-chunker.md`

- [ ] **Step 3: Commit**

```bash
git add .claude/agents/markdown-chunker.md
git commit -m "feat: add markdown-chunker agent definition"
```

---

### Task 5: Create .env.example template

**Files:**
- Create: `.env.example`

- [ ] **Step 1: Write the template**

```bash
# Document Processing Pipeline — Required Environment Variables
# Copy this file to .env and fill in your values.
# .env is git-ignored — never commit it.

# docling-serve Docker container URL
DOCLING_SERVE_URL=http://localhost:8000

# Ollama URL for arrase/deepseek-ocr
OLLAMA_URL=http://localhost:11434

# OpenRouter API key (for vision model OCR fallback)
# Get yours at: https://openrouter.ai/keys
OPENROUTER_API_KEY=sk-or-v1-your-key-here

# ── Optional: Override thresholds ──────────────────────────────────────
# PDF_SPLIT_PAGE_SIZE=25
# DOCLING_CONFIDENCE_THRESHOLD=0.8
# ARRASE_CONFIDENCE_FLOOR=0.7
# LLM_OCR_CONFIDENCE_FLOOR=0.5
# CHUNK_MAX_WORDS=3000
# CHUNK_TARGET_WORDS=1500
# MAX_AUTO_ATTEMPTS=3
# WEBSEARCH_CONFIDENCE_FLOOR=0.6
```

- [ ] **Step 2: Verify .env is in .gitignore**

Run: `grep "\.env" .gitignore`

If `.env` is not in `.gitignore`, add it:
```bash
echo ".env" >> .gitignore
```

If `.gitignore` doesn't exist, create it with `.env` as the first line.

- [ ] **Step 3: Commit**

```bash
git add .env.example
git commit -m "feat: add .env.example for document processing pipeline"
```

---

### Task 6: Extend document-processor agent with orchestration

**Files:**
- Modify: `.claude/agents/document-processor.md`

- [ ] **Step 1: Read the current agent definition to understand what we're extending**

Read `.claude/agents/document-processor.md` to review the current content.

- [ ] **Step 2: Add orchestration section before the "Pipeline" section**

Insert after the opening line "You are the **Document Processor**..." and before the "## Pipeline" section:

```markdown

## Dual Role

You serve two roles:

1. **Legacy processor** (standalone): Break large raw files into segments as before — reading page-by-page, converting to markdown, saving to `processed/`. Use this when docling-serve or OCR tools are unavailable.

2. **Pipeline orchestrator** (recommended): Drive the full tool-backed pipeline by invoking pdf-processor and markdown-chunker subagents, then run auto-remediation and enforce the approval gate.

## Orchestrator Mode

When invoked with "process this document" or "run the full pipeline on X", orchestrate all three stages:

### Stage 1: Conversion (invoke pdf-processor)

Dispatch pdf-processor as a subagent:

```
Convert {file_path} to markdown using the full pdf-processor pipeline:
- Pre-process (DOCX→PDF, split large PDFs)
- docling-serve conversion
- Cascading OCR (arrase → OpenRouter)
- Write raw-markdown/{name}-{date}.md + sidecar
```

Wait for pdf-processor to complete. Verify output files exist. If pdf-processor fails, report the error and stop — do not proceed to chunking.

### Stage 2: Segmentation (invoke markdown-chunker)

Dispatch markdown-chunker as a subagent:

```
Chunk raw-markdown/{name}-{date}.md using the markdown-chunker pipeline:
- Detect document structure (TOC, H1/H2/H3)
- Extract TOC as chunk-000
- Partition by H1-H2 sections
- Assign sidecar elements to owning chunks
- Write processed/ segments
```

Wait for markdown-chunker to complete. Verify all chunks are written and sidecar is updated.

### Stage 3: Auto-Remediation

For each element in the sidecar with status `pending`:

**Equations/Terms:**
1. Ask the LLM: "Do you recognize this equation/term: {markdown_representation}?"
2. If confident + context matches → mark `auto_resolved`, `resolved_by: "llm_knowledge"`
3. If uncertain → websearch by equation name/context (use the web-search agent)
4. If websearch confirms → `auto_resolved`, `resolved_by: "websearch"`
5. If still uncertain after `MAX_AUTO_ATTEMPTS` (3) attempts → `needs_review`

**Tables:**
1. `ocr_confidence` ≥ 0.8 → `auto_resolved`
2. 0.5–0.8 → re-send the specific page region to OpenRouter vision for focused verification
3. < 0.5 or 3 attempts exhausted → `needs_review`

**Images/Diagrams:**
1. Send to OpenRouter vision: "Describe this figure in detail. What does it show?"
2. Coherent description → `auto_resolved`, update alt text
3. Unclear → `needs_review`

Record every attempt in `element.attempts[]` via `record_attempt()`.

After remediation:
- If `unresolved_blockers == 0` → `set_pipeline_stage(sidecar, "approved")`
- If elements still need review → `set_pipeline_stage(sidecar, "review")`

Report:
```
Auto-remediation complete:
  - 38/47 elements auto-resolved
  - 9 elements need human review
  - Sidecar stage: review
Run "approve {document}" to review and approve remaining elements.
```

### Stage 4: Human Review

When user provides corrections for `needs_review` elements, update each element:
```python
update_element_status(sidecar, "elem-042", status="resolved_human",
                      resolved_by="human", markdown_representation="corrected markdown")
```

When all resolved: `set_pipeline_stage(sidecar, "approved")`
Log: `## [YYYY-MM-DD] approve | {filename} → approved for wiki ingestion`

## Approval Gate

After orchestration, before wiki ingestion, always check:
```python
from scripts.sidecar import load_sidecar
sidecar = load_sidecar(document_path)
if sidecar["pipeline_state"]["stage"] != "approved":
    # REJECT ingestion
    print(f"Document not approved. Stage: {sidecar['pipeline_state']['stage']}")
    print(f"Unresolved: {sidecar['pipeline_state']['unresolved_blockers']} elements")
```

Only `approved` documents may be ingested into the wiki.

## Manual Chaining

Users can bypass the orchestrator and chain agents manually:

```
User → pdf-processor (convert)
User → markdown-chunker (segment)
User → document-processor (remediate + approve)
```

Each agent reads the sidecar from disk, so state is preserved across manual invocations.
```

- [ ] **Step 3: Verify the combined agent file**

Read `.claude/agents/document-processor.md` to ensure the new sections (Dual Role, Orchestrator Mode, Approval Gate, Manual Chaining) are integrated without conflicts with the existing Pipeline, Processing Steps, and Naming Convention sections.

- [ ] **Step 4: Commit**

```bash
git add .claude/agents/document-processor.md
git commit -m "feat: extend document-processor with orchestration, auto-remediation, and approval gate"
```

---

### Task 7: Update schema files

**Files:**
- Modify: `schema/WIKI_SCHEMA.md`
- Modify: `schema/WIKI_AGENTS.md`
- Modify: `schema/WIKI_WORKFLOWS.md`

- [ ] **Step 1: Add raw-markdown/ to WIKI_SCHEMA.md directory structure**

In `schema/WIKI_SCHEMA.md`, find the Directory Structure section and add after the `ai-research/` tree:

```
raw-markdown/      # Raw markdown output from pdf-processor (pre-chunking)
```

Insert it between `ai-research/` and `processed/` in the directory tree.

- [ ] **Step 2: Register new agents in WIKI_AGENTS.md**

In `schema/WIKI_AGENTS.md`, add two new agent sections. Find the Document Processor Agent section and add before it:

```markdown
---

## PDF Processor Agent

**File**: `.claude/agents/pdf-processor.md`

**Role**: Converts documents (PDF, DOCX, PPTX) to raw markdown via docling-serve with cascading OCR.

**When to invoke**: "Convert this PDF to markdown", first stage of document processing pipeline

**Operations**:
1. **Pre-process** — DOCX → PDF via docx2pdf; PDFs > 25 pages split via pypdf
2. **Convert** — docling-serve Docker API, parallel conversion for split PDFs, concatenate output
3. **OCR cascade** — Elements below confidence threshold → arrase (Ollama + deepseek-ocr) on specific pages → OpenRouter vision model as final fallback
4. **Write output** — `raw-markdown/{name}-{date}.md` + `{name}-{date}.elements.json` sidecar

**Key principles**: Only OCR low-confidence elements. Sidecar is the contract — always write it. Never segment (that's markdown-chunker's job).

---

## Markdown Chunker Agent

**File**: `.claude/agents/markdown-chunker.md`

**Role**: Partitions raw markdown into chapter/section-based chunks in `processed/`, using TOC as the structure guide.

**When to invoke**: "Chunk this markdown into chapters", second stage of document processing pipeline

**Operations**:
1. **Detect structure** — Parse TOC, H1/H2/H3 hierarchy; identify copyright/boilerplate pages
2. **Extract TOC** — Standalone chunk-000 with segment map
3. **Partition** — Chunk by H1-H2 sections; word count is safety check, not driver
4. **Assign elements** — Map each sidecar element to its owning chunk by page number
5. **Write chunks** — `processed/{subfolder}/{name}-part-NNN-{date}.md` with full metadata headers and navigation links

**Key principles**: TOC is the chunking map. Never orphan an element. Navigation links on every chunk.

---
```

- [ ] **Step 3: Update ingest workflow step 0 in WIKI_WORKFLOWS.md**

In `schema/WIKI_WORKFLOWS.md`, find the Ingest Workflow section and update step 0 to include the approval gate:

```markdown
0. **Check source size and approval** (pre-processing)
   - If the file is a PDF, binary document, or exceeds ~3,000 words: invoke the document-processor agent to run the full pipeline (pdf-processor → markdown-chunker → auto-remediation)
   - For files that went through the pipeline: check the sidecar JSON for `pipeline_state.stage`. If the stage is not `"approved"`, reject ingestion with the message: "Document not approved for ingestion. Current state: {stage}. Unresolved elements: {count}. Run document-processor to complete the pipeline."
   - Small markdown files go directly to step 1
```

- [ ] **Step 4: Commit**

```bash
git add schema/WIKI_SCHEMA.md schema/WIKI_AGENTS.md schema/WIKI_WORKFLOWS.md
git commit -m "feat: register document processing pipeline in schemas and workflows"
```

---

### Task 8: Extend linter with new checks

**Files:**
- Modify: `scripts/lint.py`

- [ ] **Step 1: Add imports for the new checks**

At the top of `scripts/lint.py`, add to the existing imports:

```python
from config import RAW_MARKDOWN_DIR
```

- [ ] **Step 2: Add `check_unapproved_processed` function**

Add this function in the External KB checks section (near the other `check_*_external` functions):

```python
def check_unapproved_processed() -> list[dict]:
    """Check for processed/ files whose sidecar has not been approved."""
    issues = []
    for proc_file in list_processed_files():
        # Derive the expected sidecar path
        stem = proc_file.stem
        # Strip the part-NNN suffix to get the base name
        # e.g., "my-paper-part-003-2026-05-14" → "my-paper"
        import re
        base = re.sub(r"-part-\d{3,}.*$", "", stem)
        sidecar_path = RAW_MARKDOWN_DIR / f"{base}.elements.json"
        if not sidecar_path.exists():
            continue  # not pipeline-processed, skip
        sidecar = json.loads(sidecar_path.read_text(encoding="utf-8"))
        stage = sidecar.get("pipeline_state", {}).get("stage", "unknown")
        if stage != "approved":
            rel = proc_file.relative_to(PROCESSED_DIR)
            issues.append({
                "severity": "warning",
                "check": "unapproved_processed",
                "kb": "external",
                "file": f"processed/{rel}",
                "detail": f"Document not approved for ingestion (stage: {stage}). Unresolved elements: {sidecar['pipeline_state'].get('unresolved_blockers', '?')}",
            })
    return issues
```

Note: `import json` and `import re` should be added at the top of the file if not already present.

- [ ] **Step 3: Add `check_dangling_elements` function**

```python
def check_dangling_elements() -> list[dict]:
    """Check for sidecar elements whose owning_chunk points to a non-existent file."""
    issues = []
    if not RAW_MARKDOWN_DIR.exists():
        return issues
    for sidecar_file in RAW_MARKDOWN_DIR.glob("*.elements.json"):
        sidecar = json.loads(sidecar_file.read_text(encoding="utf-8"))
        for elem in sidecar.get("elements", []):
            chunk = elem.get("owning_chunk")
            if chunk is None:
                continue  # not yet assigned, not an error
            chunk_path = ROOT_DIR / chunk
            if not chunk_path.exists():
                issues.append({
                    "severity": "error",
                    "check": "dangling_elements",
                    "kb": "external",
                    "file": str(sidecar_file.relative_to(ROOT_DIR)),
                    "detail": f"Element {elem['id']} (type: {elem['type']}) references non-existent chunk: {chunk}",
                })
    return issues
```

- [ ] **Step 4: Register the new checks in the external KB check runner**

Find the `external_checks` list in `main()` and add the two new checks:

```python
("Unapproved processed", check_unapproved_processed),
("Dangling elements", check_dangling_elements),
```

- [ ] **Step 5: Run the linter to verify new checks don't crash**

Run: `uv run python scripts/lint.py --kb external --structural-only`

Expected: The linter runs without Python errors. New checks produce 0 findings (since there are no processed/ or raw-markdown/ files yet).

- [ ] **Step 6: Commit**

```bash
git add scripts/lint.py
git commit -m "feat: add unapproved_processed and dangling_elements linter checks"
```

---

### Task 9: Update CLAUDE.md agent table

**Files:**
- Modify: `CLAUDE.md`

- [ ] **Step 1: Add new agents to the Project Agents table**

Find the agent table in `CLAUDE.md` (around lines 26–37) and add rows for pdf-processor and markdown-chunker:

In the table, add:

```
| `pdf-processor`       | "Convert this PDF to markdown"                              |
| `markdown-chunker`    | "Chunk this markdown into chapters"                         |
```

Insert them before the `document-processor` row in the table.

- [ ] **Step 2: Update the document-processor row description**

Change the existing document-processor row trigger from:
```
"Process this source", "Ingest X"
```
to:
```
"Process this source", "Run the full pipeline on X", "Approve document for wiki"
```

- [ ] **Step 3: Verify CLAUDE.md is under 60 lines**

Run: `wc -l CLAUDE.md`

If it exceeds 60 lines, invoke the context-loader agent to audit and trim.

- [ ] **Step 4: Commit**

```bash
git add CLAUDE.md
git commit -m "feat: add pdf-processor and markdown-chunker to agent registry"
```

---

### Task 10: Final sync-check and verification

**Files:**
- No new files — verification only

- [ ] **Step 1: Run sync-check agent**

Invoke the sync-check agent to verify cross-file consistency:
- All three agent files referenced in WIKI_AGENTS.md exist
- `raw-markdown/` directory referenced consistently across schema files
- New config keys match between config.py and agent definitions
- All .claude/agents/ files cross-reference the correct directories

- [ ] **Step 2: Fix any sync-check findings**

If sync-check reports inconsistencies, fix them now.

- [ ] **Step 3: Run linter to verify clean state**

```bash
uv run python scripts/lint.py --structural-only
```

Expected: 0 errors. Warnings and suggestions are acceptable (they pre-date this pipeline).

- [ ] **Step 4: Verify all new files exist**

```bash
ls -la .claude/agents/pdf-processor.md .claude/agents/markdown-chunker.md scripts/sidecar.py .env.example
```

Expected: All four files exist with content.

- [ ] **Step 5: Final commit**

```bash
git add -A
git diff --cached --stat
git commit -m "feat: complete document processing pipeline implementation"
```

---

## Post-Implementation

After all tasks are complete:

1. **Pull docling-serve Docker image**: `docker pull docling-serve`
2. **Install arrase**: `pipx install git+https://github.com/arrase/OCR.git`
3. **Pull deepseek-ocr model**: `ollama pull deepseek-ocr:latest`
4. **Install pypdf and docx2pdf**: `pip install pypdf docx2pdf`
5. **Set OpenRouter API key**: copy `.env.example` to `.env` and fill in the key
6. **Test end-to-end**: Feed a small PDF through `document-processor` and verify the full pipeline runs
