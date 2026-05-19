---
title: "Openrouter Guides Routing Model Variants Exacto"
summary: "The Exacto variant is an explicit quality-first provider sorting mode on OpenRouter, activated by appending :exacto to a model slug to prioritize tool-calling reliability over price"
type: summary
sources:
  - raw/document/openrouter/openrouter-022-guides-routing-model-variants-exacto-2026-04-29.md
tags:
  - openrouter
  - exacto
  - model-variants
  - provider-routing
  - tool-calling
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Openrouter Guides Routing Model Variants Exacto

## Key Points

- The `:exacto` suffix on a model slug explicitly activates quality-first provider sorting, overriding the default price-weighted routing ^[raw/document/openrouter/openrouter-022-guides-routing-model-variants-exacto-2026-04-29.md]
- Exacto uses three signal classes: tool-calling success/reliability from real traffic, provider performance metrics (throughput, latency), and benchmark/evaluation data ^[raw/document/openrouter/openrouter-022-guides-routing-model-variants-exacto-2026-04-29.md]
- Providers with strong track records are moved to the front; limited-data providers are kept behind established performers; poor-quality providers are deprioritized further ^[raw/document/openrouter/openrouter-022-guides-routing-model-variants-exacto-2026-04-29.md]
- Explicit sort preferences (price, throughput, latency) take precedence over Exacto sorting ^[raw/document/openrouter/openrouter-022-guides-routing-model-variants-exacto-2026-04-29.md]
- Exacto differs from [[concepts/auto_exacto]] in that it is opt-in via the `:exacto` suffix, whereas Auto Exacto runs automatically on tool-calling requests ^[raw/document/openrouter/openrouter-022-guides-routing-model-variants-exacto-2026-04-29.md]
- Can be used alongside the `models` fallback array — any model with `:exacto` will request Exacto sorting when selected ^[raw/document/openrouter/openrouter-022-guides-routing-model-variants-exacto-2026-04-29.md]
- Most useful on models that support tool calling, have multiple providers, and show meaningful variance in tool-use reliability ^[raw/document/openrouter/openrouter-022-guides-routing-model-variants-exacto-2026-04-29.md]

## Quotes

> "Exacto is a routing shortcut for quality-first provider ordering. Unlike standard routing, which primarily favors lower-cost providers, Exacto prefers providers with stronger signals for tool-calling reliability and deprioritizes weaker performers." ^[raw/document/openrouter/openrouter-022-guides-routing-model-variants-exacto-2026-04-29.md]

> "Providers serving the same model can vary meaningfully in tool-use behavior. Exacto gives you an explicit, request-level way to prefer higher-quality providers when you care more about tool-calling reliability than the default price-weighted route." ^[raw/document/openrouter/openrouter-022-guides-routing-model-variants-exacto-2026-04-29.md]

## Notes

- The `:exacto` suffix works with the OpenRouter TypeScript SDK (`@openrouter/sdk`), the OpenAI-compatible SDK, and direct cURL requests ^[raw/document/openrouter/openrouter-022-guides-routing-model-variants-exacto-2026-04-29.md]
- Exacto is a virtual variant with no separate endpoint pool — it modifies routing behavior only ^[raw/document/openrouter/openrouter-022-guides-routing-model-variants-exacto-2026-04-29.md]
- Feedback on Exacto is collected via a Notion form linked in the documentation ^[raw/document/openrouter/openrouter-022-guides-routing-model-variants-exacto-2026-04-29.md]

## Related

- [[entities/openrouter]]
- [[concepts/exacto]]
- [[concepts/auto_exacto]]
- [[concepts/model_variants]]
- [[concepts/provider_routing]]
- [[concepts/performance_thresholds]]