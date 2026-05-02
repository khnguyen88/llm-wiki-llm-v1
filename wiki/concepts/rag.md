---
title: "RAG"
summary: "Retrieval-Augmented Generation — a pattern where an LLM retrieves relevant document chunks at query time, re-deriving knowledge from scratch on every question"
type: concept
sources:
  - raw/articles/karpathy-github-llm-wiki.md
  - raw/articles/karpathy-tweet-llm-wiki.md
tags:
  - rag
  - llm-wiki
  - retrieval
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T16:30:00Z"
confidence: 0.9
provenance: extracted
---

# RAG

Retrieval-Augmented Generation — the dominant pattern for LLM-document interaction where the LLM retrieves relevant chunks from uploaded files at query time and generates an answer. NotebookLM, ChatGPT file uploads, and most RAG systems work this way. ^[raw/articles/karpathy-github-llm-wiki.md:11]

## Key Points

- In RAG, the LLM retrieves relevant document chunks at query time and generates an answer — there is no accumulation of knowledge across queries ^[raw/articles/karpathy-github-llm-wiki.md:11]
- Subtle questions requiring synthesis of multiple documents force the LLM to find and piece together relevant fragments every time, with nothing built up ^[raw/articles/karpathy-github-llm-wiki.md:11]
- The LLM Wiki pattern avoids embedding-based RAG infrastructure at moderate scale (~100 sources, ~hundreds of pages) by using an index file for navigation instead ^[raw/articles/karpathy-github-llm-wiki.md:49]
- Karpathy expected to need "fancy RAG" for querying his wiki, but found the LLM could navigate ~100 articles and ~400K words via auto-maintained index files and summaries ^[raw/articles/karpathy-tweet-llm-wiki.md:13]

## Details

RAG contrasts with the LLM Wiki pattern in a fundamental way. RAG re-derives knowledge on every query; the LLM Wiki compiles knowledge once and keeps it current. In RAG, cross-references must be discovered anew each time, contradictions are not pre-flagged, and synthesis does not accumulate across sources. The LLM Wiki addresses these limitations by maintaining a persistent, structured wiki that compounds with every source added. ^[raw/articles/karpathy-github-llm-wiki.md:11-15]

Karpathy reports that at moderate scale (~100 articles, ~400K words), RAG is unnecessary. The LLM auto-maintains index files and brief summaries of all documents, enabling it to read the relevant related data directly. This suggests a practical threshold below which the overhead of embedding-based RAG infrastructure is not justified. ^[raw/articles/karpathy-tweet-llm-wiki.md:13]

## Related

- [[concepts/llm_wiki]]