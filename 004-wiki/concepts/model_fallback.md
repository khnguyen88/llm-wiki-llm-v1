---
title: "Model Fallback"
summary: "A reliability pattern where an ordered list of model IDs is specified so that if the primary model fails, the next model in the list is tried automatically"
type: concept
sources:
  - raw/document/openrouter/openrouter-017-guides-routing-model-fallbacks-2026-04-29.md
  - raw/document/openrouter/openrouter-018-guides-routing-provider-selection-2026-04-29.md
  - raw/document/openrouter/openrouter-069-guides-best-practices-latency-and-performance-2026-04-29.md
tags:
  - model-fallback
  - routing
  - reliability
  - openrouter
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:03Z"
confidence: 0.9
provenance: merged
---

# Model Fallback

A reliability pattern where an ordered list of model IDs is specified in a request so that if the primary model returns an error, the next model in the list is tried automatically. On OpenRouter, this is implemented via the `models` parameter on the chat completions endpoint. ^[raw/document/openrouter/openrouter-017-guides-routing-model-fallbacks-2026-04-29.md]

## Key Points

- The `models` parameter accepts an array of model IDs in priority order; OpenRouter tries each model in sequence until one succeeds ^[raw/document/openrouter/openrouter-017-guides-routing-model-fallbacks-2026-04-29.md]
- Any error triggers fallback by default: context length validation errors, moderation flags on filtered models, rate-limiting, and provider downtime ^[raw/document/openrouter/openrouter-017-guides-routing-model-fallbacks-2026-04-29.md]
- If both the primary and fallback models fail, OpenRouter returns the fallback model's error ^[raw/document/openrouter/openrouter-017-guides-routing-model-fallbacks-2026-04-29.md]
- Pricing is based on whichever model ultimately handled the request, returned in the response `model` attribute ^[raw/document/openrouter/openrouter-017-guides-routing-model-fallbacks-2026-04-29.md]
- With the OpenAI SDK, the `models` array is passed via `extra_body` (Python) or directly (TypeScript) since it is not a standard OpenAI parameter ^[raw/document/openrouter/openrouter-017-guides-routing-model-fallbacks-2026-04-29.md]
- A failed initial completion attempt adds latency to the specific request; OpenRouter tracks provider failures and routes around unavailable providers to prevent this latency from recurring on every request ^[raw/document/openrouter/openrouter-069-guides-best-practices-latency-and-performance-2026-04-29.md]

## Details

Model fallback is distinct from [[concepts/provider_fallback]]: provider fallback reroutes to an alternative provider for the *same model*, while model fallback switches to an entirely *different model*. Model fallback gives developers explicit control over which alternative models to use, whereas provider fallback is handled automatically by the platform. ^[raw/document/openrouter/openrouter-017-guides-routing-model-fallbacks-2026-04-29.md]

The `models` array is useful for applications that require high availability but can tolerate differences in model capability or behavior across fallback options. Developers should choose fallback models that are functionally adequate for their use case, since the fallback may handle any given request. ^[raw/document/openrouter/openrouter-017-guides-routing-model-fallbacks-2026-04-29.md]

## Related

- [[entities/openrouter]]
- [[concepts/provider_fallback]]
- [[concepts/routing_mode]]
- [[concepts/rate_limiting]]
- [[concepts/llm_gateway]]
- [[summaries/openrouter-guides-routing-model-fallbacks]]
- [[concepts/auto_router]]
- [[summaries/openrouter-guides-best-practices-latency-and-performance]]