---
title: LLM Wiki Pattern
type: summary
date: 2026-04-22
sources:
  - raw/articles/karpathy-github-llm-wiki.md
tags:
  - knowledge-management
  - llm
  - personal-wiki
  - karpathy
---

# LLM Wiki Pattern

## Key Points

- Instead of RAG (rediscovering knowledge per query), the LLM incrementally builds a **persistent, compounding wiki** from raw sources
- The wiki is a structured, interlinked collection of markdown files that sits between you and the raw sources
- Three layers: **raw sources** (immutable), **the wiki** (LLM-owned), **the schema** (configuration that makes the LLM a disciplined maintainer)
- Three operations: **Ingest** (add source → update 10-15 wiki pages), **Query** (index-guided retrieval, file answers back), **Lint** (health-check for contradictions, orphans, gaps)
- Key files: `index.md` (content catalog for retrieval) and `log.md` (chronological record of operations)
- Works well at moderate scale (~100 sources, hundreds of pages) without needing RAG infrastructure

## Quotes

> "The wiki is a persistent, compounding artifact. The cross-references are already there. The contradictions have already been flagged. The synthesis already reflects everything you've read."

> "The tedious part of maintaining a knowledge base is not the reading or the thinking — it's the bookkeeping. LLMs don't get bored, don't forget to update a cross-reference, and can touch 15 files in one pass."

> "The idea is related in spirit to Vannevar Bush's Memex (1945) — a personal, curated knowledge store with associative trails between documents."

## Applications

- **Personal**: goals, health, psychology tracking
- **Research**: deep topic exploration over weeks/months
- **Reading**: chapter-by-chapter companion wikis (like fan wikis)
- **Business/team**: internal wikis fed by Slack, transcripts, documents
- **Competitive analysis, due diligence, trip planning, course notes**

## Tooling

- **Obsidian**: IDE/frontend for viewing raw data and compiled wiki
- **Obsidian Web Clipper**: converts web articles to markdown
- **Marp**: markdown-based slide decks from wiki content
- **Dataview**: queries over page frontmatter
- **qmd**: local hybrid BM25/vector search engine for larger wikis
- **Git**: version history, branching, collaboration

## Notes

This document is intentionally abstract — describes the pattern, not a specific implementation. Everything is optional and modular. The right approach is to share it with your LLM agent and co-evolve the implementation.