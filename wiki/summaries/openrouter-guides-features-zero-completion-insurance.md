---
title: "Openrouter Guides Features Zero Completion Insurance"
summary: "OpenRouter's zero completion insurance automatically waives charges for requests that produce no output tokens, protecting users from paying for failed or empty responses"
type: summary
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

# Openrouter Guides Features Zero Completion Insurance

## Key Points

- Zero completion insurance protects users from being charged for failed or empty responses ^[raw/document/openrouter/openrouter-043-guides-features-zero-completion-insurance-2026-04-29.md]
- No credits are deducted when a response has zero completion tokens and a blank or null finish reason ^[raw/document/openrouter/openrouter-043-guides-features-zero-completion-insurance-2026-04-29.md]
- No credits are deducted when a response has an error finish reason ^[raw/document/openrouter/openrouter-043-guides-features-zero-completion-insurance-2026-04-29.md]
- The feature applies even if the underlying provider charged OpenRouter for prompt processing ^[raw/document/openrouter/openrouter-043-guides-features-zero-completion-insurance-2026-04-29.md]
- Zero completion insurance is automatically enabled for all accounts and requires no configuration ^[raw/document/openrouter/openrouter-043-guides-features-zero-completion-insurance-2026-04-29.md]
- It applies to all requests across all models and providers ^[raw/document/openrouter/openrouter-043-guides-features-zero-completion-insurance-2026-04-29.md]

## Notes

- Protected requests are visible on the activity page with zero credits deducted.

## Related

- [[entities/openrouter]]
- [[concepts/zero_completion_insurance]]
- [[concepts/credit_system]]
- [[concepts/model_fallback]]