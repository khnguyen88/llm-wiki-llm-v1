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

- OpenRouter provides a unified API to all major LLM models with provider pass-through pricing (no markup on inference) and aggregated uptime via automatic fallback ^[raw/document/openrouter/openrouter-015-faq-2026-04-29.md]
- Model variants modify behavior via slug suffixes: static variants (`:free`, `:extended`, `:thinking`) apply to specific models; dynamic variants (`:nitro`, `:floor`, `:exacto`) apply to all models ^[raw/document/openrouter/openrouter-015-faq-2026-04-29.md]
- Credits are purchased in USD; a fee is charged on credit purchases (Stripe and Coinbase/crypto have different fee rates); unused credits may expire after one year ^[raw/document/openrouter/openrouter-015-faq-2026-04-29.md]
- Prompt and completion data are not logged by default; an opt-in setting provides a 1% usage discount in exchange for logging ^[raw/document/openrouter/openrouter-015-faq-2026-04-29.md]
- BYOK (Bring Your Own Key) has a free monthly request threshold, after which a percentage fee of equivalent OpenRouter pricing applies ^[raw/document/openrouter/openrouter-015-faq-2026-04-29.md]
- Refunds for unused credits are available within 24 hours of purchase; cryptocurrency payments are never refundable ^[raw/document/openrouter/openrouter-015-faq-2026-04-29.md]
- Three authentication methods: cookie-based (web/chatroom), API keys as Bearer tokens, and Management API keys for programmatic key management ^[raw/document/openrouter/openrouter-015-faq-2026-04-29.md]

## Quotes

- "We pass through the pricing of the underlying providers; there is no markup on inference pricing" ^[raw/document/openrouter/openrouter-015-faq-2026-04-29.md]
- "We do zero logging of your prompts/completions, even if an error occurs, unless you opt-in to logging them" ^[raw/document/openrouter/openrouter-015-faq-2026-04-29.md]

## Notes

- Some numeric values in the source (credit fees, BYOK thresholds, free model rate limits) are dynamically rendered and not available in the static document. These are flagged in related concept pages where applicable.
- The `:online` variant is deprecated in favor of the `openrouter:web_search` server tool.

## Related

- [[entities/openrouter]]
- [[concepts/model_variants]]
- [[concepts/credit_system]]
- [[concepts/data_privacy]]
- [[concepts/byok]]
- [[concepts/rate_limiting]]
- [[concepts/provider_fallback]]
- [[concepts/authentication]]
- [[concepts/models_api]]
- [[concepts/streaming_output]]