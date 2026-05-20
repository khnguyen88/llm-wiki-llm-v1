---
title: "Auto Exacto"
summary: "An OpenRouter routing step that automatically reorders providers for tool-calling requests based on throughput, tool-calling success rate, and benchmark performance signals"
type: concept
sources:
  - raw/document/openrouter/openrouter-019-guides-routing-auto-exacto-2026-04-29.md
  - raw/document/openrouter/openrouter-022-guides-routing-model-variants-exacto-2026-04-29.md
tags:
  - openrouter
  - auto-exacto
  - provider-routing
  - tool-calling
  - routing
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:01Z"
confidence: 0.9
provenance: extracted
---

# Auto Exacto

A routing step in OpenRouter that automatically optimizes provider ordering for all requests that include tools. It runs by default on every tool-calling request without requiring configuration. ^[001a-raw/document/openrouter/openrouter-019-guides-routing-auto-exacto-2026-04-29.md]

## Key Points

- Activates automatically on any request that includes tools — no configuration needed ^[001a-raw/document/openrouter/openrouter-019-guides-routing-auto-exacto-2026-04-29.md]
- Reorders providers using three signals: real-time throughput (tokens-per-second), tool-calling success rate, and internal benchmark data ^[001a-raw/document/openrouter/openrouter-019-guides-routing-auto-exacto-2026-04-29.md]
- Overrides the default price-weighted routing for tool-calling requests, prioritizing quality over cost ^[001a-raw/document/openrouter/openrouter-019-guides-routing-auto-exacto-2026-04-29.md]
- Providers that underperform on throughput, success rate, or benchmarks are deprioritized; strong performers are moved to the front ^[001a-raw/document/openrouter/openrouter-019-guides-routing-auto-exacto-2026-04-29.md]
- Can be opted out of by explicitly sorting by price via `provider.sort: "price"`, the `:floor` model slug suffix, or the default sort setting in account preferences ^[001a-raw/document/openrouter/openrouter-019-guides-routing-auto-exacto-2026-04-29.md]

## Details

### Performance Signals

Auto Exacto uses three categories of real-world performance signals to reorder providers:

- **Throughput**: real-time tokens-per-second metrics, visible on the Performance tab of model pages ^[001a-raw/document/openrouter/openrouter-019-guides-routing-auto-exacto-2026-04-29.md]
- **Tool-calling success rate**: how reliably each provider completes tool calls, also visible on the Performance tab ^[001a-raw/document/openrouter/openrouter-019-guides-routing-auto-exacto-2026-04-29.md]
- **Benchmark data**: internal evaluation results that are not yet publicly available on the site ^[001a-raw/document/openrouter/openrouter-019-guides-routing-auto-exacto-2026-04-29.md]

### Opting Out

Without Auto Exacto, OpenRouter defaults to price-weighted load balancing. Since Auto Exacto changes routing for tool-calling requests to quality-based ordering, users who prefer price-weighted behavior can opt out by setting `sort` to `"price"` in the `provider` object, appending `:floor` to the model slug, or setting the default provider sort to price in account settings. Any of these methods bypasses Auto Exacto entirely. ^[001a-raw/document/openrouter/openrouter-019-guides-routing-auto-exacto-2026-04-29.md]

### Observed Results

OpenRouter reports notable improvements in tau-bench scores and tool-calling success rates when Auto Exacto is active, with more detailed benchmark results to be published as evaluation data becomes publicly available. ^[001a-raw/document/openrouter/openrouter-019-guides-routing-auto-exacto-2026-04-29.md]

## Related

- [[004-wiki/entities/openrouter]]
- [[004-wiki/concepts/provider_routing]]
- [[004-wiki/concepts/model_variants]]
- [[004-wiki/concepts/exacto]]
- [[004-wiki/concepts/performance_thresholds]]
- [[004-wiki/summaries/openrouter-guides-routing-auto-exacto]]
- [[004-wiki/summaries/openrouter-guides-routing-model-variants-exacto]]