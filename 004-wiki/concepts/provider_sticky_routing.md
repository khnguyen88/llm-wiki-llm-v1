---
title: "Provider Sticky Routing"
summary: "OpenRouter's mechanism that routes subsequent requests to the same provider endpoint after a cached request, maximizing prompt cache hit rates"
type: concept
sources:
  - raw/document/openrouter/openrouter-070-guides-best-practices-prompt-caching-2026-04-29.md
tags:
  - openrouter
  - provider-routing
  - prompt-caching
  - cost-optimization
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 1.0
provenance: extracted
---

# Provider Sticky Routing

OpenRouter's mechanism for maximizing [[concepts/prompt_caching|prompt cache]] hit rates by routing subsequent requests to the same provider endpoint after a cached request. It works automatically with both implicit caching (e.g., OpenAI, DeepSeek, Gemini 2.5) and explicit caching (e.g., Anthropic `cache_control` breakpoints). ^[raw/document/openrouter/openrouter-070-guides-best-practices-prompt-caching-2026-04-29.md]

## Key Points

- After a request that uses prompt caching, OpenRouter remembers which provider served the request and routes subsequent requests for the same model to that provider to keep the cache warm ^[raw/document/openrouter/openrouter-070-guides-best-practices-prompt-caching-2026-04-29.md]
- Sticky routing only activates when the provider's cache read pricing is cheaper than regular prompt pricing, ensuring the user always benefits from cost savings ^[raw/document/openrouter/openrouter-070-guides-best-practices-prompt-caching-2026-04-29.md]
- If the sticky provider becomes unavailable, OpenRouter automatically falls back to the next-best provider ^[raw/document/openrouter/openrouter-070-guides-best-practices-prompt-caching-2026-04-29.md]
- Sticky routing is not used when a manual provider order is specified via `provider.order`; explicit ordering takes priority ^[raw/document/openrouter/openrouter-070-guides-best-practices-prompt-caching-2026-04-29.md]
- Routing is tracked at the account level, per model and per conversation, identified by hashing the first system (or developer) message and the first non-system message ^[raw/document/openrouter/openrouter-070-guides-best-practices-prompt-caching-2026-04-29.md]

## Details

Provider sticky routing improves load-balancing and throughput by keeping different conversations on different providers while maintaining cache warmth within each conversation. Because conversations are identified by the hash of their opening messages, requests that share the same opening messages naturally stick to the same provider. This means different conversations with different system prompts distribute across providers, but related requests within the same conversation remain cache-friendly.

The mechanism is transparent to the user and requires no configuration. It activates automatically whenever a provider offers cheaper cache reads compared to regular prompt pricing, and deactivates gracefully when the user explicitly controls provider ordering.

## Related

- [[concepts/prompt_caching]]
- [[concepts/provider_routing]]
- [[entities/openrouter]]