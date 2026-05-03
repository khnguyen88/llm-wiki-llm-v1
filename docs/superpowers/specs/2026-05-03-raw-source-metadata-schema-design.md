# Raw Source Metadata Schema Design

**Date**: 2026-05-03
**Status**: Draft
**Scope**: Define standardized metadata headers for LLM-extracted raw sources, update schema docs and agents.

---

## Problem

Raw source files currently use inconsistent metadata formats:

- **OpenRouter crawl files** use Title Case HTML comments: `URL`, `Download Date`, `Website`, `Webpage`, `Index`
- **Claude Code crawl files** use snake_case HTML comments: `url`, `download_date`, `website`, `webpage`
- **Forum threads** use YAML frontmatter: `title`, `source`, `author`, `published`, `created`, `description`, `tags`
- **Obsidian Web Clipper** files use YAML frontmatter with `source`, `author`, `published`, `created`, `description`, `tags`
- **AI-research** has a partial schema (`url`, `fetched`, `summary`) in WIKI_SCHEMA.md but it's incomplete — no `query`, `type`, or `published_date`
- **No format exists** for video transcripts or web search results

There is no standard for what metadata LLM tools should provide when extracting content. This makes it hard for the wiki-maintainer to know what provenance information is available, and inconsistent across the project.

## Design

### Two-Tier Approach

1. **LLM-extracted content** (going forward): Must follow the standardized HTML comment metadata schema defined below. This applies to any web crawler or MCP extraction, web search results, video transcript extractions, and AI research files — regardless of which tool produced them.

2. **Human-curated content** (existing and future): The linter accepts whatever metadata format is present — YAML frontmatter, HTML comments, or nothing. No normalization, no backfill. The Obsidian Web Clipper format, forum thread format, and other human-generated files stay as-is.

The linter validates LLM-extracted files against the schema and warns about missing fields, but does not enforce any format on human-curated files.

### Format: HTML Comment Envelope

All LLM-extracted source metadata uses HTML comment blocks at the top of the file:

```html
<!--
type: <source-type>
field1: value1
field2: value2
-->
```

**Why HTML comments?** They are invisible in rendered markdown/Obsidian, don't interfere with YAML frontmatter (which some raw files already use), and are trivial for LLM tools to parse and generate. Human-curated files that already have YAML frontmatter can keep it.

**Why a shared envelope?** Each source type has distinct fields, but sharing one format means the linter has one parsing path, agents have one pattern to follow, and it's easy to add new source types later. The `type` field is the discriminator.

### Field Tiers

Each field is classified as one of:

| Tier | Meaning | Linter behavior |
|------|---------|-----------------|
| **Required** | Must be present for LLM-extracted files | Error if missing |
| **Recommended** | Should be present when available | Warning if missing |
| **Optional** | Nice to have, no warning if absent | No check |

### Source Types

#### 1. `web-crawl` — Web crawler extraction

Used for files extracted from websites by any web crawler or MCP tool.

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
| `fetched_date` | Required | ISO 8601 date when the page was crawled (`YYYY-MM-DD`) |
| `website` | Recommended | Domain or site identifier (e.g., `openrouter`, `claude-code`) |
| `webpage` | Recommended | Slug identifying the specific page within the site |
| `index` | Optional | Retrieval order number within a crawl batch. Omit if not available from the extraction tool. |
| `published_date` | Optional | Date the source content was originally published. Omit if not available from the source. |

#### 2. `web-search` — LLM tool web search result

Used when an LLM tool (e.g., web search MCP) retrieves a single page as a search result.

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
| `published_date` | Optional | Original publication date if available |
| `snippet` | Optional | Brief summary of what the page contains |

#### 3. `ai-research` — Single-source AI discovery

Used when the LLM discovers and saves a single web source to `ai-research/`.

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
| `published_date` | Optional | Original publication date if available |

**Note**: This replaces the existing `ai-research` frontmatter spec in WIKI_SCHEMA.md (which had `url`, `fetched`, `summary`). The `fetched` field becomes `search_date` for consistency with `web-search`. The `summary` field stays in YAML frontmatter (not the HTML comment) since it's a content description rather than source metadata.

#### 4. `ai-research-multi` — Multi-source AI synthesis

Used when the LLM synthesizes content from multiple sources into a single file in `ai-research/`.

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

**Citation requirement**: The body of an `ai-research-multi` file must include inline citations referencing which source each claim comes from. Use `[1]`, `[2]`, etc. corresponding to the `sources` list order, or `^[ai-research/path/to/source.md]` claim citations pointing to individual source files if they exist.

#### 5. `video-transcript` — Direct video transcript extraction

Used for video transcripts obtained directly (not via LLM extraction).

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
| `duration` | Recommended | Video duration in `MM:SS` or `HH:MM:SS` format |
| `published_date` | Optional | Original video publication date |
| `sections` | Optional | `true` if the transcript body includes section/topic headers |

**Body format**: Transcript body must include timestamps in `[HH:MM:SS]` or `[MM:SS]` format at regular intervals. If `sections: true`, section headers must use `## Section Title` markdown heading format.

Example body:
```markdown
## Introduction

[00:00:00] Welcome to this talk about LLM architecture...

[00:01:30] The key insight is that attention mechanisms...

## Transformer Architecture

[00:03:15] Let's dive into how transformers work...
```

#### 6. `video-transcript-llm` — LLM-extracted video transcript

Used when an LLM tool or MCP extracts a video transcript. Same as `video-transcript` but adds `extraction_tool` to identify how it was obtained.

```html
<!--
type: video-transcript-llm
url: https://youtube.com/watch?v=abc123
fetched_date: 2026-05-03
channel: Channel Name
duration: 45:30
extraction_tool: youtube-mcp
published_date: 2026-04-01
sections: true
-->
```

| Field | Tier | Description |
|-------|------|-------------|
| `type` | Required | Always `video-transcript-llm` |
| `url` | Required | Full URL of the video |
| `fetched_date` | Required | ISO 8601 date when transcript was extracted |
| `extraction_tool` | Required | Name of the tool or MCP that extracted the transcript (e.g., `youtube-mcp`, any web crawler, or any video extraction tool) |
| `channel` | Recommended | Channel or creator name |
| `duration` | Recommended | Video duration |
| `published_date` | Optional | Original video publication date |
| `sections` | Optional | `true` if transcript includes section/topic headers |

**Section headers**: When `sections` is `true`, the transcript must use `## Section Title` headings. For pure extractions (no LLM editing), section headers are optional in the metadata but mandatory in the body if present.

#### 7. `manual` — Human-curated source

Used for manually added sources that may not have structured metadata.

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

### Human-Curated Files

Files that already use a different metadata format (YAML frontmatter from Obsidian Web Clipper, forum thread format, etc.) are accepted as-is. The linter does not validate or normalize them. Examples:

- Obsidian Web Clipper files with YAML frontmatter (`source`, `author`, `published`, `tags`)
- Forum threads with YAML frontmatter (`title`, `source`, `author`, `published`)
- Articles with no metadata header at all

These files remain valid. Only **LLM-extracted** files must follow the schema.

### Date Format Convention

All date fields use ISO 8601 date-only format: `YYYY-MM-DD`. Timestamps may be appended when precision is needed: `YYYY-MM-DDTHH:MM:SSZ`.

Field naming uses `snake_case` consistently (no Title Case, no kebab-case).

### Unavailable Fields

If a tool or MCP cannot provide a specific field (e.g., `published_date` is not available from the source, or `index` is not tracked by the extraction tool), **omit the field entirely** rather than using placeholder values like `N/A` or `unknown`. The linter will only warn about missing recommended fields — it will not flag omitted optional fields.

---

## Integration

### WIKI_SCHEMA.md Changes

1. Add a new section **"Raw Source Metadata"** after the existing "AI-Research Source Files" section documenting:
   - The HTML comment envelope format
   - Field tier definitions (required, recommended, optional)
   - All 7 source types with their field tables
   - Date format convention
   - Human-curated file acceptance rule
   - Video transcript body format requirements

2. Update the existing "AI-Research Source Files" section to reference the new schema. Replace the inline `url`, `fetched`, `summary` spec with a reference to the `ai-research` and `ai-research-multi` types defined in the new section. Keep `summary` in YAML frontmatter (it's a content field, not a source metadata field).

### WIKI_WORKFLOWS.md Changes

Update the Research workflow step 2 to include:
- The HTML comment metadata header requirement for LLM-extracted sources
- The `type` field and required/recommended fields per source type
- The citation requirement for `ai-research-multi` files

### Agent Updates

#### wiki-linter

Add a new lint check: **raw-source-metadata**
- Only validates LLM-extracted files (files with `type:` in an HTML comment block)
- Validates `type` is one of the 7 valid values
- Errors on missing required fields
- Warns on missing recommended fields
- For `video-transcript` / `video-transcript-llm`: warns if body lacks timestamps
- For `ai-research-multi`: verifies `sources` has at least one entry with `url`
- Skips validation for files without a metadata header (human-curated)

#### wiki-maintainer

Update the Ingest operation to:
- Read the metadata header from source files when present
- Carry `url` and `published_date` into wiki page frontmatter where applicable
- Note the `type` of source for provenance tracking

#### document-processor

Update to preserve metadata headers when segmenting large files into `processed/`.

#### sync-check

Add the 7 source types and their field requirements to the consistency check list. Verify that WIKI_SCHEMA.md documents all types.

---

## Files to Modify

1. `schema/WIKI_SCHEMA.md` — Add "Raw Source Metadata" section, update AI-Research section
2. `schema/WIKI_WORKFLOWS.md` — Update Research workflow step 2
3. `.claude/agents/wiki-linter.md` — Add raw-source-metadata lint check
4. `.claude/agents/wiki-maintainer.md` — Update Ingest to carry metadata
5. `.claude/agents/document-processor.md` — Preserve metadata headers during segmentation
6. `.claude/agents/sync-check.md` — Add source types and field requirements to check list