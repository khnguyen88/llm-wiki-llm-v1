---
title: Compound Knowledge
type: concept
date: 2026-04-22
sources:
  - raw/articles/karpathy-github-llm-wiki.md
  - raw/articles/karpathy-tweet-llm-wiki.md
tags:
  - knowledge-management
  - compounding
---

# Compound Knowledge

The principle that every interaction with the wiki enriches it — not just source ingestion, but also queries. When an answer is valuable, it gets filed back as a new page, making future queries smarter.

## How It Works

1. **Ingest**: New sources update 10-15 wiki pages
2. **Query**: Complex answers can be filed back as Q&A pages
3. **Lint**: Health checks find gaps and suggest new investigations

Each cycle adds permanent structure. Cross-references, contradictions, and synthesis accumulate rather than being rediscovered.

## Related

- [[llm_wiki]] — the system built on this principle
- [[concepts/file_over_app]] — the data philosophy enabling compounding
- [[summaries/claude-memory-compiler]] — implements the compounding loop via `--file-back` queries and auto-compilation