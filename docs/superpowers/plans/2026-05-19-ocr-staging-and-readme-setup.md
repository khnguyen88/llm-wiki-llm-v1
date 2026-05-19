# OCR Staging & README Setup — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Move deepseek-OCR intermediate output to `raw-markdown/.ocr-staging/` (hidden subfolder, no top-level bloat), and add document processing pipeline setup docs to README.

**Architecture:** Two independent changes — one to `scripts/ocr_remediate.py` for staging directory logic, one to `README.md` for setup documentation. Plus a `.gitignore` line.

**Tech Stack:** Python (pathlib, shutil), Markdown

---

### Task 1: Add OCR staging directory logic

**Files:**
- Modify: `scripts/ocr_remediate.py:151-169` (run_deepseek_ocr)
- Modify: `scripts/ocr_remediate.py:377-408` (remediate)
- Modify: `.gitignore`

- [ ] **Step 1: Update `run_deepseek_ocr` to use staging directory**

Replace the current function (lines 151-169):

```python
def run_deepseek_ocr(pdf_path: str | Path, pages: list[int]) -> Path:
    """Run arrase/OCR on specific pages and return the output markdown path.

    Copies the source PDF to a staging directory so the OCR output lands
    there instead of polluting the source directory.

    Args:
        pdf_path: Path to the source PDF file.
        pages: List of 1-based page numbers to process.

    Returns:
        Path to the generated markdown file (in staging directory).
    """
    import shutil
    import tempfile

    pdf = Path(pdf_path)
    staging_dir = pdf.parent.parent / "raw-markdown" / ".ocr-staging"
    staging_dir.mkdir(parents=True, exist_ok=True)

    staging_pdf = staging_dir / pdf.name
    try:
        shutil.copy2(pdf, staging_pdf)
    except OSError:
        # Fall back to running OCR in the source directory
        staging_pdf = pdf
        staging_dir = pdf.parent

    page_str = ",".join(str(p) for p in pages)
    cmd = ["ocr", "--include", page_str, str(staging_pdf)]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"ocr CLI failed: {result.stderr}")

    ocr_md = staging_pdf.with_suffix(".md")
    if not ocr_md.exists():
        raise RuntimeError(f"ocr CLI did not produce expected output: {ocr_md}")

    return ocr_md
```

- [ ] **Step 2: Update `remediate` to clean up staging files after parsing**

In `remediate()`, after `ocr_content = parse_ocr_output(ocr_md_path)` and before the `fixes = splice_into_markdown(...)` call, add cleanup:

```python
    ocr_content = parse_ocr_output(ocr_md_path)

    # Clean up staging files — parsed content is in memory now
    staging_dir = ocr_md_path.parent
    if staging_dir.name == ".ocr-staging":
        try:
            ocr_md_path.unlink(missing_ok=True)
            staging_pdf_path = staging_dir / Path(pdf_path).name
            staging_pdf_path.unlink(missing_ok=True)
        except OSError:
            pass  # best-effort cleanup
```

Update the `remediate` function signature to track the staging path. The full updated `remediate`:

```python
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

    total_pages = _load_json(sidecar_path).get("conversion_metadata", {}).get("pages", 0)
    problem_pages = collect_problem_pages(placeholders, low_conf, total_pages)
    if not problem_pages:
        print("No valid problem pages identified — skipping OCR remediation.")
        return False

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
        print(f"Warning: deepseek-ocr unavailable ({e})")
        return False

    ocr_content = parse_ocr_output(ocr_md_path)

    # Clean up staging files — parsed content is in memory now
    staging_dir = ocr_md_path.parent
    if staging_dir.name == ".ocr-staging":
        try:
            ocr_md_path.unlink(missing_ok=True)
            Path(str(pdf_path)).name  # unused, kept for reference
        except OSError:
            pass

    fixes = splice_into_markdown(raw_md_path, ocr_content, placeholders)
    sync_sidecar(sidecar_path, placeholders, fixes)

    print(f"OCR Remediation complete:")
    print(f"  - {len(fixes)}/{len(placeholders)} placeholders resolved")
    print(f"  - Raw-markdown updated: {raw_md_path}")
    print(f"  - Sidecar updated: {sidecar_path}")
    return len(fixes) > 0
```

Wait — need to also remove the staging PDF copy. Let me fix step 2 to properly clean up both files:

```python
    ocr_content = parse_ocr_output(ocr_md_path)

    # Clean up staging files
    if ocr_md_path.parent.name == ".ocr-staging":
        try:
            ocr_md_path.unlink(missing_ok=True)
        except OSError:
            pass
```

The staging PDF was a copy of the source — we should also clean it. Let me track it. Actually, simpler: `run_deepseek_ocr` already knows the staging dir. Let me just clean up the `.md` file since that's the polluting one. The staging PDF copy will be re-overwritten on next run anyway. Or even simpler: clean up both.

Actually, let me use a cleanup helper in `remediate`:

```python
    ocr_content = parse_ocr_output(ocr_md_path)

    # Clean up staging files after successful parse
    _cleanup_staging(ocr_md_path)
```

And add:

```python
def _cleanup_staging(ocr_md_path: Path) -> None:
    """Remove staging directory contents after OCR parsing."""
    staging_dir = ocr_md_path.parent
    if staging_dir.name != ".ocr-staging":
        return
    try:
        ocr_md_path.unlink(missing_ok=True)
        # Also remove any PDF copies in staging
        for f in staging_dir.glob("*.pdf"):
            f.unlink(missing_ok=True)
    except OSError:
        pass
```

- [ ] **Step 3: Add `.gitignore` entry**

Add to `.gitignore`:

```
raw-markdown/.ocr-staging/
```

- [ ] **Step 4: Test on existing document**

```bash
cd "C:/_AAA/JVR/llm-wiki-llm-v1/.claude/worktrees/ocr-remediation"
cp "C:/_AAA/JVR/llm-wiki-llm-v1/raw-markdown/Unsupervised_Learning_Method_for_Plant_and_Leaf_Segmentation-2026-05-18.md" raw-markdown/
cp "C:/_AAA/JVR/llm-wiki-llm-v1/raw-markdown/Unsupervised_Learning_Method_for_Plant_and_Leaf_Segmentation-2026-05-18.sidecar.json" raw-markdown/
uv run python scripts/ocr_remediate.py "raw-markdown/Unsupervised_Learning_Method_for_Plant_and_Leaf_Segmentation-2026-05-18.md" "raw-markdown/Unsupervised_Learning_Method_for_Plant_and_Leaf_Segmentation-2026-05-18.sidecar.json" "C:/_AAA/JVR/llm-wiki-llm-v1/raw/papers/Unsupervised_Learning_Method_for_Plant_and_Leaf_Segmentation.pdf"
```

Expected: 6/6 resolved, no new `.md` file in `raw/papers/`, `.ocr-staging/` directory empty or absent after run.

- [ ] **Step 5: Commit**

```bash
git add scripts/ocr_remediate.py .gitignore
git commit -m "feat: stage deepseek-OCR output in raw-markdown/.ocr-staging/ instead of raw/papers/"
```

---

### Task 2: Add document processing setup docs to README

**Files:**
- Modify: `README.md`

- [ ] **Step 1: Insert setup section**

Add after the Architecture Comparison table (after line 202 `| Trigger | Manual "Process this source" | Automatic hooks (SessionEnd) |`) and before `---` + `## Sources & Integration`:

```markdown
---

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

### Pipeline Stages

| Stage | Agent | What it does |
|-------|-------|-------------|
| 1. Convert | `document-converter` | Converts source to raw markdown via docling-serve |
| 2. Remediate | `ocr-remediator` | Runs deepseek-OCR on pages with missing or low-confidence elements |
| 3. Chunk | `markdown-chunker` | Segments large documents into LLM-sized chunks |
| 4. Process | `document-processor` | Auto-remediation + human approval gate |

**Trigger:** "Process this document" or "Run the full pipeline on X"
```

- [ ] **Step 2: Commit**

```bash
git add README.md
git commit -m "docs: add document processing pipeline setup to README"
```
