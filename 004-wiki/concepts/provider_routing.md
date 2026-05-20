---
title: "Provider Routing"
summary: "The mechanism by which OpenRouter selects and orders backend providers for each request, using price-based load balancing by default and configurable via sorting, ordering, filtering, and performance thresholds"
type: concept
sources:
  - raw/document/openrouter/openrouter-018-guides-routing-provider-selection-2026-04-29.md
  - raw/document/openrouter/openrouter-019-guides-routing-auto-exacto-2026-04-29.md
  - raw/document/openrouter/openrouter-022-guides-routing-model-variants-exacto-2026-04-29.md
  - raw/document/openrouter/openrouter-025-guides-routing-model-variants-nitro-2026-04-29.md
  - raw/document/openrouter/openrouter-026-guides-routing-routers-auto-router-2026-04-29.md
  - raw/document/openrouter/openrouter-029-guides-features-workspaces-2026-04-29.md
  - raw/document/openrouter/openrouter-068-guides-privacy-provider-logging-2026-04-29.md
  - raw/document/openrouter/openrouter-069-guides-best-practices-latency-and-performance-2026-04-29.md
  - raw/document/openrouter/openrouter-070-guides-best-practices-prompt-caching-2026-04-29.md
tags:
  - openrouter
  - provider-routing
  - load-balancing
  - sorting
  - auto-exacto
  - api
  - data-policy-filtering
  - provider-logging
  - prompt-caching
  - latency
  - workspaces
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:02Z"
confidence: 0.9
provenance: merged
---

# Provider Routing

The mechanism by which OpenRouter selects and orders backend providers for each model request. By default, requests are load balanced across providers prioritizing price; this behavior is fully configurable via the `provider` object in the request body. ^[001a-raw/document/openrouter/openrouter-018-guides-routing-provider-selection-2026-04-29.md]

## Key Points

- Default strategy: price-based load balancing — providers without recent outages (30-second window) are selected weighted by inverse square of price; remaining providers serve as fallbacks ^[001a-raw/document/openrouter/openrouter-018-guides-routing-provider-selection-2026-04-29.md]
- Setting `sort` or `order` disables load balancing and switches to deterministic ordering ^[001a-raw/document/openrouter/openrouter-018-guides-routing-provider-selection-2026-04-29.md]
- `sort` supports `"price"`, `"throughput"`, or `"latency"`; model slug suffixes `:nitro` and `:floor` are shortcuts for throughput and price sorting respectively ^[001a-raw/document/openrouter/openrouter-018-guides-routing-provider-selection-2026-04-29.md]
- `order` accepts an array of provider slugs tried in sequence; providers not in the list are tried afterward unless `allow_fallbacks: false` is set ^[001a-raw/document/openrouter/openrouter-018-guides-routing-provider-selection-2026-04-29.md]
- `only` restricts routing to a whitelist of providers; `ignore` excludes specific providers — both support base slug matching (e.g., `"google-vertex"` matches all regions) ^[001a-raw/document/openrouter/openrouter-018-guides-routing-provider-selection-2026-04-29.md]
- `partition: "none"` in the `sort` object removes model-grouped ordering, allowing cross-model sorting for use with [[004-wiki/concepts/model_fallback]] ^[001a-raw/document/openrouter/openrouter-018-guides-routing-provider-selection-2026-04-29.md]
- For tool-calling requests, [[004-wiki/concepts/auto_exacto]] overrides price-weighted routing by reordering providers based on throughput, tool-calling success rate, and benchmark performance ^[001a-raw/document/openrouter/openrouter-019-guides-routing-auto-exacto-2026-04-29.md]
- The `:exacto` model slug suffix explicitly opts into the same quality-first sorting that Auto Exacto applies automatically, preferring providers with stronger tool-calling reliability signals ^[001a-raw/document/openrouter/openrouter-022-guides-routing-model-variants-exacto-2026-04-29.md]
- Individual requests can be restricted to providers complying with specific data policies via the `provider` object; this is also available as an account-wide privacy setting ^[001a-raw/document/openrouter/openrouter-068-guides-privacy-provider-logging-2026-04-29.md]
- OpenRouter does not route based on provider data retention policies; retention policies are surfaced per provider so users can manually exclude non-compliant providers ^[001a-raw/document/openrouter/openrouter-068-guides-privacy-provider-logging-2026-04-29.md]
- Provider preferences can be used to optimize for specific latency requirements, whether time to first token or time to last token, alongside cost considerations ^[001a-raw/document/openrouter/openrouter-069-guides-best-practices-latency-and-performance-2026-04-29.md]
- Provider sticky routing maximizes prompt cache hit rates by routing subsequent requests to the same provider endpoint after a cached request; it is not used when a manual `provider.order` is specified ^[001a-raw/document/openrouter/openrouter-070-guides-best-practices-prompt-caching-2026-04-29.md]

## Details

### Provider Object Fields

The `provider` object in the Chat Completions request body controls routing behavior. Key fields include:

| Field | Type | Default | Purpose |
|---|---|---|---|
| `order` | string[] | - | Provider slugs to try in order |
| `allow_fallbacks` | boolean | `true` | Whether to allow backup providers |
| `require_parameters` | boolean | `false` | Only use providers supporting all request parameters |
| `data_collection` | "allow" \| "deny" | "allow" | Filter by data policy compliance |
| `zdr` | boolean | - | Restrict to Zero Data Retention endpoints |
| `enforce_distillable_text` | boolean | - | Restrict to models allowing text distillation |
| `only` | string[] | - | Whitelist of allowed provider slugs |
| `ignore` | string[] | - | Blacklist of excluded provider slugs |
| `quantizations` | string[] | - | Filter by quantization level |
| `sort` | string \| object | - | Sort strategy (price/throughput/latency) |
| `preferred_min_throughput` | number \| object | - | Minimum throughput threshold |
| `preferred_max_latency` | number \| object | - | Maximum latency threshold |
| `max_price` | object | - | Maximum acceptable pricing |

^[001a-raw/document/openrouter/openrouter-018-guides-routing-provider-selection-2026-04-29.md]

### Provider Slug Matching

Provider slugs support base and specific variants. A base slug like `"google-vertex"` matches all endpoints for that provider (every region). A specific slug like `"google-vertex/us-east5"` or `"deepinfra/turbo"` matches only that variant. The copy button next to provider names on model detail pages provides the exact slug. ^[001a-raw/document/openrouter/openrouter-018-guides-routing-provider-selection-2026-04-29.md]

### Interaction with Request Parameters

When `tools` or `tool_choice` is sent, OpenRouter only routes to providers that support tool use. When `max_tokens` is set, only providers supporting a response of that length are considered. Setting `require_parameters: true` excludes providers that do not support all parameters in the request. ^[001a-raw/document/openrouter/openrouter-018-guides-routing-provider-selection-2026-04-29.md]

### Provider Routing in Workspaces

In OpenRouter [[004-wiki/concepts/workspaces|Workspaces]], provider routing is configured independently per workspace. Each workspace can optimize routing for different priorities (cost, latency, throughput, or tool-calling quality) without affecting other workspaces. ^[001a-raw/document/openrouter/openrouter-029-guides-features-workspaces-2026-04-29.md]

## Related

- [[004-wiki/entities/openrouter]]
- [[004-wiki/concepts/provider_fallback]]
- [[004-wiki/concepts/model_fallback]]
- [[004-wiki/concepts/performance_thresholds]]
- [[004-wiki/concepts/data_collection_policy]]
- [[004-wiki/concepts/quantization]]
- [[004-wiki/concepts/zero_data_retention]]
- [[004-wiki/concepts/byok]]
- [[004-wiki/concepts/model_variants]]
- [[004-wiki/summaries/openrouter-guides-routing-provider-selection]]
- [[004-wiki/concepts/auto_exacto]]
- [[004-wiki/concepts/exacto]]
- [[004-wiki/concepts/nitro_variant]]
- [[004-wiki/concepts/workspaces]]
- [[004-wiki/concepts/auto_router]]
- [[004-wiki/summaries/openrouter-guides-routing-routers-auto-router]]
- [[004-wiki/summaries/openrouter-guides-routing-auto-exacto]]
- [[004-wiki/summaries/openrouter-guides-routing-model-variants-exacto]]
- [[004-wiki/summaries/openrouter-guides-routing-model-variants-nitro]]
- [[004-wiki/concepts/provider_logging]]
- [[004-wiki/summaries/openrouter-guides-privacy-provider-logging]]
- [[004-wiki/summaries/openrouter-guides-best-practices-latency-and-performance]]
- [[004-wiki/concepts/provider_sticky_routing]]
- [[004-wiki/concepts/uptime_optimization]]
- [[004-wiki/summaries/openrouter-guides-best-practices-prompt-caching]]
- [[004-wiki/summaries/openrouter-guides-best-practices-uptime-optimization]]