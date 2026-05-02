---
title: "Karpathy Github Llm Wiki"
summary: "Karpathy's original design document for the LLM Wiki pattern — a persistent, compounding wiki built and maintained by an LLM from curated sources, contrasting with RAG's per-query retrieval"
type: summary
sources:
  - raw/articles/karpathy-github-llm-wiki.md
tags:
  - llm-wiki
  - architecture
  - knowledge-management
  - rag
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 1.0
provenance: extracted
---

# Karpathy Github Llm Wiki

## Key Points

- The LLM Wiki pattern replaces per-query retrieval (RAG) with a persistent, compounding wiki that integrates knowledge as sources are added ^[raw/articles/karpathy-github-llm-wiki.md:11-15]
- Three architecture layers: raw sources (immutable), the wiki (LLM-owned markdown), and the schema (configuration for LLM behavior) ^[raw/articles/karpathy-github-llm-wiki.md:29-35]
- Three operations: ingest (add sources, update 10-15 wiki pages), query (synthesize answers with citations, file good answers back), lint (health-check for contradictions, orphans, gaps) ^[raw/articles/karpathy-github-llm-wiki.md:39-43]
- index.md (content catalog) and log.md (chronological record) provide navigation without needing embedding-based RAG infrastructure ^[raw/articles/karpathy-github-llm-wiki.md:47-51]
- The wiki works because LLMs eliminate the bookkeeping burden that causes humans to abandon knowledge bases ^[raw/articles/karpathy-github-llm-wiki.md:68-70]
- The idea relates to Vannevar Bush's Memex (1945) — a personal curated knowledge store with associative trails ^[raw/articles/karpathy-github-llm-wiki.md:72]
- The document is intentionally abstract; exact implementation depends on domain, preferences, and LLM of choice ^[raw/articles/karpathy-github-llm-wiki.md:74-76]

## Quotes

- "The wiki is a persistent, compounding artifact." ^[raw/articles/karpathy-github-llm-wiki.md:15]
- "Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase." ^[raw/articles/karpathy-github-llm-wiki.md:17]
- "Good answers can be filed back into the wiki as new pages." ^[raw/articles/karpathy-github-llm-wiki.md:41]
- "Humans abandon wikis because the maintenance burden grows faster than the value. LLMs don't get bored, don't forget to update a cross-reference, and can touch 15 files in one pass." ^[raw/articles/karpathy-github-llm-wiki.md:68]

## Notes

- This is Karpathy's original design document for the LLM Wiki pattern, more comprehensive than the earlier Farzapedia commentary
- Use cases listed: personal tracking, research, book reading, business/team, competitive analysis, due diligence, trip planning, course notes, hobby deep-dives ^[raw/articles/karpathy-github-llm-wiki.md:19-25]
- CLI tools mentioned: qmd (local search engine with hybrid BM25/vector search and LLM re-ranking) ^[raw/articles/karpathy-github-llm-wiki.md:55]

## Related

- [[concepts/llm_wiki]]
- [[entities/obsidian]]
- [[concepts/rag]]
- [[concepts/memex]]
- [[concepts/file_over_app]]
- [[concepts/byoai]]