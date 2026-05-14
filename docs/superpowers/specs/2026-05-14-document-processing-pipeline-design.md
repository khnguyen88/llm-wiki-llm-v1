# Document Processing Pipeline — Design Spec

**Date:** 2026-05-14
**Status:** approved

## Overview

Redesign the document processing pipeline into three specialized agents that can work independently or chained through an orchestrator. The pipeline converts documents (PDF, DOCX, PPTX) to markdown — DOCX normalized to PDF via docx2pdf, large PDFs split into 25-page chunks via pypdf before docling-serve conversion, performs on-demand OCR for low-confidence elements via arrase (Ollama + deepseek-ocr) with OpenRouter vision models as final fallback, partitions content into chapter/section chunks, and tracks every table, image, and equation at element-level through an approval-gated sidecar metadata system.

## Motivation

The existing document-processor agent relies on the LLM reading files page-by-page and converting them to markdown — no actual file conversion tooling. For complex PDFs with tables, equations, and images (potentially 400+ pages), this is unreliable and slow. This redesign adds real conversion tools (docling-serve, arrase OCR, OpenRouter vision), element-level confidence tracking, auto-remediation before human escalation, and an approval gate before wiki ingestion.

---

## 1. Agent Architecture & Boundaries

### pdf-processor (Conversion Frontend)
- **Solo mode:** "Convert this PDF to markdown" — takes a file path, returns raw markdown + elements sidecar
- **Pipeline role:** First stage, called by document-processor

Pre-processing:
- If DOCX: convert to PDF via docx2pdf (normalizes to single input format)
- If PDF > `PDF_SPLIT_PAGE_SIZE` (25 pages): split into N smaller PDFs via pypdf
- Routes each resulting PDF to docling-serve

Responsibilities:
- Talks to docling-serve Docker API (`POST /v1/convert`)
- Receives markdown with per-element confidence scores from docling
- Concatenates markdown from split PDFs in page order
- Extracts images and tables from docling output
- Collects page numbers for elements below confidence threshold
- Runs arrase (Ollama + deepseek-ocr) on specific pages: `ocr --include 14,22,45-47 mydoc.pdf`
- Compares arrase output against docling for those elements
- Escalates still-low-confidence elements to OpenRouter vision models
- Produces: `raw-markdown/{name}-{date}.md` + `raw-markdown/{name}-{date}.elements.json`
- Sets initial element statuses and confidence scores
- Does NOT segment — that's markdown-chunker's job

### markdown-chunker (Segmentation Engine)
- **Solo mode:** "Chunk this markdown into chapters" — takes a markdown file + sidecar, produces processed/ segments
- **Pipeline role:** Second stage, reads pdf-processor output

Responsibilities:
- Parses document structure — identifies TOC, headers, copyright/boilerplate pages
- Extracts TOC as standalone chunk (chunk-000)
- Uses TOC to map chapter/section boundaries for chunking strategy
- Chunks by logical H1-H2 sections (not arbitrary word counts)
- Word count (~1,500 target, ~3,000 hard ceiling) is a safety check, not the driver
- Assigns each element from sidecar to its owning chunk via `owning_chunk` field
- Produces: `processed/{subfolder}/{name}-part-NNN-{date}.md` files
- Writes segment map into chunk-000 with navigation links
- Updates sidecar with per-element chunk ownership

### document-processor (Orchestrator) — Extended from existing
- **Solo mode:** none — orchestration layer
- **Pipeline role:** Drives the full pipeline or lets user manually chain agents

Responsibilities:
- Tracks pipeline state per document via sidecar (converting → chunking → remediating → review → approved)
- Invokes pdf-processor → markdown-chunker → auto-remediation
- Auto-remediation: for unresolved equations/terms, queries LLM knowledge + websearch
- For ambiguous tables: re-queries vision model with focused crop
- Flags remaining unresolved elements for human review
- Enforces approval gate — chunks cannot be ingested until state = approved
- Logs all operations to `wiki/log.md`
- Can be bypassed — user can call pdf-processor or markdown-chunker directly

### Communication Model
```
User (manual chain):   pdf-processor → markdown-chunker
User (orchestrated):   document-processor → [pdf-processor → markdown-chunker → auto-remediate]
```

State passes through files on disk. The sidecar JSON is the contract between agents — each reads what the previous wrote, adds its layer, writes back.

---

## 2. Element Sidecar Schema

`raw-markdown/{name}-{date}.elements.json` — the contract between all three agents:

```jsonc
{
  "document": "raw/document/my-paper.pdf",
  "processed_date": "2026-05-14T10:30:00Z",
  "total_pages": 87,
  "elements": [
    {
      "id": "elem-001",
      "type": "table",                          // table | image | equation | diagram
      "page": 14,
      "ocr_method": "docling",                  // docling | arrase-deepseek | openrouter-claude | openrouter-gemini
      "ocr_confidence": 0.82,                   // 0.0–1.0
      "status": "auto_resolved",                // pending | auto_resolved | needs_review | resolved_human | error
      "review_reason": null,                    // null | "low_confidence" | "ocr_unavailable" | "ambiguous" | "complex_layout" | "conversion_failed"
      "resolved_by": null,                      // null | "docling_high_confidence" | "llm_knowledge" | "websearch" | "human"
      "owning_chunk": "processed/papers/my-paper-part-003-2026-05-14.md",
      "markdown_representation": "| Col1 | Col2 |\n|-----|-----|\n| ... |",
      "source_coordinates": {
        "bbox": [120, 340, 580, 520],
        "page": 14
      },
      "attempts": [
        {
          "method": "websearch",
          "timestamp": "2026-05-14T10:32:00Z",
          "query": "Boltzmann constant equation thermodynamics",
          "result": "auto_resolved"
        }
      ]
    }
  ],
  "pipeline_state": {
    "stage": "approved",
    "total_elements": 47,
    "resolved": 47,
    "needs_review": 0,
    "unresolved_blockers": 0
  }
}
```

### Element Status Flow
```
pending → (docling confidence ≥ threshold) → auto_resolved
pending → (docling < threshold → arrase agrees) → auto_resolved
pending → (arrase low → OpenRouter agrees) → auto_resolved
pending → (all OCR low) → needs_review → (human fixes) → resolved_human
pending → (auto-remediation succeeds) → auto_resolved
pending → (auto-remediation fails, 3 attempts) → needs_review
```

### Pipeline State Stages
```
converting → chunking → remediating → review → approved
                                              ↗
 (all elements auto_resolved, no blockers) ───┘
```

Only `approved` documents can be ingested into the wiki.

---

## 3. Configuration

### `.env` (git-ignored, secrets)
```bash
OPENROUTER_API_KEY=sk-or-v1-...
DOCLING_SERVE_URL=http://localhost:8000
OLLAMA_URL=http://localhost:11434
```

### `scripts/config.py` (extended, non-sensitive)

New keys:
```python
# Tool endpoints (from .env or defaults)
DOCLING_URL = os.getenv("DOCLING_SERVE_URL", "http://localhost:8000")
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", None)

# Pre-processing
PDF_SPLIT_PAGE_SIZE = 25          # split PDFs into chunks of this many pages before docling

# Chunking thresholds
CHUNK_MAX_WORDS = 3000
CHUNK_TARGET_WORDS = 1500

# OCR cascade thresholds
DOCLING_CONFIDENCE_THRESHOLD = 0.8   # below this → invoke arrase OCR
ARRASE_CONFIDENCE_FLOOR = 0.7        # below this → escalate to OpenRouter vision
LLM_OCR_CONFIDENCE_FLOOR = 0.5       # below this → flag for human review

# Auto-remediation
MAX_AUTO_ATTEMPTS = 3                # max remediation tries per element
WEBSEARCH_CONFIDENCE_FLOOR = 0.6     # below this after websearch → human
```

---

## 4. Full Pipeline Flow

### Stage 1: Conversion (pdf-processor)
1. **Pre-process input:**
   - If DOCX → convert to PDF via docx2pdf
   - If PDF > `PDF_SPLIT_PAGE_SIZE` (25 pages) → split via pypdf into N smaller PDFs (e.g., 100 pages → 4 × 25-page PDFs)
   - Single small PDFs pass through unchanged
2. Route each PDF to docling-serve, convert in parallel
3. Concatenate markdown from split PDFs in page order
4. Receive markdown with per-element confidence scores from docling
5. Elements with confidence ≥ `DOCLING_CONFIDENCE_THRESHOLD` → status `auto_resolved`
6. Collect pages for elements with confidence < threshold
7. Run arrase on those specific pages: `ocr --include <page-list> original.pdf`
8. Compare arrase output against docling for each element
9. Elements still below `ARRASE_CONFIDENCE_FLOOR` → OpenRouter vision model with focused page/image
10. Elements below `LLM_OCR_CONFIDENCE_FLOOR` → status `needs_review`
11. Write `raw-markdown/{name}-{date}.md` + `{name}-{date}.elements.json`
12. Update `pipeline_state.stage` → `"chunking"`

### Stage 2: Segmentation (markdown-chunker)
1. Parse document structure from raw markdown — identify TOC patterns, H1/H2/H3 hierarchy, copyright/boilerplate pages
2. Extract TOC as standalone chunk (chunk-000 / part-000)
3. If no TOC detectable: use LLM to infer structure from heading patterns
4. Use TOC to map chapter/section boundaries
5. Partition content by H1-H2 sections; each major section becomes a chunk
6. Word count check: split oversized sections at next sub-heading; flag if hard ceiling exceeded
7. Assign each element from sidecar to its owning chunk (`owning_chunk` field)
8. Write `processed/{subfolder}/{name}-part-NNN-{date}.md` files with full `processed-segment` metadata headers
9. Write segment map into chunk-000 with `[[wikilinks]]` to all parts
10. Update `pipeline_state.stage` → `"remediating"`

### Stage 3: Auto-Remediation (document-processor)
For each element with status `pending`:

**Equations/Terms:**
1. Ask LLM: "Do you recognize this: {markdown_representation}?"
2. If confident + context match → `auto_resolved`, `resolved_by: "llm_knowledge"`
3. If uncertain → websearch by equation name/context
4. If websearch confirms → `auto_resolved`, `resolved_by: "websearch"`
5. If still uncertain after 3 attempts → `needs_review`

**Tables:**
1. Check `ocr_confidence`
2. ≥ 0.8 → `auto_resolved`
3. 0.5–0.8 → re-crop from original PDF, send to OpenRouter vision for verification
4. < 0.5 after 3 attempts → `needs_review`

**Images/Diagrams:**
1. Send to OpenRouter vision: "Describe this figure. What does it show?"
2. Coherent description → `auto_resolved`, replace alt text
3. Unclear → `needs_review`

Update `pipeline_state.stage` accordingly:
- No blockers → `"approved"` (if all elements resolved)
- Has `needs_review` elements → `"review"`

### Stage 4: Human Review
1. User opens sidecar, sees elements with `status: needs_review`
2. For each: user provides corrected markdown, adjusts confidence, or accepts as-is
3. Mark `resolved_human`
4. When all resolved → `pipeline_state.stage` = `"approved"`

---

## 5. Integration with Existing Systems

### Directory Structure Addition
```
raw-markdown/            # NEW: Raw markdown output from pdf-processor (pre-chunking)
```

### Linter Extensions (`scripts/lint.py`)
Two new checks for the external KB:
- **`unapproved_processed` (warning):** `processed/` files whose sidecar has `pipeline_state.stage` ≠ `"approved"` — not ready for ingestion
- **`dangling_elements` (error):** Elements in sidecar with `owning_chunk` pointing to a non-existent file

### Sync-check Extensions
- Verify `raw-markdown/` exists in directory schema
- Verify new config keys present in `scripts/config.py`
- Verify three agent definitions cross-reference each other correctly
- Verify pdf-processor and markdown-chunker registered in agent lists

### Wiki Maintainer (Ingest Gate)
During ingest step 0 (pre-processing check), before ingesting any `processed/` chunks:
1. Locate the corresponding sidecar JSON
2. Check `pipeline_state.stage`
3. If ≠ `"approved"` → reject with message: "Document not approved for ingestion. Current state: {stage}. Run document-processor to complete the pipeline."
4. If `"approved"` → proceed with standard ingest workflow

### Wiki Logging
```
## [2026-05-14] process | my-paper.pdf → 12 chunks, 47 elements, 3 need review
## [2026-05-14] approve | my-paper.pdf → approved for wiki ingestion
```

---

## 6. Error Handling

| Scenario | Behavior |
|----------|----------|
| docling-serve unreachable | Retry 3x (5s backoff), then fail with message: "Is the Docker container running? `docker run -p 8000:8000 docling-serve`" |
| Corrupted PDF (docling error) | Log the page range, create placeholder: `> [Page 42-45: Conversion failed — requires manual extraction]`, element `status: error` |
| PDF > 25 pages | Split via pypdf into N × 25-page PDFs, convert in parallel via docling, concatenate markdown in page order |
| DOCX file | Convert to PDF via docx2pdf first, then process as PDF |
| docx2pdf fails | Skip PDF conversion, try sending DOCX directly to docling-serve (it supports DOCX natively). If that also fails, mark as error |
| arrase/Ollama unreachable | Skip arrase, go straight to OpenRouter OCR. Log warning |
| OpenRouter API error / rate limit | Exponential backoff (1s→2s→4s→8s), then `needs_review` with `review_reason: "ocr_unavailable"` |
| No detectable structure (no H1/H2) | Fall back to word-count chunking at ~1,500 words, splitting at double-newlines. Flag first chunk with `review_reason` |
| TOC detection fails | Skip TOC extraction. Use LLM to infer structure from heading patterns |
| Sidecar/chunk drift (manual edits) | `dangling_elements` linter check catches this. Re-run markdown-chunker to regenerate |
| 3 auto-remediation attempts exhausted | Element gets `needs_review`. Never loops beyond `MAX_AUTO_ATTEMPTS` |

---

## 7. Auto-Remediation Flow (Detailed)

```
For each element with status "pending":

1. Route by type:
   ├─ equation/term → Step 2
   ├─ table → Step 3
   └─ image/diagram → Step 4

2. Equation/term:
   2a. Query LLM: "Recognize: {markdown_representation}? Context: {surrounding_text}"
   2b. Confident + matches → auto_resolved (llm_knowledge)
   2c. Uncertain → websearch: "{term} equation/formula definition"
   2d. Websearch confirms → auto_resolved (websearch)
   2e. Still uncertain → needs_review

3. Table:
   3a. ocr_confidence ≥ 0.8 → auto_resolved
   3b. 0.5–0.8 → re-crop page region from PDF, send to OpenRouter vision
   3c. < 0.5 → needs_review

4. Image/diagram:
   4a. Send to OpenRouter vision: "Describe this figure in detail"
   4b. Coherent → auto_resolved, update alt text
   4c. Unclear → needs_review

Attempts tracked in element.attempts[], capped at MAX_AUTO_ATTEMPTS (3).
```

---

## 8. Tools & Dependencies

| Tool | Purpose | Interface |
|------|---------|-----------|
| [docling-serve](https://github.com/docling-project/docling-serve) | Primary file→markdown conversion | Docker, REST API at `localhost:8000` |
| [pypdf](https://pypi.org/project/pypdf/) | Split large PDFs into smaller PDFs pre-docling | Python library |
| [docx2pdf](https://pypi.org/project/docx2pdf/) | Convert DOCX to PDF (normalizes to single input format) | Python library |
| [arrase/OCR](https://github.com/arrase/OCR) | Page-level OCR via Ollama + deepseek-ocr | CLI: `ocr --include <pages> file.pdf` |
| OpenRouter | Vision model fallback for complex tables/images | REST API with `OPENROUTER_API_KEY` |
| Ollama | Local LLM serving for arrase (deepseek-ocr model) | `localhost:11434` |

### Setup Commands
```bash
# docling-serve
docker pull docling-serve
docker run -p 8000:8000 docling-serve

# arrase/OCR
pipx install git+https://github.com/arrase/OCR.git
ollama pull deepseek-ocr:latest

# OpenRouter API key
# set in .env: OPENROUTER_API_KEY=sk-or-v1-...
```

## Open Questions

- Should `approved` be automatic when all elements are `auto_resolved` with zero blockers, or always require an explicit human approval step?
- Should the raw markdown files in `raw-markdown/` be deleted after successful chunking (like raw/ files after processing), or kept for reprocessing?

---

## Related

- Existing agent: `.claude/agents/document-processor.md`
- Schema: `schema/WIKI_SCHEMA.md` (processed-segment type, raw source metadata)
- Workflows: `schema/WIKI_WORKFLOWS.md` (ingest step 0, lint workflow)
- Agents registry: `schema/WIKI_AGENTS.md`
- Config: `scripts/config.py`
