---
title: "Credit System"
summary: "OpenRouter's prepaid credit-based billing model where users deposit USD to fund inference costs across all providers, with no markup on provider pricing"
type: concept
sources:
  - raw/document/openrouter/openrouter-015-faq-2026-04-29.md
  - raw/document/openrouter/openrouter-069-guides-best-practices-latency-and-performance-2026-04-29.md
tags:
  - openrouter
  - billing
  - credits
  - pricing
  - refund
  - latency
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:03Z"
confidence: 0.9
provenance: merged
---

# Credit System

OpenRouter uses a prepaid credit system where the base currency is US dollars. Users deposit credits to fund LLM inference costs, and OpenRouter deducts costs per request based on token usage and per-model pricing. Provider pricing is passed through without markup. ^[raw/document/openrouter/openrouter-015-faq-2026-04-29.md]

## Key Points

- Credits are purchased in USD; a fee is charged at purchase time (separate rates for Stripe and cryptocurrency/Coinbase) ^[raw/document/openrouter/openrouter-015-faq-2026-04-29.md]
- No markup on inference pricing — users pay the same rate as the underlying provider's listed price ^[raw/document/openrouter/openrouter-015-faq-2026-04-29.md]
- Each model has per-million-token pricing for prompt and completion tokens; some models also charge per request, per image, or per reasoning token ^[raw/document/openrouter/openrouter-015-faq-2026-04-29.md]
- Unused credits may expire after one year of purchase per OpenRouter's terms ^[raw/document/openrouter/openrouter-015-faq-2026-04-29.md]
- Refunds for unused credits are available within 24 hours of purchase via the Credits page; platform fees are non-refundable; cryptocurrency payments are never refundable ^[raw/document/openrouter/openrouter-015-faq-2026-04-29.md]
- Users can set up auto top-up to replenish their balance when it drops below a configured threshold ^[raw/document/openrouter/openrouter-015-faq-2026-04-29.md]
- All new users receive a small free allowance; free models have low rate limits and are not recommended for production use ^[raw/document/openrouter/openrouter-015-faq-2026-04-29.md]
- Low credit balances (single-digit dollars) or API keys approaching configured credit limits trigger additional database checks and more aggressive cache expiration, increasing request latency; maintaining a balance of at least $10-20 is recommended ^[raw/document/openrouter/openrouter-069-guides-best-practices-latency-and-performance-2026-04-29.md]

## Details

Pricing is displayed per million tokens on each model's page, with separate rates for prompt tokens and completion tokens. Additional cost dimensions include per-request pricing, per-image pricing, and per-reasoning-token pricing for certain models. When a request is made, OpenRouter receives the total token count from the provider, calculates the cost, and deducts it from the user's credit balance. ^[raw/document/openrouter/openrouter-015-faq-2026-04-29.md]

Payment methods include major credit cards, AliPay, and USDC cryptocurrency. PayPal integration is planned. Stripe payments may experience delays of up to one hour before credits appear; if credits do not appear and no Stripe receipt email was received, the card may have been declined. ^[raw/document/openrouter/openrouter-015-faq-2026-04-29.md]

The Activity page provides historical usage data filterable by model, provider, and API key. A credits API endpoint provides live balance and remaining credit information. OpenRouter does not currently offer volume discounts. ^[raw/document/openrouter/openrouter-015-faq-2026-04-29.md]

## Related

- [[entities/openrouter]]
- [[concepts/byok]]
- [[concepts/rate_limiting]]
- [[concepts/data_privacy]]
- [[concepts/cost_tracking]]
- [[summaries/openrouter-faq]]
- [[summaries/openrouter-guides-best-practices-latency-and-performance]]