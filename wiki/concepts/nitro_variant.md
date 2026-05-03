---
title: "Nitro Variant"
summary: "An OpenRouter model variant suffix that sorts providers by throughput, prioritizing the fastest response times"
type: concept
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

# Nitro Variant

A dynamic model variant on OpenRouter that sorts providers by throughput (tokens per second). Appending `:nitro` to a model slug causes OpenRouter to prioritize providers delivering the fastest response times. ^[raw/document/openrouter/openrouter-025-guides-routing-model-variants-nitro-2026-04-29.md]

## Key Points

- Activated by appending `:nitro` to any model ID (e.g., `"openai/gpt-5.2:nitro"`) ^[raw/document/openrouter/openrouter-025-guides-routing-model-variants-nitro-2026-04-29.md]
- Functionally equivalent to setting `provider.sort` to `"throughput"` in the request body ^[raw/document/openrouter/openrouter-025-guides-routing-model-variants-nitro-2026-04-29.md]
- Prioritizes providers with the highest throughput (tokens per second) over cost or latency ^[raw/document/openrouter/openrouter-025-guides-routing-model-variants-nitro-2026-04-29.md]
- As a dynamic variant, `:nitro` can be applied to any model on OpenRouter, not just specific ones ^[raw/document/openrouter/openrouter-025-guides-routing-model-variants-nitro-2026-04-29.md]

## Details

The `:nitro` suffix is one of three dynamic variant shortcuts on OpenRouter, alongside `:floor` (price sorting) and `:exacto` (quality-first sorting). Unlike static variants (such as `:free`, `:extended`, `:thinking`) which modify model capabilities and are limited to specific models, dynamic variants change provider selection behavior and work universally.

The `:nitro` variant is not backed by a separate endpoint pool — it is purely a routing modifier that changes which provider handles the request. When throughput sorting is active, providers are ranked by their measured tokens-per-second performance rather than by price.

## Related

- [[entities/openrouter]]
- [[concepts/model_variants]]
- [[concepts/provider_routing]]
- [[concepts/performance_thresholds]]
- [[concepts/exacto]]
- [[summaries/openrouter-guides-routing-model-variants-nitro]]