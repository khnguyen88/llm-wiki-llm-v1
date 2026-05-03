---
title: "Response Caching"
summary: "An OpenRouter feature that stores and returns identical API responses at zero cost, with cache keys derived from API key, model, endpoint, streaming mode, and request body hash"
type: concept
sources:
  - raw/document/openrouter/openrouter-031-guides-features-response-caching-2026-04-29.md
tags:
  - openrouter
  - caching
  - cost-optimization
  - api
  - performance
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Response Caching

Response caching on OpenRouter stores the full response for identical API requests and returns it immediately on subsequent identical requests, reducing both latency and cost. Cache hits are free — all billable usage counters are reported as `0`. ^[raw/document/openrouter/openrouter-031-guides-features-response-caching-2026-04-29.md]

## Key Points

- Cache keys are derived from API key, model, endpoint type, streaming mode, and a SHA-256 hash of the request body; JSON property order is significant (different orderings produce different keys) ^[raw/document/openrouter/openrouter-031-guides-features-response-caching-2026-04-29.md]
- Caching can be enabled per-request via `X-OpenRouter-Cache: true` header or configured in presets via `cache_enabled` and `cache_ttl_seconds` fields ^[raw/document/openrouter/openrouter-031-guides-features-response-caching-2026-04-29.md]
- Default TTL is 300 seconds (5 minutes), with a range of 1–86400 seconds (24 hours); customizable per-request or in presets ^[raw/document/openrouter/openrouter-031-guides-features-response-caching-2026-04-29.md]
- Cache is scoped to the API key; rotating keys results in an empty cache for the new key ^[raw/document/openrouter/openrouter-031-guides-features-response-caching-2026-04-29.md]
- Only successful (`200 OK`) responses are cached; errors, rate limits, and partial results are never cached ^[raw/document/openrouter/openrouter-031-guides-features-response-caching-2026-04-29.md]
- Response caching is disabled when account-level ZDR is enforced, since caching requires temporarily storing response data ^[raw/document/openrouter/openrouter-031-guides-features-response-caching-2026-04-29.md]

## Details

### Cache key composition

The cache key includes an endpoint type discriminator, so requests to different endpoints (`/chat/completions`, `/responses`, `/messages`, `/embeddings`) with identical bodies will not collide. The request body is normalized before hashing (extra whitespace is ignored), but JSON property order matters — `{"model":"x","messages":[]}` and `{"messages":[],"model":"x"}` produce different cache keys. Omitting optional fields vs. explicitly sending defaults also produces different keys. Attribution headers (`HTTP-Referer`, `X-Title`) and provider-specific headers are not part of the cache key. Multimodal requests including base64-encoded content are eligible for caching. ^[raw/document/openrouter/openrouter-031-guides-features-response-caching-2026-04-29.md]

### Precedence rules

Request headers and preset configuration interact as follows: (1) a preset with `cache_enabled: false` disables caching regardless of request headers; (2) `X-OpenRouter-Cache: false` disables caching even if the preset enables it; (3) `X-OpenRouter-Cache: true` enables caching when the preset does not configure it, but cannot override a preset that explicitly sets `cache_enabled: false`; (4) `X-OpenRouter-Cache-TTL` overrides the preset `cache_ttl_seconds`; (5) if neither header nor preset is set, caching is off. ^[raw/document/openrouter/openrouter-031-guides-features-response-caching-2026-04-29.md]

### Streaming and tool calls

Both streaming and non-streaming requests are eligible for caching, but they are cached separately — a `stream: true` request will not return a cached non-streaming response. For streaming hits, the cached response is replayed through the same streaming pipeline; the `id` field, `created` timestamp, and `X-Generation-Id` header in each chunk reflect the new cache-hit generation record, not the original. Responses containing tool calls are cached normally. ^[raw/document/openrouter/openrouter-031-guides-features-response-caching-2026-04-29.md]

### Cache clearing and non-determinism

The `X-OpenRouter-Cache-Clear: true` header forces a cache refresh for a specific request by deleting the existing entry, making a new provider request, and storing the new response. This only clears the entry matching the current cache key, not all entries. Cached responses are returned verbatim regardless of stochastic parameters like `temperature` — if fresh responses are needed, use `X-OpenRouter-Cache-Clear: true` or a short TTL. ^[raw/document/openrouter/openrouter-031-guides-features-response-caching-2026-04-29.md]

### Billing and rate limits

Cache hits are free: no tokens consumed, all usage counters zeroed. Cache hits also do not count toward provider rate limits since the request never reaches a provider. Only the original cache-miss request is billed. ^[raw/document/openrouter/openrouter-031-guides-features-response-caching-2026-04-29.md]

### Limitations

There is no request coalescing — two identical requests arriving simultaneously before the first response is cached both result in cache misses and are billed independently. Cached responses may be evicted before TTL expiry under memory pressure, so entries are not guaranteed to survive their full TTL. Response caching is disabled when account-level ZDR is enforced. ^[raw/document/openrouter/openrouter-031-guides-features-response-caching-2026-04-29.md]

### Data retention

Cached responses are stored in edge infrastructure, retained only for the TTL duration, and automatically evicted upon expiry. Cached data is accessible only via the API key that triggered the caching. Cached data is not used for training or shared with third parties. ^[raw/document/openrouter/openrouter-031-guides-features-response-caching-2026-04-29.md]

### Distinction from provider caching

OpenRouter response caching operates at the request level before the call reaches the provider. Provider-level caching mechanisms (e.g., Anthropic prompt caching, OpenAI cached context) operate within the provider's infrastructure. The two are independent and can be used together. ^[raw/document/openrouter/openrouter-031-guides-features-response-caching-2026-04-29.md]

## Related

- [[entities/openrouter]]
- [[concepts/prompt_caching]]
- [[concepts/presets]]
- [[concepts/zero_data_retention]]
- [[concepts/embedding_models]]
- [[concepts/rate_limiting]]
- [[concepts/streaming_output]]
- [[summaries/openrouter-guides-features-response-caching]]