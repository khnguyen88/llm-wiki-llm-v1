---
title: "Openrouter Guides Privacy Provider Logging"
summary: "How OpenRouter exposes and lets users control provider-level data handling policies for training on prompts and data retention, plus enterprise EU in-region routing"
type: summary
sources:
  - raw/document/openrouter/openrouter-068-guides-privacy-provider-logging-2026-04-29.md
tags:
  - openrouter
  - privacy
  - provider-logging
  - data-retention
  - eu-routing
  - enterprise
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Openrouter Guides Privacy Provider Logging

## Key Points

- Each AI provider on OpenRouter has its own data handling policies for logging and retention, reflected in structured data on each endpoint ^[001a-raw/document/openrouter/openrouter-068-guides-privacy-provider-logging-2026-04-29.md]
- Users can opt out of routing to providers that may train on their data via account settings; separate settings exist for paid and free models ^[001a-raw/document/openrouter/openrouter-068-guides-privacy-provider-logging-2026-04-29.md]
- Individual requests can be restricted to providers complying with specific data policies via the `provider` object, and this is also available as an account-wide setting ^[001a-raw/document/openrouter/openrouter-068-guides-privacy-provider-logging-2026-04-29.md]
- OpenRouter does not have routing rules based on provider data retention policies, but retention policies are surfaced per provider so users can ignore non-compliant providers ^[001a-raw/document/openrouter/openrouter-068-guides-privacy-provider-logging-2026-04-29.md]
- Enterprise EU in-region routing ensures prompts and completions are processed within the European Union using the base URL `https://eu.openrouter.ai` ^[001a-raw/document/openrouter/openrouter-068-guides-privacy-provider-logging-2026-04-29.md]
- EU in-region routing is only available for enterprise customers by request ^[001a-raw/document/openrouter/openrouter-068-guides-privacy-provider-logging-2026-04-29.md]

## Notes

- The training opt-out setting in account settings controls provider routing only; it has no bearing on OpenRouter's own policies for handling prompts ^[001a-raw/document/openrouter/openrouter-068-guides-privacy-provider-logging-2026-04-29.md]
- Provider terms of service are linked from each provider's page and aggregated in the documentation ^[001a-raw/document/openrouter/openrouter-068-guides-privacy-provider-logging-2026-04-29.md]
- Available EU-routed models can be listed by calling `/api/v1/models/user` through the EU domain ^[001a-raw/document/openrouter/openrouter-068-guides-privacy-provider-logging-2026-04-29.md]

## Related

- [[004-wiki/entities/openrouter]]
- [[004-wiki/concepts/provider-logging]]
- [[004-wiki/concepts/data-privacy]]
- [[004-wiki/concepts/provider-routing]]
- [[004-wiki/concepts/zero-data-retention]]
- [[004-wiki/concepts/data-collection-policy]]