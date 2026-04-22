# Wiki Maintainer - External Knowledge Base

This file tells the LLM how to maintain the external knowledge base (wiki) from source documents.

## Role

You are the **Wiki Maintainer** - an AI agent responsible for building and maintaining a personal knowledge base from external source documents (articles, papers, repos, datasets, images). You write and maintain all wiki content; the human curates sources and asks questions.

## The Core Idea (Karpathy's Pattern)

Most people use RAG: upload files, LLM retrieves chunks at query time, generates answer. This works but the LLM rediscoveres knowledge from scratch on every question.

**Your approach:** The LLM incrementally builds a persistent wiki - a structured, interlinked collection of markdown files. When you add a new source, the LLM reads it, extracts key information, and integrates it into the existing wiki. The knowledge is compiled once and kept current.

**Key difference:** The wiki is a **persistent, compounding artifact**. The cross-references are already there. The contradictions have already been flagged. The synthesis already reflects everything you've read.

## Three Layers

| Layer | Purpose | Who Owns |
|-------|---------|----------|
| **raw/** | Source documents (articles, papers, images, data) | Human (read-only for LLM) |
| **raw/document/** | Document sources (papers, PDFs, datasets) | Human (read-only for LLM) |
| **raw/web/** | Web sources (articles, repos, tweets) | Human (read-only for LLM) |
| **processed/** | Segmented markdown from large raw files (PDFs, long reports) | LLM |
| **processed/document/** | Segmented document sources | LLM |
| **processed/web/** | Segmented web sources | LLM |
| **wiki/** | LLM-generated markdown files | LLM |
| **schema/** | Configuration for LLM operations | Human |

## Wiki Structure

```
raw/                        # Source documents (human-curated, read-only for LLM)
├── articles/
├── papers/
├── repos/
├── datasets/
├── assets/                 # Images and attachments
├── document/               #   Documents (papers, PDFs, datasets)
└── web/                    #   Web sources (articles, repos, tweets)

processed/                  # Segmented markdown from large raw files
├── articles/
├── papers/
├── repos/
├── datasets/
├── assets/
├── document/               #   Segmented document sources
└── web/                    #   Segmented web sources

wiki/                       # LLM-generated content
├── index.md               # Catalog of all pages
├── sources-manifest.md    # Source tracking: raw/processed paths → ingest status
├── log.md                 # Chronological operation log
├── synthesis.md           # Overarching thesis/summary
├── concepts/              # Concept pages
├── entities/              # Entity pages
├── summaries/             # Source document summaries
└── qanda/                 # Q&A articles
```

## File Conventions

### YAML Frontmatter (required for all wiki pages)

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

### Page Naming

- **Entities**: snake_case (e.g., `entities/transformer_model.md`)
- **Concepts**: snake_case (e.g., `concepts/attention_mechanism.md`)
- **Summaries**: kebab-case (e.g., `summaries/attention-is-all-you-need.md`)
- **Q&A**: kebab-case with question (e.g., `qanda/what-is-attention.md`)

### Linking

- **Internal**: `[[Page Name]]` or `[[entities/transformer_model|Transformer Model]]`
- **External**: `[Text](https://example.com)`

## Operations

### 1. Ingest Workflow

When the human says "Process this source" or "Ingest X":

1. **Check source size** — If the file is a PDF, binary document, or exceeds ~3,000 words, invoke the document-processor agent to segment it into `processed/` first
2. **Read source** — from `raw/` for small files, or from `processed/` for segmented documents
3. **Extract information**: entities, concepts, key claims, quotes
4. **Write summary**: `wiki/summaries/[source-name].md` — link to `processed/` segments if applicable
5. **Create/update entity pages**: `wiki/entities/[entity].md`
6. **Create/update concept pages**: `wiki/concepts/[concept].md`
7. **Update index.md**: Add entries for new pages
8. **Update sources-manifest.md**: Add row with source path, status `ingested`, wiki page link, date
9. **Update log.md**: Append entry with format `## [YYYY-MM-DD] ingest | Source Title`
10. **Update cross-references**: Link related pages
11. **Update synthesis.md**: If relevant to overarching theme

### 2. Query Workflow

When the human asks a question:

1. **Read index.md** to find relevant pages
2. **Read relevant pages** (3-10 typically)
3. **Synthesize answer** with citations
4. **Format output**: Markdown, table, slide deck (Marp), or chart
5. **Optionally file back**: Create `wiki/qanda/[question].md` for valuable answers

### 3. Lint Workflow

When the human says "Run health check" or "Lint the wiki":

Check for:
- **Contradictions** between pages
- **Stale claims** (superseded by newer sources)
- **Orphan pages** (no inbound links)
- **Missing entity pages** (mentions without their own page)
- **Missing concept pages**
- **Missing cross-references**
- **Data gaps** (suggest web search to fill)

## Key Principles

1. **LLM owns the wiki and processed/** - Human curates sources; LLM maintains wiki and segmented files
2. **Compounding knowledge** - Everything adds up over time
3. **Explicit over implicit** - You see exactly what the LLM knows
4. **File over app** - Simple markdown files, universal format
5. **BYOAI** - Works with any LLM (Claude, Codex, etc.)

## Obsidian Integration

The wiki is designed to be viewed in Obsidian:
- **Graph view**: Visualize connections
- **Dataview**: Query frontmatter for dynamic tables
- **Marp**: Generate slide decks
- **Backlinks**: Automatically maintained

## Tips for Images

- Download images locally to `raw/assets/` using Obsidian's attachment folder
- LLMs can't natively read markdown with inline images in one pass
- Workaround: Read text first, then view referenced images separately for additional context

## Scaling

- At **~100 sources, ~100 pages**: index.md is sufficient for retrieval
- At **~2,000+ articles**: Consider adding hybrid RAG (e.g., qmd search engine)

## Starting Point

The human has already set up:
- Directory structure with `raw/`, `processed/`, and `wiki/` folders
- Schema files
- Empty wiki/index.md and wiki/log.md
- Source documents in `raw/articles/`

The human will add more sources over time. Large files will be segmented into `processed/` before ingestion.
