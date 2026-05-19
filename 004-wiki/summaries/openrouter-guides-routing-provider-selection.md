---
title: "Openrouter Guides Routing Provider Selection"
summary: "Comprehensive guide to OpenRouter's provider routing system, covering load balancing, sorting, performance thresholds, provider ordering, quantization filtering, data policies, ZDR enforcement, and Anthropic beta header passthrough"
type: summary
sources:
  - raw/document/openrouter/openrouter-018-guides-routing-provider-selection-2026-04-29.md
tags:
  - openrouter
  - provider-routing
  - load-balancing
  - performance
  - quantization
  - data-privacy
  - zdr
  - byok
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Openrouter Guides Routing Provider Selection

## Key Points

- OpenRouter defaults to price-based load balancing: providers without recent outages are selected weighted by inverse square of price, with remaining providers as fallbacks ^[raw/document/openrouter/openrouter-018-guides-routing-provider-selection-2026-04-29.md]
- The `provider` object in request bodies controls routing via fields: `order`, `allow_fallbacks`, `require_parameters`, `data_collection`, `zdr`, `enforce_distillable_text`, `only`, `ignore`, `quantizations`, `sort`, `preferred_min_throughput`, `preferred_max_latency`, and `max_price` ^[raw/document/openrouter/openrouter-018-guides-routing-provider-selection-2026-04-29.md]
- `sort` supports `"price"`, `"throughput"`, or `"latency"` and can be combined with `partition: "none"` for cross-model sorting; model slug suffixes `:nitro` (throughput) and `:floor` (price) are shortcuts ^[raw/document/openrouter/openrouter-018-guides-routing-provider-selection-2026-04-29.md]
- Performance thresholds (`preferred_min_throughput`, `preferred_max_latency`) deprioritize non-compliant providers rather than excluding them, and support percentile cutoffs (p50, p75, p90, p99) calculated over a 5-minute rolling window ^[raw/document/openrouter/openrouter-018-guides-routing-provider-selection-2026-04-29.md]
- Provider slugs support base matching (e.g., `"google-vertex"` matches all regions) and specific variant targeting (e.g., `"deepinfra/turbo"`, `"google-vertex/us-east5"`) ^[raw/document/openrouter/openrouter-018-guides-routing-provider-selection-2026-04-29.md]
- Data policy controls include `data_collection: "deny"` (exclude providers that store data), `zdr: true` (restrict to Zero Data Retention endpoints), and `enforce_distillable_text: true` (restrict to models allowing text distillation) ^[raw/document/openrouter/openrouter-018-guides-routing-provider-selection-2026-04-29.md]
- Anthropic beta features (fine-grained tool streaming, interleaved thinking, structured outputs) are passed through via the `x-anthropic-beta` header; prompt caching and JSON schema response format are applied automatically ^[raw/document/openrouter/openrouter-018-guides-routing-provider-selection-2026-04-29.md]

## Quotes

- "OpenRouter routes requests to the best available providers for your model. By default, requests are load balanced across the top providers to maximize uptime." ^[raw/document/openrouter/openrouter-018-guides-routing-provider-selection-2026-04-29.md]

- "If Provider A costs $1 per million tokens, Provider B costs $2, and Provider C costs $3, and Provider B recently saw a few outages... Your request is routed to Provider A. Provider A is 9x more likely to be first routed to Provider A than Provider C because (1 / 3^2 = 1/9)." ^[raw/document/openrouter/openrouter-018-guides-routing-provider-selection-2026-04-29.md]

- "preferred_max_latency and preferred_min_throughput do not guarantee you will get a provider or model with this performance level. However, providers and models that hit your thresholds will be preferred." ^[raw/document/openrouter/openrouter-018-guides-routing-provider-selection-2026-04-29.md]

## Notes

- The source document focuses exclusively on OpenRouter's provider selection and routing API. It does not cover model-level routing or fallbacks (covered in the model fallbacks guide).
- EU data residency for enterprise customers is mentioned but details are deferred to OpenRouter's privacy documentation.
- BYOK endpoints are automatically prioritized when API keys are configured; `partition: "none"` extends this prioritization across model boundaries.

## Related

- [[entities/openrouter]]
- [[concepts/provider_routing]]
- [[concepts/performance_thresholds]]
- [[concepts/data_collection_policy]]
- [[concepts/provider_fallback]]
- [[concepts/model_fallback]]
- [[concepts/quantization]]
- [[concepts/zero_data_retention]]
- [[concepts/distillation]]
- [[concepts/byok]]
- [[concepts/model_variants]]