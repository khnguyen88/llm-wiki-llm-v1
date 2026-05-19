---
title: "Web Fetch"
summary: "An OpenRouter server tool (openrouter:web_fetch) that enables any model to fetch and extract content from a specific URL, with configurable engines, domain filtering, and content truncation"
type: concept
sources:
  - raw/document/openrouter/openrouter-035-guides-features-server-tools-web-fetch-2026-04-29.md
tags:
  - openrouter
  - server-tools
  - web-fetch
  - url-fetching
  - content-extraction
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Web Fetch

The `openrouter:web_fetch` server tool gives any model on OpenRouter the ability to fetch content from a specific URL. When the model needs to read a web page or PDF document, it calls the tool with the URL; OpenRouter fetches and extracts the content server-side, returning text that the model can use in its response. ^[raw/document/openrouter/openrouter-035-guides-features-server-tools-web-fetch-2026-04-29.md]

## Key Points

- Activated by including `{ "type": "openrouter:web_fetch" }` in the `tools` array; the model decides whether and when to fetch URLs based on the user's prompt ^[raw/document/openrouter/openrouter-035-guides-features-server-tools-web-fetch-2026-04-29.md]
- Supports five fetch engines: `auto` (default, native with Exa fallback), `native` (provider's built-in), `exa` (Exa Contents API, supports BYOK), `openrouter` (direct HTTP fetch), and `firecrawl` (Firecrawl scrape API, BYOK) ^[raw/document/openrouter/openrouter-035-guides-features-server-tools-web-fetch-2026-04-29.md]
- Configurable parameters: `engine`, `max_uses` (max fetches per request), `max_content_tokens` (truncation limit), `allowed_domains` (whitelist), `blocked_domains` (blacklist) ^[raw/document/openrouter/openrouter-035-guides-features-server-tools-web-fetch-2026-04-29.md]
- The model may fetch multiple URLs in a single request ^[raw/document/openrouter/openrouter-035-guides-features-server-tools-web-fetch-2026-04-29.md]
- Works with both Chat Completions (`/api/v1/chat/completions`) and Responses (`/api/v1/responses`) APIs ^[raw/document/openrouter/openrouter-035-guides-features-server-tools-web-fetch-2026-04-29.md]

## Details

### Engine Selection

The `auto` engine (default) uses native provider fetch when available and falls back to Exa. The `native` engine forces the provider's built-in web fetch. The `exa` engine uses Exa's Contents API to extract page content and supports BYOK (Bring Your Own Key) for free usage. The `openrouter` engine uses direct HTTP fetch with content extraction. The `firecrawl` engine uses Firecrawl's scrape API and requires BYOK via the OpenRouter plugin settings at `openrouter.ai/settings/plugins`. ^[raw/document/openrouter/openrouter-035-guides-features-server-tools-web-fetch-2026-04-29.md]

Engine capabilities vary: all engines support domain filtering except native (varies by provider). Exa, Firecrawl, and OpenRouter support token truncation; native does not. Exa supports server-side or BYOK API keys, Firecrawl requires BYOK, OpenRouter uses server-side keys, and native is provider-handled. Exa and Firecrawl have no hard fetch limit per request, while OpenRouter and native are capped at 50 fetches per request. ^[raw/document/openrouter/openrouter-035-guides-features-server-tools-web-fetch-2026-04-29.md]

### Domain Filtering and Content Truncation

`allowed_domains` restricts fetching to specified domains only; `blocked_domains` prevents fetching from specified domains. `max_content_tokens` limits content length in approximate tokens; content exceeding this limit is truncated, helping control context window usage when fetching large pages. ^[raw/document/openrouter/openrouter-035-guides-features-server-tools-web-fetch-2026-04-29.md]

### Response Format

Successful fetches return a JSON object with `url`, `title`, `content` (full text), `status` ("completed"), and `retrieved_at` (ISO 8601 timestamp). Failed fetches return `url`, `status` ("failed"), and `error` (e.g., "HTTP 404: Page not found"). ^[raw/document/openrouter/openrouter-035-guides-features-server-tools-web-fetch-2026-04-29.md]

### Pricing

Exa costs $1 per 1,000 fetches (free with BYOK). Firecrawl uses your Firecrawl credits directly with no OpenRouter charge. The OpenRouter engine is free. Native engine pricing is passed through from the provider. All pricing is in addition to standard LLM token costs for processing the fetched content. ^[raw/document/openrouter/openrouter-035-guides-features-server-tools-web-fetch-2026-04-29.md]

## Related

- [[entities/openrouter]]
- [[entities/exa]]
- [[entities/firecrawl]]
- [[concepts/server_tools]]
- [[concepts/web_search]]
- [[concepts/byok]]
- [[concepts/tool_calling]]
- [[summaries/openrouter-guides-features-server-tools-web-fetch]]