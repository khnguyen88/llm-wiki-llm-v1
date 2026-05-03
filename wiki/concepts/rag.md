---
title: "RAG"
summary: "Retrieval-Augmented Generation -- a pattern where an LLM retrieves relevant document chunks at query time, re-deriving knowledge from scratch on every question"
type: concept
sources:
  - raw/articles/karpathy-github-llm-wiki.md
  - raw/articles/karpathy-tweet-llm-wiki.md
tags:
  - rag
  - llm-wiki
  - retrieval
created: "2026-05-01T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: merged
---

# RAG

Retrieval-Augmented Generation is the dominant pattern for LLM-document interaction. In RAG, the system retrieves relevant chunks from uploaded files at query time and generates an answer from those chunks. NotebookLM, ChatGPT file uploads, and most RAG systems work this way. ^[raw/articles/karpathy-github-llm-wiki.md:11]

## Key Points

- In RAG, the LLM retrieves relevant document chunks at query time and generates an answer -- there is no accumulation of knowledge across queries ^[raw/articles/karpathy-github-llm-wiki.md:11]
- Subtle questions requiring synthesis of multiple documents force the LLM to find and piece together relevant fragments every time, with nothing built up across queries ^[raw/articles/karpathy-github-llm-wiki.md:11]
- There is no persistent cross-referencing, contradiction tracking, or synthesis accumulation ^[raw/articles/karpathy-github-llm-wiki.md:11]
- The LLM Wiki pattern avoids embedding-based RAG infrastructure at moderate scale (~100 sources, ~hundreds of pages) by using index file navigation instead ^[raw/articles/karpathy-github-llm-wiki.md:49]

## RAG vs. LLM Wiki: Comparison

| Dimension | RAG | LLM Wiki |
|-----------|-----|----------|
| Knowledge persistence | Re-derived on every query | Compiled once, kept current |
| Cross-references | Discovered anew each time | Pre-built and maintained |
| Contradictions | Not pre-flagged | Flagged during ingest/lint |
| Synthesis | Generated per query, then discarded | Accumulated across sources |
| Infrastructure | Embedding db, vector search, reranking | Flat markdown files + index |
| Scale for practical use | Unlimited | Moderate (~100 sources) without RAG |

^[raw/articles/karpathy-github-llm-wiki.md:11-15]

## Practical Observations

Karpathy expected to need "fancy RAG" for querying his wiki, but found the LLM could navigate ~100 articles and ~400K words via auto-maintained index files and brief summaries. This suggests a practical threshold below which the overhead of embedding-based RAG infrastructure is not justified. ^[raw/articles/karpathy-tweet-llm-wiki.md:13]

However, the LLM Wiki pattern is not inherently opposed to RAG. At larger scales, search tools (like qmd or a custom search engine) can complement the wiki, providing hybrid BM25/vector search and LLM re-ranking. ^[raw/articles/karpathy-github-llm-wiki.md:55]

## Related

- [[concepts/llm_wiki]]
- [[entities/qmd]]
