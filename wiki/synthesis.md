---
title: Synthesis
type: synthesis
date: 2026-04-22
sources:
  - raw/articles/karpathy-github-llm-wiki.md
  - raw/articles/karpathy-tweet-llm-wiki.md
  - raw/articles/farzapedia.md
---

# Synthesis

## Key Themes

- **Persistent, compounding knowledge**: The LLM Wiki pattern replaces RAG's rediscovery-per-query with a wiki that grows richer with every source and question. Cross-references, contradictions, and synthesis accumulate permanently.
- **File over app, BYOAI**: Knowledge lives in universal formats (markdown, images) under your control, not locked in an AI provider. Any LLM can plug in. This is both a practical and philosophical stance.
- **LLM as maintainer, human as curator**: The tedious bookkeeping (cross-references, consistency, summaries) is the LLM's job. The human directs sources, asks questions, and judges what matters.
- **Index-guided retrieval at scale**: At ~100 sources, a structured index.md outperforms vector similarity. At ~2,000+ articles, add hybrid RAG as a pre-filter.

## Key Findings

- A single source touches 10-15 wiki pages — entities, concepts, summaries, cross-references
- Karpathy's own research wiki reached ~100 articles / ~400K words and works well without RAG
- The approach traces back to Vannevar Bush's Memex (1945): personal, curated knowledge with associative trails
- Answers can be filed back into the wiki, creating a compounding loop where exploration enriches the KB
- The three operations (ingest, query, lint) form a complete cycle for building and maintaining knowledge

## Open Questions

- At what scale does index-guided retrieval break down? Karpathy suggests ~2,000 articles
- How well does finetuning on a wiki work as an alternative to context-window retrieval?
- What product could make this workflow accessible beyond the "agent-proficient" user?
- How do multi-user wikis work? Can team wikis be maintained by LLMs with human review?

## How This File Works

This file represents the "thesis" of your knowledge base. The LLM maintains it by:
1. Reading new source summaries
2. Identifying how they connect to existing knowledge
3. Updating themes and findings
4. Noting any contradictions or gaps

You rarely need to edit this directly - let the LLM maintain it as you add sources.

---

*Last updated: 2026-04-22*