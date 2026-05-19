---
title: "Openrouter Guides Overview Auth Byok"
summary: "OpenRouter's BYOK feature lets users bring their own provider API keys (AWS Bedrock, Google Vertex AI, Azure) for direct cost and rate limit control, with BYOK endpoints always prioritized over shared capacity in routing"
type: summary
sources:
  - raw/document/openrouter/openrouter-014-guides-overview-auth-byok-2026-04-29.md
tags:
  - openrouter
  - byok
  - authentication
  - provider-routing
  - api-keys
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Openrouter Guides Overview Auth Byok

## Key Points

- OpenRouter supports both OpenRouter credits and BYOK (Bring Your Own Keys); provider keys give direct control over rate limits and costs via the user's own provider account ^[raw/document/openrouter/openrouter-014-guides-overview-auth-byok-2026-04-29.md]
- BYOK keys are securely encrypted and used for all requests routed through the specified provider; cost is a percentage of normal OpenRouter pricing, deducted from OpenRouter credits, with the fee waived for the first monthly threshold of BYOK requests ^[raw/document/openrouter/openrouter-014-guides-overview-auth-byok-2026-04-29.md]
- OpenRouter always prioritizes BYOK keys when available; by default, if a BYOK key hits a rate limit or failure, OpenRouter falls back to shared credits ^[raw/document/openrouter/openrouter-014-guides-overview-auth-byok-2026-04-29.md]
- The "Always use this key" option prevents any fallback to OpenRouter credits, ensuring all requests go through the user's own account but risking rate limit errors ^[raw/document/openrouter/openrouter-014-guides-overview-auth-byok-2026-04-29.md]
- BYOK endpoints always take priority over provider ordering, regardless of position in the specified order array; after all BYOK endpoints are exhausted, shared capacity is used in the user's specified order ^[raw/document/openrouter/openrouter-014-guides-overview-auth-byok-2026-04-29.md]
- Multiple BYOK keys for the same provider are all used for routing but their ordering is not guaranteed ^[raw/document/openrouter/openrouter-014-guides-overview-auth-byok-2026-04-29.md]
- Azure AI Services, AWS Bedrock, and Google Vertex AI each have specific BYOK configuration formats requiring provider-specific credential structures ^[raw/document/openrouter/openrouter-014-guides-overview-auth-byok-2026-04-29.md]

## Quotes

- "OpenRouter always prioritizes using your provider keys when available. By default, if your key encounters a rate limit or failure, OpenRouter will fall back to using shared OpenRouter credits." ^[raw/document/openrouter/openrouter-014-guides-overview-auth-byok-2026-04-29.md]
- "BYOK keys effectively override your provider ordering for the initial routing attempts. There is currently no way to change this behavior." ^[raw/document/openrouter/openrouter-014-guides-overview-auth-byok-2026-04-29.md]

## Notes

- The source document includes detailed provider-specific credential formats for Azure (JSON with endpoint_url, api_key, model_slug, model_id), AWS Bedrock (API key string or JSON with accessKeyId/secretAccessKey/region), and Google Vertex AI (service account JSON with optional region field)
- Debugging BYOK issues is done via the Activity page's "View Raw Metadata" feature, examining the `provider_responses` field for HTTP status codes from each provider attempt

## Related

- [[concepts/byok]]
- [[entities/openrouter]]
- [[entities/amazon_bedrock]]
- [[entities/google_vertex_ai]]
- [[entities/azure_ai_services]]
- [[concepts/provider_fallback]]
- [[concepts/authentication]]
- [[concepts/rate_limiting]]