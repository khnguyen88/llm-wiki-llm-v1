# Document Naming and Metadata Convention Design

**Date**: 2026-05-03
**Status**: Draft
**Scope**: Define standardized filename conventions and metadata schemas for processed document segments, deep crawl files, and LLM-generated raw/ai-research files.

---

## Problem

File naming and metadata across the project are inconsistent:

- **Processed documents** use `{base-name}-{date}-part-{###}[-chapter]` with the date after the base name, making it hard to glob by document name and inconsistent with the "date at end" convention used for crawl files
- **Crawl files** already follow a `{website}-{index}-{webpage}-{date}` pattern but it's not formally documented
- **Other LLM-generated files** (web-search, ai-research, video transcripts) have no standardized naming convention
- **Processed segment metadata** lives only in YAML frontmatter and body navigation links, lacking machine-readable fields for page range, subsections, and cross-segment navigation
- No formal metadata schema for processed segments (they're a distinct source type but have no `type` field)

The recently added Raw Source Metadata schema (7 source types with HTML comment envelopes) doesn't cover processed segments or document naming conventions.

## Design

### 1. Processed Document Naming Convention

**New convention:**
```
processed/{subfolder}/{base-name}-part-{###}[-{chapter-##|section-slug}]-{YYYY-MM-DD}.md
```

| Component | Format | Required | Example |
|-----------|--------|----------|---------|
| `base-name` | kebab-case filename stem | Yes | `design-report` |
| `part-###` | Zero-padded part number | Yes | `part-001` |
| `chapter-##` | Chapter number (zero-padded) | No | `chapter-01` |
| `section-slug` | kebab-case section name | No | `thermal-analysis` |
| `YYYY-MM-DD` | Process date (always at end) | Yes | `2026-05-03` |

**Key changes from current:**
- Date moves from after `base-name` to **end of filename** — consistent with crawl file naming and the "date at end" convention for all LLM-generated files
- Page range is **not included in filenames** — it lives in the HTML comment metadata header only

**Examples:**
- `processed/document/design-report-part-001-2026-05-03.md` (minimal)
- `processed/document/design-report-part-001-chapter-01-2026-05-03.md` (with chapter)
- `processed/document/design-report-part-003-chapter-02-thermal-analysis-2026-05-03.md` (chapter + section)

**Old format examples (for reference):**
- `processed/document/design-report-2026-04-22-part-001.md`
- `processed/papers/research-paper-2026-04-22-part-001-chapter-01.md`

### 2. Processed Segment Metadata (processed-segment source type)

Add a `processed-segment` source type to the Raw Source Metadata schema in `WIKI_SCHEMA.md`.

**Format:**
```html
<!--
type: processed-segment
source: raw/document/design-report.pdf
document_name: Design Report
part: 1
total_parts: 7
page_range: 1-15
chapter: 1
section: Introduction
subsections:
  - "1.1 Background"
  - "1.2 Scope"
prev_section: processed/document/design-report-part-000-2026-05-03.md
next_section: processed/document/design-report-part-002-2026-05-03.md
prev_subsection:
next_subsection: "1.1 Background"
process_date: 2026-05-03
-->
```

| Field | Tier | Description |
|-------|------|-------------|
| `type` | Required | Always `processed-segment` |
| `source` | Required | Path to the original raw file |
| `document_name` | Required | Human-readable title of the source document |
| `part` | Required | This segment's part number |
| `total_parts` | Required | Total number of segments |
| `page_range` | Recommended | Page range from source (e.g., `1-15`, `42-58`). Omit if source has no page numbers. |
| `chapter` | Recommended | Chapter or main section number |
| `section` | Recommended | Section heading name |
| `subsections` | Optional | List of subsection headers within this segment |
| `prev_section` | Recommended | Relative path from project root to the previous segment. Omit for first segment. |
| `next_section` | Recommended | Relative path from project root to the next segment. Omit for last segment. |
| `prev_subsection` | Optional | Name of the prior subsection (for cross-segment navigation) |
| `next_subsection` | Optional | Name of the following subsection (for cross-segment navigation) |
| `process_date` | Required | ISO 8601 date when the segment was created |

**Relationship to frontmatter:** The HTML comment header carries provenance and navigation metadata. The YAML frontmatter (title, source, part, total_parts, date, created, chapter, section, word_count, has_images, has_tables) remains for Obsidian/Dataview compatibility. The two overlap intentionally — frontmatter is for display and querying, the HTML comment is for the linter and agent processing.

**Relationship to body navigation:** The existing `← Previous | Part N of M | Next →` wikilink navigation in the segment body stays. The metadata header provides the same information in a machine-parseable format for the linter and agents.

### 3. Deep Crawl File Naming Convention

For web crawl files extracted from an index (like `llms.txt`, `llms-full.txt`, or a sitemap):

```
raw/{subfolder}/{website}-{index-###}-{webpage-topic}-{YYYY-MM-DD}.md
```

| Component | Format | Required | Example |
|-----------|--------|----------|---------|
| `website` | kebab-case site identifier | Yes | `openrouter`, `claude-code` |
| `index-###` | Zero-padded crawl order from index | Yes | `001`, `115` |
| `webpage-topic` | kebab-case page topic/slug | Yes | `api-reference-overview` |
| `YYYY-MM-DD` | Date crawled (always at end) | Yes | `2026-05-03` |

**Examples:**
- `raw/document/openrouter-115-api-reference-overview-2026-04-29.md`
- `raw/document/claude-code-001-admin-setup-2026-04-29.md`

This codifies the existing naming pattern. Going forward, indices should be zero-padded to 3 digits. Existing files are not renamed — the convention applies to new files only.

The `web-crawl` metadata type already captures `website`, `webpage`, and `index` fields in the HTML comment header. No changes needed to the metadata schema for crawl files.

### 4. LLM-Generated Raw and AI-Research File Naming Convention

All LLM-generated files in `raw/` and `ai-research/` must end with the curation date in `YYYY-MM-DD` format:

```
{subfolder}/{slug}-{YYYY-MM-DD}.md
```

| Source Type | Naming Pattern | Example |
|-------------|---------------|---------|
| `web-search` | `{topic-slug}-{YYYY-MM-DD}.md` | `raw/web/llm-quantization-2026-05-03.md` |
| `video-transcript` | `{channel-or-topic}-{YYYY-MM-DD}.md` | `raw/transcripts/karpathy-llm-wiki-2026-05-03.md` |
| `video-transcript-llm` | `{channel-or-topic}-{YYYY-MM-DD}.md` | `raw/transcripts/3b1b-attention-2026-05-03.md` |
| `ai-research` | `{website}-{slug}-{YYYY-MM-DD}.md` | `ai-research/web/openrouter-pricing-2026-05-03.md` |
| `ai-research-multi` | `{topic-slug}-{YYYY-MM-DD}.md` | `ai-research/web/quantization-techniques-2026-05-03.md` |
| `manual` | `{descriptive-slug}-{YYYY-MM-DD}.md` | `raw/articles/llm-wiki-pattern-2026-05-03.md` |

**Rule:** The date always comes at the end, just before `.md`. This applies to all source types going forward. Existing files are not renamed.

**Exception:** `web-crawl` files use their own naming convention (Section 3) which already ends with the date.

---

## Files to Modify

1. **`schema/WIKI_SCHEMA.md`** — Add `processed-segment` source type to Raw Source Metadata section; update Processed File Naming section to use new convention; add LLM-Generated File Naming section
2. **`.claude/agents/document-processor.md`** — Update Naming Convention, Segment Frontmatter, and add metadata header generation; update segment body navigation to include subsection info
3. **`.claude/agents/wiki-linter.md`** — Add `processed-segment` to valid source types; add naming convention lint checks; add filename date-suffix validation
4. **`.claude/agents/wiki-maintainer.md`** — Update Ingest step to reference new naming and metadata for processed segments
5. **`.claude/agents/sync-check.md`** — Add naming convention consistency checks
6. **`schema/WIKI_WORKFLOWS.md`** — Update Ingest workflow step 0 to reference new processed document naming