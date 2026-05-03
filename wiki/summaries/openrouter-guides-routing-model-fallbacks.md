---
title: "Openrouter Guides Routing Model Fallbacks"
summary: "OpenRouter's models parameter lets developers specify an ordered list of model IDs as fallbacks, automatically trying the next model if the primary returns an error from rate-limiting, downtime, moderation, or context length issues"
type: summary
sources:
  - raw/document/openrouter/openrouter-017-guides-routing-model-fallbacks-2026-04-29.md
tags:
  - openrouter
  - model-fallback
  - routing
  - api
  - reliability
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Openrouter Guides Routing Model Fallbacks

## Key Points

- The `models` parameter accepts an array of model IDs in priority order; if the first model returns an error, OpenRouter automatically tries the next model in the list ^[raw/document/openrouter/openrouter-017-guides-routing-model-fallbacks-2026-04-29.md]
- Any error can trigger a fallback by default, including context length validation errors, moderation flags for filtered models, rate-limiting, and provider downtime ^[raw/document/openrouter/openrouter-017-guides-routing-model-fallbacks-2026-04-29.md]
- Requests are priced using whichever model ultimately handled the request, as indicated by the `model` attribute in the response body ^[raw/document/openrouter/openrouter-017-guides-routing-model-fallbacks-2026-04-29.md]
- The `models` array works with the OpenAI SDK by passing it via the `extra_body` parameter; the `model` field specifies the primary model and the `models` array specifies ordered fallbacks ^[raw/document/openrouter/openrouter-017-guides-routing-model-fallbacks-2026-04-29.md]
- If both the primary model and the fallback model return errors, OpenRouter returns the fallback model's error ^[raw/document/openrouter/openrouter-017-guides-routing-model-fallbacks-2026-04-29.md]

## Quotes

> "The `models` parameter lets you automatically try other models if the primary model's providers are down, rate-limited, or refuse to reply due to content moderation." ^[raw/document/openrouter/openrouter-017-guides-routing-model-fallbacks-2026-04-29.md:1]

## Notes

- The source shows usage examples in TypeScript SDK, TypeScript fetch, and Python, all using the `models` array in the chat completions request body
- OpenAI SDK integration requires `extra_body` (Python) or direct inclusion (TypeScript) since `models` is not a standard OpenAI parameter

## Related

- [[entities/openrouter]]
- [[concepts/model_fallback]]
- [[concepts/provider_fallback]]
- [[concepts/routing_mode]]
- [[concepts/rate_limiting]]