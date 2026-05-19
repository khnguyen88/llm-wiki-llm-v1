---
title: "Management API Keys"
summary: "Dedicated administrative credentials for programmatically managing API keys via OpenRouter's key management endpoints, distinct from completion API keys"
type: concept
sources:
  - raw/document/openrouter/openrouter-013-guides-overview-auth-management-api-keys-2026-04-29.md
  - raw/document/openrouter/openrouter-029-guides-features-workspaces-2026-04-29.md
tags:
  - openrouter
  - api-keys
  - authentication
  - key-management
  - security
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Management API Keys

Management API Keys are a separate credential type in OpenRouter used exclusively for administrative operations on API keys — creating, listing, updating, and deleting completion API keys programmatically. They cannot be used to make model completion requests. ^[raw/document/openrouter/openrouter-013-guides-overview-auth-management-api-keys-2026-04-29.md]

## Key Points

- Management keys are created via the Management API Keys page at `/settings/management-keys` and are distinct from regular completion API keys ^[raw/document/openrouter/openrouter-013-guides-overview-auth-management-api-keys-2026-04-29.md]
- All key management endpoints reside under `/api/v1/keys` and require a Management API key in the `Authorization: Bearer` header ^[raw/document/openrouter/openrouter-013-guides-overview-auth-management-api-keys-2026-04-29.md]
- Supports full CRUD operations: list keys (with `offset` pagination), create keys (with optional `name` and credit `limit`), get a specific key by hash, update key properties, and delete keys ^[raw/document/openrouter/openrouter-013-guides-overview-auth-management-api-keys-2026-04-29.md]
- The `limit_reset` field controls automatic credit limit resets at `daily`, `weekly`, or `monthly` intervals (resets at midnight UTC) ^[raw/document/openrouter/openrouter-013-guides-overview-auth-management-api-keys-2026-04-29.md]
- The `include_byok_in_limit` field controls whether BYOK (Bring Your Own Key) usage counts toward a key's credit limit ^[raw/document/openrouter/openrouter-013-guides-overview-auth-management-api-keys-2026-04-29.md]

## Details

### Use Cases

Three primary scenarios drive programmatic key management: SaaS applications that automatically create unique API keys for each customer instance; security-conscious organizations that regularly rotate API keys for compliance; and automated usage monitoring that disables keys exceeding configured limits with optional periodic resets. ^[raw/document/openrouter/openrouter-013-guides-overview-auth-management-api-keys-2026-04-29.md]

### Key Properties

API responses return JSON objects with key metadata including: `hash` (the key identifier used in API calls), `label` (masked key display), `name` (human-readable label), `disabled` (boolean), `limit` and `limit_remaining` (credit tracking), `limit_reset` (reset schedule), `usage` and `byok_usage` (each with total, daily, weekly, and monthly breakdowns). The full key string is returned only at creation time and cannot be retrieved afterward. ^[raw/document/openrouter/openrouter-013-guides-overview-auth-management-api-keys-2026-04-29.md]

### SDK Support

The TypeScript SDK (`@openrouter/sdk`) provides a dedicated `openRouter.apiKeys` namespace with methods: `list()`, `list({ offset })`, `create({ name, limit })`, `get(keyHash)`, `update(keyHash, { name, disabled, includeByokInLimit, limitReset })`, and `delete(keyHash)`. Python usage requires direct HTTP requests to the REST endpoints. ^[raw/document/openrouter/openrouter-013-guides-overview-auth-management-api-keys-2026-04-29.md]

## Related

- [[entities/openrouter]]
- [[concepts/authentication]]
- [[concepts/oauth_pkce]]
- [[concepts/rate_limiting]]
- [[concepts/byoai]]