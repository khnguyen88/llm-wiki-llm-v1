---
title: "Server Tools"
summary: "Model-invoked tools executed server-side by OpenRouter, requiring no client-side implementation — distinct from user-defined tools and plugins"
type: concept
sources:
  - raw/document/openrouter/openrouter-033-guides-features-server-tools-overview-2026-04-29.md
  - raw/document/openrouter/openrouter-034-guides-features-server-tools-web-search-2026-04-29.md
  - raw/document/openrouter/openrouter-035-guides-features-server-tools-web-fetch-2026-04-29.md
  - raw/document/openrouter/openrouter-036-guides-features-server-tools-datetime-2026-04-29.md
  - raw/document/openrouter/openrouter-037-guides-features-server-tools-image-generation-2026-04-29.md
  - raw/document/openrouter/openrouter-038-guides-features-plugins-overview-2026-04-29.md
tags:
  - openrouter
  - server-tools
  - tool-calling
  - web-search
  - domain-filtering
  - web-fetch
  - image-generation
  - datetime
  - api
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Server Tools

Server tools are specialized tools operated by OpenRouter that any model can call during a request. When the model decides to use a server tool, OpenRouter intercepts the tool call, executes it server-side, and returns the result to the model — no client-side implementation is needed. ^[raw/document/openrouter/openrouter-033-guides-features-server-tools-overview-2026-04-29.md]

## Key Points

- Server tools are model-decided (0 to N calls per request), server-executed by OpenRouter, and specified via the `tools` array with the `openrouter:*` type prefix ^[raw/document/openrouter/openrouter-033-guides-features-server-tools-overview-2026-04-29.md]
- Four available server tools: `openrouter:web_search` (search the web), `openrouter:datetime` (get current date/time), `openrouter:image_generation` (generate images from text), and `openrouter:web_fetch` (fetch and extract URL content) ^[raw/document/openrouter/openrouter-033-guides-features-server-tools-overview-2026-04-29.md]
- Server tools work alongside user-defined tools — both can be included in the same `tools` array in a single request ^[raw/document/openrouter/openrouter-033-guides-features-server-tools-overview-2026-04-29.md]
- Usage is tracked in the response `usage.server_tool_use` object (e.g., `{"web_search_requests": 2}`) ^[raw/document/openrouter/openrouter-033-guides-features-server-tools-overview-2026-04-29.md]
- Server tools are currently in beta; API and behavior may change ^[raw/document/openrouter/openrouter-033-guides-features-server-tools-overview-2026-04-29.md]
- The `openrouter:web_fetch` server tool enables any model to fetch content from a specific URL; supports five engines (`auto`, `native`, `exa`, `openrouter`, `firecrawl`), domain filtering, content truncation, and BYOK for Exa and Firecrawl ^[raw/document/openrouter/openrouter-035-guides-features-server-tools-web-fetch-2026-04-29.md]

## Details

### Server Tools vs Plugins vs User-Defined Tools

Three tool-like mechanisms operate on OpenRouter with distinct execution models. **Server tools** are model-decided (0 to N calls), server-executed, and use the `openrouter:*` type prefix in the `tools` array. **Plugins** are always-run-once mechanisms that inject or mutate requests/responses (e.g., response healing, PDF parsing), specified via the `plugins` array. **User-defined tools** are model-decided (0 to N calls) but client-executed, using the standard `function` type in the `tools` array. ^[raw/document/openrouter/openrouter-033-guides-features-server-tools-overview-2026-04-29.md] ^[raw/document/openrouter/openrouter-038-guides-features-plugins-overview-2026-04-29.md]

### How Server Tools Work

The execution flow is: (1) the developer includes one or more server tools in the `tools` array of the API request, (2) the model decides whether and when to call each server tool based on the user's prompt, (3) OpenRouter intercepts the tool call and executes it server-side, returning the result to the model, (4) the model uses the result to formulate its response and may call the tool again if needed. ^[raw/document/openrouter/openrouter-033-guides-features-server-tools-overview-2026-04-29.md]

Server tools can be combined with user-defined tools in the same request. OpenRouter executes server tools automatically while the client handles user-defined tool calls as usual. ^[raw/document/openrouter/openrouter-033-guides-features-server-tools-overview-2026-04-29.md]

### Web Search Server Tool

The `openrouter:web_search` server tool gives any model on OpenRouter access to real-time web information. When the model determines it needs current information, it calls the tool with a search query; OpenRouter executes the search and returns results (URLs, titles, and content snippets) that the model uses to formulate a grounded response. The model may search multiple times in a single request. ^[raw/document/openrouter/openrouter-034-guides-features-server-tools-web-search-2026-04-29.md]

Five search engines are available: `auto` (default, uses native provider search when available, falls back to Exa), `native` (forces provider's built-in search), `exa`, `firecrawl` (BYOK), and `parallel`. Configuration parameters include `engine`, `max_results` (1–25, default 5), `max_total_results`, `search_context_size` (`low`/`medium`/`high`), `allowed_domains`, `excluded_domains`, and `user_location`. ^[raw/document/openrouter/openrouter-034-guides-features-server-tools-web-search-2026-04-29.md]

### Web Fetch Server Tool

The `openrouter:web_fetch` server tool gives any model on OpenRouter the ability to fetch content from a specific URL. When the model determines it needs to read a web page or PDF document, it calls the tool with the URL; OpenRouter fetches and extracts the content server-side, returning text that the model incorporates into its response. The model may fetch multiple URLs in a single request. ^[raw/document/openrouter/openrouter-035-guides-features-server-tools-web-fetch-2026-04-29.md]

Five fetch engines are available: `auto` (default, uses native provider fetch when available, falls back to Exa), `native` (forces provider's built-in fetch), `exa` (Exa Contents API, supports BYOK), `openrouter` (direct HTTP fetch with content extraction), and `firecrawl` (Firecrawl scrape API, BYOK). Configuration parameters include `engine`, `max_uses` (maximum fetches per request), `max_content_tokens` (content length limit before truncation), `allowed_domains` (whitelist), and `blocked_domains` (blacklist). ^[raw/document/openrouter/openrouter-035-guides-features-server-tools-web-fetch-2026-04-29.md]

Engine capabilities vary across domain filtering, token truncation, API key handling, and hard fetch limits. Exa and Firecrawl have no hard fetch limit per request; OpenRouter and native engines are capped at 50 fetches per request. Pricing: Exa $1/1,000 fetches (free with BYOK), Firecrawl uses own credits (no OpenRouter charge), OpenRouter engine is free, and native pricing is passed through from the provider. ^[raw/document/openrouter/openrouter-035-guides-features-server-tools-web-fetch-2026-04-29.md]

### Datetime Server Tool

The `openrouter:datetime` server tool gives any model access to the current date and time. It accepts an optional `timezone` parameter (IANA timezone name, default `UTC`) and returns a JSON response with `datetime` (ISO 8601 with timezone offset) and `timezone` fields. No additional cost beyond standard token usage. ^[raw/document/openrouter/openrouter-036-guides-features-server-tools-datetime-2026-04-29.md]

### Image Generation Server Tool

The `openrouter:image_generation` server tool enables any model to generate images from text prompts. When the model determines an image is needed, it calls the tool with a description; OpenRouter generates the image server-side and returns the result. Activated by including `{ "type": "openrouter:image_generation" }` in the `tools` array. The default image generation model is `openai/gpt-image-1`, configurable via the `parameters` object. Available configuration parameters: `model`, `quality`, `size`, `aspect_ratio`, `background`, `output_format`, `output_compression`, and `moderation`. All parameters except `model` are passed directly to the underlying image generation API. The response returns `{ "status": "ok", "imageUrl": "https://..." }` on success or `{ "status": "error", "error": "..." }` on failure. The model may generate multiple images in a single request. Works with both Chat Completions and Responses APIs. Image generation cost is in addition to standard LLM token costs. ^[raw/document/openrouter/openrouter-037-guides-features-server-tools-image-generation-2026-04-29.md]

## Related

- [[entities/openrouter]]
- [[concepts/tool_calling]]
- [[concepts/plugins]]
- [[concepts/response_healing]]
- [[concepts/context_compression]]
- [[summaries/openrouter-guides-features-plugins-overview]]
- [[concepts/image_generation]]
- [[concepts/online_variant]]
- [[concepts/web_search]]
- [[entities/exa]]
- [[entities/firecrawl]]
- [[entities/parallel]]
- [[summaries/openrouter-guides-features-server-tools-overview]]
- [[summaries/openrouter-guides-features-server-tools-web-search]]
- [[concepts/web_fetch]]
- [[summaries/openrouter-guides-features-server-tools-web-fetch]]
- [[concepts/server_tools_datetime]]
- [[summaries/openrouter-guides-features-server-tools-datetime]]
- [[summaries/openrouter-guides-features-server-tools-image-generation]]