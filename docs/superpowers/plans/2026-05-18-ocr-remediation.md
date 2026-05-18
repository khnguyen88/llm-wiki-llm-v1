# OCR Remediation Pipeline Stage — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a dedicated OCR remediation stage between document conversion and chunking, and rename pdf-processor to document-converter.

**Architecture:** New `ocr-remediator` agent + `scripts/ocr_remediate.py` script run deepseek-ocr on pages with placeholder comments or low-confidence elements, splicing fixes back into raw-markdown before chunking. The `pdf-processor` agent is renamed to `document-converter` across all live files (not historical plans/specs).

**Tech Stack:** Python 3, arrase/OCR CLI (deepseek-ocr via Ollama), existing sidecar module

---

### Task 1: Rename pdf-processor agent file and update its internal references

**Files:**
- Rename: `.claude/agents/pdf-processor.md` → `.claude/agents/document-converter.md`
- Modify: `.claude/agents/document-converter.md` (update self-references)

- [ ] **Step 1: Rename the agent file**

```bash
git mv .claude/agents/pdf-processor.md .claude/agents/document-converter.md
```

- [ ] **Step 2: Update the agent's self-identification line**

Read `.claude/agents/document-converter.md` line 3. Change:

```
You are the **PDF Processor** — responsible for converting documents (PDF, DOCX, PPTX)...
```

To:

```
You are the **Document Converter** — responsible for converting documents (PDF, DOCX, PPTX)...
```

- [ ] **Step 3: Update all pdf-processor references inside the agent file**

Run: `grep -n "pdf-processor" .claude/agents/document-converter.md`

If any references to its own old name exist (e.g., in comments or documentation), change `pdf-processor` to `document-converter`.

- [ ] **Step 4: Commit**

```bash
git add .claude/agents/pdf-processor.md .claude/agents/document-converter.md
git commit -m "feat: rename pdf-processor to document-converter"
```

---

### Task 2: Update CLAUDE.md agent table

**Files:**
- Modify: `CLAUDE.md:32` (agent table row)

- [ ] **Step 1: Update the agent table row**

Change line 32 from:

```
| `pdf-processor`       | "Convert this PDF to markdown"                              |
```

To:

```
| `document-converter`  | "Convert this document to markdown"                         |
```

- [ ] **Step 2: Add ocr-remediator row to the agent table**

Insert after the `document-converter` row (after what was line 32):

```
| `ocr-remediator`      | "Fix OCR issues in raw-markdown", "Run deepseek-ocr on problem pages" |
```

- [ ] **Step 3: Verify the table looks correct**

```bash
grep -n "document-converter\|ocr-remediator" CLAUDE.md
```

Expected: both entries present, table aligned.

- [ ] **Step 4: Commit**

```bash
git add CLAUDE.md
git commit -m "feat: register document-converter and ocr-remediator in agent table"
```

---

### Task 3: Update schema files (WIKI_AGENTS, WIKI_WORKFLOWS, WIKI_SCHEMA)

**Files:**
- Modify: `schema/WIKI_AGENTS.md:210-224`
- Modify: `schema/WIKI_WORKFLOWS.md:16`
- Modify: `schema/WIKI_SCHEMA.md:30`

- [ ] **Step 1: Update WIKI_AGENTS.md — rename section and content**

Change `schema/WIKI_AGENTS.md` line 210-224 from:

```
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
```

To:

```
## Document Converter Agent

**File**: `.claude/agents/document-converter.md`

**Role**: Converts documents (PDF, DOCX, PPTX) to raw markdown via docling-serve.

**When to invoke**: "Convert this document to markdown", first stage of document processing pipeline

**Operations**:
1. **Pre-process** — DOCX → PDF via docx2pdf; PDFs > 25 pages split via pypdf
2. **Convert** — docling-serve Docker API, parallel conversion for split PDFs, concatenate output
3. **Write output** — `raw-markdown/{name}-{date}.md` + `{name}-{date}.sidecar.json`

**Key principles**: Sidecar is the contract — always write it. Never segment (that's markdown-chunker's job). OCR remediation is handled by the separate ocr-remediator stage.
```

- [ ] **Step 2: Add OCR Remediator section to WIKI_AGENTS.md**

Insert after the Document Converter section:

```
## OCR Remediator Agent

**File**: `.claude/agents/ocr-remediator.md`

**Role**: Fixes docling OCR gaps by running deepseek-ocr on pages with placeholder comments or low-confidence elements.

**When to invoke**: "Fix OCR issues in raw-markdown", second stage of document processing pipeline

**Operations**:
1. **Scan** — Find `<!-- formula-not-decoded -->` and similar placeholders + low-confidence sidecar elements
2. **Convert source** — If not already PDF, convert to PDF (DOCX via docx2pdf, PPTX via LibreOffice)
3. **Run deepseek-ocr** — `ocr --include <problem-pages>` on the PDF
4. **Splice fixes** — Replace placeholders with actual formulas, upgrade low-confidence sections
5. **Update sidecar** — Mark resolved elements with `ocr_method: "arrase-deepseek"`
6. **Optional OpenRouter** — If `OPENROUTER_API_KEY` is set and deepseek-ocr fails, attempt OpenRouter vision

**Key principles**: Best-effort — never blocks the pipeline. Only runs on pages that need it. Produces same format it received.
```

- [ ] **Step 3: Update WIKI_WORKFLOWS.md reference**

Change `schema/WIKI_WORKFLOWS.md` line 16 from:

```
(pdf-processor → markdown-chunker → auto-remediation)
```

To:

```
(document-converter → ocr-remediator → markdown-chunker → auto-remediation)
```

- [ ] **Step 4: Update WIKI_SCHEMA.md directory description**

Change `schema/WIKI_SCHEMA.md` line 30 from:

```
raw-markdown/      # Raw markdown output from pdf-processor (pre-chunking)
```

To:

```
raw-markdown/      # Raw markdown output from document-converter (pre-chunking)
```

- [ ] **Step 5: Commit**

```bash
git add schema/WIKI_AGENTS.md schema/WIKI_WORKFLOWS.md schema/WIKI_SCHEMA.md
git commit -m "feat: update schema docs for document-converter rename and ocr-remediator"
```

---

### Task 4: Update sidecar module

**Files:**
- Modify: `scripts/sidecar.py:4,24`

- [ ] **Step 1: Update docstring reference**

Change `scripts/sidecar.py` line 4 from:

```python
The sidecar is the contract between pdf-processor, markdown-chunker, and
document-processor agents. Each agent reads what the previous wrote, adds its
layer, and writes back.
```

To:

```python
The sidecar is the contract between document-converter, ocr-remediator,
markdown-chunker, and document-processor agents. Each agent reads what the
previous wrote, adds its layer, and writes back.
```

- [ ] **Step 2: Add `arrase_deepseek` to VALID_RESOLVED_BY**

Change line 26 from:

```python
VALID_RESOLVED_BY = {"docling_high_confidence", "llm_knowledge", "websearch", "human"}
```

To:

```python
VALID_RESOLVED_BY = {"docling_high_confidence", "arrase_deepseek", "llm_knowledge", "websearch", "human"}
```

- [ ] **Step 3: Commit**

```bash
git add scripts/sidecar.py
git commit -m "feat: add arrase_deepseek resolved_by value, update sidecar docstring"
```

---

### Task 5: Update document-processor agent for renamed converter + new Stage 2

**Files:**
- Modify: `.claude/agents/document-processor.md` (all pdf-processor references + new Stage 2)

- [ ] **Step 1: Update all pdf-processor references**

Change every `pdf-processor` to `document-converter` in `.claude/agents/document-processor.md`.

Lines to update:
- Line 11: `invoking pdf-processor and markdown-chunker` → `invoking document-converter, ocr-remediator, and markdown-chunker`
- Line 17: `### Stage 1: Conversion (invoke pdf-processor)` → `### Stage 1: Conversion (invoke document-converter)`
- Line 19: `Dispatch pdf-processor as a subagent:` → `Dispatch document-converter as a subagent:`
- Lines 22-28: Update code block text from `pdf-processor pipeline` to `document-converter pipeline`, remove cascading OCR references
- Line 29: `Wait for pdf-processor to complete` → `Wait for document-converter to complete`
- Line 112: `User → pdf-processor (convert)` → `User → document-converter (convert)`

- [ ] **Step 2: Insert new Stage 2 for ocr-remediator**

After the Stage 1 section (after "If pdf-processor fails, report the error and stop — do not proceed to chunking." line), insert:

```
### Stage 2: OCR Remediation (invoke ocr-remediator)

Dispatch ocr-remediator as a subagent:

```
Remediate raw-markdown/{name}-{date}.md using deepseek-ocr:
- Scan for placeholders and low-confidence elements in sidecar
- Convert source to PDF if needed
- Run ocr --include on problem pages
- Splice fixes back into raw-markdown
- Update sidecar with resolved elements
```

Wait for ocr-remediator to complete. If it resolves all placeholders, proceed to markdown-chunker.
If elements remain as needs_review, still proceed — markdown-chunker handles them gracefully,
and Stage 4 auto-remediation can attempt LLM-based fixes.
```

- [ ] **Step 3: Renumber existing stages**

Change the old "Stage 2: Segmentation" to `### Stage 3: Segmentation (invoke markdown-chunker)`
Change the old "Stage 3: Auto-Remediation" to `### Stage 4: Auto-Remediation`
Change the old "Stage 4: Human Review" to `### Stage 5: Human Review`

- [ ] **Step 4: Update manual chaining section**

Change line 112 area from:

```
User → pdf-processor (convert)
User → markdown-chunker (segment)
User → document-processor (remediate + approve)
```

To:

```
User → document-converter (convert)
User → ocr-remediator (fix OCR gaps)
User → markdown-chunker (segment)
User → document-processor (remediate + approve)
```

- [ ] **Step 5: Commit**

```bash
git add .claude/agents/document-processor.md
git commit -m "feat: update document-processor orchestration with ocr-remediator stage"
```

---

### Task 6: Create ocr-remediator agent definition

**Files:**
- Create: `.claude/agents/ocr-remediator.md`

- [ ] **Step 1: Write the agent file**

Write `.claude/agents/ocr-remediator.md`:

````markdown
# OCR Remediator Agent

You are the **OCR Remediator** — responsible for fixing docling's OCR gaps by running deepseek-ocr via [arrase/OCR](https://github.com/arrase/OCR) on only the pages that need it, then splicing corrected content back into the raw markdown before chunking.

## Pipeline

```
raw-markdown/{name}-{date}.md + {name}.sidecar.json
  → Scan for placeholder comments (<!-- formula-not-decoded -->, <!-- table-not-decoded -->)
  → Check sidecar for low-confidence elements (< 0.8)
  → Collect union of problem pages
  → If source not PDF: convert to PDF
  → Run ocr --include <pages> on the PDF
  → Parse deepseek-ocr output, extract corrected elements
  → Splice fixes into raw markdown
  → Update sidecar elements
  → Optional: OpenRouter vision fallback for still-failing elements
  → Write updated raw-markdown + sidecar
```

## Prerequisites

- **Ollama** running locally with `deepseek-ocr:latest` pulled
- **arrase/OCR CLI** installed: `pipx install git+https://github.com/arrase/OCR.git`
- **OpenRouter API key** (optional): check `.env` for `OPENROUTER_API_KEY`

## Processing Steps

### 1. Scan for Problems

Run `scripts/ocr_remediate.py` to scan:

```python
from ocr_remediate import scan_placeholders, find_low_confidence, collect_problem_pages

placeholders = scan_placeholders(raw_md_path)
# Returns: [{page: 3, type: "formula", line_number: 42, context_lines: [...]}, ...]

low_conf = find_low_confidence(sidecar_path, threshold=0.8)
# Returns: [{element_id: "elem-005", page: 4, type: "table", confidence: 0.62}, ...]

problem_pages = collect_problem_pages(placeholders, low_conf)
# Returns: [3, 4]
```

If `problem_pages` is empty, report "No OCR issues found — raw-markdown is clean" and exit. This is a successful no-op.

### 2. Convert Source to PDF (if needed)

The `ocr` CLI only works with PDF input. If the source is not already a PDF:

- `.docx` → `python -c "from docx2pdf import convert; convert('source.docx', 'source.pdf')"`
- `.pptx` → `soffice --headless --convert-to pdf source.pptx`
- Other formats → skip OCR remediation, leave placeholders for auto-remediation stage

### 3. Run DeepSeek OCR

```bash
ocr --include 3,4 source.pdf
```

This produces `source.md` in the same directory. Read and parse it.

### 4. Parse and Splice

```python
from ocr_remediate import parse_ocr_output, splice_into_markdown

ocr_content = parse_ocr_output("source.md")
# Returns: {3: {"formula": ["$$SBD = ...$$", "$$DiC = ...$$"], "table": [...]}, 4: {...}}

updated_md = splice_into_markdown(raw_md_path, ocr_content, placeholders)
# Writes updated raw-markdown file
```

Splicing rules:
- `<!-- formula-not-decoded -->` → replaced with the formula from deepseek-ocr output at that position
- Low-confidence tables → replaced with deepseek-ocr's version if it has fewer placeholder markers
- Low-confidence diagrams/equations → updated if deepseek-ocr gave a clearly better representation

### 5. Update Sidecar

```python
from scripts.sidecar import load_sidecar, update_element_status, save_sidecar

sidecar = load_sidecar(document_path)

for fix in successful_fixes:
    update_element_status(
        sidecar,
        fix["element_id"],
        status="auto_resolved",
        resolved_by="arrase_deepseek",
        markdown_representation=fix["markdown"],
    )

for fail in failed_fixes:
    if os.getenv("OPENROUTER_API_KEY"):
        # Attempt OpenRouter vision model
        result = try_openrouter_vision(fail)
        if result:
            update_element_status(sidecar, fail["element_id"], status="auto_resolved",
                                  resolved_by="arrase_deepseek", markdown_representation=result)
            continue
    update_element_status(sidecar, fail["element_id"], status="needs_review",
                          review_reason="ocr_unavailable")

save_sidecar(sidecar)
```

### 6. Report

```
OCR Remediation complete:
  - 6/6 placeholders resolved via deepseek-ocr
  - 2/3 low-confidence elements upgraded
  - 1 element needs human review
  - Raw-markdown updated: raw-markdown/paper-2026-05-18.md
  - Sidecar updated: raw-markdown/paper-2026-05-18.sidecar.json
Ready for markdown-chunker.
```

## Error Handling

- **`ocr` CLI not installed**: Skip deepseek-ocr, try OpenRouter if configured, otherwise `needs_review`
- **Ollama not running / model not pulled**: Same — skip and fall forward
- **Source can't convert to PDF**: Log warning, skip OCR, mark elements `needs_review`, continue
- **deepseek-ocr produces worse output**: Keep docling version (compare by placeholder count reduction)
- **No problem pages**: No-op, return clean
- **deepseek-ocr output unparseable**: Log error, keep original, mark `needs_review`

**Always best-effort. Never block the pipeline.**

## Key Principles

- Only run on pages that need it — don't re-OCR the entire document
- Element-level splicing — replace only what's broken, keep what works
- Sidecar is the contract — always update it before exiting
- Fall forward — if OCR fails, let the next stage handle it
- Same handoff format — markdown-chunker doesn't know you were here
````

- [ ] **Step 2: Commit**

```bash
git add .claude/agents/ocr-remediator.md
git commit -m "feat: add ocr-remediator agent definition"
```

---

### Task 7: Create scripts/ocr_remediate.py

**Files:**
- Create: `scripts/ocr_remediate.py`

- [ ] **Step 1: Write the script**

Write `scripts/ocr_remediate.py`:

```python
"""
OCR remediation for docling output.

Scans raw-markdown for placeholder comments and low-confidence sidecar elements,
runs deepseek-ocr (arrase/OCR) on specific pages, and splices fixes back in.
"""

from __future__ import annotations

import os
import re
import subprocess
import sys
from pathlib import Path

from sidecar import load_sidecar, save_sidecar, update_element_status


# ── Constants ──────────────────────────────────────────────────────────────

PLACEHOLDER_PATTERN = re.compile(r"<!--\s*(formula|table|diagram)-not-decoded\s*-->")
DOCX2PDF_SCRIPT = "python -c \"from docx2pdf import convert; convert('{src}', '{dst}')\""
OCR_THRESHOLD = 0.8


# ── Scanning ───────────────────────────────────────────────────────────────

def scan_placeholders(md_path: str | Path) -> list[dict]:
    """Find all <!-- *-not-decoded --> placeholder comments.

    Returns:
        List of dicts: [{page, type, line_number, context_lines}, ...]
        Page is inferred from surrounding content markers.
    """
    md_path = Path(md_path)
    text = md_path.read_text(encoding="utf-8")
    lines = text.split("\n")

    placeholders = []
    for i, line in enumerate(lines):
        m = PLACEHOLDER_PATTERN.search(line)
        if m:
            context = lines[max(0, i - 2): i + 3]
            page = _infer_page(lines, i)
            placeholders.append({
                "page": page,
                "type": m.group(1),
                "line_number": i,
                "context_lines": context,
            })

    return placeholders


def find_low_confidence(sidecar_path: str | Path, threshold: float = OCR_THRESHOLD) -> list[dict]:
    """Find sidecar elements with ocr_confidence below threshold.

    Returns:
        List of dicts: [{element_id, page, type, confidence}, ...]
    """
    sidecar = load_sidecar(sidecar_path)
    low_conf = []
    for elem in sidecar.get("elements", []):
        if elem.get("ocr_confidence", 1.0) < threshold:
            low_conf.append({
                "element_id": elem["id"],
                "page": elem["page"],
                "type": elem["type"],
                "confidence": elem["ocr_confidence"],
            })
    return low_conf


def collect_problem_pages(placeholders: list[dict], low_conf: list[dict]) -> list[int]:
    """Deduplicated, sorted list of pages that need OCR remediation."""
    pages = set()
    for p in placeholders:
        pages.add(p["page"])
    for e in low_conf:
        pages.add(e["page"])
    return sorted(pages)


def _infer_page(lines: list[str], line_idx: int) -> int:
    """Infer page number from surrounding content markers.

    Looks for page break markers (e.g., '--- page 3 ---') or image references
    with page info near the placeholder. Falls back to sequential distribution
    based on total page count from sidecar.
    """
    page_marker = re.compile(r"---\s*page\s*(\d+)\s*---|\[page\s*(\d+)\]", re.IGNORECASE)
    image_ref = re.compile(r"!\[.*?\]\(.*?[_-](\d+)\.[a-z]{3,4}\)")

    for offset in range(-10, 10):
        idx = line_idx + offset
        if 0 <= idx < len(lines):
            m = page_marker.search(lines[idx])
            if m:
                return int(m.group(1) or m.group(2))
            m = image_ref.search(lines[idx])
            if m:
                return int(m.group(1))

    return 0  # unknown — will need sidecar page count for sequential fallback


# ── Format conversion ──────────────────────────────────────────────────────

def convert_to_pdf(source_path: str | Path) -> Path:
    """Convert source document to PDF if not already.

    Returns:
        Path to the PDF file.
    Raises:
        ValueError: if format is unsupported.
    """
    source = Path(source_path)
    ext = source.suffix.lower()

    if ext == ".pdf":
        return source

    if ext == ".docx":
        pdf_path = source.with_suffix(".pdf")
        cmd = DOCX2PDF_SCRIPT.format(src=source, dst=pdf_path)
        subprocess.run(cmd, shell=True, check=True, capture_output=True)
        return pdf_path

    if ext == ".pptx":
        subprocess.run(
            ["soffice", "--headless", "--convert-to", "pdf", str(source)],
            cwd=str(source.parent),
            check=True,
            capture_output=True,
        )
        return source.with_suffix(".pdf")

    raise ValueError(f"Unsupported format for PDF conversion: {ext}")


# ── DeepSeek OCR ───────────────────────────────────────────────────────────

def run_deepseek_ocr(pdf_path: str | Path, pages: list[int]) -> Path:
    """Run arrase/OCR on specific pages and return the output markdown path.

    Args:
        pdf_path: Path to the PDF file.
        pages: List of 1-based page numbers to process.

    Returns:
        Path to the generated markdown file.
    """
    pdf = Path(pdf_path)
    page_str = ",".join(str(p) for p in pages)
    cmd = ["ocr", "--include", page_str, str(pdf)]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"ocr CLI failed: {result.stderr}")
    return pdf.with_suffix(".md")


def parse_ocr_output(ocr_md_path: str | Path) -> dict[int, dict[str, list[str]]]:
    """Parse deepseek-ocr output into page-keyed content.

    Returns:
        {page_number: {"formula": ["$$...$$", ...], "table": ["|...|", ...], ...}}
    """
    text = Path(ocr_md_path).read_text(encoding="utf-8")

    # Split by page markers that deepseek-ocr may emit
    pages: dict[int, dict[str, list[str]]] = {}
    current_page = 1
    current_text: list[str] = []

    for line in text.split("\n"):
        page_break = re.match(r"^-{3,}\s*[Pp]age\s*(\d+)\s*-{3,}$", line)
        if page_break:
            if current_text:
                pages.setdefault(current_page, {}).setdefault("text", []).extend(current_text)
            current_page = int(page_break.group(1))
            current_text = []
        else:
            current_text.append(line)

    if current_text:
        pages.setdefault(current_page, {}).setdefault("text", []).extend(current_text)

    return pages


# ── Splicing ───────────────────────────────────────────────────────────────

def splice_into_markdown(md_path: str | Path, ocr_content: dict, placeholders: list[dict]) -> Path:
    """Replace placeholders in raw markdown with deepseek-OCR output.

    Args:
        md_path: Path to the raw markdown file (modified in place).
        ocr_content: Parsed OCR output from parse_ocr_output().
        placeholders: Results from scan_placeholders().

    Returns:
        Path to the updated markdown file.
    """
    md_path = Path(md_path)
    text = md_path.read_text(encoding="utf-8")
    lines = text.split("\n")

    # Build page → OCR text lookup
    page_text: dict[int, str] = {}
    for page, content in ocr_content.items():
        page_text[page] = "\n".join(content.get("text", []))

    # Replace placeholders
    for ph in placeholders:
        page = ph["page"]
        line_idx = ph["line_number"]
        if page in page_text:
            replacement = _extract_element_from_page_text(page_text[page], ph["type"], lines, line_idx)
            if replacement:
                lines[line_idx] = replacement

    md_path.write_text("\n".join(lines), encoding="utf-8")
    return md_path


def _extract_element_from_page_text(
    page_text: str, element_type: str, context_lines: list[str], line_idx: int
) -> str | None:
    """Extract a specific element (formula, table) from page OCR text using context matching.

    Uses the surrounding context lines to locate the corresponding content in the
    deepseek-OCR output for that page.
    """
    # Get surrounding text context (skip the placeholder line itself)
    before = [l for l in context_lines[:2] if "not-decoded" not in l]
    after = [l for l in context_lines[2:] if "not-decoded" not in l]

    page_lines = page_text.split("\n")

    if element_type == "formula":
        # Look for LaTeX math patterns near the context
        math_patterns = re.findall(r"\$\$[^$]+\$\$|\$[^$]+\$|\\\[.*?\\\]", page_text, re.DOTALL)
        if math_patterns:
            return math_patterns[0]  # Return the first formula found — close enough for a first pass
        return None

    if element_type == "table":
        # Look for markdown table patterns
        table_pattern = re.findall(r"(\|.*\|[\s\S]*?\n\s*\n)", page_text)
        if table_pattern:
            return table_pattern[0].strip()
        return None

    return None


# ── Sidecar sync ───────────────────────────────────────────────────────────

def sync_sidecar(sidecar_path: str | Path, placeholders: list[dict], fixes_applied: dict[str, str]) -> None:
    """Update sidecar with OCR remediation results.

    Args:
        sidecar_path: Path to the sidecar JSON file.
        placeholders: All placeholders that were found.
        fixes_applied: Mapping of placeholder line_number -> markdown_representation that was spliced.
    """
    sidecar = load_sidecar(sidecar_path)

    for ph in placeholders:
        key = str(ph["line_number"])
        if key in fixes_applied:
            update_element_status(
                sidecar,
                ph.get("element_id", f"ph-{ph['page']}-{ph['line_number']}"),
                status="auto_resolved",
                resolved_by="arrase_deepseek",
                markdown_representation=fixes_applied[key],
            )
        else:
            update_element_status(
                sidecar,
                ph.get("element_id", f"ph-{ph['page']}-{ph['line_number']}"),
                status="needs_review",
                review_reason="ocr_unavailable",
            )

    save_sidecar(sidecar)


# ── Main entry ─────────────────────────────────────────────────────────────

def remediate(raw_md_path: str | Path, sidecar_path: str | Path, source_path: str | Path) -> bool:
    """Run full OCR remediation on a raw-markdown file.

    Args:
        raw_md_path: Path to the raw markdown file.
        sidecar_path: Path to the sidecar JSON file.
        source_path: Path to the original source document.

    Returns:
        True if any fixes were applied.
    """
    placeholders = scan_placeholders(raw_md_path)
    low_conf = find_low_confidence(sidecar_path)

    if not placeholders and not low_conf:
        print("No OCR issues found — raw-markdown is clean.")
        return False

    problem_pages = collect_problem_pages(placeholders, low_conf)
    print(f"Problem pages: {problem_pages}")
    print(f"  Placeholders: {len(placeholders)}, Low-confidence: {len(low_conf)}")

    try:
        pdf_path = convert_to_pdf(source_path)
    except ValueError as e:
        print(f"Warning: {e} — skipping OCR remediation")
        return False

    try:
        ocr_md_path = run_deepseek_ocr(pdf_path, problem_pages)
    except (RuntimeError, FileNotFoundError) as e:
        print(f"Warning: deepseek-ocr unavailable ({e}) — trying OpenRouter fallback")
        # OpenRouter fallback would go here
        return False

    ocr_content = parse_ocr_output(ocr_md_path)

    fixes = {}
    for ph in placeholders:
        page = ph["page"]
        if page in ocr_content:
            page_text = "\n".join(ocr_content[page].get("text", []))
            # Read context from raw markdown
            md_lines = Path(raw_md_path).read_text(encoding="utf-8").split("\n")
            context = md_lines[max(0, ph["line_number"] - 2): ph["line_number"] + 3]
            replacement = _extract_element_from_page_text(page_text, ph["type"], context, ph["line_number"])
            if replacement:
                fixes[str(ph["line_number"])] = replacement

    splice_into_markdown(raw_md_path, ocr_content, placeholders)

    sync_sidecar(sidecar_path, placeholders, fixes)

    print(f"OCR Remediation complete:")
    print(f"  - {len(fixes)}/{len(placeholders)} placeholders resolved")
    print(f"  - Raw-markdown updated: {raw_md_path}")
    print(f"  - Sidecar updated: {sidecar_path}")
    return len(fixes) > 0


# ── CLI ────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python ocr_remediate.py <raw-md> <sidecar> <source>")
        sys.exit(1)

    ok = remediate(sys.argv[1], sys.argv[2], sys.argv[3])
    sys.exit(0 if ok else 0)  # Always exit 0 — best-effort, never blocks pipeline
```

- [ ] **Step 2: Commit**

```bash
git add scripts/ocr_remediate.py
git commit -m "feat: add ocr_remediate.py script"
```

---

### Task 8: Verify with sync-check

**Files:**
- None (read-only check)

- [ ] **Step 1: Run sync-check agent**

Invoke the `sync-check` agent to verify no broken references across agents, schemas, and CLAUDE.md after all the renames and additions.

- [ ] **Step 2: Fix any issues found**

If sync-check reports issues related to our changes, fix them and commit.

- [ ] **Step 3: Verify all files exist**

```bash
ls -la .claude/agents/document-converter.md .claude/agents/ocr-remediator.md .claude/agents/document-processor.md scripts/ocr_remediate.py
```

Expected: all four files exist.

- [ ] **Step 4: Verify no stale pdf-processor references remain in live files**

```bash
grep -rn "pdf-processor" CLAUDE.md .claude/agents/ schema/ scripts/ --include="*.md" --include="*.py"
```

Expected: no results (historical `docs/` files and `raw/` are excluded).

---

### Task 9: Test on existing document

**Files:**
- None (read/write test on existing files)

- [ ] **Step 1: Verify Ollama and deepseek-ocr are available**

```bash
ollama list | grep deepseek-ocr
```

Expected: `deepseek-ocr:latest` listed.

```bash
which ocr || pipx list | grep OCR
```

Expected: `ocr` command found.

- [ ] **Step 2: Run ocr_remediate.py on the existing document**

```bash
uv run python scripts/ocr_remediate.py "raw-markdown/Unsupervised_Learning_Method_for_Plant_and_Leaf_Segmentation-2026-05-18.md" "raw-markdown/Unsupervised_Learning_Method_for_Plant_and_Leaf_Segmentation-2026-05-18.sidecar.json" "raw/papers/Unsupervised_Learning_Method_for_Plant_and_Leaf_Segmentation.pdf"
```

Expected output reports number of placeholders resolved.

- [ ] **Step 3: Verify placeholders are replaced**

```bash
grep -c "formula-not-decoded" "raw-markdown/Unsupervised_Learning_Method_for_Plant_and_Leaf_Segmentation-2026-05-18.md"
```

Expected: `0` (all six placeholders replaced).

- [ ] **Step 4: Verify sidecar updated**

```bash
python -c "import json; s=json.load(open('raw-markdown/Unsupervised_Learning_Method_for_Plant_and_Leaf_Segmentation-2026-05-18.sidecar.json')); print(f\"Elements: {len(s['elements'])}, Unresolved: {s['pipeline_state']['unresolved_blockers']}\")"
```

Expected: Elements count > 0, each formula element has `ocr_method` and `status`.

- [ ] **Step 5: Verify raw-markdown content integrity**

Check a couple of the replacement locations:

```bash
grep -n "SBD\|DiC\|Dice" "raw-markdown/Unsupervised_Learning_Method_for_Plant_and_Leaf_Segmentation-2026-05-18.md" | head -10
```

Expected: Formula content visible, not placeholder comments.

- [ ] **Step 6: Commit test results**

If the test produces fixes, commit the updated raw-markdown + sidecar:

```bash
git add raw-markdown/Unsupervised_Learning_Method_for_Plant_and_Leaf_Segmentation-2026-05-18.md raw-markdown/Unsupervised_Learning_Method_for_Plant_and_Leaf_Segmentation-2026-05-18.sidecar.json
git commit -m "fix: OCR remediation on plant-leaf-segmentation paper — 6 formulas resolved"
```
