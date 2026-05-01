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

## Key Points
- Point 1^[raw/articles/source.md]
- Point 2

## Quotes
> "Important quote"^[raw/articles/source.md:45]

## Notes
Additional remarks.
```

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

When the LLM conducts autonomous web research, save full cleaned source content here:

```markdown
---
url: https://example.com/article
fetched: YYYY-MM-DD
summary: One-line description of what this source covers
---

[Full article content in markdown, cleaned, not summarized]
```

- One source, one file — never combine multiple URLs into one file
- File names: lowercase hyphenated (e.g., `ai-research/web/qmd-github-readme.md`)
- Immutable once saved — do not overwrite, create new files
- These are the source of truth for citation verification

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
