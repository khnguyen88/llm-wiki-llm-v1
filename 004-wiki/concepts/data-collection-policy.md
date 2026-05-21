---
title: "Data Collection Policy"
summary: "OpenRouter routing controls that filter providers by their data retention and privacy practices, plus OpenRouter's own data handling: two opt-in settings control prompt/completion storage, and metadata is always collected"
type: concept
sources:
  - raw/document/openrouter/openrouter-018-guides-routing-provider-selection-2026-04-29.md
  - raw/document/openrouter/openrouter-067-guides-privacy-data-collection-2026-04-29.md
tags:
  - openrouter
  - data-privacy
  - data-collection
  - zdr
  - routing
  - metadata
  - logging
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: merged
---

# Data Collection Policy

OpenRouter provides three routing controls that filter providers by their data retention and privacy practices: `data_collection`, `zdr` (Zero Data Retention), and `enforce_distillable_text`. These let developers ensure requests are only routed to providers that meet specific data handling requirements. ^[001a-raw/document/openrouter/openrouter-018-guides-routing-provider-selection-2026-04-29.md]

## Key Points

- `data_collection: "deny"` excludes providers that store user data non-transiently and may train on it; default is `"allow"` ^[001a-raw/document/openrouter/openrouter-018-guides-routing-provider-selection-2026-04-29.md]
- `zdr: true` restricts routing to only Zero Data Retention endpoints — providers that do not retain prompts after delivery ^[001a-raw/document/openrouter/openrouter-018-guides-routing-provider-selection-2026-04-29.md]
- `enforce_distillable_text: true` restricts routing to only models where the author has explicitly enabled text distillation, useful for building fine-tuning or distillation datasets ^[001a-raw/document/openrouter/openrouter-018-guides-routing-provider-selection-2026-04-29.md]
- `data_collection` is also available as an account-wide setting in privacy settings; per-request values apply on top of account settings ^[001a-raw/document/openrouter/openrouter-018-guides-routing-provider-selection-2026-04-29.md]
- `zdr` operates as an OR with account-wide ZDR settings — if either is enabled, ZDR enforcement applies; per-request cannot override account-wide enforcement ^[001a-raw/document/openrouter/openrouter-018-guides-routing-provider-selection-2026-04-29.md]

## Details

OpenRouter displays a **Data Policy** tag on model pages for providers that may log prompts, representing best-known data practices rather than a definitive guarantee of third-party policies. The `data_collection` field provides request-level filtering beyond what the account-wide setting offers. ^[001a-raw/document/openrouter/openrouter-018-guides-routing-provider-selection-2026-04-29.md]

ZDR enforcement is useful for customers who do not want to globally enforce ZDR but need specific requests to route only to ZDR endpoints. EU in-region routing is available for enterprise customers, ensuring prompts and completions are processed entirely within the EU. ^[001a-raw/document/openrouter/openrouter-018-guides-routing-provider-selection-2026-04-29.md]

### OpenRouter's Own Data Collection

OpenRouter does not store user prompts or completions by default. Two separate opt-in settings control data handling: ^[001a-raw/document/openrouter/openrouter-067-guides-privacy-data-collection-2026-04-29.md]

- **Private Input & Output Logging** (off by default, enabled in Observability settings) makes prompts and completions visible in logs for debugging and prompt optimization; OpenRouter does not access or use this data; for organizations, only admins can view it ^[001a-raw/document/openrouter/openrouter-067-guides-privacy-data-collection-2026-04-29.md]
- **OpenRouter Use of Inputs/Outputs** (off by default, enabled in Privacy settings) allows OpenRouter to use prompt and completion data to improve the product, in exchange for a 1% discount on all model usage ^[001a-raw/document/openrouter/openrouter-067-guides-privacy-data-collection-2026-04-29.md]

OpenRouter samples a small number of prompts for anonymous categorization to power reporting and model ranking. If a user is not opted in to OpenRouter use of inputs/outputs, categorization is stored completely anonymously and never associated with the user's account or user ID. The categorization is performed by a model with a zero-data-retention policy. ^[001a-raw/document/openrouter/openrouter-067-guides-privacy-data-collection-2026-04-29.md]

Metadata (prompt/completion token counts, latency, etc.) is stored for every request regardless of opt-in status, but does not include the content of prompts or responses. This metadata powers reporting, model ranking, and the logs metadata page. ^[001a-raw/document/openrouter/openrouter-067-guides-privacy-data-collection-2026-04-29.md]

## Related

- [[004-wiki/entities/openrouter]]
- [[004-wiki/concepts/provider-routing]]
- [[004-wiki/concepts/zero-data-retention]]
- [[004-wiki/concepts/distillation]]
- [[004-wiki/concepts/data-privacy]]
- [[004-wiki/concepts/input-output-logging]]
- [[004-wiki/summaries/openrouter-guides-routing-provider-selection]]
- [[004-wiki/summaries/openrouter-guides-privacy-data-collection]]