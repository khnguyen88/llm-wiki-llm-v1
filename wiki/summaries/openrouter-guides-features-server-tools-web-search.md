---
title: "Openrouter Guides Features Server Tools Web Search"
summary: "OpenRouter's web search server tool (`openrouter:web_search`) gives any model real-time web information, with configurable search engines, domain filtering, and cost controls"
type: summary
sources:
  - raw/document/openrouter/openrouter-034-guides-features-server-tools-web-search-2026-04-29.md
tags:
  - openrouter
  - web-search
  - server-tools
  - search-engine
  - domain-filtering
  - exa
  - firecrawl
  - parallel
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Openrouter Guides Features Server Tools Web Search

## Key Points

- The `openrouter:web_search` server tool gives any model on OpenRouter access to real-time web information; the model decides when and whether to search (0 to N calls per request) ^[raw/document/openrouter/openrouter-034-guides-features-server-tools-web-search-2026-04-29.md]
- Five search engines available: `auto` (default, uses native provider search when available, falls back to Exa), `native`, `exa`, `firecrawl`, and `parallel` ^[raw/document/openrouter/openrouter-034-guides-features-server-tools-web-search-2026-04-29.md]
- Configuration parameters include `engine`, `max_results` (1–25, default 5), `max_total_results` (caps cumulative results across multiple searches), `search_context_size` (`low`/`medium`/`high`), `allowed_domains`, `excluded_domains`, and `user_location` ^[raw/document/openrouter/openrouter-034-guides-features-server-tools-web-search-2026-04-29.md]
- Domain filtering behavior varies by engine: Exa supports both `allowed_domains` and `excluded_domains` simultaneously; Parallel supports both but they are mutually exclusive; Firecrawl returns an error if domain filters are set; native providers vary (Anthropic allows either but not both, OpenAI silently ignores `excluded_domains`) ^[raw/document/openrouter/openrouter-034-guides-features-server-tools-web-search-2026-04-29.md]
- Usage is tracked in the response `usage.server_tool_use.web_search_requests` field, counting total search queries made during the request ^[raw/document/openrouter/openrouter-034-guides-features-server-tools-web-search-2026-04-29.md]
- Works with both Chat Completions (`/api/v1/chat/completions`) and Responses (`/api/v1/responses`) APIs ^[raw/document/openrouter/openrouter-034-guides-features-server-tools-web-search-2026-04-29.md]
- Replaces the deprecated web search plugin (`plugins: [{ id: "web" }]`) and `:online` model variant; the server tool gives the model agency over search behavior rather than unconditionally attaching results ^[raw/document/openrouter/openrouter-034-guides-features-server-tools-web-search-2026-04-29.md]

## Quotes

- "Server tools are currently in beta. The API and behavior may change." ^[raw/document/openrouter/openrouter-034-guides-features-server-tools-web-search-2026-04-29.md]

## Notes

- Pricing: Exa and Parallel both cost $4 per 1,000 results via OpenRouter credits; Firecrawl uses its own credits directly (no OpenRouter charge); native provider pricing is passed through
- `max_total_results` is useful for controlling cost and context window usage in agentic loops; once the limit is reached, subsequent search calls return a message telling the model the limit was hit
- `user_location` only affects native provider search results and is ignored by Exa, Firecrawl, and Parallel engines

## Related

- [[entities/openrouter]]
- [[entities/exa]]
- [[entities/firecrawl]]
- [[entities/parallel]]
- [[concepts/web_search]]
- [[concepts/server_tools]]
- [[concepts/online_variant]]
- [[concepts/plugins]]
- [[concepts/tool_calling]]