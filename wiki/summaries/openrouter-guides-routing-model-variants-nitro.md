---
title: "OpenRouter Guides: Routing — Model Variants — Nitro"
summary: "The :nitro model variant suffix sorts OpenRouter providers by throughput, prioritizing the fastest response times"
type: summary
sources:
  - raw/document/openrouter/openrouter-025-guides-routing-model-variants-nitro-2026-04-29.md
tags:
  - openrouter
  - nitro
  - model-variants
  - provider-routing
  - throughput
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 1.0
provenance: extracted
---

# OpenRouter Guides: Routing — Model Variants — Nitro

## Key Points

- The `:nitro` variant is an alias for sorting providers by throughput, prioritizing providers with the highest tokens-per-second rate ^[raw/document/openrouter/openrouter-025-guides-routing-model-variants-nitro-2026-04-29.md]
- Activated by appending `:nitro` to any model ID (e.g., `"openai/gpt-5.2:nitro"`) ^[raw/document/openrouter/openrouter-025-guides-routing-model-variants-nitro-2026-04-29.md]
- Exactly equivalent to setting `provider.sort` to `"throughput"` in the request body ^[raw/document/openrouter/openrouter-025-guides-routing-model-variants-nitro-2026-04-29.md]

## Quotes

> The `:nitro` variant is an alias for sorting providers by throughput. When you use `:nitro`, OpenRouter will prioritize providers with the highest throughput (tokens per second). ^[raw/document/openrouter/openrouter-025-guides-routing-model-variants-nitro-2026-04-29.md]

## Notes

- This is one of three dynamic variant suffixes on OpenRouter (`:nitro`, `:floor`, `:exacto`), each mapping to a `provider.sort` value
- The source document is brief (~96 words), covering only the definition and usage syntax

## Related

- [[entities/openrouter]]
- [[concepts/nitro_variant]]
- [[concepts/model_variants]]
- [[concepts/provider_routing]]
- [[concepts/performance_thresholds]]