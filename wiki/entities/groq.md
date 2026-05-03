---
title: "Groq"
summary: "High-speed inference provider available on OpenRouter with automated prompt caching for Kimi K2 models and no cache write costs"
type: entity
sources:
  - raw/document/openrouter/openrouter-070-guides-best-practices-prompt-caching-2026-04-29.md
tags:
  - llm-provider
  - groq
  - inference
  - prompt-caching
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Groq

High-speed inference provider available on OpenRouter. Prompt caching on Groq is automated and currently available on Kimi K2 models. Cache writes incur no cost, and cache reads are charged at a reduced multiplier of the original input pricing. ^[raw/document/openrouter/openrouter-070-guides-best-practices-prompt-caching-2026-04-29.md]

## Key Facts

- Prompt caching is automated and requires no additional configuration on OpenRouter ^[raw/document/openrouter/openrouter-070-guides-best-practices-prompt-caching-2026-04-29.md]
- Currently available on Kimi K2 models ^[raw/document/openrouter/openrouter-070-guides-best-practices-prompt-caching-2026-04-29.md]
- Cache writes: no cost ^[raw/document/openrouter/openrouter-070-guides-best-practices-prompt-caching-2026-04-29.md]
- Cache reads: charged at a reduced multiplier of the original input pricing ^[raw/document/openrouter/openrouter-070-guides-best-practices-prompt-caching-2026-04-29.md]

## Related

- [[entities/openrouter]]
- [[concepts/prompt_caching]]
- [[concepts/provider_sticky_routing]]