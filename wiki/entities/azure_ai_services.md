---
title: "Azure AI Services"
summary: "Microsoft Azure cloud service providing AI model deployments, supported as a BYOK provider on OpenRouter with JSON-formatted API key configurations"
type: entity
sources:
  - raw/document/openrouter/openrouter-014-guides-overview-auth-byok-2026-04-29.md
tags:
  - azure
  - microsoft
  - cloud-provider
  - byok
  - openrouter
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Azure AI Services

Microsoft Azure cloud service providing AI model deployments. Supported as a BYOK (Bring Your Own Key) provider on OpenRouter, requiring JSON-formatted API key configuration that maps Azure deployments to OpenRouter model slugs. ^[raw/document/openrouter/openrouter-014-guides-overview-auth-byok-2026-04-29.md]

## Key Facts

- When used as a BYOK provider on OpenRouter, Azure API keys must be provided in JSON format with fields: `model_slug` (OpenRouter model identifier), `endpoint_url` (must end with `/chat/completions`), `api_key`, and `model_id` (Azure deployment name) ^[raw/document/openrouter/openrouter-014-guides-overview-auth-byok-2026-04-29.md]
- The `endpoint_url` is constructed from the Azure resource endpoint with `/chat/completions` appended and must include the `api-version` query parameter ^[raw/document/openrouter/openrouter-014-guides-overview-auth-byok-2026-04-29.md]
- Supports multiple model deployments via an array of configurations, each mapping a different Azure deployment to an OpenRouter model slug ^[raw/document/openrouter/openrouter-014-guides-overview-auth-byok-2026-04-29.md]
- Values for configuration are found in the Azure portal under the AI Services resource: endpoint URL in "Overview", API key under "Keys and Endpoint", and model ID is the deployment name ^[raw/document/openrouter/openrouter-014-guides-overview-auth-byok-2026-04-29.md]
- BYOK keys for Azure take routing priority over shared OpenRouter capacity, regardless of provider ordering ^[raw/document/openrouter/openrouter-014-guides-overview-auth-byok-2026-04-29.md]

## Related

- [[entities/openrouter]]
- [[entities/amazon_bedrock]]
- [[entities/google_vertex_ai]]
- [[concepts/byok]]
- [[concepts/authentication]]