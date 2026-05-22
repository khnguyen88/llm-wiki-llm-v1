"""Tests for split-table merging in sidecar module."""

import json
from pathlib import Path
from scripts.sidecar import create_sidecar, add_element, merge_split_tables


def make_sidecar():
    """Helper: create a sidecar with no elements."""
    return create_sidecar("001a-raw/document/test.pdf", 20)


def test_no_tables_returns_unchanged():
    """No table elements should be unchanged."""
    sc = make_sidecar()
    add_element(sc, "image", page=3, ocr_method="docling", ocr_confidence=0.9,
                markdown_representation="![img](x.png)", bbox=[100, 200, 400, 300])
    before = json.dumps(sc["elements"])
    merge_split_tables(sc, page_height=842)
    after = json.dumps(sc["elements"])
    assert before == after


def test_single_table_no_merge():
    """A single table with no continuation should not be merged."""
    sc = make_sidecar()
    add_element(sc, "table", page=5, ocr_method="docling", ocr_confidence=0.9,
                markdown_representation="| A | B |\n|---|---|\n| 1 | 2 |",
                bbox=[100, 200, 500, 400])
    merge_split_tables(sc, page_height=842)
    assert len(sc["elements"]) == 1


def test_split_table_across_pages_gets_merged():
    """Two tables on consecutive pages near page edges should be merged into one."""
    sc = make_sidecar()
    # Page 14 — table ends near page bottom (bbox[3] = 800 > 842*0.85 = 715.7)
    add_element(sc, "table", page=14, ocr_method="docling", ocr_confidence=0.9,
                markdown_representation="| Name | Value |\n|---|---|\n| foo | 10 |",
                bbox=[100, 700, 500, 800])
    # Page 15 — table starts near page top (bbox[1] = 10 < 842*0.15 = 126.3)
    add_element(sc, "table", page=15, ocr_method="docling", ocr_confidence=0.9,
                markdown_representation="| Name | Value |\n|---|---|\n| bar | 20 |",
                bbox=[100, 10, 500, 200])

    merge_split_tables(sc, page_height=842)

    assert len(sc["elements"]) == 1
    merged = sc["elements"][0]
    assert merged["page_range"] == [14, 15]
    assert "merged_from" in merged
    assert len(merged["merged_from"]) == 1
    assert "foo" in merged["markdown_representation"]
    assert "bar" in merged["markdown_representation"]
    # Header should only appear once
    assert merged["markdown_representation"].count("|---|---") == 1


def test_non_consecutive_pages_not_merged():
    """Tables on non-consecutive pages should NOT be merged."""
    sc = make_sidecar()
    add_element(sc, "table", page=5, ocr_method="docling", ocr_confidence=0.9,
                markdown_representation="| A |\n|---|\n| 1 |",
                bbox=[100, 700, 500, 800])
    add_element(sc, "table", page=7, ocr_method="docling", ocr_confidence=0.9,
                markdown_representation="| A |\n|---|\n| 2 |",
                bbox=[100, 10, 500, 200])

    merge_split_tables(sc, page_height=842)

    assert len(sc["elements"]) == 2


def test_table_not_near_page_bottom_does_not_merge():
    """A table ending mid-page should NOT trigger a merge even on consecutive pages."""
    sc = make_sidecar()
    # Table ends at y=400 (mid-page, well below the 0.85 threshold)
    add_element(sc, "table", page=8, ocr_method="docling", ocr_confidence=0.9,
                markdown_representation="| A |\n|---|\n| 1 |",
                bbox=[100, 200, 500, 400])
    add_element(sc, "table", page=9, ocr_method="docling", ocr_confidence=0.9,
                markdown_representation="| A |\n|---|\n| 2 |",
                bbox=[100, 10, 500, 200])

    merge_split_tables(sc, page_height=842)

    assert len(sc["elements"]) == 2


def test_three_page_table_chain_merges():
    """A table spanning 3 consecutive pages should merge into one element."""
    sc = make_sidecar()
    add_element(sc, "table", page=10, ocr_method="docling", ocr_confidence=0.9,
                markdown_representation="| Col |\n|---|\n| a |",
                bbox=[100, 700, 500, 800])
    add_element(sc, "table", page=11, ocr_method="docling", ocr_confidence=0.9,
                markdown_representation="| Col |\n|---|\n| b |",
                bbox=[100, 10, 500, 200])
    add_element(sc, "table", page=12, ocr_method="docling", ocr_confidence=0.9,
                markdown_representation="| Col |\n|---|\n| c |",
                bbox=[100, 10, 500, 200])

    merge_split_tables(sc, page_height=842)

    assert len(sc["elements"]) == 1
    merged = sc["elements"][0]
    assert merged["page_range"] == [10, 12]
    assert len(merged["merged_from"]) == 2
    assert "a" in merged["markdown_representation"]
    assert "b" in merged["markdown_representation"]
    assert "c" in merged["markdown_representation"]


def test_mixed_element_types_dont_merge():
    """A table followed by an image on the next page should NOT merge."""
    sc = make_sidecar()
    add_element(sc, "table", page=4, ocr_method="docling", ocr_confidence=0.9,
                markdown_representation="| X |\n|---|\n| 1 |",
                bbox=[100, 700, 500, 800])
    add_element(sc, "image", page=5, ocr_method="docling", ocr_confidence=0.9,
                markdown_representation="![img](y.png)", bbox=[100, 10, 500, 200])

    merge_split_tables(sc, page_height=842)

    assert len(sc["elements"]) == 2


def test_merge_preserves_pipeline_state():
    """After merging, pipeline state counts should reflect the merge."""
    sc = make_sidecar()
    add_element(sc, "table", page=1, ocr_method="docling", ocr_confidence=0.9,
                markdown_representation="| A |\n|---|\n| 1 |",
                bbox=[100, 700, 500, 800])
    add_element(sc, "table", page=2, ocr_method="docling", ocr_confidence=0.9,
                markdown_representation="| A |\n|---|\n| 2 |",
                bbox=[100, 10, 500, 200])

    merge_split_tables(sc, page_height=842)

    ps = sc["pipeline_state"]
    assert ps["total_elements"] == 1
    assert ps["resolved"] == 1
