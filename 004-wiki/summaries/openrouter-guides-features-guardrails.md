---
title: "OpenRouter Guardrails"
summary: "OpenRouter guardrails let organizations control spending, restrict models and providers, and enforce data privacy policies for members and API keys"
type: summary
sources:
  - raw/document/openrouter/openrouter-046-guides-features-guardrails-2026-04-29.md
tags:
  - openrouter
  - guardrails
  - budget
  - data-privacy
  - organization
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# OpenRouter Guardrails

## Key Points

- Guardrails let organizations control spending, model/provider access, and data privacy for members and API keys ^[raw/document/openrouter/openrouter-046-guides-features-guardrails-2026-04-29.md]
- Each guardrail can combine a budget limit (daily/weekly/monthly), model allowlist, provider allowlist, and Zero Data Retention enforcement ^[raw/document/openrouter/openrouter-046-guides-features-guardrails-2026-04-29.md]
- Guardrails are assigned to organization members or API keys; member guardrails set a baseline for all of that member's keys, and API key guardrails layer on top ^[raw/document/openrouter/openrouter-046-guides-features-guardrails-2026-04-29.md]
- When multiple guardrails apply, allowlists are intersected (stricter wins), ZDR uses OR logic (any enforcement triggers it), and budgets are checked independently per guardrail ^[raw/document/openrouter/openrouter-046-guides-features-guardrails-2026-04-29.md]
- Guardrail budgets are per-user and per-key, not shared across assignees; a key's usage counts toward both its own budget and the owning member's budget ^[raw/document/openrouter/openrouter-046-guides-features-guardrails-2026-04-29.md]
- Organization admins manage guardrails at Settings > Privacy; only one guardrail can be directly assigned per user or key ^[raw/document/openrouter/openrouter-046-guides-features-guardrails-2026-04-29.md]
- Guardrails can be managed programmatically via the OpenRouter API ^[raw/document/openrouter/openrouter-046-guides-features-guardrails-2026-04-29.md]

## Notes

- Individual API key budgets still apply alongside guardrail budgets; the lower limit wins ^[raw/document/openrouter/openrouter-046-guides-features-guardrails-2026-04-29.md]

## Related

- [[entities/openrouter]]
- [[concepts/guardrails]]
- [[concepts/zero_data_retention]]
- [[concepts/workspaces]]