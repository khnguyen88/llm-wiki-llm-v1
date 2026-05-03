---
title: "OpenAI"
summary: "An AI research and deployment company whose API service tiers are supported through OpenRouter, with automated prompt caching and no cache write costs"
type: entity
sources:
  - raw/document/openrouter/openrouter-047-guides-features-service-tiers-2026-04-29.md
  - raw/document/openrouter/openrouter-070-guides-best-practices-prompt-caching-2026-04-29.md
tags:
  - openai
  - llm-provider
  - service-tier
  - prompt-caching
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: merged
---

# OpenAI

An AI research and deployment company that provides language models and API services. OpenAI is the only provider currently listed as supporting the `service_tier` parameter through OpenRouter. OpenAI prompt caching is automated on OpenRouter with no cache write costs and reduced cache read pricing. ^[raw/document/openrouter/openrouter-047-guides-features-service-tiers-2026-04-29.md] ^[raw/document/openrouter/openrouter-070-guides-best-practices-prompt-caching-2026-04-29.md]

## Key Facts

- OpenAI is the supported provider for the `service_tier` parameter on OpenRouter ^[raw/document/openrouter/openrouter-047-guides-features-service-tiers-2026-04-29.md]
- Accepted `service_tier` values for OpenAI: `auto`, `default`, `flex`, `priority` ^[raw/document/openrouter/openrouter-047-guides-features-service-tiers-2026-04-29.md]
- OpenAI's Chat Completions and Responses APIs return `service_tier` at the top level of the response object ^[raw/document/openrouter/openrouter-047-guides-features-service-tiers-2026-04-29.md]
- Prompt caching with OpenAI is automated and requires no additional configuration on OpenRouter; minimum prompt size of 1024 tokens ^[raw/document/openrouter/openrouter-070-guides-best-practices-prompt-caching-2026-04-29.md]
- OpenAI cache writes incur no cost; cache reads are charged at 0.25x or 0.50x the original input pricing depending on the model ^[raw/document/openrouter/openrouter-070-guides-best-practices-prompt-caching-2026-04-29.md]

## Related

- [[concepts/service_tier]]
- [[concepts/prompt_caching]]
- [[entities/openrouter]]
- [[summaries/openrouter-guides-features-service-tiers]]
- [[summaries/openrouter-guides-best-practices-prompt-caching]]