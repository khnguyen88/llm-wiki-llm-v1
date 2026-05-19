# OCR Staging Directory & README Setup Design

> **Goal:** Keep deepseek-OCR intermediate output out of `raw/papers/`, and document the document processing pipeline prerequisites in README.

**Scope:** Two small, independent changes — a single file edit to `scripts/ocr_remediate.py` for staging, and a section addition to `README.md` for setup docs.

---

## 1. OCR Staging Directory

### Problem

The `ocr` CLI from [arrase/OCR](https://github.com/arrase/OCR) always creates `<input>.md` in the same directory as the input PDF. Currently `run_deepseek_ocr` calls `ocr --include <pages> <pdf>` which writes the intermediate `.md` file back into `raw/papers/`, polluting the source directory.

### Solution

Use `raw-markdown/.ocr-staging/` as a transient working directory:

1. `run_deepseek_ocr` copies the source PDF into `raw-markdown/.ocr-staging/`
2. Runs `ocr --include <pages>` on the copy
3. The `.md` output lands in `.ocr-staging/` beside the copy
4. `parse_ocr_output` reads and parses it
5. `run_deepseek_ocr` deletes the staging copy and returns the path (caller deletes after parsing)
6. `remediate()` cleans up the `.md` file after parsing

Add `raw-markdown/.ocr-staging/` to `.gitignore`.

### Files changed

- **`scripts/ocr_remediate.py`**: `run_deepseek_ocr` function — copy PDF to staging, run OCR there, return staging `.md` path. `remediate` — delete staging `.md` after parsing.
- **`.gitignore`**: Add `raw-markdown/.ocr-staging/`

### Error handling

- If staging dir creation fails: log warning, fall back to running OCR in source dir (current behavior)
- If copy fails: same fallback
- Cleanup is best-effort — never fail if staging files can't be deleted

---

## 2. README Setup Documentation

### Problem

The README describes the knowledge base architecture but has no setup instructions for the document processing pipeline (docling-serve, deepseek-OCR, `.docling.env`).

### Solution

Add a **"Document Processing Pipeline Setup"** section after the Architecture Comparison table, before Sources & Integration.

Content to cover:

```markdown
## Document Processing Pipeline Setup

The document processing pipeline converts PDF, DOCX, and PPTX files to
markdown, runs OCR remediation on problem pages, and segments large documents
for wiki ingestion.

### Prerequisites

1. **docling-serve** (document conversion):

   ```bash
   docker pull quay.io/docling-project/docling-serve
   docker run -d -p 5001:5001 docling-serve
   ```

2. **Environment configuration**:

   ```bash
   cp .env.example .docling.env
   # Edit .docling.env — set OPENROUTER_API_KEY (optional, for vision fallback)
   ```

3. **arrase/OCR CLI** (deepseek-OCR remediation):

   ```bash
   pipx install git+https://github.com/arrase/OCR.git
   ```

4. **Ollama + deepseek-ocr model**:

   ```bash
   ollama pull deepseek-ocr:latest
   ```

### Pipeline stages

1. **document-converter** — converts source to raw markdown via docling-serve
2. **ocr-remediator** — runs deepseek-OCR on pages with missing/low-confidence elements
3. **markdown-chunker** — segments into LLM-sized chunks
4. **document-processor** — auto-remediation + human approval gate

Trigger: "Process this document" or "Run the full pipeline on X"
```

### Files changed

- **`README.md`**: Insert section between Architecture Comparison and Sources & Integration

---

## Self-Review

- **Placeholder scan**: No TBDs or TODOs — both items are fully specified with exact code paths and content.
- **Internal consistency**: Both items are independent, no cross-dependencies. The staging dir name `raw-markdown/.ocr-staging/` is referenced consistently.
- **Scope**: Two single-file changes, one new gitignore line. Tight and minimal.
- **Ambiguity**: None. Exact Markdown content for README section provided. Exact function behavior for staging described.
