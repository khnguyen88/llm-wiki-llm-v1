---
title: "Zero Completion Insurance"
summary: "An OpenRouter feature that automatically waives charges for requests producing no output tokens or returning errors, even when providers charge for prompt processing"
type: concept
sources:
  - raw/document/openrouter/openrouter-043-guides-features-zero-completion-insurance-2026-04-29.md
tags:
  - openrouter
  - billing
  - credits
  - error-handling
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Zero Completion Insurance

An OpenRouter feature that automatically protects users from being charged for requests that produce failed or empty responses.

## Key Points

- Zero completion insurance waives charges when a response has zero completion tokens and a blank or null finish reason ^[raw/document/openrouter/openrouter-043-guides-features-zero-completion-insurance-2026-04-29.md]
- It also waives charges when a response has an error finish reason ^[raw/document/openrouter/openrouter-043-guides-features-zero-completion-insurance-2026-04-29.md]
- The protection applies even if the underlying provider charged OpenRouter for prompt processing ^[raw/document/openrouter/openrouter-043-guides-features-zero-completion-insurance-2026-04-29.md]
- Automatically enabled for all accounts with no configuration required ^[raw/document/openrouter/openrouter-043-guides-features-zero-completion-insurance-2026-04-29.md]
- Applies to all requests across all models and providers ^[raw/document/openrouter/openrouter-043-guides-features-zero-completion-insurance-2026-04-29.md]

## Details

Zero completion insurance is a cost-protection mechanism built into OpenRouter's billing system. When an API request results in a response that contains no useful output — either because the model produced zero completion tokens with a blank finish reason, or because the response terminated with an error — OpenRouter absorbs the cost rather than passing it to the user. This includes cases where the upstream provider still charges for prompt processing tokens.

Protected requests are identifiable on the OpenRouter activity page, where zero credits are shown as deducted.

## Related

- [[entities/openrouter]]
- [[concepts/credit_system]]
- [[concepts/model_fallback]]