---
title: "Memex"
summary: "Vannevar Bush's 1945 concept of a personal, curated knowledge store with associative trails between documents -- a conceptual predecessor to the LLM Wiki"
type: concept
sources:
  - raw/articles/karpathy-github-llm-wiki.md
tags:
  - memex
  - knowledge-management
  - history
created: "2026-05-01T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: merged
---

# Memex

Vannevar Bush's 1945 concept of a personal, curated knowledge store with associative trails between documents. Bush's vision -- described in his essay "As We May Think" -- was closer to the LLM Wiki pattern than to what the web became: private, actively curated, with the connections between documents as valuable as the documents themselves. ^[raw/articles/karpathy-github-llm-wiki.md:72]

## Key Points

- Proposed by Vannevar Bush in 1945 as a personal knowledge store with associative trails between documents ^[raw/articles/karpathy-github-llm-wiki.md:72]
- Bush's vision was private and actively curated, with document connections as valuable as the documents themselves ^[raw/articles/karpathy-github-llm-wiki.md:72]
- The critical unsolved problem in Bush's vision was who performs the maintenance -- the LLM solves this ^[raw/articles/karpathy-github-llm-wiki.md:72]

## Relationship to LLM Wiki

The Memex concept is the intellectual predecessor of the LLM Wiki pattern. Both share the core idea of a personal knowledge store where the connections between documents are as important as the documents themselves. The critical difference is that Bush could not solve the maintenance problem -- who would keep the knowledge store current and consistent across dozens or hundreds of documents.

The LLM Wiki pattern addresses this by delegating all bookkeeping (updating cross-references, flagging contradictions, maintaining consistency across dozens of pages) to the LLM, making the cost of maintenance near zero. This effectively realizes Bush's vision with a mechanism he could not have anticipated: an AI agent that handles the grunt work of knowledge base maintenance. ^[raw/articles/karpathy-github-llm-wiki.md:68-72]

## Contrast with the Web

Bush's Memex was fundamentally different from the World Wide Web in key ways:

| Aspect | Memex / LLM Wiki | World Wide Web |
|--------|-------------------|---------------|
| Ownership | Private, personal | Public, shared |
| Curation | Actively curated by individual | Crowd-sourced, algorithmic |
| Connections (trails) | Manually (or LLM-) created, persistent | Hyperlinks, often broken |
| Purpose | Personal knowledge amplification | Global information sharing |

## Related

- [[concepts/llm_wiki]]
