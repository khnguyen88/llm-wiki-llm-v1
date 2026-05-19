---
title: "Provider Logging"
summary: "The data handling policies of individual AI providers on OpenRouter regarding prompt training and data retention, with user controls to restrict routing based on those policies"
type: concept
sources:
  - raw/document/openrouter/openrouter-068-guides-privacy-provider-logging-2026-04-29.md
tags:
  - openrouter
  - privacy
  - provider-logging
  - data-retention
  - provider-routing
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Provider Logging

Each AI provider on OpenRouter has its own data handling policies for logging and retention. OpenRouter exposes these policies in structured data on each AI endpoint, enabling users to control which providers can access their data. ^[raw/document/openrouter/openrouter-068-guides-privacy-provider-logging-2026-04-29.md]

## Key Points

- Provider data handling policies are reflected in structured data on each AI endpoint offered by OpenRouter ^[raw/document/openrouter/openrouter-068-guides-privacy-provider-logging-2026-04-29.md]
- Account settings allow users to opt out of routing to providers that may train on data, with separate settings for paid and free models ^[raw/document/openrouter/openrouter-068-guides-privacy-provider-logging-2026-04-29.md]
- Individual requests can be restricted to providers complying with specific data policies via the `provider` object in the request body ^[raw/document/openrouter/openrouter-068-guides-privacy-provider-logging-2026-04-29.md]
- OpenRouter does not have routing rules that change based on provider data retention policies, but retention policies are surfaced so users can filter manually ^[raw/document/openrouter/openrouter-068-guides-privacy-provider-logging-2026-04-29.md]
- Provider terms of service are linked from each provider's page and aggregated in the routing documentation ^[raw/document/openrouter/openrouter-068-guides-privacy-provider-logging-2026-04-29.md]

## Details

### Training on Prompts

Wherever possible, OpenRouter works with providers to ensure prompts will not be trained on. If a user opts out of training in account settings, OpenRouter will not route to providers that train. This setting only controls provider routing behavior and has no bearing on OpenRouter's own policies for handling prompts. ^[raw/document/openrouter/openrouter-068-guides-privacy-provider-logging-2026-04-29.md]

### Data Retention

Providers have their own data retention policies, often for compliance reasons. OpenRouter does not enforce routing rules based on these retention policies, but exposes them so users can make informed decisions about which providers to use. ^[raw/document/openrouter/openrouter-068-guides-privacy-provider-logging-2026-04-29.md]

## Related

- [[entities/openrouter]]
- [[concepts/data_privacy]]
- [[concepts/provider_routing]]
- [[concepts/zero_data_retention]]
- [[concepts/data_collection_policy]]
- [[summaries/openrouter-guides-privacy-provider-logging]]