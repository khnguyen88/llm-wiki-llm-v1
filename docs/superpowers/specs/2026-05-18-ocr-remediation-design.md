# OCR Remediation Pipeline Stage — Design Spec

**Date:** 2026-05-18
**Status:** approved

## Overview

Add a dedicated OCR remediation stage between document conversion and chunking. When docling produces placeholder comments (`<!-- formula-not-decoded -->`, `<!-- table-not-decoded -->`) or low-confidence elements (confidence < 0.8), the stage runs deepseek-ocr via [arrase/OCR](https://github.com/arrase/OCR) on only the affected pages and splices corrected content back into the raw markdown before chunking.

Includes renaming `pdf-processor` to `document-converter` to reflect its actual scope (PDF, DOCX, PPTX, and any format docling-serve supports).

## Motivation

The current pipeline produced output with 6 `<!-- formula-not-decoded -->` placeholder comments in a 4-page paper, and the sidecar had `"elements": []` — the cascading OCR step defined in the pdf-processor spec was never executed. The remediation step needs to be a dedicated, reliable pipeline stage with clear trigger conditions, not an optional postscript.

---

## 1. Pipeline Architecture

```
raw/anything.{pdf,docx,pptx,...}
  -> Stage 1: document-converter (docling-serve -> raw-markdown + sidecar)
  -> Stage 2: ocr-remediator     (scan placeholders + low-confidence, deepseek-ocr, splice)
  -> Stage 3: markdown-chunker   (segment clean markdown into processed/)
  -> Stage 4: document-processor (auto-remediate remaining, approval gate)
```

Stage 2 is the new addition. It receives raw-markdown + sidecar from document-converter, produces updated raw-markdown + updated sidecar, and hands off to markdown-chunker.

### Rename

`pdf-processor` -> `document-converter`. Agent file renamed. All references in document-processor, wiki-maintainer, and CLAUDE.md updated.

---

## 2. ocr-remediator Agent

### Triggers (either condition activates the page)

- Placeholder comments: `<!-- formula-not-decoded -->`, `<!-- table-not-decoded -->`, `<!-- diagram-not-decoded -->`
- Sidecar elements with `ocr_confidence < 0.8`

### Operations

1. Scan raw-markdown for placeholder comments -> collect page numbers from surrounding context
2. Check sidecar for low-confidence elements -> collect their page numbers
3. Union of problem pages, deduplicated
4. If source is not PDF: convert to PDF (DOCX via docx2pdf, PPTX via LibreOffice)
5. Run `ocr --include <pages>` on the PDF
6. For each problem page, extract specific elements from deepseek-ocr output
7. Splice into docling raw-markdown: replace placeholders with formulas, upgrade low-confidence sections
8. Update sidecar elements to `auto_resolved` with `ocr_method: "deepseek-ocr"`
9. If deepseek-ocr fails on an element AND `OPENROUTER_API_KEY` is set -> attempt OpenRouter vision
10. If OpenRouter unavailable or fails -> `needs_review`
11. Write updated raw-markdown + sidecar

### Handoff Contract

Produces the same file format it received (raw-markdown + sidecar), just with fewer placeholders and more resolved elements. markdown-chunker doesn't need to know ocr-remediator was involved.

---

## 3. scripts/ocr_remediate.py

Callable standalone or from the agent. Key functions:

```
scan_placeholders(md_path) -> [{page, type, line_number, context_lines}]

find_low_confidence(sidecar_path, threshold=0.8) -> [{element_id, page, type, confidence}]

collect_problem_pages(placeholders, low_conf) -> [3, 4]  # deduplicated, sorted

convert_to_pdf(source_path) -> Path
    # no-op if already PDF, .docx -> docx2pdf, .pptx -> LibreOffice, unsupported -> raise

run_deepseek_ocr(pdf_path, pages) -> Path
    # ocr --include 3,4 paper.pdf -> produces paper.md

parse_ocr_output(ocr_md_path) -> {page: {type: markdown_content}}

splice_into_markdown(md_path, fixes) -> updated_md_path

update_sidecar(sidecar_path, fixes)

remediate(raw_md_path, sidecar_path, source_path) -> bool
    # main entry point, returns True if any fixes were applied
```

Page inference for placeholders: docling output includes page break markers or image references with page info. The script uses these to map placeholder line numbers to pages. If no page markers exist, assumes sequential distribution of lines across known page count.

---

## 4. Document-Processor Orchestration Changes

New stage inserted between conversion and chunking:

```
Stage 1: document-converter (was pdf-processor)
Stage 2: ocr-remediator     <- NEW
Stage 3: markdown-chunker
Stage 4: auto-remediation + approval gate
```

Invoke instruction for Stage 2:

```
After document-converter completes, invoke ocr-remediator as a subagent:

"Remediate raw-markdown/{name}-{date}.md using deepseek-ocr:
- Scan for placeholders and low-confidence elements in sidecar
- Convert source to PDF if needed
- Run ocr --include on problem pages
- Splice fixes back into raw-markdown
- Update sidecar with resolved elements"

Wait for ocr-remediator to complete. If it resolves all placeholders, proceed to markdown-chunker.
If elements remain as needs_review, still proceed - markdown-chunker handles them gracefully,
and the auto-remediation stage can attempt LLM-based fixes.
```

---

## 5. Error Handling

| Scenario | Behavior |
|----------|----------|
| `ocr` CLI not installed | Skip deepseek-ocr, try OpenRouter if configured, otherwise `needs_review` |
| Ollama not running / model not pulled | Same as above - skip and fall forward |
| Source format can't convert to PDF | Log warning, skip OCR, mark elements `needs_review`, continue |
| deepseek-ocr produces worse output than docling | Keep docling version - compare by placeholder count reduction |
| No problem pages found | No-op, return clean |
| deepseek-ocr output can't be parsed | Log error, keep original markdown, mark elements `needs_review` |
| Mixed results | Splice successes, flag failures individually in sidecar |

**Principle:** OCR remediation is best-effort. It never blocks the pipeline.

---

## 6. Testing

- Run `ocr_remediate.py` on the existing `Unsupervised_Learning_Method_for_Plant_and_Leaf_Segmentation` document -> verify all 6 `<!-- formula-not-decoded -->` placeholders replaced with formula markdown
- Verify sidecar elements updated with `ocr_method: "deepseek-ocr"` and `status: "auto_resolved"`
- Test with DOCX file to verify PDF conversion path
- Test with deepseek-ocr unavailable to verify graceful fallback
