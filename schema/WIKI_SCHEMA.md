# Wiki Schema - External Knowledge Base

This file defines the structure and conventions for the external knowledge base wiki.

## Directory Structure

```
raw/              # Source documents (immutable)
  articles/       # Article sources (web articles, blog posts)
  papers/         # Paper sources (PDFs, academic papers)
  repos/          # Repository sources (GitHub repos)
  datasets/       # Dataset sources
  assets/         # Images and attachments
  document/       # Documents (papers, PDFs, datasets)
  web/            # Web sources (articles, repos, tweets)
  forum-thread/   # Forum discussions
  transcripts/    # Conversation transcripts

ai-research/      # AI-discovered web sources (LLM-writes, immutable once saved)
  articles/
  papers/
  repos/
  datasets/
  assets/
  document/
  web/
  forum-thread/
  transcripts/

processed/        # Segmented markdown from large raw files
  articles/       # Segmented articles
  papers/         # Segmented papers
  repos/          # Segmented repos
  datasets/       # Segmented datasets
  assets/         # Segmented assets
  document/       # Segmented document sources
  web/            # Segmented web sources
  forum-thread/   # Segmented forum discussions
  transcripts/    # Segmented conversation transcripts

wiki/             # LLM-generated content
  index.md        # Catalog of all wiki pages
  log.md          # Chronological operation log
  sources-manifest.md # Source tracking: raw/processed paths → ingest status
  synthesis.md    # Overarching thesis/summary
  concepts/       # Concept pages
  entities/       # Entity pages
  summaries/      # Source document summaries
  qanda/          # Q&A articles
```

## Page Naming Conventions

| Page Type | Naming | Example |
|-----------|--------|---------|
| Entity | snake_case | `entities/transformer_model.md` |
| Concept | snake_case | `concepts/attention_mechanism.md` |
| Summary | kebab-case | `summaries/attention-is-all-you-need.md` |
| Q&A | kebab-case | `qanda/what-is-attention.md` |

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

## Frontmatter Format

All wiki pages must include YAML frontmatter. Fields are split into **required** and **optional provenance** groups.

### Required Fields

```yaml
---
title: Page Title
summary: One-line description of what this page covers
type: entity | concept | summary | qanda | index | manifest | synthesis | other
sources:
  - raw/document/path/to/source.md or raw/web/path/to/source.md or ai-research/web/path/to/source.md
tags:
  - topic1
  - topic2
created: "2026-04-05T12:00:00Z"
updated: "2026-04-05T12:00:00Z"
---
```

### Optional Provenance Fields

Add these when the LLM has enough information to populate them. They improve lint quality and knowledge tracking.

```yaml
confidence: 0.9                    # 0.0–1.0 float — overall confidence in this page's claims
provenance: extracted               # extracted | merged | inferred | ambiguous
contradictedBy: []                 # list of slugs referencing contradicting pages (with optional reason)
orphaned: false                    # true when source was deleted and no other source contributes
```

**`provenance` values:**
- `extracted` — content directly extracted from source material
- `merged` — content combined from multiple sources
- `inferred` — content synthesized or inferred (not directly stated in sources)
- `ambiguous` — content with unclear or conflicting source support

**`confidence` guidance:**
- `1.0` — directly verbatim from source
- `0.8–0.9` — well-supported by sources
- `0.5–0.7` — partially supported, some inference needed
- `<0.5` — flag for review, consider adding to `## Open Questions` instead

## Claim-Level Citations

In addition to page-level `sources:` in frontmatter, pages can use **inline claim citations** for paragraph-level provenance:

- `^[raw/articles/source.md]` — cite an entire source file (use project-root-relative path)
- `^[raw/articles/source.md:42-58]` — cite specific line range
- `^[raw/articles/source.md:45]` — cite a single line

For multiple sources, use separate citation markers rather than combining them in one bracket.

Example in body:

```markdown
The transformer architecture uses self-attention to process sequences in parallel.^[raw/articles/attention-is-all-you-need.md]

Key innovations include scaled dot-product attention^[raw/articles/attention-is-all-you-need.md:3-12] and multi-head attention^[raw/articles/attention-is-all-you-need.md].
```

Claim citations are validated by the linter (broken-citation and malformed-citation checks). Citations must use project-root-relative paths (e.g., `^[raw/articles/source.md]`) for unambiguous file resolution.

## Linking Conventions

- **Internal links**: `[[path/to/article]]` or `[[entities/transformer_model|Transformer Model]]`
- **External links**: `[Text](https://example.com)`
- **Claim citations**: `^[raw/articles/source.md]` or `^[raw/articles/source.md:42-58]`
- **Backlinks**: Automatically maintained by Obsidian

## File Formats

### Entity Pages

```markdown
---
title: Entity Name
summary: One-line description of this entity
type: entity
sources:
  - raw/document/path/to/source.md or raw/web/path/to/source.md
tags:
  - topic1
created: "2026-04-05T12:00:00Z"
updated: "2026-04-05T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Entity Name

Brief definition/description.

## Key Facts
- Fact 1^[raw/articles/source.md]
- Fact 2

## Related
- [[Concept Name]]
- [[Entity Name]]
```

### Concept Pages

```markdown
---
title: Concept Name
summary: One-line explanation of this concept
type: concept
sources:
  - raw/document/path/to/source.md or ai-research/web/path/to/source.md
tags:
  - topic1
created: "2026-04-05T12:00:00Z"
updated: "2026-04-05T12:00:00Z"
confidence: 0.85
provenance: merged
---

# Concept Name

Explanation of the concept.

## Origins
- When/where it was introduced^[raw/articles/source.md:10-25]
- Key contributors

## Applications
- Use case 1
- Use case 2

## Related
- [[Entity Name]]
- [[Concept Name]]
```

### Summary Pages

```markdown
---
title: Source Title
summary: One-line summary of this source document
type: summary
sources:
  - raw/document/path/to/source.md or raw/web/path/to/source.md or ai-research/web/path/to/source.md
tags:
  - topic1
created: "2026-04-05T12:00:00Z"
updated: "2026-04-05T12:00:00Z"
---

# Source Title

## Summary
2-4 sentence narrative overview of the source's argument and significance.^[raw/articles/source.md]

## [Custom Section Headings]
Use section headings drawn from the source's structure. When the source
compares items, creates a taxonomy, or presents data — use tables.

Cite sources at the section level (end of section) rather than per-bullet.
Use tables whenever the source contains structured or comparative data.

## Key Quotes
> "Important quote"^[raw/articles/source.md:45]

## Related
- [[concepts/topic]]
- [[entities/name]]
```

### Style Guide for Summaries

Summaries should be rich, encyclopedia-style articles — not flat bullet lists. Follow these guidelines:

- **Use section headings drawn from the source's structure** (e.g., "Anatomy of an LLM Name", "Decision Guide", "Why Naming Conventions Exist") rather than generic headings like "Key Points"
- **Use tables** for any comparative, tiered, or structured data from the source (comparison matrices, tier lists, risk/consequence/mitigation tables, parameter tables)
- **Write narrative paragraphs** for the `## Summary` section and for transitions between sections — not bullet lists
- **Cite at section level** — place `^[source.md]` at the end of a section or on the first claim in a section, not on every bullet point
- **The `summary` frontmatter field** is a one-line abstract; the `## Summary` body section is a narrative overview (2-4 sentences)
- **When a source has distinct topics**, create subsections rather than flattening into a uniform bullet list
- **Preserve the author's original structure** when it provides clarity (e.g., decision frameworks, comparison matrices, step-by-step guides)
- **`## Key Quotes`** collects the most important direct quotes from the source (2-5 quotes maximum)
- **`## Related`** links to wiki concepts and entities with `[[wikilinks]]`

### Q&A Pages

```markdown
---
title: Q: Original Question
summary: One-line summary of the answer
type: qanda
sources:
  - raw/document/path/to/source.md or ai-research/web/path/to/source.md
tags:
  - topic1
created: "2026-04-05T12:00:00Z"
updated: "2026-04-05T12:00:00Z"
---

# Q: Original Question

## Answer

[The synthesized answer with [[wikilinks]] to sources]

## Sources Consulted
- [[concepts/article-1]] - Relevant because...
- [[concepts/article-2]] - Provided context on...
```

### Synthesis Page

```markdown
---
title: Synthesis
summary: Overarching thesis or summary of all knowledge
type: synthesis
sources:
  - raw/document/path/to/source.md
tags:
  - topic1
created: "2026-04-05T12:00:00Z"
updated: "2026-04-05T12:00:00Z"
confidence: 0.7
provenance: inferred
---

# Synthesis

[Overarching thesis or summary of all knowledge]

## Key Themes
- Theme 1
- Theme 2

## Key Findings
- Finding 1
- Finding 2

## Open Questions
- Question 1
- Question 2
```

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

### Raw Source Metadata

All LLM-extracted source files must include an HTML comment metadata header at the top of the file. Human-curated files are accepted as-is — no normalization required.

**Two-tier approach:**
1. **LLM-extracted content** (going forward): Must follow the standardized HTML comment metadata schema. This applies to any web crawler or MCP extraction, web search results, video transcript extractions, AI research files, and processed document segments.
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
search_date: 2026-05-03T14:22:00Z
query: LLM quantization techniques
tool_used: vane_web_search
tool_model: gemma4:31b-cloud
website: example.com
published_date: 2026-01-15
snippet: Summary of key findings from the page
-->
```

| Field | Tier | Description |
|-------|------|-------------|
| `type` | Required | Always `web-search` |
| `url` | Required | Full URL of the source page |
| `search_date` | Required | ISO 8601 timestamp when the search was performed |
| `query` | Recommended | The search query that found this result |
| `tool_used` | Recommended | Name of the tool used to perform the search (e.g., `vane_web_search`) |
| `tool_model` | Recommended | Chat model used for synthesis (e.g., `gemma4:31b-cloud`) |
| `website` | Recommended | Domain or site identifier (e.g., `example.com`) |
| `published_date` | Optional | Original publication date |
| `snippet` | Optional | Brief summary of page content |

The body of web-search results must include inline citations `[N]` referencing the numbered Sources list, so every factual claim is traceable to its specific source. All sources returned by the search tool must be included in the Sources list — do not filter or truncate.

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
search_date: 2026-05-03T19:30:00Z
query: LLM quantization techniques
tool_used: vane_web_search
tool_model: gemma4:31b-cloud
embedding_model: mixedbread-ai/mxbai-embed-large-v1
sources:
  - url: https://example.com/article
    title: "Quantization Techniques for LLMs"
    website: example.com
    published_date: 2026-01-15
  - url: https://other.com/guide
    title: "A Guide to Model Compression"
    website: other.com
-->
```

| Field | Tier | Description |
|-------|------|-------------|
| `type` | Required | Always `ai-research-multi` |
| `search_date` | Required | ISO 8601 timestamp when the research was performed |
| `sources` | Required | List of source objects, each with at least `url` |
| `query` | Recommended | Search query that drove the research |
| `tool_used` | Recommended | Name of the tool used to perform the search (e.g., `vane_web_search`) |
| `tool_model` | Recommended | Chat model used for synthesis (e.g., `gemma4:31b-cloud`) |
| `embedding_model` | Optional | Embedding model used for retrieval (e.g., `mixedbread-ai/mxbai-embed-large-v1`) |
| `sources[].url` | Required | Full URL of each source |
| `sources[].title` | Recommended | Title of each source |
| `sources[].website` | Recommended | Domain identifier extracted from the URL (e.g., `example.com`) |
| `sources[].published_date` | Optional | Original publication date of each source |

The body must include inline citations referencing which source each claim comes from: `[1]`, `[2]`, etc. corresponding to the `sources` list order. All sources returned by the search tool must be included in the `sources` list — do not filter or truncate.

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

## Index Format

`wiki/index.md` should organize pages by category:

```markdown
# Wiki Index

## Entities
- [[entities/name|Name]]

## Concepts
- [[concepts/name|Name]]

## Summaries
- [[summaries/name|Title]]

## Source Manifest
- [[sources-manifest|Sources Manifest]]

## Q&A
- [[qanda/name|Question]]

## Synthesis
- [[synthesis|Overall Synthesis]]
```

## Log Format

`wiki/log.md` entries:

```markdown
# Wiki Log

## [2026-04-22] action | details
- Description of what happened
- Files affected
```

Example:
```markdown
## [2026-04-22] ingest | Attention Is All You Need
- Added summary: summaries/attention-is-all-you-need.md
- Created entity: entities/transformer.md
- Created concept: concepts/attention-mechanism.md
- Updated index.md
```

## Obsidian Integration

- **Graph View**: Visualize connections between pages
- **Dataview**: Query frontmatter for dynamic tables
- **Marp**: Generate slide decks from wiki content
- **Backlinks**: Automatically maintained via markdown links
- **Web Clipper**: Browser extension to convert web articles to markdown

## File over App Philosophy

The wiki is just a collection of simple markdown files with `[[wikilinks]]`. This means:
- You can use any tool to view or edit
- Works natively in Obsidian
- Can be version controlled with git
- No vendor lock-in
