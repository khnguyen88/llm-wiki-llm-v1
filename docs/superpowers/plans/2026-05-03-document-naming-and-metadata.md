# Document Naming and Metadata Convention Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Standardize filename conventions for processed document segments, deep crawl files, and LLM-generated raw/ai-research files; add the `processed-segment` source type to the Raw Source Metadata schema; update agents and linter to enforce the new conventions.

**Architecture:** Extend the existing Raw Source Metadata schema (HTML comment envelope format) with an 8th source type (`processed-segment`) and add formal naming convention sections to `WIKI_SCHEMA.md`. Update document-processor, wiki-linter, wiki-maintainer, sync-check, and WIKI_WORKFLOWS.md to reference the new conventions. No retroactive renaming of existing files.

**Tech Stack:** Markdown documentation, YAML frontmatter conventions, HTML comment metadata blocks.

---

## File Structure

| File | Action | Purpose |
|------|--------|---------|
| `schema/WIKI_SCHEMA.md` | Modify (Raw Source Metadata section + add naming sections) | Add `processed-segment` source type; add Processed File Naming, Crawl File Naming, LLM-Generated File Naming sections |
| `.claude/agents/document-processor.md` | Modify (Naming Convention, Segment Frontmatter, add metadata header step) | Update naming to new convention; add metadata header generation step; update frontmatter to include page_range and subsections |
| `.claude/agents/wiki-linter.md` | Modify (check #12 + add check #13) | Add `processed-segment` to valid types; add filename convention lint check |
| `.claude/agents/wiki-maintainer.md` | Modify (Conventions section + Research steps) | Add file naming convention for raw/ai-research files |
| `.claude/agents/sync-check.md` | Modify (section 4 + section 8) | Update processed file naming convention; add crawl/LLM naming convention checks |
| `schema/WIKI_WORKFLOWS.md` | Modify (Ingest step 0) | Reference new processed document naming convention |

---

### Task 1: Update WIKI_SCHEMA.md — Add processed-segment source type

**Files:**
- Modify: `schema/WIKI_SCHEMA.md` (Raw Source Metadata → Source Types section, after type 7 `manual`)

- [ ] **Step 1: Add the processed-segment source type after the `manual` type definition**

After the `manual` type table (the last row of which reads `| \`fetched_date\` | Required | ISO 8601 date when the source was added |`) and before `## Index Format`, insert:

```markdown
**8. `processed-segment`** — Segmented chunk of a large document in `processed/`.

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
| `source` | Required | Relative path to the original raw file |
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
```

- [ ] **Step 2: Update the linter type list in the raw-source-metadata description**

In the Raw Source Metadata section's introductory paragraph, the text currently reads: "This applies to any web crawler or MCP extraction, web search results, video transcript extractions, and AI research files." Update to also mention processed segments:

Replace:

```
This applies to any web crawler or MCP extraction, web search results, video transcript extractions, and AI research files.
```

With:

```
This applies to any web crawler or MCP extraction, web search results, video transcript extractions, AI research files, and processed document segments.
```

- [ ] **Step 3: Verify the edit renders correctly**

Read the modified file and confirm:
- The `processed-segment` type appears as type 8 after `manual` and before `## Index Format`
- The introductory paragraph mentions processed segments
- The anchor link structure is intact

- [ ] **Step 4: Commit**

```bash
git add schema/WIKI_SCHEMA.md
git commit -m "feat: add processed-segment source type to Raw Source Metadata schema

Adds the 8th source type with navigation fields (prev/next section,
subsection), page range, and document identification fields for
processed document segments.

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>"
```

---

### Task 2: Update WIKI_SCHEMA.md — Add naming convention sections

**Files:**
- Modify: `schema/WIKI_SCHEMA.md` (after Page Naming Conventions section, around line 59)

- [ ] **Step 1: Add three new naming convention sections after the Page Naming Conventions table**

After the Page Naming Conventions table (the row ending with `| Q&A | kebab-case | qanda/what-is-attention.md |`) and before `## Frontmatter Format`, insert:

```markdown
### Processed File Naming

Files in `processed/` follow this convention:

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

Examples:
- `processed/document/design-report-part-001-2026-05-03.md`
- `processed/document/design-report-part-001-chapter-01-2026-05-03.md`
- `processed/document/design-report-part-003-chapter-02-thermal-analysis-2026-05-03.md`

Page range is captured in the metadata header only, not in filenames.

### Crawl File Naming

Web crawl files extracted from an index (e.g., `llms.txt`, sitemap) follow:

```
raw/{subfolder}/{website}-{index-###}-{webpage-topic}-{YYYY-MM-DD}.md
```

| Component | Format | Required | Example |
|-----------|--------|----------|---------|
| `website` | kebab-case site identifier | Yes | `openrouter`, `claude-code` |
| `index-###` | Zero-padded crawl order from index | Yes | `001`, `115` |
| `webpage-topic` | kebab-case page topic/slug | Yes | `api-reference-overview` |
| `YYYY-MM-DD` | Date crawled (always at end) | Yes | `2026-05-03` |

Examples:
- `raw/document/openrouter-115-api-reference-overview-2026-04-29.md`
- `raw/document/claude-code-001-admin-setup-2026-04-29.md`

### LLM-Generated File Naming

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

Exception: `web-crawl` files use the Crawl File Naming convention above.
```

- [ ] **Step 2: Verify the edit renders correctly**

Read the modified file and confirm:
- Three new subsections appear after Page Naming Conventions and before Frontmatter Format
- All table formatting is intact
- No markdown rendering issues

- [ ] **Step 3: Commit**

```bash
git add schema/WIKI_SCHEMA.md
git commit -m "feat: add processed, crawl, and LLM-generated file naming conventions

Three new naming convention sections: processed files (date at end,
part-### format), crawl files (website-index-topic-date), and
LLM-generated files (slug-date). All enforce YYYY-MM-DD at end.

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>"
```

---

### Task 3: Update document-processor.md — New naming convention and metadata header

**Files:**
- Modify: `.claude/agents/document-processor.md` (Naming Convention, Segment Frontmatter, add metadata header step)

- [ ] **Step 1: Update the Naming Convention section**

Replace the current naming convention:

```
## Naming Convention

```
processed/{subfolder}/{base-name}-{YYYY-MM-DD}-part-{###}[-{chapter-##|section-slug}].md
```

| Component | Format | Required | Example |
|-----------|--------|----------|---------|
| `base-name` | kebab-case filename stem | Yes | `design-report` |
| `YYYY-MM-DD` | Date of processing | Yes | `2026-04-22` |
| `part-###` | Zero-padded part number | Yes | `part-001` |
| `chapter-##` | Chapter number (zero-padded) | No, for reports/papers | `chapter-01` |
| `section-slug` | kebab-case section name | No | `introduction` |

**Examples:**
- `processed/document/design-report-2026-04-22-part-001.md` (simple document, no chapters)
- `processed/papers/research-paper-2026-04-22-part-001-chapter-01.md` (paper with chapters)
- `processed/document/engineering-spec-2026-04-22-part-003-chapter-02-thermal-analysis.md` (chapter + section)
```

With:

```
## Naming Convention

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

**Examples:**
- `processed/document/design-report-part-001-2026-05-03.md` (simple document, no chapters)
- `processed/document/design-report-part-001-chapter-01-2026-05-03.md` (paper with chapters)
- `processed/document/engineering-spec-part-003-chapter-02-thermal-analysis-2026-05-03.md` (chapter + section)

Page range is captured in the metadata header (see step 4c), not in filenames.
```

- [ ] **Step 2: Update the Segment Frontmatter section**

Replace the current frontmatter example:

```yaml
---
title: "Chapter 2: Thermal Analysis"
source: "raw/design-report.pdf"
part: 3
total_parts: 7
date: 2026-04-22
created: "2026-04-22T12:00:00Z"
chapter: 2
section: "Thermal Analysis"
word_count: 1240
has_images: true
has_tables: true
---
```

With:

```yaml
---
title: "Chapter 2: Thermal Analysis"
source: "raw/design-report.pdf"
part: 3
total_parts: 7
date: 2026-05-03
created: "2026-05-03T12:00:00Z"
chapter: 2
section: "Thermal Analysis"
page_range: "15-28"
subsections:
  - "2.1 Heat Transfer"
  - "2.2 Thermal Resistance"
word_count: 1240
has_images: true
has_tables: true
---
```

Added `page_range` and `subsections` fields to frontmatter. These mirror the same fields in the HTML comment metadata header for Obsidian/Dataview compatibility.

- [ ] **Step 3: Add metadata header generation step**

After step 4b ("Preserve source metadata") and before step 5 ("Write segments"), insert a new step 4c:

```markdown
4c. **Generate processed-segment metadata header** — Write an HTML comment metadata header at the top of each segment file with `type: processed-segment`. Include all fields per the schema in `schema/WIKI_SCHEMA.md`: `source`, `document_name`, `part`, `total_parts`, `page_range` (if available), `chapter`, `section`, `subsections`, `prev_section`, `next_section`, `prev_subsection`, `next_subsection`, and `process_date`. If the original raw file had an HTML comment metadata header, combine its fields with the processed-segment fields — the raw source metadata header goes only on the first segment (step 4b), while every segment gets its own `processed-segment` header.
```

- [ ] **Step 4: Update the Segment Body section to include subsection navigation**

After the existing navigation links line:

```markdown
← [[processed/{subfolder}/{prev-segment}|Previous]] | Part 3 of 7 | [[processed/{subfolder}/{next-segment}|Next]] →
```

Add a subsection navigation line when subsection info is available:

```markdown
← [[processed/{subfolder}/{prev-segment}|Previous]] | Part 3 of 7 | [[processed/{subfolder}/{next-segment}|Next]] →
↑ Section: Chapter 2 · ↓ Next: 2.1 Heat Transfer
```

The second line is optional — include it only when `section` and `next_subsection`/`prev_subsection` are available.

- [ ] **Step 5: Commit**

```bash
git add .claude/agents/document-processor.md
git commit -m "feat: update document-processor with new naming and metadata conventions

New naming convention (date at end), processed-segment metadata
header generation, page_range and subsections in frontmatter,
subsection navigation in segment body.

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>"
```

---

### Task 4: Update wiki-linter.md — Add processed-segment and naming checks

**Files:**
- Modify: `.claude/agents/wiki-linter.md` (check #12 + add check #13)

- [ ] **Step 1: Add processed-segment to valid types in check #12**

In the raw-source-metadata check (check #12), replace:

```
    - Error: `type` field is not one of the 7 valid values (`web-crawl`, `web-search`, `ai-research`, `ai-research-multi`, `video-transcript`, `video-transcript-llm`, `manual`)
```

With:

```
    - Error: `type` field is not one of the 8 valid values (`web-crawl`, `web-search`, `ai-research`, `ai-research-multi`, `video-transcript`, `video-transcript-llm`, `manual`, `processed-segment`)
```

- [ ] **Step 2: Add processed-segment specific validation rules to check #12**

After the existing `ai-research-multi` rule:

```
    - Error (ai-research-multi): `sources` list is missing or has no entries with `url`
```

Add:

```
    - Error (processed-segment): `source`, `document_name`, `part`, `total_parts`, or `process_date` missing
    - Warning (processed-segment): missing recommended field `page_range`, `prev_section`, or `next_section`
```

- [ ] **Step 3: Add check #13 for filename conventions**

After check #12 (raw-source-metadata) and before `### LLM Judgment Check`, insert:

```markdown
13. **Filename convention** (warning) — LLM-generated files must follow the naming conventions in `schema/WIKI_SCHEMA.md`
    - Warning (processed/): filename does not match `{base-name}-part-{###}[-{chapter-##|section-slug}]-{YYYY-MM-DD}.md` pattern
    - Warning (raw/ crawl files): filename does not match `{website}-{index-###}-{webpage-topic}-{YYYY-MM-DD}.md` pattern
    - Warning (other LLM-generated raw/ai-research/): filename does not end with `-{YYYY-MM-DD}.md`
    - Only validate files with an HTML comment metadata header (skip human-curated files without headers)
```

- [ ] **Step 4: Add filename convention examples to Output Format**

In the `## Output Format` section, in the Warnings list, after the `[raw-source-metadata]` warning line, add:

```markdown
- [filename-convention] `raw/web/llm-quantization.md` missing date suffix in filename (expected `-{YYYY-MM-DD}.md`)
- [filename-convention] `processed/document/report-2026-05-03-part-001.md` uses old naming convention (date before part number)
```

- [ ] **Step 5: Commit**

```bash
git add .claude/agents/wiki-linter.md
git commit -m "feat: add processed-segment validation and filename convention checks

Updated raw-source-metadata check to include 8th type. New check #13
validates filename conventions for processed, crawl, and LLM-generated
files. Only validates files with HTML comment metadata headers.

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>"
```

---

### Task 5: Update wiki-maintainer.md — Add file naming conventions

**Files:**
- Modify: `.claude/agents/wiki-maintainer.md` (Conventions section)

- [ ] **Step 1: Add file naming conventions to the Conventions section**

After the existing `**Naming**` line:

```
- **Naming**: snake_case for entities/concepts, kebab-case for summaries and qanda
```

Add:

```
- **File naming** (raw/ai-research): All LLM-generated files must end with `-{YYYY-MM-DD}.md`. Crawl files: `{website}-{index-###}-{webpage-topic}-{YYYY-MM-DD}.md`. Other types: `{slug}-{YYYY-MM-DD}.md`. See `schema/WIKI_SCHEMA.md` → LLM-Generated File Naming and Crawl File Naming.
- **File naming** (processed): `{base-name}-part-{###}[-{chapter-##|section-slug}]-{YYYY-MM-DD}.md`. See `schema/WIKI_SCHEMA.md` → Processed File Naming.
```

- [ ] **Step 2: Update Research step 2 naming example**

In the Research operation, after the line:

```
2. **One source, one file** — save each URL as a separate markdown file in `ai-research/`
```

Add a note about naming:

```
   - Name the file `{website}-{slug}-{YYYY-MM-DD}.md` per the LLM-Generated File Naming convention in `schema/WIKI_SCHEMA.md`
```

- [ ] **Step 3: Commit**

```bash
git add .claude/agents/wiki-maintainer.md
git commit -m "feat: add file naming conventions to wiki-maintainer

Conventions section now references processed, crawl, and
LLM-generated file naming patterns from WIKI_SCHEMA.md.
Research step 2 includes naming guidance.

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>"
```

---

### Task 6: Update sync-check.md — Naming convention consistency checks

**Files:**
- Modify: `.claude/agents/sync-check.md` (section 4 + section 8)

- [ ] **Step 1: Update the processed file naming convention in section 4**

In section 4 (Conventions), replace:

```
- Processed file naming: `{base-name}-{YYYY-MM-DD}-part-{###}[-{chapter-##|section-slug}].md`
```

With:

```
- Processed file naming: `{base-name}-part-{###}[-{chapter-##|section-slug}]-{YYYY-MM-DD}.md` (date always at end)
- Crawl file naming: `{website}-{index-###}-{webpage-topic}-{YYYY-MM-DD}.md`
- LLM-generated file naming: `{slug}-{YYYY-MM-DD}.md` (date always at end)
```

- [ ] **Step 2: Update section 8 (Raw source metadata) to include processed-segment and naming**

In section 8, replace the current source types list:

```
- **Source types**: The 7 valid types (`web-crawl`, `web-search`, `ai-research`, `ai-research-multi`, `video-transcript`, `video-transcript-llm`, `manual`) must match across WIKI_SCHEMA.md, WIKI_WORKFLOWS.md, wiki-linter, and wiki-maintainer
```

With:

```
- **Source types**: The 8 valid types (`web-crawl`, `web-search`, `ai-research`, `ai-research-multi`, `video-transcript`, `video-transcript-llm`, `manual`, `processed-segment`) must match across WIKI_SCHEMA.md, WIKI_WORKFLOWS.md, wiki-linter, and wiki-maintainer
```

Add after the existing check items:

```
Check that:
- `schema/WIKI_SCHEMA.md` documents all 8 source types with correct required/recommended/optional fields
- `.claude/agents/wiki-linter.md` references the same 8 types and field tiers
- `.claude/agents/wiki-maintainer.md` references the metadata header format
- `schema/WIKI_WORKFLOWS.md` Research step 2 references the metadata schema
- **Naming conventions**: Processed, crawl, and LLM-generated file naming patterns in WIKI_SCHEMA.md must match references in document-processor, wiki-maintainer, and wiki-linter
- **Filename convention lint**: wiki-linter must validate the same naming patterns documented in WIKI_SCHEMA.md
```

- [ ] **Step 3: Commit**

```bash
git add .claude/agents/sync-check.md
git commit -m "feat: update sync-check with new naming conventions and 8th source type

Updated processed file naming to date-at-end format, added crawl and
LLM-generated naming checks, updated source type count to 8.

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>"
```

---

### Task 7: Update WIKI_WORKFLOWS.md — Reference new naming conventions

**Files:**
- Modify: `schema/WIKI_WORKFLOWS.md` (Ingest step 0)

- [ ] **Step 1: Update Ingest step 0 to reference naming convention**

Replace the current step 0:

```
0. **Check source size** (pre-processing)
   - If the file is a PDF, binary document, or exceeds ~3,000 words: invoke the document-processor agent to segment it into `processed/`
   - Small markdown files go directly to step 1
```

With:

```
0. **Check source size** (pre-processing)
   - If the file is a PDF, binary document, or exceeds ~3,000 words: invoke the document-processor agent to segment it into `processed/` using the naming convention in `schema/WIKI_SCHEMA.md` → Processed File Naming
   - Small markdown files go directly to step 1
```

- [ ] **Step 2: Commit**

```bash
git add schema/WIKI_WORKFLOWS.md
git commit -m "feat: reference processed file naming convention in Ingest workflow

Step 0 now points to WIKI_SCHEMA.md Processed File Naming
convention for segmented document output.

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>"
```

---

### Task 8: Run sync-check to verify consistency

**Files:**
- Verify: all modified files are consistent with each other

- [ ] **Step 1: Invoke the sync-check agent**

Run the sync-check agent to verify that all 6 modified files are consistent. The agent will check:
- The 8 source types (including `processed-segment`) match across all files
- Naming conventions are consistent between WIKI_SCHEMA.md, document-processor, wiki-maintainer, wiki-linter, and sync-check
- The linter validates the same types and naming patterns as the schema documents

- [ ] **Step 2: Fix any inconsistencies found by sync-check**

Address any issues reported. Common issues to watch for:
- Mismatched source type counts (7 vs 8)
- Old naming convention patterns still referenced somewhere
- Missing cross-references to new naming convention sections

- [ ] **Step 3: Commit any fixes**

```bash
git add -A
git commit -m "fix: resolve sync-check inconsistencies after naming convention update

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>"
```