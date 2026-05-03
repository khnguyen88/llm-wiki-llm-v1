# Raw Source Metadata Schema Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add standardized metadata headers for LLM-extracted raw sources across 7 source types, update schema docs and agents, and add a raw-source-metadata lint check.

**Architecture:** A two-tier approach where LLM-extracted files must follow the new HTML comment metadata schema (with a `type` discriminator and required/recommended/optional field tiers), while human-curated files are accepted as-is. The schema is documented in `WIKI_SCHEMA.md`, referenced by `WIKI_WORKFLOWS.md`, and enforced by the `wiki-linter` agent.

**Tech Stack:** Markdown documentation, YAML frontmatter conventions, HTML comment metadata blocks.

---

## File Structure

| File | Action | Purpose |
|------|--------|---------|
| `schema/WIKI_SCHEMA.md` | Modify (lines 307–325) | Replace AI-Research Source Files section with reference to new Raw Source Metadata section; add new section after it |
| `schema/WIKI_WORKFLOWS.md` | Modify (lines 194–214) | Update Research workflow step 2 with metadata header requirements |
| `.claude/agents/wiki-linter.md` | Modify (add check after line 26) | Add raw-source-metadata lint check |
| `.claude/agents/wiki-maintainer.md` | Modify (lines 18, 45–49) | Update Ingest step 1 and Research step 3 |
| `.claude/agents/document-processor.md` | Modify (add after line 34) | Add metadata header preservation step |
| `.claude/agents/sync-check.md` | Modify (add new section 8) | Add source types and field requirements to check list |

---

### Task 1: Update WIKI_SCHEMA.md — Add Raw Source Metadata section

**Files:**
- Modify: `schema/WIKI_SCHEMA.md:307–325` (replace AI-Research Source Files section)

- [ ] **Step 1: Replace the AI-Research Source Files section with a reference to the new schema**

Replace lines 307–325 in `schema/WIKI_SCHEMA.md` (the current `### AI-Research Source Files (ai-research/)` section) with:

```markdown
### AI-Research Source Files (`ai-research/`)

When the LLM conducts autonomous web research, save full cleaned source content here. Source metadata uses the HTML comment envelope format defined in [Raw Source Metadata](#raw-source-metadata) — use `type: ai-research` for single sources or `type: ai-research-multi` for multi-source synthesis.

The file body must include a YAML frontmatter block with a `summary` field:

```yaml
---
summary: One-line description of what this source covers
---
```

- One source, one file — never combine multiple URLs into one file (use `type: ai-research` per URL)
- For multi-source synthesis, use `type: ai-research-multi` and list all source URLs in the metadata header
- File names: lowercase hyphenated (e.g., `ai-research/web/qmd-github-readme.md`)
- Immutable once saved — do not overwrite, create new files
- These are the source of truth for citation verification

See [Raw Source Metadata](#raw-source-metadata) for the full metadata schema.
```

- [ ] **Step 2: Add the Raw Source Metadata section after the AI-Research section**

Insert a new section after the AI-Research Source Files section (after the line `See [Raw Source Metadata](#raw-source-metadata) for the full metadata schema.`) and before `## Index Format`:

```markdown
### Raw Source Metadata

All LLM-extracted source files must include an HTML comment metadata header at the top of the file. Human-curated files are accepted as-is — no normalization required.

**Two-tier approach:**
1. **LLM-extracted content** (going forward): Must follow the standardized HTML comment metadata schema. This applies to any web crawler or MCP extraction, web search results, video transcript extractions, and AI research files.
2. **Human-curated content** (existing and future): The linter accepts whatever metadata format is present — YAML frontmatter, HTML comments, or nothing.

#### Format: HTML Comment Envelope

```html
<!--
type: <source-type>
field1: value1
field2: value2
-->
```

- HTML comments are invisible in rendered markdown/Obsidian and don't interfere with YAML frontmatter
- The `type` field determines which other fields are required/recommended/optional

#### Field Tiers

| Tier | Meaning | Linter behavior |
|------|---------|-----------------|
| **Required** | Must be present for LLM-extracted files | Error if missing |
| **Recommended** | Should be present when available | Warning if missing |
| **Optional** | Nice to have, no warning if absent | No check |

If a tool cannot provide a specific field, **omit the field entirely** rather than using placeholder values like `N/A` or `unknown`.

All date fields use ISO 8601 format: `YYYY-MM-DD` (or `YYYY-MM-DDTHH:MM:SSZ` when precision is needed). Field names use `snake_case`.

#### Source Types

**1. `web-crawl`** — Files extracted from websites by any web crawler or MCP tool.

```html
<!--
type: web-crawl
url: https://openrouter.ai/docs/api/reference/overview.mdx
fetched_date: 2026-04-29
website: openrouter
webpage: api-reference-overview
index: 115
published_date: 2026-03-15
-->
```

| Field | Tier | Description |
|-------|------|-------------|
| `type` | Required | Always `web-crawl` |
| `url` | Required | Full URL of the source page |
| `fetched_date` | Required | ISO 8601 date when the page was crawled |
| `website` | Recommended | Domain or site identifier (e.g., `openrouter`, `claude-code`) |
| `webpage` | Recommended | Slug identifying the specific page within the site |
| `index` | Optional | Retrieval order within a crawl batch. Omit if not available. |
| `published_date` | Optional | Original publication date. Omit if not available. |

**2. `web-search`** — Single page retrieved by an LLM web search tool.

```html
<!--
type: web-search
url: https://example.com/article
search_date: 2026-05-03
query: LLM quantization techniques
website: example.com
published_date: 2026-01-15
snippet: Summary of key findings from the page
-->
```

| Field | Tier | Description |
|-------|------|-------------|
| `type` | Required | Always `web-search` |
| `url` | Required | Full URL of the source page |
| `search_date` | Required | ISO 8601 date when the search was performed |
| `query` | Recommended | The search query that found this result |
| `website` | Optional | Domain or site identifier |
| `published_date` | Optional | Original publication date |
| `snippet` | Optional | Brief summary of page content |

**3. `ai-research`** — Single-source AI discovery saved to `ai-research/`.

```html
<!--
type: ai-research
url: https://example.com/article
search_date: 2026-05-03
query: LLM quantization techniques
website: example.com
published_date: 2026-01-15
-->
```

| Field | Tier | Description |
|-------|------|-------------|
| `type` | Required | Always `ai-research` |
| `url` | Required | Full URL of the source |
| `search_date` | Required | ISO 8601 date when the source was discovered |
| `query` | Recommended | Search query that found this source |
| `website` | Optional | Domain or site identifier |
| `published_date` | Optional | Original publication date |

The file body includes a YAML frontmatter `summary` field (separate from the HTML comment metadata).

**4. `ai-research-multi`** — Multi-source AI synthesis saved to `ai-research/`.

```html
<!--
type: ai-research-multi
search_date: 2026-05-03
query: LLM quantization techniques
sources:
  - url: https://example.com/article
    title: "Quantization Techniques for LLMs"
    published_date: 2026-01-15
  - url: https://other.com/guide
    title: "A Guide to Model Compression"
-->
```

| Field | Tier | Description |
|-------|------|-------------|
| `type` | Required | Always `ai-research-multi` |
| `search_date` | Required | ISO 8601 date when the research was performed |
| `sources` | Required | List of source objects, each with at least `url` |
| `query` | Recommended | Search query that drove the research |
| `sources[].url` | Required | Full URL of each source |
| `sources[].title` | Optional | Title of each source |
| `sources[].published_date` | Optional | Original publication date of each source |

The body must include inline citations referencing which source each claim comes from: `[1]`, `[2]`, etc. corresponding to the `sources` list order.

**5. `video-transcript`** — Video transcript obtained directly.

```html
<!--
type: video-transcript
url: https://youtube.com/watch?v=abc123
fetched_date: 2026-05-03
channel: Channel Name
duration: 45:30
published_date: 2026-04-01
sections: true
-->
```

| Field | Tier | Description |
|-------|------|-------------|
| `type` | Required | Always `video-transcript` |
| `url` | Required | Full URL of the video |
| `fetched_date` | Required | ISO 8601 date when transcript was obtained |
| `channel` | Recommended | Channel or creator name |
| `duration` | Recommended | Video duration (`MM:SS` or `HH:MM:SS`) |
| `published_date` | Optional | Original video publication date |
| `sections` | Optional | `true` if transcript includes section headers |

Transcript body must include timestamps (`[HH:MM:SS]` or `[MM:SS]`). If `sections: true`, section headers use `## Section Title` format.

**6. `video-transcript-llm`** — Video transcript extracted by an LLM tool or MCP.

```html
<!--
type: video-transcript-llm
url: https://youtube.com/watch?v=abc123
fetched_date: 2026-05-03
channel: Channel Name
duration: 45:30
extraction_tool: crawl4ai
published_date: 2026-04-01
sections: true
-->
```

| Field | Tier | Description |
|-------|------|-------------|
| `type` | Required | Always `video-transcript-llm` |
| `url` | Required | Full URL of the video |
| `fetched_date` | Required | ISO 8601 date when transcript was extracted |
| `extraction_tool` | Required | Name of the tool/MCP that extracted the transcript |
| `channel` | Recommended | Channel or creator name |
| `duration` | Recommended | Video duration |
| `published_date` | Optional | Original video publication date |
| `sections` | Optional | `true` if transcript includes section headers |

**7. `manual`** — Human-curated source with minimal metadata.

```html
<!--
type: manual
fetched_date: 2026-04-29
-->
```

| Field | Tier | Description |
|-------|------|-------------|
| `type` | Required | Always `manual` |
| `fetched_date` | Required | ISO 8601 date when the source was added |

Any additional fields are accepted. Human curators can add `url`, `author`, `published_date`, etc. as they see fit.
```

- [ ] **Step 3: Verify the edit renders correctly**

Read the modified file and confirm:
- The new "Raw Source Metadata" section appears between the AI-Research section and the "Index Format" section
- The AI-Research section now references the new section
- The anchor link `#raw-source-metadata` will work (heading is `### Raw Source Metadata`)

- [ ] **Step 4: Commit**

```bash
git add schema/WIKI_SCHEMA.md
git commit -m "feat: add Raw Source Metadata section to WIKI_SCHEMA.md

Defines 7 source types (web-crawl, web-search, ai-research,
ai-research-multi, video-transcript, video-transcript-llm, manual)
with HTML comment envelope format and required/recommended/optional
field tiers. Updates AI-Research section to reference the new schema.

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>"
```

---

### Task 2: Update WIKI_WORKFLOWS.md — Research workflow metadata requirements

**Files:**
- Modify: `schema/WIKI_WORKFLOWS.md:202–207` (Research workflow step 2)

- [ ] **Step 1: Update Research workflow step 2 to include metadata header requirements**

Replace lines 202–207 in `schema/WIKI_WORKFLOWS.md`:

Current:
```
2. **Save each source as a separate file** in `ai-research/` (one source, one file)
   - Include frontmatter: `url`, `fetched` date, `summary`
   - Save the FULL cleaned content, not a summary
   - Use lowercase hyphenated file names (e.g., `ai-research/web/topic-source-name.md`)
   - Do NOT overwrite existing files — always create new files
```

With:
```
2. **Save each source as a separate file** in `ai-research/` (one source, one file)
   - Include an HTML comment metadata header at the top with `type: ai-research`, `url`, `search_date`, and other fields per the Raw Source Metadata schema in `schema/WIKI_SCHEMA.md`
   - Include YAML frontmatter with `summary` (one-line description of the source content)
   - For multi-source synthesis: use `type: ai-research-multi` with a `sources` list, and include inline citations (`[1]`, `[2]`, etc.) in the body referencing the sources list order
   - Save the FULL cleaned content, not a summary
   - Use lowercase hyphenated file names (e.g., `ai-research/web/topic-source-name.md`)
   - Do NOT overwrite existing files — always create new files
```

- [ ] **Step 2: Commit**

```bash
git add schema/WIKI_WORKFLOWS.md
git commit -m "feat: update Research workflow with metadata header requirements

Step 2 now requires HTML comment metadata headers per the
Raw Source Metadata schema, including type, url, search_date,
and multi-source citation requirements.

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>"
```

---

### Task 3: Update wiki-linter agent — Add raw-source-metadata check

**Files:**
- Modify: `.claude/agents/wiki-linter.md` (add check after check #11)

- [ ] **Step 1: Add raw-source-metadata lint check after check #11 (Broken citation)**

Insert after the `11. **Broken citation**` check (line 25) and before `### LLM Judgment Check`:

```markdown
12. **Raw source metadata** (error/warning) — Validate LLM-extracted source files against the Raw Source Metadata schema in `schema/WIKI_SCHEMA.md`
    - Only validate files in `raw/` or `ai-research/` that contain a `<!-- ... type: ... -->` HTML comment block (skip human-curated files without metadata headers)
    - Error: `type` field is not one of the 7 valid values (`web-crawl`, `web-search`, `ai-research`, `ai-research-multi`, `video-transcript`, `video-transcript-llm`, `manual`)
    - Error: missing required fields for the declared `type` (see schema for required fields per type)
    - Warning: missing recommended fields for the declared `type`
    - Warning (video types): body lacks timestamps (`[HH:MM:SS]` or `[MM:SS]` format)
    - Error (ai-research-multi): `sources` list is missing or has no entries with `url`
```

- [ ] **Step 2: Update the lint report example to include raw-source-metadata**

In the `## Output Format` section, add a new error line after `[broken-citation]`:

```markdown
- [raw-source-metadata] `raw/document/example/file.md` missing required field `url` for type `web-crawl`
```

Add a new warning line after `[orphan]`:

```markdown
- [raw-source-metadata] `ai-research/web/topic.md` missing recommended field `query` for type `ai-research`
```

- [ ] **Step 3: Commit**

```bash
git add .claude/agents/wiki-linter.md
git commit -m "feat: add raw-source-metadata lint check to wiki-linter

Validates LLM-extracted files against the 7 source types,
errors on missing required fields, warns on missing recommended
fields. Skips human-curated files without metadata headers.

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>"
```

---

### Task 4: Update wiki-maintainer agent — Carry metadata during ingest

**Files:**
- Modify: `.claude/agents/wiki-maintainer.md:18` (Ingest step 1)
- Modify: `.claude/agents/wiki-maintainer.md:45–49` (Research steps 2–3)

- [ ] **Step 1: Update Ingest step 1 to read metadata headers**

Replace the current line 18:

```
1. Read the source document — from `raw/` or `ai-research/` for small files, or from `processed/` for segmented documents
```

With:

```
1. Read the source document — from `raw/` or `ai-research/` for small files, or from `processed/` for segmented documents. If the file has an HTML comment metadata header (starting with `<!--`), parse it to extract source provenance: `type`, `url`, `fetched_date`/`search_date`, `published_date`, and any other fields. Carry `url` and `published_date` into the wiki page frontmatter where applicable. Note the `type` for provenance tracking.
```

- [ ] **Step 2: Update Research step 2 to include metadata header**

Replace the current lines 45–49:

```
2. **One source, one file** — save each URL as a separate markdown file in `ai-research/`
3. Include frontmatter: `url`, `fetched` date, `summary`
4. Save FULL cleaned content, not summaries
5. Do NOT overwrite existing files — always create new files
```

With:

```
2. **One source, one file** — save each URL as a separate markdown file in `ai-research/`
3. Include an HTML comment metadata header at the top with `type: ai-research`, `url`, `search_date`, `query`, and other fields per the Raw Source Metadata schema in `schema/WIKI_SCHEMA.md`
4. Include YAML frontmatter with `summary` (one-line description)
5. For multi-source synthesis, use `type: ai-research-multi` with a `sources` list and inline citations (`[1]`, `[2]`) in the body
6. Save FULL cleaned content, not summaries
7. Do NOT overwrite existing files — always create new files
```

- [ ] **Step 3: Commit**

```bash
git add .claude/agents/wiki-maintainer.md
git commit -m "feat: update wiki-maintainer to read and produce metadata headers

Ingest step 1 now parses HTML comment metadata headers for
provenance. Research step 2 now produces metadata headers per
the Raw Source Metadata schema.

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>"
```

---

### Task 5: Update document-processor agent — Preserve metadata headers

**Files:**
- Modify: `.claude/agents/document-processor.md` (add step after step 4, around line 33)

- [ ] **Step 1: Add metadata header preservation step**

Insert a new step after step 4 ("Convert each segment to markdown") and before step 5 ("Write segments"):

```markdown
4b. **Preserve source metadata** — If the original raw file has an HTML comment metadata header (starting with `<!--`), copy it to the first segment only. Adjust `index` if present to reflect the segment's position. Do not duplicate the header across other segments — only the first segment carries the metadata.
```

- [ ] **Step 2: Commit**

```bash
git add .claude/agents/document-processor.md
git commit -m "feat: preserve raw source metadata headers during segmentation

First segment gets the original metadata header with adjusted
index. Other segments do not duplicate the header.

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>"
```

---

### Task 6: Update sync-check agent — Add source types to check list

**Files:**
- Modify: `.claude/agents/sync-check.md` (add new section 8 after section 7)

- [ ] **Step 1: Add section 8 for Raw Source Metadata consistency**

Insert a new section after section 7 (Wiki directory naming) and before the `## Output Format` section:

```markdown
### 8. Raw source metadata

The Raw Source Metadata schema in `schema/WIKI_SCHEMA.md` must be consistent with agent references:

- **Source types**: The 7 valid types (`web-crawl`, `web-search`, `ai-research`, `ai-research-multi`, `video-transcript`, `video-transcript-llm`, `manual`) must match across WIKI_SCHEMA.md, WIKI_WORKFLOWS.md, wiki-linter, and wiki-maintainer
- **Field requirements**: Required and recommended fields per type must match the schema definition
- **Agent references**: wiki-maintainer must reference the metadata header format in both Ingest and Research steps
- **Linter checks**: wiki-linter must validate the same 7 types and field requirements
- **Workflow references**: WIKI_WORKFLOWS.md Research step 2 must reference the metadata schema

Check that:
- `schema/WIKI_SCHEMA.md` documents all 7 source types with correct required/recommended/optional fields
- `.claude/agents/wiki-linter.md` references the same 7 types and field tiers
- `.claude/agents/wiki-maintainer.md` references the metadata header format
- `schema/WIKI_WORKFLOWS.md` Research step 2 references the metadata schema
```

- [ ] **Step 2: Add the sync-check agent's files-to-read list to include the new check**

In the `## Files to Read` section, the list already covers the relevant files (WIKI_SCHEMA.md, WIKI_WORKFLOWS.md, wiki-linter.md, wiki-maintainer.md). No additional files need to be added since the new check validates consistency between existing files.

- [ ] **Step 3: Commit**

```bash
git add .claude/agents/sync-check.md
git commit -m "feat: add raw source metadata consistency check to sync-check

New section 8 verifies that the 7 source types and field
requirements are consistent across WIKI_SCHEMA.md, agents,
and workflows.

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>"
```

---

### Task 7: Run sync-check to verify consistency

**Files:**
- Verify: all modified files are consistent with each other

- [ ] **Step 1: Invoke the sync-check agent**

Run the sync-check agent to verify that all 6 modified files are consistent with each other and with the project conventions. The agent will check:

- Directory references are correct
- Agent cross-references point to the right files and paths
- Naming conventions match
- The new Raw Source Metadata section is referenced correctly
- The 7 source types and their field requirements are consistent across all files

- [ ] **Step 2: Fix any inconsistencies found by sync-check**

Address any issues reported by the sync-check agent. Common issues to watch for:
- Mismatched source type names between files
- Missing or incorrect cross-references
- Inconsistent field names or tier classifications

- [ ] **Step 3: Commit any fixes**

```bash
git add -A
git commit -m "fix: resolve sync-check inconsistencies after metadata schema update

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>"
```

---

### Task 8: Run wiki-linter on existing files to establish baseline

**Files:**
- Verify: existing raw/ and ai-research/ files pass the new lint check

- [ ] **Step 1: Manually spot-check existing crawl files against the new schema**

Read a few existing crawl files to verify they use the HTML comment format (they do — OpenRouter and Claude Code files already have `<!-- URL: ... -->` headers). Confirm that:

- OpenRouter files have `URL`, `Download Date`, `Website`, `Webpage`, `Index` (Title Case) — these will be **warnings** since they don't have the new schema's `type` field yet
- Claude Code files have `url`, `download_date`, `website`, `webpage` (snake_case) — these will also be **warnings** since they don't have `type`
- Forum threads and Obsidian Web Clipper files have YAML frontmatter — these should be **skipped** (no HTML comment metadata header)

- [ ] **Step 2: Verify the linter correctly skips human-curated files**

Confirm that files in `raw/articles/`, `raw/forum-thread/` etc. that only have YAML frontmatter (no `<!-- ... type: ... -->` block) are not flagged by the raw-source-metadata check.

- [ ] **Step 3: Commit any adjustments**

If the lint check needs adjustments to handle existing files gracefully (e.g., recognizing old-format HTML comments without a `type` field as valid human-curated files), commit those fixes.

```bash
git add -A
git commit -m "fix: adjust raw-source-metadata lint for existing file formats

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>"
```