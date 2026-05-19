---
title: "Farzapedia"
summary: "Karpathy's analysis of Farzapedia as an exemplar of the LLM Wiki personalization pattern, highlighting four advantages: explicit memory, data ownership, file-over-app interoperability, and BYOAI flexibility"
type: summary
sources:
  - raw/articles/farzapedia.md
tags:
  - llm-wiki
  - personalization
  - knowledge-management
  - farzapedia
created: "2026-05-01T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: reingested
---

# Farzapedia

## Summary

Karpathy's commentary on Farzapedia (Farza's personal wiki) presents the LLM Wiki pattern through the lens of AI personalization. He contrasts the approach with the "status quo" of implicit AI learning (where an AI "allegedly gets better the more you use it") and articulates four distinct advantages that put the user in full control of their data and AI relationship. ^[raw/articles/farzapedia.md:4-6]

## The Four Pillars of LLM Wiki Personalization

| Pillar | Principle | Implication |
|--------|-----------|-------------|
| **Explicit** | Memory artifacts are explicit and navigable | You can see exactly what the AI does and does not know; inspectable even if LLM-written |
| **Yours** | Data is on your local computer | Not locked in a provider's system; fully extractable and portable |
| **File over App** | Stored in universal formats (markdown, images) | Interoperable with any tool, CLI, or agent; entire Unix toolkit applicable |
| **BYOAI** | Use any AI you want | Claude, Codex, OpenCode, or finetuned open-source models; keeps providers competitive |

^[raw/articles/farzapedia.md:4-9]

## Comparison: LLM Wiki vs. Implicit AI Personalization

| Dimension | LLM Wiki Pattern | Status Quo (Implicit Learning) |
|-----------|-----------------|-------------------------------|
| Memory format | Explicit, navigable markdown files | Implicit, black-box model weights |
| Data location | Local computer, user-controlled | AI provider's system |
| Data format | Universal (markdown, images) | Proprietary, often non-extractable |
| AI flexibility | Any model, any provider | Tied to specific provider |
| Control | User in full control | Provider-centric |

^[raw/articles/farzapedia.md:4-11]

## Agent Proficiency

Karpathy emphasizes that managing file directories requires some technical comfort, but agents make it simple. He argues that **agent proficiency** is a core skill of the 21st century:

> "These are extremely powerful tools - they speak English and they do all the computer stuff for you. Try this opportunity to play with one." ^[raw/articles/farzapedia.md:13]

## Finetuning Vision

The strongest form of BYOAI involves finetuning an open-source model on the wiki data. This would allow the AI to "know" the user in its weights -- not merely attend over the data in a context window. This represents the ultimate expression of data ownership and AI flexibility combined. ^[raw/articles/farzapedia.md:9]

## Key Quotes

> "This approach to personalization puts _you_ in full control. The data is yours. In Universal formats. Explicit and inspectable. Use whatever AI you want over it, keep the AI companies on their toes!" ^[raw/articles/farzapedia.md:11]

> "'agent proficiency' is a CORE SKILL of the 21st century. These are extremely powerful tools - they speak English and they do all the computer stuff for you." ^[raw/articles/farzapedia.md:13]

## Related

- [[concepts/llm_wiki]]
- [[concepts/file_over_app]]
- [[concepts/byoai]]
- [[summaries/karpathy-github-llm-wiki]]
- [[summaries/karpathy-tweet-llm-wiki]]
