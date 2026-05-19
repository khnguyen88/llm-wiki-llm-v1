---
title: "Provider Fallback"
summary: "An availability pattern where requests are automatically rerouted to alternative providers when the primary provider is down or degraded"
type: concept
sources:
  - raw/document/openrouter/openrouter-002-guides-overview-principles-2026-04-29.md
  - raw/document/openrouter/openrouter-015-faq-2026-04-29.md
  - raw/document/openrouter/openrouter-017-guides-routing-model-fallbacks-2026-04-29.md
tags:
  - provider-fallback
  - availability
  - routing
  - openrouter
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Provider Fallback

An availability pattern where requests are automatically rerouted to alternative providers when the primary provider experiences downtime or degradation. OpenRouter implements this through fallback providers and automatic smart routing, ensuring requests continue to work even when individual providers go down. ^[raw/document/openrouter/openrouter-002-guides-overview-principles-2026-04-29.md]

## Key Points

- Fallback providers serve as backup endpoints that absorb traffic when a primary provider becomes unavailable ^[raw/document/openrouter/openrouter-002-guides-overview-principles-2026-04-29.md]
- Smart routing automatically directs requests away from degraded providers without manual intervention ^[raw/document/openrouter/openrouter-002-guides-overview-principles-2026-04-29.md]
- This pattern is a core benefit of multi-provider platforms like OpenRouter, which aggregate many providers and can transparently switch between them ^[raw/document/openrouter/openrouter-002-guides-overview-principles-2026-04-29.md]
- On OpenRouter, when a provider returns an error, the system automatically falls back to the next available provider; this happens transparently to the user ^[raw/document/openrouter/openrouter-015-faq-2026-04-29.md]
- OpenRouter offers extensive configuration options for provider routing behavior, including the ability to specify provider ordering and fallback preferences ^[raw/document/openrouter/openrouter-015-faq-2026-04-29.md]

## Details

Provider fallback is distinct from simple retry logic. Rather than retrying the same provider, fallback routing sends the request to a different provider entirely, leveraging the multi-provider architecture of gateway platforms. This provides higher availability than any single provider can offer on its own. ^[raw/document/openrouter/openrouter-002-guides-overview-principles-2026-04-29.md]

Provider fallback is also distinct from [[concepts/model_fallback]], which switches to an entirely different model rather than a different provider for the same model. The two patterns can complement each other: a request may first attempt provider fallback for the primary model, then fall back to an alternative model if all providers for the primary model are unavailable. ^[raw/document/openrouter/openrouter-017-guides-routing-model-fallbacks-2026-04-29.md]

## Related

- [[entities/openrouter]]
- [[concepts/llm_gateway]]
- [[concepts/routing_mode]]
- [[concepts/rate_limiting]]
- [[summaries/openrouter-faq]]
- [[concepts/model_fallback]]
- [[summaries/openrouter-guides-routing-model-fallbacks]]