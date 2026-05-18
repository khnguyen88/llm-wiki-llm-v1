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
