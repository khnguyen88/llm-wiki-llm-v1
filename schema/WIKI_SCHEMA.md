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

processed/        # Segmented markdown from large raw files
  articles/       # Segmented articles
  papers/         # Segmented papers
  repos/          # Segmented repos
  datasets/       # Segmented datasets
  assets/         # Segmented assets
  document/       # Segmented document sources
  web/            # Segmented web sources

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

All wiki pages should include YAML frontmatter:

```yaml
---
title: Page Title
type: entity | concept | summary | qanda | index | other
date: YYYY-MM-DD
sources:
  - raw/document/path/to/source.md or raw/web/path/to/source.md
tags:
  - topic1
  - topic2
---
```

## Linking Conventions

- **Internal links**: `[[Page Name]]` or `[[entities/transformer_model|Transformer Model]]`
- **External links**: `[Text](https://example.com)`
- **Backlinks**: Automatically maintained by Obsidian

## File Formats

### Entity Pages

```markdown
---
title: Entity Name
type: entity
date: YYYY-MM-DD
---

# Entity Name

Brief definition/description.

## Key Facts
- Fact 1
- Fact 2

## Related
- [[Concept Name]]
- [[Entity Name]]
```

### Concept Pages

```markdown
---
title: Concept Name
type: concept
date: YYYY-MM-DD
---

# Concept Name

Explanation of the concept.

## Origins
- When/where it was introduced
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
type: summary
date: YYYY-MM-DD
sources:
  - raw/document/path/to/source.md or raw/web/path/to/source.md
---

# Source Title

## Key Points
- Point 1
- Point 2

## Quotes
> "Important quote"

## Notes
Additional remarks.
```

### Q&A Pages

```markdown
---
title: Q: Original Question
type: qanda
date: YYYY-MM-DD
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
type: synthesis
date: YYYY-MM-DD
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
