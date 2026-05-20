---
title: "OpenRouter FAQ"
summary: "Covers getting started, pricing, model variants, API specs, privacy, credit system, and account management for OpenRouter"
type: summary
sources:
  - raw/document/openrouter/openrouter-015-faq-2026-04-29.md
tags:
  - openrouter
  - faq
  - pricing
  - credits
  - privacy
  - model-variants
  - rate-limiting
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# OpenRouter FAQ

## Key Points

- OpenRouter provides a unified API to all major LLM models with provider pass-through pricing (no markup on inference) and aggregated uptime via automatic fallback ^[001a-raw/document/openrouter/openrouter-015-faq-2026-04-29.md]
- Model variants modify behavior via slug suffixes: static variants (`:free`, `:extended`, `:thinking`) apply to specific models; dynamic variants (`:nitro`, `:floor`, `:exacto`) apply to all models ^[001a-raw/document/openrouter/openrouter-015-faq-2026-04-29.md]
- Credits are purchased in USD; a fee is charged on credit purchases (Stripe and Coinbase/crypto have different fee rates); unused credits may expire after one year ^[001a-raw/document/openrouter/openrouter-015-faq-2026-04-29.md]
- Prompt and completion data are not logged by default; an opt-in setting provides a 1% usage discount in exchange for logging ^[001a-raw/document/openrouter/openrouter-015-faq-2026-04-29.md]
- BYOK (Bring Your Own Key) has a free monthly request threshold, after which a percentage fee of equivalent OpenRouter pricing applies ^[001a-raw/document/openrouter/openrouter-015-faq-2026-04-29.md]
- Refunds for unused credits are available within 24 hours of purchase; cryptocurrency payments are never refundable ^[001a-raw/document/openrouter/openrouter-015-faq-2026-04-29.md]
- Three authentication methods: cookie-based (web/chatroom), API keys as Bearer tokens, and Management API keys for programmatic key management ^[001a-raw/document/openrouter/openrouter-015-faq-2026-04-29.md]

## Quotes

- "We pass through the pricing of the underlying providers; there is no markup on inference pricing" ^[001a-raw/document/openrouter/openrouter-015-faq-2026-04-29.md]
- "We do zero logging of your prompts/completions, even if an error occurs, unless you opt-in to logging them" ^[001a-raw/document/openrouter/openrouter-015-faq-2026-04-29.md]

## Notes

- Some numeric values in the source (credit fees, BYOK thresholds, free model rate limits) are dynamically rendered and not available in the static document. These are flagged in related concept pages where applicable.
- The `:online` variant is deprecated in favor of the `openrouter:web_search` server tool.

## Related

- [[004-wiki/entities/openrouter]]
- [[004-wiki/concepts/model_variants]]
- [[004-wiki/concepts/credit_system]]
- [[004-wiki/concepts/data_privacy]]
- [[004-wiki/concepts/byok]]
- [[004-wiki/concepts/rate_limiting]]
- [[004-wiki/concepts/provider_fallback]]
- [[004-wiki/concepts/authentication]]
- [[004-wiki/concepts/models_api]]
- [[004-wiki/concepts/streaming_output]]