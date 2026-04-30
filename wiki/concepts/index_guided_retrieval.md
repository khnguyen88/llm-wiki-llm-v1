---
title: Index-Guided Retrieval
type: concept
date: 2026-04-22
sources:
  - raw/articles/karpathy-github-llm-wiki.md
  - raw/articles/karpathy-tweet-llm-wiki.md
tags:
  - retrieval
  - rag
  - knowledge-management
---

# Index-Guided Retrieval

The retrieval strategy used by LLM wikis at moderate scale: the LLM reads a structured `index.md` listing all pages with one-line summaries, then selectively reads the relevant pages in full.

## Why It Works

At personal knowledge base scale (~100 sources, hundreds of pages), the LLM reading a structured index outperforms vector similarity. The LLM understands what the question is really asking; cosine similarity just finds similar words.

## When RAG Becomes Necessary

At ~2,000+ articles / ~2M+ tokens, the index exceeds the context window. At that point, add hybrid RAG (keyword + semantic search with LLM re-ranking) as a pre-filter before the LLM reads selected pages.

## Related

- [[llm_wiki]] — the system that uses this retrieval
- [[concepts/compound_knowledge]] — the compounding loop that makes retrieval effective