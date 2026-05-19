---
title: "Openrouter Guides Routing Auto Exacto"
summary: "Auto Exacto is an OpenRouter routing step that automatically reorders providers for tool-calling requests based on throughput, tool-calling success rate, and benchmark data, overriding the default price-weighted routing"
type: summary
sources:
  - raw/document/openrouter/openrouter-019-guides-routing-auto-exacto-2026-04-29.md
tags:
  - openrouter
  - auto-exacto
  - provider-routing
  - tool-calling
  - routing
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Openrouter Guides Routing Auto Exacto

## Key Points

- Auto Exacto runs by default on every tool-calling request, requiring no configuration ^[raw/document/openrouter/openrouter-019-guides-routing-auto-exacto-2026-04-29.md]
- It reorders available providers for the chosen model using throughput (tokens-per-second), tool-calling success rate, and internal benchmark data ^[raw/document/openrouter/openrouter-019-guides-routing-auto-exacto-2026-04-29.md]
- Providers that underperform on these signals are deprioritized; providers with strong track records are moved to the front ^[raw/document/openrouter/openrouter-019-guides-routing-auto-exacto-2026-04-29.md]
- Observed improvements in tau-bench scores and tool-calling success rates when Auto Exacto is active ^[raw/document/openrouter/openrouter-019-guides-routing-auto-exacto-2026-04-29.md]
- Without Auto Exacto, the default routing is price-weighted — requests are load balanced with a strong preference for lower cost ^[raw/document/openrouter/openrouter-019-guides-routing-auto-exacto-2026-04-29.md]
- Three ways to opt out and restore price-weighted behavior: `provider.sort` parameter set to `"price"`, `:floor` virtual variant suffix on the model slug, or default sort set to price in account settings ^[raw/document/openrouter/openrouter-019-guides-routing-auto-exacto-2026-04-29.md]

## Quotes

- "Auto Exacto is a routing step that automatically optimizes provider ordering for all requests that include tools." ^[raw/document/openrouter/openrouter-019-guides-routing-auto-exacto-2026-04-29.md:5]
- "Auto Exacto changes this for tool-calling requests by reordering providers based on quality signals instead of price." ^[raw/document/openrouter/openrouter-019-guides-routing-auto-exacto-2026-04-29.md:22]

## Notes

- Throughput and tool-calling success rate metrics are visible on the Performance tab of model pages at openrouter.ai/models ^[raw/document/openrouter/openrouter-019-guides-routing-auto-exacto-2026-04-29.md]
- Internal benchmark data used by Auto Exacto is not yet publicly available on the site ^[raw/document/openrouter/openrouter-019-guides-routing-auto-exacto-2026-04-29.md]
- More detailed benchmark results will be published as evaluation data becomes publicly available ^[raw/document/openrouter/openrouter-019-guides-routing-auto-exacto-2026-04-29.md]

## Related

- [[concepts/auto_exacto]]
- [[concepts/provider_routing]]
- [[entities/openrouter]]
- [[concepts/model_variants]]
- [[concepts/performance_thresholds]]