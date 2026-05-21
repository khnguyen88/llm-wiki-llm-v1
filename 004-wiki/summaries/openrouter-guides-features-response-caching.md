---
title: "OpenRouter Response Caching"
summary: "OpenRouter's response caching feature stores identical API responses and returns them at zero cost on subsequent requests, configurable per-request or via presets with TTL control"
type: summary
sources:
  - raw/document/openrouter/openrouter-031-guides-features-response-caching-2026-04-29.md
tags:
  - openrouter
  - caching
  - cost-optimization
  - api
  - response-caching
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# OpenRouter Response Caching

## Key Points

- Response caching returns previously computed responses for identical requests at zero cost, with all billable usage counters reported as `0` on cache hits ^[001a-raw/document/openrouter/openrouter-031-guides-features-response-caching-2026-04-29.md]
- Cache keys are derived from API key, model, endpoint type, streaming mode, and a SHA-256 hash of the request body; JSON property order is significant and different orderings produce different keys ^[001a-raw/document/openrouter/openrouter-031-guides-features-response-caching-2026-04-29.md]
- Caching can be enabled per-request via the `X-OpenRouter-Cache` header or configured in presets via `cache_enabled` and `cache_ttl_seconds` fields ^[001a-raw/document/openrouter/openrouter-031-guides-features-response-caching-2026-04-29.md]
- Default TTL is 300 seconds (5 minutes), configurable from 1 to 86400 seconds (24 hours) ^[001a-raw/document/openrouter/openrouter-031-guides-features-response-caching-2026-04-29.md]
- Cache is scoped to the API key; different keys under the same account do not share cache ^[001a-raw/document/openrouter/openrouter-031-guides-features-response-caching-2026-04-29.md]
- Cached responses are returned verbatim regardless of stochastic parameters like `temperature`; use `X-OpenRouter-Cache-Clear: true` to force a fresh response ^[001a-raw/document/openrouter/openrouter-031-guides-features-response-caching-2026-04-29.md]
- Response caching is disabled when account-level Zero Data Retention (ZDR) is enforced, since caching requires temporarily storing response data ^[001a-raw/document/openrouter/openrouter-031-guides-features-response-caching-2026-04-29.md]

## Quotes

- "When a cached response is available, OpenRouter returns it immediately from cache with no billing (all billable usage counters are reported as `0`), reducing both latency and cost." ^[001a-raw/document/openrouter/openrouter-031-guides-features-response-caching-2026-04-29.md]
- "Cache hits do not count toward provider rate limits since the request never reaches a provider." ^[001a-raw/document/openrouter/openrouter-031-guides-features-response-caching-2026-04-29.md]
- "Cached responses are returned verbatim regardless of stochastic parameters like `temperature`. If you need fresh responses, use `X-OpenRouter-Cache-Clear: true` or a short TTL." ^[001a-raw/document/openrouter/openrouter-031-guides-features-response-caching-2026-04-29.md]

## Notes

- Response caching is currently in beta; the API and behavior may change ^[001a-raw/document/openrouter/openrouter-031-guides-features-response-caching-2026-04-29.md]
- Only successful (`200 OK`) responses are cached; error responses, rate limit responses, and partial results are never cached ^[001a-raw/document/openrouter/openrouter-031-guides-features-response-caching-2026-04-29.md]
- Responses containing tool calls are cached normally as part of successful completions ^[001a-raw/document/openrouter/openrouter-031-guides-features-response-caching-2026-04-29.md]
- For streaming requests, cached responses are replayed through the same streaming pipeline with new generation IDs and timestamps ^[001a-raw/document/openrouter/openrouter-031-guides-features-response-caching-2026-04-29.md]
- OpenRouter response caching is separate from provider-side prompt caching (e.g., Anthropic prompt caching, OpenAI cached context); the two can be used together ^[001a-raw/document/openrouter/openrouter-031-guides-features-response-caching-2026-04-29.md]
- There is no request coalescing — two identical concurrent requests both result in cache misses ^[001a-raw/document/openrouter/openrouter-031-guides-features-response-caching-2026-04-29.md]

## Related

- [[004-wiki/entities/openrouter]]
- [[004-wiki/concepts/response-caching]]
- [[004-wiki/concepts/prompt-caching]]
- [[004-wiki/concepts/presets]]
- [[004-wiki/concepts/zero-data-retention]]
- [[004-wiki/concepts/embedding-models]]
- [[004-wiki/concepts/rate-limiting]]
- [[004-wiki/concepts/streaming-output]]