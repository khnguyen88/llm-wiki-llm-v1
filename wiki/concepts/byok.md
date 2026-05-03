---
title: "BYOK (Bring Your Own Key)"
summary: "A feature allowing users to supply their own cloud provider API keys to a routing platform, giving direct control over rate limits and costs while the platform handles request routing"
type: concept
sources:
  - raw/document/openrouter/openrouter-014-guides-overview-auth-byok-2026-04-29.md
  - raw/document/openrouter/openrouter-015-faq-2026-04-29.md
  - raw/document/openrouter/openrouter-018-guides-routing-provider-selection-2026-04-29.md
  - raw/document/openrouter/openrouter-029-guides-features-workspaces-2026-04-29.md
tags:
  - byok
  - authentication
  - api-keys
  - provider-routing
  - openrouter
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# BYOK (Bring Your Own Key)

A feature that allows users to supply their own cloud provider API keys to a routing platform (such as OpenRouter), giving direct control over rate limits and costs for each provider while the platform handles request routing and fallback logic. ^[raw/document/openrouter/openrouter-014-guides-overview-auth-byok-2026-04-29.md]

## Key Points

- Provider keys are securely encrypted and used for all requests routed through the specified provider; cost is a percentage of normal platform pricing, deducted from platform credits, with the fee waived for a first monthly threshold of requests ^[raw/document/openrouter/openrouter-014-guides-overview-auth-byok-2026-04-29.md]
- BYOK endpoints always take routing priority regardless of the user's specified provider order; after BYOK endpoints are exhausted, shared capacity is used in the user's specified order ^[raw/document/openrouter/openrouter-014-guides-overview-auth-byok-2026-04-29.md]
- By default, if a BYOK key hits a rate limit or failure, the platform falls back to shared credits; the "Always use this key" option disables fallback, ensuring all requests go through the user's account ^[raw/document/openrouter/openrouter-014-guides-overview-auth-byok-2026-04-29.md]
- Multiple BYOK keys for the same provider are all used for routing but their ordering is not guaranteed; deterministic ordering between keys requires separate provider accounts ^[raw/document/openrouter/openrouter-014-guides-overview-auth-byok-2026-04-29.md]
- Supported providers with specific credential formats include Azure AI Services, AWS Bedrock (API key or AWS credentials), and Google Vertex AI (service account JSON) ^[raw/document/openrouter/openrouter-014-guides-overview-auth-byok-2026-04-29.md]
- BYOK has a free monthly request threshold; beyond that threshold, a fee equal to a percentage of the equivalent OpenRouter model/provider cost is charged and deducted from OpenRouter credits ^[raw/document/openrouter/openrouter-015-faq-2026-04-29.md]

## Details

OpenRouter's BYOK feature lets users bring provider API keys for direct control over rate limits and costs. When a BYOK key is available for a provider, OpenRouter always prioritizes it over shared capacity. This priority override applies even when the user specifies a custom provider ordering — BYOK endpoints are tried first regardless of their position in the order array. Only after all BYOK endpoints are exhausted does OpenRouter fall back to shared capacity in the user's specified order. ^[raw/document/openrouter/openrouter-014-guides-overview-auth-byok-2026-04-29.md]

For partial BYOK configurations (keys for some providers but not others), BYOK providers still take priority. For example, if a user specifies `order: ["amazon-bedrock", "google-vertex"]` but only has a BYOK key for Google Vertex AI, the Vertex BYOK endpoint is tried first, followed by Amazon Bedrock shared capacity, then Google Vertex shared capacity. ^[raw/document/openrouter/openrouter-014-guides-overview-auth-byok-2026-04-29.md]

BYOK issues can be debugged via the Activity page by examining the `provider_responses` field in raw metadata, which shows HTTP status codes from each provider attempt. Common error codes include 400 (invalid request format), 401 (invalid/revoked key), 403 (insufficient permissions), 429 (rate limit hit), and 500 (provider internal error). ^[raw/document/openrouter/openrouter-014-guides-overview-auth-byok-2026-04-29.md]

### BYOK with Cross-Model Routing

When using BYOK with [[concepts/model_fallback]], `partition: "none"` in the `sort` object allows BYOK prioritization to work across model boundaries. Without this setting, the router always tries the primary model's endpoints first, even if a fallback model has a BYOK key available. With `partition: "none"`, the router can route to any model's BYOK endpoint based on the sort criteria, maximizing usage of the user's own API keys. ^[raw/document/openrouter/openrouter-018-guides-routing-provider-selection-2026-04-29.md]

### BYOK in Workspaces

In OpenRouter [[concepts/workspaces|Workspaces]], BYOK provider keys can be configured per workspace or shared across multiple workspaces. Each workspace maintains its own BYOK configuration independent of other workspaces. ^[raw/document/openrouter/openrouter-029-guides-features-workspaces-2026-04-29.md]

## Related

- [[entities/openrouter]]
- [[entities/amazon_bedrock]]
- [[entities/google_vertex_ai]]
- [[entities/azure_ai_services]]
- [[concepts/provider_fallback]]
- [[concepts/authentication]]
- [[concepts/rate_limiting]]
- [[summaries/openrouter-guides-overview-auth-byok]]
- [[concepts/credit_system]]
- [[concepts/provider_routing]]
- [[concepts/model_fallback]]
- [[concepts/workspaces]]
- [[summaries/openrouter-faq]]
- [[summaries/openrouter-guides-routing-provider-selection]]