"""
Element-level sidecar JSON for the document processing pipeline.

The sidecar is the contract between document-converter, ocr-remediator,
markdown-chunker, and document-processor agents. Each agent reads what the
previous wrote, adds its layer, and writes back.
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
VALID_RESOLVED_BY = {"docling_high_confidence", "arrase_deepseek", "llm_knowledge", "websearch", "human"}


# ── Create sidecar ───────────────────────────────────────────────────────

def create_sidecar(
    document_path: str,
    total_pages: int,
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
    if not 0.0 <= ocr_confidence <= 1.0:
        raise ValueError(f"ocr_confidence must be between 0.0 and 1.0, got {ocr_confidence}")

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
    return sum(1 for e in sidecar["elements"] if e["status"] in ("pending", "needs_review", "error"))


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
