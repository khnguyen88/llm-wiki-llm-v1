---
title: "OpenRouter Guides Overview Auth Management Api Keys"
summary: "OpenRouter Management API Keys enable programmatic CRUD operations on API keys for automated key distribution, rotation, and usage monitoring"
type: summary
sources:
  - raw/document/openrouter/openrouter-013-guides-overview-auth-management-api-keys-2026-04-29.md
tags:
  - openrouter
  - api-keys
  - authentication
  - management-api
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# OpenRouter Guides Overview Auth Management Api Keys

## Key Points

- Management API keys are separate from completion API keys and can only be used for administrative operations, not for making model completion requests ^[raw/document/openrouter/openrouter-013-guides-overview-auth-management-api-keys-2026-04-29.md]
- Created via the Management API Keys page at `/settings/management-keys` by clicking "Create New Key" ^[raw/document/openrouter/openrouter-013-guides-overview-auth-management-api-keys-2026-04-29.md]
- All key management endpoints are under `/api/v1/keys` and require a Management API key in the Authorization header ^[raw/document/openrouter/openrouter-013-guides-overview-auth-management-api-keys-2026-04-29.md]
- Supports full CRUD: list (with pagination via `offset`), create (with optional credit `limit` and `name`), get, update (including `disabled`, `include_byok_in_limit`, `limit_reset`), and delete ^[raw/document/openrouter/openrouter-013-guides-overview-auth-management-api-keys-2026-04-29.md]
- Primary use cases: SaaS applications creating unique API keys per customer, automated key rotation for security compliance, and usage monitoring with automatic key disabling when limits are exceeded ^[raw/document/openrouter/openrouter-013-guides-overview-auth-management-api-keys-2026-04-29.md]
- API responses return JSON objects with key metadata including `hash`, `name`, `disabled`, `limit`, `limit_remaining`, `limit_reset`, `usage` (total/daily/weekly/monthly), and `byok_usage` breakdowns ^[raw/document/openrouter/openrouter-013-guides-overview-auth-management-api-keys-2026-04-29.md]
- The `limit_reset` parameter supports `daily`, `weekly`, and `monthly` intervals, resetting limits at midnight UTC ^[raw/document/openrouter/openrouter-013-guides-overview-auth-management-api-keys-2026-04-29.md]

## Quotes

> "Management keys cannot be used to make API calls to OpenRouter's completion endpoints - they are exclusively for administrative operations." ^[raw/document/openrouter/openrouter-013-guides-overview-auth-management-api-keys-2026-04-29.md]

## Notes

- The TypeScript SDK (`@openrouter/sdk`) provides a dedicated `openRouter.apiKeys` namespace with `list()`, `create()`, `get()`, `update()`, and `delete()` methods
- Python usage requires direct HTTP requests with `requests` library; no dedicated SDK namespace is documented for key management
- Newly created keys return the full key string in the response (only available at creation time)

## Related

- [[entities/openrouter]]
- [[concepts/management_api_keys]]
- [[concepts/authentication]]
- [[concepts/oauth_pkce]]
- [[concepts/rate_limiting]]