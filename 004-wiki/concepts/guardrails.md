---
title: "Guardrails"
summary: "OpenRouter feature that enforces spending limits, model and provider restrictions, and data privacy policies at the organization member and API key level"
type: concept
sources:
  - raw/document/openrouter/openrouter-046-guides-features-guardrails-2026-04-29.md
tags:
  - openrouter
  - guardrails
  - budget
  - access-control
  - data-privacy
  - organization
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Guardrails

Guardrails are an OpenRouter feature that lets organizations control how their members and API keys use the platform — setting spending limits, restricting which models and providers are available, and enforcing data privacy policies. ^[raw/document/openrouter/openrouter-046-guides-features-guardrails-2026-04-29.md]

## Key Points

- Each guardrail can include any combination of: budget limit (USD, reset daily/weekly/monthly), model allowlist, provider allowlist, and Zero Data Retention enforcement ^[raw/document/openrouter/openrouter-046-guides-features-guardrails-2026-04-29.md]
- Guardrails are assigned at two levels: organization members (baseline for all their keys and chatroom usage) and individual API keys (granular control layered on top of member guardrails) ^[raw/document/openrouter/openrouter-046-guides-features-guardrails-2026-04-29.md]
- Only one guardrail can be directly assigned to a user or key; a member's guardrail implicitly applies to all keys they create ^[raw/document/openrouter/openrouter-046-guides-features-guardrails-2026-04-29.md]
- When multiple guardrails apply, provider and model allowlists are intersected (only providers/models allowed by all guardrails remain available), while ZDR enforcement uses OR logic (any guardrail requiring ZDR triggers it) ^[raw/document/openrouter/openrouter-046-guides-features-guardrails-2026-04-29.md]
- Guardrail budgets are enforced per-user and per-key, not pooled across assignees; a key's usage counts toward both the key's budget and the owning member's budget ^[raw/document/openrouter/openrouter-046-guides-features-guardrails-2026-04-29.md]

## Details

Account-wide privacy and provider settings always apply as a default guardrail. When additional guardrails are layered on, the stricter rule wins for allowlists, while ZDR uses OR logic across all applicable guardrails. ^[raw/document/openrouter/openrouter-046-guides-features-guardrails-2026-04-29.md]

### Budget enforcement

Guardrail budgets are not shared across users with the same guardrail. If a guardrail with a $50/day limit is assigned to three members, each member gets their own $50/day allowance. Usage by one member does not affect the others. ^[raw/document/openrouter/openrouter-046-guides-features-guardrails-2026-04-29.md]

When an API key has its own guardrail, the key's usage accumulates toward both the key's budget and the owning member's budget. If a member's combined key usage exceeds their member-level budget, the member is blocked even if individual keys are within their own limits. ^[raw/document/openrouter/openrouter-046-guides-features-guardrails-2026-04-29.md]

### Management

Guardrails are created and managed at Settings > Privacy in the OpenRouter dashboard. Organization admin privileges are required. An eligibility preview shows which providers and models remain available after combining the guardrail with account settings. Guardrails can also be managed programmatically via the OpenRouter API. ^[raw/document/openrouter/openrouter-046-guides-features-guardrails-2026-04-29.md]

## Related

- [[entities/openrouter]]
- [[concepts/zero_data_retention]]
- [[concepts/workspaces]]
- [[concepts/data_privacy]]
- [[concepts/budget_limit]]