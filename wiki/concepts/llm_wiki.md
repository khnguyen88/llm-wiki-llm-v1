---
title: LLM Wiki
type: concept
date: 2026-04-22
sources:
  - raw/articles/karpathy-github-llm-wiki.md
  - raw/articles/karpathy-tweet-llm-wiki.md
tags:
  - knowledge-management
  - llm
  - architecture
---

# LLM Wiki

A personal knowledge base pattern where an LLM incrementally builds and maintains a structured wiki from raw source documents, instead of retrieving from raw documents on every query (RAG).

## Core Mechanism

The LLM reads source documents, extracts key information, and integrates it into an existing wiki — creating/updating entity pages, concept pages, summaries, and cross-references. Knowledge is compiled once and kept current, not re-derived per query.

## Key Properties

- **Persistent and compounding**: Every source and query enriches the wiki
- **Explicit**: You can see exactly what the LLM knows and doesn't know
- **Yours**: Local files in universal formats, no vendor lock-in
- **File over app**: Simple markdown, interoperable with any tool
- **BYOAI**: Works with any LLM (Claude, Codex, OpenCode, etc.)

## Scale Considerations

Works well at ~100 sources / hundreds of pages using index-guided retrieval. At ~2,000+ articles, hybrid RAG (keyword + semantic search) becomes necessary.

## Related

- [[compound-knowledge]] — the compounding mechanism
- [[index-guided-retrieval]] — the retrieval strategy
- [[file-over-app]] — the data philosophy
- [[memex]] — the historical precedent
- [[claude-memory-compiler]] — a reference implementation of the LLM Wiki pattern for conversation-based compilation