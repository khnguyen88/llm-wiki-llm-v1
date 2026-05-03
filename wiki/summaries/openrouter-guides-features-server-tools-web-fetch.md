---
title: "Openrouter Guides Features Server Tools Web Fetch"
summary: "OpenRouter's openrouter:web_fetch server tool enables any model to fetch and extract content from URLs, with configurable engines (auto/native/exa/openrouter/firecrawl), domain filtering, content truncation, and BYOK support"
type: summary
sources:
  - raw/document/openrouter/openrouter-035-guides-features-server-tools-web-fetch-2026-04-29.md
tags:
  - openrouter
  - web-fetch
  - server-tools
  - exa
  - firecrawl
  - byok
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Openrouter Guides Features Server Tools Web Fetch

## Key Points

- The `openrouter:web_fetch` server tool allows any model on OpenRouter to fetch content from a specific URL; the model decides when to call it, and OpenRouter fetches and extracts the content server-side ^[raw/document/openrouter/openrouter-035-guides-features-server-tools-web-fetch-2026-04-29.md]
- Five fetch engines are available: `auto` (default, uses native provider fetch or falls back to Exa), `native` (provider's built-in fetch), `exa` (Exa Contents API, supports BYOK), `openrouter` (direct HTTP fetch), and `firecrawl` (Firecrawl scrape API, BYOK) ^[raw/document/openrouter/openrouter-035-guides-features-server-tools-web-fetch-2026-04-29.md]
- Configuration parameters include `engine`, `max_uses` (maximum fetches per request), `max_content_tokens` (content length limit before truncation), `allowed_domains`, and `blocked_domains` ^[raw/document/openrouter/openrouter-035-guides-features-server-tools-web-fetch-2026-04-29.md]
- OpenRouter and native engines have a hard limit of 50 fetches per request; Exa and Firecrawl have no hard limit ^[raw/document/openrouter/openrouter-035-guides-features-server-tools-web-fetch-2026-04-29.md]
- Works with both Chat Completions (`/api/v1/chat/completions`) and Responses (`/api/v1/responses`) APIs ^[raw/document/openrouter/openrouter-035-guides-features-server-tools-web-fetch-2026-04-29.md]
- Pricing: Exa $1 per 1,000 fetches (free with BYOK), Firecrawl uses your Firecrawl credits directly, OpenRouter engine is free, Native pricing is passed through from the provider ^[raw/document/openrouter/openrouter-035-guides-features-server-tools-web-fetch-2026-04-29.md]
- Domain filtering with `allowed_domains` (whitelist) and `blocked_domains` (blacklist) restricts which URLs can be fetched ^[raw/document/openrouter/openrouter-035-guides-features-server-tools-web-fetch-2026-04-29.md]

## Quotes

> "Server tools are currently in beta. The API and behavior may change." ^[raw/document/openrouter/openrouter-035-guides-features-server-tools-web-fetch-2026-04-29.md:1]

## Notes

- The web_fetch tool is distinct from `openrouter:web_search` — it fetches specific URLs rather than searching for information
- The `auto` engine selects native provider fetch when available, otherwise falls back to Exa

## Related

- [[entities/openrouter]]
- [[entities/exa]]
- [[entities/firecrawl]]
- [[concepts/server_tools]]
- [[concepts/web_fetch]]
- [[concepts/byok]]
- [[concepts/tool_calling]]
- [[summaries/openrouter-guides-features-server-tools-overview]]
- [[summaries/openrouter-guides-features-server-tools-web-search]]