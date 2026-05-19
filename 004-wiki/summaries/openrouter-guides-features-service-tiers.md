---
title: "Openrouter Guides Features Service Tiers"
summary: "The service_tier parameter on OpenRouter controls cost and latency tradeoffs; currently supported for OpenAI models with values auto, default, flex, and priority, with response field placement varying by API format"
type: summary
sources:
  - raw/document/openrouter/openrouter-047-guides-features-service-tiers-2026-04-29.md
tags:
  - openrouter
  - service-tier
  - cost-optimization
  - latency
  - openai
  - api
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Openrouter Guides Features Service Tiers

## Key Points

- The `service_tier` request parameter controls cost and latency tradeoffs when sending requests through OpenRouter ^[raw/document/openrouter/openrouter-047-guides-features-service-tiers-2026-04-29.md]
- Currently only OpenAI is listed as a supported provider for `service_tier` ^[raw/document/openrouter/openrouter-047-guides-features-service-tiers-2026-04-29.md]
- Accepted request values for OpenAI: `auto`, `default`, `flex`, `priority` ^[raw/document/openrouter/openrouter-047-guides-features-service-tiers-2026-04-29.md]
- The API response includes a `service_tier` field indicating which tier was actually used ^[raw/document/openrouter/openrouter-047-guides-features-service-tiers-2026-04-29.md]
- For Chat Completions API (`/api/v1/chat/completions`) and Responses API (`/api/v1/responses`), `service_tier` is returned at the top level of the response object ^[raw/document/openrouter/openrouter-047-guides-features-service-tiers-2026-04-29.md]
- For Messages API (`/api/v1/messages`), `service_tier` is returned inside the `usage` object, matching Anthropic's native format ^[raw/document/openrouter/openrouter-047-guides-features-service-tiers-2026-04-29.md]

## Related

- [[concepts/service_tier]]
- [[entities/openrouter]]
- [[entities/openai]]