---
title: "App Attribution"
summary: "A mechanism for associating API requests with a specific application via HTTP headers, enabling public rankings, per-app analytics, and marketplace categorization"
type: concept
sources:
  - raw/document/openrouter/openrouter-045-app-attribution-2026-04-29.md
tags:
  - openrouter
  - app-attribution
  - http-headers
  - rankings
  - marketplace
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# App Attribution

App attribution allows developers to associate their API usage with their application, enabling visibility in public rankings and detailed analytics dashboards. ^[raw/document/openrouter/openrouter-045-app-attribution-2026-04-29.md]

## Key Points

- The `HTTP-Referer` header is required and serves as the primary identifier for app rankings; without it, no app page is created and usage is invisible in rankings ^[raw/document/openrouter/openrouter-045-app-attribution-2026-04-29.md]
- The `X-OpenRouter-Title` header sets or modifies an app's display name in rankings and analytics; `X-Title` is supported for backwards compatibility but must be paired with `HTTP-Referer` ^[raw/document/openrouter/openrouter-045-app-attribution-2026-04-29.md]
- The `X-OpenRouter-Categories` header assigns marketplace categories; unrecognized values are silently dropped ^[raw/document/openrouter/openrouter-045-app-attribution-2026-04-29.md]
- Apps using `localhost` URLs must include `X-OpenRouter-Title` alongside `HTTP-Referer` to be tracked ^[raw/document/openrouter/openrouter-045-app-attribution-2026-04-29.md]
- Attribution headers do not expose sensitive information about requests — only public apps that send headers appear in rankings ^[raw/document/openrouter/openrouter-045-app-attribution-2026-04-29.md]

## Details

OpenRouter tracks app attribution through three HTTP headers included in API requests. The `HTTP-Referer` header identifies the app by its URL and is mandatory — it acts as the unique identifier in the ranking system. The `X-OpenRouter-Title` header provides a human-readable display name. The `X-OpenRouter-Categories` header assigns the app to one or more marketplace categories, using a comma-separated list of lowercase, hyphen-separated values (each limited to 30 characters). ^[raw/document/openrouter/openrouter-045-app-attribution-2026-04-29.md]

Recognized marketplace categories are organized into four groups. **Coding** includes `cli-agent`, `ide-extension`, `cloud-agent`, `programming-app`, and `native-app-builder`. **Creative** includes `creative-writing`, `video-gen`, and `image-gen`. **Productivity** includes `writing-assistant`, `general-chat`, and `personal-agent`. **Entertainment** includes `roleplay` and `game`. Categories are merged across requests up to a per-app maximum. ^[raw/document/openrouter/openrouter-045-app-attribution-2026-04-29.md]

Attributed apps appear in three locations: the public rankings page at `openrouter.ai/rankings` (showing top apps by token usage across daily, weekly, and monthly periods), the "Apps" tab on individual model pages (showing which apps use each model most), and per-app analytics at `openrouter.ai/apps?url=<referer-url>` (showing model usage over time, token consumption, and usage patterns). ^[raw/document/openrouter/openrouter-045-app-attribution-2026-04-29.md]

## Related

- [[entities/openrouter]]
- [[summaries/openrouter-app-attribution]]
- [[concepts/analytics]]
- [[concepts/rate_limiting]]