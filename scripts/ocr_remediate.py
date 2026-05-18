"""
OCR remediation for docling output.

Scans raw-markdown for placeholder comments and low-confidence sidecar elements,
runs deepseek-ocr (arrase/OCR) on specific pages, and splices fixes back in.
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

from sidecar import add_element, load_sidecar, save_sidecar, update_element_status


# ── Constants ──────────────────────────────────────────────────────────────

PLACEHOLDER_PATTERN = re.compile(r"<!--\s*(formula|table|diagram)-not-decoded\s*-->")
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
        if p["page"] > 0:
            pages.add(p["page"])
    for e in low_conf:
        if e["page"] > 0:
            pages.add(e["page"])
    return sorted(pages) if pages else []


def _infer_page(lines: list[str], line_idx: int) -> int:
    """Infer page number from surrounding content markers.

    Looks for page break markers (e.g., '--- page 3 ---') or image references
    with page info near the placeholder.
    """
    page_marker = re.compile(r"---\s*page\s*(\d+)\s*---|\[page\s*(\d+)\]", re.IGNORECASE)

    for offset in range(-10, 10):
        idx = line_idx + offset
        if 0 <= idx < len(lines):
            m = page_marker.search(lines[idx])
            if m:
                return int(m.group(1) or m.group(2))

    return 0  # unknown — caller filters out page 0


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
        subprocess.run(
            [sys.executable, "-c", f"from docx2pdf import convert; convert({str(source)!r}, {str(pdf_path)!r})"],
            check=True,
            capture_output=True,
        )
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
        {page_number: {"text": ["line1", "line2", ...]}}
    """
    text = Path(ocr_md_path).read_text(encoding="utf-8")

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

def splice_into_markdown(md_path: str | Path, ocr_content: dict, placeholders: list[dict]) -> dict[str, str]:
    """Replace placeholders in raw markdown with deepseek-OCR output.

    Args:
        md_path: Path to the raw markdown file (modified in place).
        ocr_content: Parsed OCR output from parse_ocr_output().
        placeholders: Results from scan_placeholders().

    Returns:
        Mapping of placeholder line_number -> markdown_representation for fixes applied.
    """
    md_path = Path(md_path)
    lines = md_path.read_text(encoding="utf-8").split("\n")

    # Build page → OCR text lookup
    page_text: dict[int, str] = {}
    for page, content in ocr_content.items():
        page_text[page] = "\n".join(content.get("text", []))

    fixes = {}
    for ph in placeholders:
        page = ph["page"]
        line_idx = ph["line_number"]
        if page in page_text and page > 0:
            replacement = _extract_element_from_page_text(page_text[page], ph["type"])
            if replacement:
                lines[line_idx] = replacement
                fixes[str(line_idx)] = replacement

    md_path.write_text("\n".join(lines), encoding="utf-8")
    return fixes


def _extract_element_from_page_text(page_text: str, element_type: str) -> str | None:
    """Extract an element (formula, table) from deepseek-OCR page text.

    Returns the first matching element found on the page.
    """
    if element_type == "formula":
        # Match LaTeX display/inline math and \[ \] environments
        math_patterns = re.findall(r"\$\$[\s\S]+?\$\$|\$[^$\n]+?\$|\\\[[\s\S]+?\\\]", page_text)
        if math_patterns:
            return math_patterns[0]
        return None

    if element_type == "table":
        # Match markdown table blocks (lines starting and ending with |)
        table_pattern = re.findall(r"(\|[^\n]+\|[\s\S]*?\n\s*\n)", page_text)
        if table_pattern:
            return table_pattern[0].strip()
        return None

    return None


# ── Sidecar sync ───────────────────────────────────────────────────────────

def sync_sidecar(sidecar_path: str | Path, placeholders: list[dict], fixes_applied: dict[str, str]) -> None:
    """Update sidecar with OCR remediation results.

    For each placeholder: if fixed, create or update a sidecar element.
    If not fixed, record as needs_review if an element exists for it.

    Args:
        sidecar_path: Path to the sidecar JSON file.
        placeholders: All placeholders that were found.
        fixes_applied: Mapping of placeholder line_number -> markdown_representation that was spliced.
    """
    sidecar = load_sidecar(sidecar_path)

    for ph in placeholders:
        key = str(ph["line_number"])
        existing = _find_matching_element(sidecar, ph)

        if key in fixes_applied:
            if existing:
                update_element_status(
                    sidecar,
                    existing["id"],
                    status="auto_resolved",
                    resolved_by="arrase_deepseek",
                    markdown_representation=fixes_applied[key],
                )
            else:
                add_element(
                    sidecar,
                    type_=ph["type"],
                    page=ph["page"],
                    ocr_method="arrase-deepseek",
                    ocr_confidence=0.9,
                    markdown_representation=fixes_applied[key],
                )
        elif existing:
            # Placeholder wasn't fixed but element exists — flag for review
            update_element_status(
                sidecar,
                existing["id"],
                status="needs_review",
                review_reason="ocr_unavailable",
            )
        # else: no element and no fix — nothing to record in sidecar

    save_sidecar(sidecar)


def _find_matching_element(sidecar: dict, placeholder: dict) -> dict | None:
    """Find a sidecar element matching a placeholder by page and type."""
    for elem in sidecar.get("elements", []):
        if elem.get("page") == placeholder["page"] and elem.get("type") == placeholder["type"]:
            return elem
    return None


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
    fixes = splice_into_markdown(raw_md_path, ocr_content, placeholders)
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
    sys.exit(0)  # Always exit 0 — best-effort, never blocks pipeline
