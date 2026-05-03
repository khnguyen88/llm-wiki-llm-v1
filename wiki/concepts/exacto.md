---
title: "Exacto Variant"
summary: "An explicit OpenRouter model variant that applies quality-first provider sorting via the :exacto suffix, prioritizing tool-calling reliability over price"
type: concept
sources:
  - raw/document/openrouter/openrouter-022-guides-routing-model-variants-exacto-2026-04-29.md
tags:
  - openrouter
  - exacto
  - provider-routing
  - model-variants
  - tool-calling
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Exacto Variant

A virtual model variant on OpenRouter that explicitly applies quality-first provider sorting. Appending `:exacto` to a model slug causes OpenRouter to prefer providers with stronger tool-calling quality signals instead of using the default price-weighted ordering. ^[raw/document/openrouter/openrouter-022-guides-routing-model-variants-exacto-2026-04-29.md]

## Key Points

- Activated by appending `:exacto` to any supported model slug (e.g., `moonshotai/kimi-k2-0905:exacto`), which is a shortcut for setting the provider sort to Exacto on that model ^[raw/document/openrouter/openrouter-022-guides-routing-model-variants-exacto-2026-04-29.md]
- Uses the same three signal classes as [[concepts/auto_exacto]]: tool-calling success and reliability from real traffic, provider performance metrics (throughput, latency), and benchmark/evaluation data ^[raw/document/openrouter/openrouter-022-guides-routing-model-variants-exacto-2026-04-29.md]
- Providers with strong track records are prioritized; providers with limited data are placed behind established performers; providers with poor quality signals are deprioritized further ^[raw/document/openrouter/openrouter-022-guides-routing-model-variants-exacto-2026-04-29.md]
- Explicit sort preferences (price, throughput, latency) take precedence over Exacto sorting ^[raw/document/openrouter/openrouter-022-guides-routing-model-variants-exacto-2026-04-29.md]
- Can be combined with fallback models via the `models` array; any model carrying the `:exacto` suffix will request Exacto sorting when selected ^[raw/document/openrouter/openrouter-022-guides-routing-model-variants-exacto-2026-04-29.md]
- Not backed by a separate endpoint pool — it is a routing modifier that changes provider selection order ^[raw/document/openrouter/openrouter-022-guides-routing-model-variants-exacto-2026-04-29.md]

## Details

Unlike [[concepts/auto_exacto]], which runs automatically on every tool-calling request without configuration, the `:exacto` suffix is an explicit opt-in. It is most useful on models that support tool calling, have multiple providers available on OpenRouter, and exhibit meaningful provider variance in tool-use reliability. ^[raw/document/openrouter/openrouter-022-guides-routing-model-variants-exacto-2026-04-29.md]

Exacto was built because providers serving the same model can vary meaningfully in tool-use behavior. It gives request-level control to prefer higher-quality providers when tool-calling accuracy matters more than cost efficiency. ^[raw/document/openrouter/openrouter-022-guides-routing-model-variants-exacto-2026-04-29.md]

## Related

- [[entities/openrouter]]
- [[concepts/auto_exacto]]
- [[concepts/model_variants]]
- [[concepts/provider_routing]]
- [[concepts/performance_thresholds]]
- [[summaries/openrouter-guides-routing-model-variants-exacto]]