---
title: "Openrouter Guides Best Practices Prompt Caching"
summary: "Covers prompt caching across providers on OpenRouter, including provider sticky routing, per-provider caching behavior, cache TTL options, and usage inspection"
type: summary
sources:
  - raw/document/openrouter/openrouter-070-guides-best-practices-prompt-caching-2026-04-29.md
tags:
  - openrouter
  - prompt-caching
  - provider-sticky-routing
  - anthropic
  - openai
  - deepseek
  - gemini
  - groq
  - grok
  - moonshot
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Openrouter Guides Best Practices Prompt Caching

## Key Points

- OpenRouter uses provider sticky routing to maximize cache hit rates by routing subsequent requests to the same provider endpoint after a cached request ^[raw/document/openrouter/openrouter-070-guides-best-practices-prompt-caching-2026-04-29.md]
- Sticky routing is tracked at the account level, per model and per conversation, identified by hashing the first system message and first non-system message ^[raw/document/openrouter/openrouter-070-guides-best-practices-prompt-caching-2026-04-29.md]
- Most providers enable prompt caching automatically; Anthropic requires explicit `cache_control` configuration on a per-message basis ^[raw/document/openrouter/openrouter-070-guides-best-practices-prompt-caching-2026-04-29.md]
- Cache usage can be inspected via the Activity page, the `/api/v1/generation` API, or the `prompt_tokens_details` object in API responses ^[raw/document/openrouter/openrouter-070-guides-best-practices-prompt-caching-2026-04-29.md]
- OpenAI, Grok, Moonshot AI, and Groq offer automated caching with no cost for cache writes and reduced-cost cache reads ^[raw/document/openrouter/openrouter-070-guides-best-practices-prompt-caching-2026-04-29.md]
- Anthropic supports both automatic caching (top-level `cache_control`) and explicit cache breakpoints (per-block `cache_control`), with a 5-minute default TTL and an optional 1-hour TTL ^[raw/document/openrouter/openrouter-070-guides-best-practices-prompt-caching-2026-04-29.md]
- Google Gemini 2.5 Pro and 2.5 Flash support implicit caching with no cache write or storage costs, and explicit `cache_control` breakpoints via OpenRouter ^[raw/document/openrouter/openrouter-070-guides-best-practices-prompt-caching-2026-04-29.md]

## Quotes

- "Sticky routing only activates when the provider's cache read pricing is cheaper than regular prompt pricing, ensuring you always benefit from cost savings." ^[raw/document/openrouter/openrouter-070-guides-best-practices-prompt-caching-2026-04-29.md]

## Notes

- The source uses placeholder tokens like `{ANTHROPIC_CACHE_WRITE_MULTIPLIER}` and `{GOOGLE_CACHE_READ_MULTIPLIER}` for provider-specific pricing multipliers, indicating these are dynamic values that vary by model and may change over time.
- DeepSeek charges the same rate for cache writes as regular input tokens, unlike most other providers that offer free cache writes.

## Related

- [[concepts/prompt_caching]]
- [[concepts/provider_sticky_routing]]
- [[entities/openrouter]]
- [[entities/anthropic]]
- [[entities/openai]]
- [[entities/deepseek]]
- [[entities/google_gemini]]
- [[entities/grok]]
- [[entities/moonshot_ai]]
- [[entities/groq]]