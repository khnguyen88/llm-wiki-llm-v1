---
title: "Openrouter Guides Features Server Tools Overview"
summary: "OpenRouter server tools are model-invoked, server-side tools that any model can call during a request — the platform executes them transparently without client-side implementation"
type: summary
sources:
  - raw/document/openrouter/openrouter-033-guides-features-server-tools-overview-2026-04-29.md
tags:
  - openrouter
  - server-tools
  - tool-calling
  - web-search
  - image-generation
  - api
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Openrouter Guides Features Server Tools Overview

## Key Points

- Server tools are specialized tools operated by OpenRouter that any model can call during a request; OpenRouter executes them server-side and returns results to the model with no client-side implementation needed ^[raw/document/openrouter/openrouter-033-guides-features-server-tools-overview-2026-04-29.md]
- Four server tools are available: `openrouter:web_search` (web search), `openrouter:datetime` (current date/time), `openrouter:image_generation` (image generation from text), and `openrouter:web_fetch` (fetch and extract content from URLs) ^[raw/document/openrouter/openrouter-033-guides-features-server-tools-overview-2026-04-29.md]
- Server tools differ from plugins (which always run once per request to inject or mutate data) and user-defined tools (which the model suggests but the client executes); server tools are model-invoked and server-executed ^[raw/document/openrouter/openrouter-033-guides-features-server-tools-overview-2026-04-29.md]
- Server tools use the `openrouter:*` type prefix in the `tools` array and can be mixed with user-defined tools (`type: "function"`) in the same request ^[raw/document/openrouter/openrouter-033-guides-features-server-tools-overview-2026-04-29.md]
- Server tool usage is tracked in the response `usage.server_tool_use` object (e.g., `web_search_requests: 2`) ^[raw/document/openrouter/openrouter-033-guides-features-server-tools-overview-2026-04-29.md]
- Server tools are currently in beta; the API and behavior may change ^[raw/document/openrouter/openrouter-033-guides-features-server-tools-overview-2026-04-29.md]

## Quotes

> Server tools are specialized tools operated by OpenRouter that any model can call during a request. When a model decides to use a server tool, OpenRouter executes it server-side and returns the result to the model — no client-side implementation needed. ^[raw/document/openrouter/openrouter-033-guides-features-server-tools-overview-2026-04-29.md]

## Notes

- The `:online` model variant is deprecated in favor of the `openrouter:web_search` server tool, which gives the model control over search timing and frequency rather than injecting search results automatically

## Related

- [[entities/openrouter]]
- [[concepts/server_tools]]
- [[concepts/tool_calling]]
- [[concepts/plugins]]
- [[concepts/image_generation]]
- [[concepts/online_variant]]