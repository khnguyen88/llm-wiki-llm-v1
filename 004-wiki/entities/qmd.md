---
title: "qmd"
summary: "Local search engine for markdown files with hybrid BM25/vector search and LLM re-ranking, usable as CLI or MCP server"
type: entity
sources:
  - raw/articles/karpathy-github-llm-wiki.md
tags:
  - llm-wiki
  - search
  - tools
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# qmd

A local search engine for markdown files, recommended by Karpathy as a search tool for LLM Wiki wikis that have outgrown index-based navigation. ^[raw/articles/karpathy-github-llm-wiki.md:55]

## Key Facts

- Offers hybrid BM25/vector search with LLM re-ranking, all on-device ^[raw/articles/karpathy-github-llm-wiki.md:55]
- Provides both a CLI interface (for the LLM to shell out to) and an MCP server (for the LLM to use as a native tool) ^[raw/articles/karpathy-github-llm-wiki.md:55]
- Intended for wikis that have outgrown index-based navigation but don't need full embedding-based RAG infrastructure ^[raw/articles/karpathy-github-llm-wiki.md:49-55]

## Related

- [[concepts/llm_wiki]]
- [[concepts/rag]]