---
title: "File over App"
summary: "A philosophy advocating that personal data and knowledge should be stored in universal file formats rather than being locked into specific applications"
type: concept
sources:
  - raw/articles/farzapedia.md
tags:
  - file-over-app
  - interoperability
  - data-ownership
  - llm-wiki
created: "2026-05-01T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: merged
---

# File over App

A philosophy advocating that personal data and knowledge should be stored in universal file formats (images, markdown) rather than being locked into specific applications. This makes data interoperable -- any tool, CLI, or agent can read, process, and write to it. Karpathy references this philosophy as a broader design movement, recommending a dedicated article on the subject. ^[raw/articles/farzapedia.md:8]

## Key Points

- Data stored in universal formats (images, markdown) is inherently interoperable -- a large collection of tools and CLIs can operate on it because it is just files ^[raw/articles/farzapedia.md:8]
- Agents can apply the entire Unix toolkit over file-based data, and natively read and understand the content ^[raw/articles/farzapedia.md:8]
- Any kind of data can be imported into files as input, and any kind of interface can be used to view them as output -- e.g., Obsidian for viewing or custom vibe-coded interfaces ^[raw/articles/farzapedia.md:8]
- This philosophy is one of four pillars of the LLM Wiki personalization pattern, directly supporting the "Yours" property ^[raw/articles/farzapedia.md:4-8]

## Relationship to Multi-Agent Systems

In multi-agent setups, the "File over App" philosophy extends naturally: multiple agents can operate on the same file-based knowledge base simultaneously. Each agent can read, write, and cross-reference wiki pages without contention, because the data is in a simple, universal format that every agent natively understands. This is harder to achieve with application-locked data formats. ^[raw/articles/farzapedia.md:7-8]

## Related

- [[concepts/llm_wiki]]
- [[concepts/byoai]]
