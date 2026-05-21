---
title: "Openrouter App Attribution"
summary: "OpenRouter's app attribution system lets developers associate API usage with their applications via HTTP headers, enabling public rankings, model-level app listings, and detailed analytics"
type: summary
sources:
  - raw/document/openrouter/openrouter-045-app-attribution-2026-04-29.md
tags:
  - openrouter
  - app-attribution
  - rankings
  - api-headers
  - marketplace
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Openrouter App Attribution

## Key Points

- App attribution uses three HTTP headers: `HTTP-Referer` (required, identifies the app URL), `X-OpenRouter-Title` (sets display name), and `X-OpenRouter-Categories` (assigns marketplace categories) ^[001a-raw/document/openrouter/openrouter-045-app-attribution-2026-04-29.md]
- `HTTP-Referer` is required — without it no app page is created and usage does not appear in rankings; `X-OpenRouter-Title` alone is insufficient ^[001a-raw/document/openrouter/openrouter-045-app-attribution-2026-04-29.md]
- Attributed apps appear in public rankings at `openrouter.ai/rankings` (daily, weekly, monthly leaderboards), on model "Apps" tabs, and in per-app analytics dashboards at `openrouter.ai/apps?url=<referer-url>` ^[001a-raw/document/openrouter/openrouter-045-app-attribution-2026-04-29.md]
- `X-OpenRouter-Categories` accepts a comma-separated list of recognized categories organized into four groups: Coding (`cli-agent`, `ide-extension`, `cloud-agent`, `programming-app`, `native-app-builder`), Creative (`creative-writing`, `video-gen`, `image-gen`), Productivity (`writing-assistant`, `general-chat`, `personal-agent`), Entertainment (`roleplay`, `game`) ^[001a-raw/document/openrouter/openrouter-045-app-attribution-2026-04-29.md]
- Unrecognized categories are silently dropped; only the recognized list above is accepted ^[001a-raw/document/openrouter/openrouter-045-app-attribution-2026-04-29.md]
- Apps using `localhost` URLs must also include `X-OpenRouter-Title` to be tracked ^[001a-raw/document/openrouter/openrouter-045-app-attribution-2026-04-29.md]
- `X-Title` is supported alongside `X-OpenRouter-Title` for backwards compatibility ^[001a-raw/document/openrouter/openrouter-045-app-attribution-2026-04-29.md]

## Quotes

- "HTTP-Referer is **required** to create an app page and appear in rankings. Setting only `X-OpenRouter-Title` without a URL will not create an app entry." ^[001a-raw/document/openrouter/openrouter-045-app-attribution-2026-04-29.md]

## Notes

- Categories are limited to {MAX_CATEGORIES_PER_REQUEST} per request and {MAX_CATEGORIES_PER_APP} per app (exact numeric limits not specified in the source). ^[001a-raw/document/openrouter/openrouter-045-app-attribution-2026-04-29.md]
- Implementation examples are provided for TypeScript SDK, Python (OpenAI SDK), TypeScript (OpenAI SDK), Python (direct API), TypeScript (fetch), and cURL. ^[001a-raw/document/openrouter/openrouter-045-app-attribution-2026-04-29.md]

## Related

- [[004-wiki/entities/openrouter]]
- [[004-wiki/concepts/app-attribution]]
- [[004-wiki/concepts/analytics]]