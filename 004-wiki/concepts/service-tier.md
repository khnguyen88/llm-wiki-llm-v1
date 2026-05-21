---
title: "Service Tier"
summary: "A request parameter on OpenRouter that controls cost and latency tradeoffs by selecting a processing tier, with the actual tier used reported back in the API response"
type: concept
sources:
  - raw/document/openrouter/openrouter-047-guides-features-service-tiers-2026-04-29.md
tags:
  - openrouter
  - service-tier
  - cost-optimization
  - latency
  - api-parameter
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Service Tier

The `service_tier` parameter lets API consumers control cost and latency tradeoffs when sending requests through OpenRouter. The value specified in the request selects a processing tier, and the response reports which tier was actually used. ^[001a-raw/document/openrouter/openrouter-047-guides-features-service-tiers-2026-04-29.md]

## Key Points

- The `service_tier` parameter is passed in the request to select a specific processing tier ^[001a-raw/document/openrouter/openrouter-047-guides-features-service-tiers-2026-04-29.md]
- Currently only OpenAI supports the `service_tier` parameter, with accepted values: `auto`, `default`, `flex`, `priority` ^[001a-raw/document/openrouter/openrouter-047-guides-features-service-tiers-2026-04-29.md]
- The API response includes a `service_tier` field indicating which capacity tier was actually used ^[001a-raw/document/openrouter/openrouter-047-guides-features-service-tiers-2026-04-29.md]
- Response field placement varies by API format: top-level for Chat Completions and Responses APIs; inside `usage` for Messages API ^[001a-raw/document/openrouter/openrouter-047-guides-features-service-tiers-2026-04-29.md]

## Details

The placement of `service_tier` in the response depends on which API format is used. For the Chat Completions API (`/api/v1/chat/completions`) and Responses API (`/api/v1/responses`), the field appears at the top level of the response object, matching OpenAI's native format. For the Messages API (`/api/v1/messages`), it appears inside the `usage` object, matching Anthropic's native format. ^[001a-raw/document/openrouter/openrouter-047-guides-features-service-tiers-2026-04-29.md]

## Related

- [[004-wiki/entities/openrouter]]
- [[004-wiki/entities/openai]]
- [[004-wiki/concepts/provider-routing]]
- [[004-wiki/concepts/performance-thresholds]]
- [[004-wiki/summaries/openrouter-guides-features-service-tiers]]