---
title: "Exa"
summary: "A search engine API that combines keyword and embeddings-based search, used as a backend for OpenRouter's web search server tool"
type: entity
sources:
  - raw/document/openrouter/openrouter-034-guides-features-server-tools-web-search-2026-04-29.md
  - raw/document/openrouter/openrouter-035-guides-features-server-tools-web-fetch-2026-04-29.md
  - raw/document/openrouter/openrouter-039-guides-features-plugins-web-search-2026-04-29.md
tags:
  - search-engine
  - openrouter
  - web-search
  - web-fetch
  - embeddings
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Exa

A search engine API (exa.ai) that combines keyword and embeddings-based search, serving as a backend for OpenRouter's web search server tool. ^[raw/document/openrouter/openrouter-034-guides-features-server-tools-web-search-2026-04-29.md]

## Key Facts

- Used as the default fallback engine when `engine: "auto"` is set and the provider does not support native search ^[raw/document/openrouter/openrouter-034-guides-features-server-tools-web-search-2026-04-29.md]
- Can be explicitly selected with `engine: "exa"` in the `openrouter:web_search` tool parameters ^[raw/document/openrouter/openrouter-034-guides-features-server-tools-web-search-2026-04-29.md]
- Supports both `allowed_domains` and `excluded_domains` simultaneously for domain filtering ^[raw/document/openrouter/openrouter-034-guides-features-server-tools-web-search-2026-04-29.md]
- Supports `search_context_size` (`low`/`medium`/`high`) which controls characters per result ^[raw/document/openrouter/openrouter-034-guides-features-server-tools-web-search-2026-04-29.md]
- `max_results` applies per search call (1–25, default 5) ^[raw/document/openrouter/openrouter-034-guides-features-server-tools-web-search-2026-04-29.md]
- Pricing: $4 per 1,000 results using OpenRouter credits (default 5 results = max $0.02 per search) ^[raw/document/openrouter/openrouter-034-guides-features-server-tools-web-search-2026-04-29.md]
- Does not support `user_location` for location-biased results ^[raw/document/openrouter/openrouter-034-guides-features-server-tools-web-search-2026-04-29.md]
- Also used as a fetch engine for the `openrouter:web_fetch` server tool, providing page content extraction via Exa's Contents API ^[raw/document/openrouter/openrouter-035-guides-features-server-tools-web-fetch-2026-04-29.md]
- Supports BYOK for web fetch — configuring your own Exa API key makes web fetches free through OpenRouter, billed directly by Exa ^[raw/document/openrouter/openrouter-035-guides-features-server-tools-web-fetch-2026-04-29.md]
- In web fetch mode, Exa supports domain filtering and content truncation, with no hard limit on fetches per request ^[raw/document/openrouter/openrouter-035-guides-features-server-tools-web-fetch-2026-04-29.md]
- Web fetch pricing with Exa: $1 per 1,000 fetches via OpenRouter credits, or free with BYOK ^[raw/document/openrouter/openrouter-035-guides-features-server-tools-web-fetch-2026-04-29.md]
- In the deprecated `web` plugin, Exa uses an "auto" method combining keyword search and embeddings-based search to find relevant results ^[raw/document/openrouter/openrouter-039-guides-features-plugins-web-search-2026-04-29.md]
- The plugin's domain filtering uses `include_domains` and `exclude_domains` (vs. `allowed_domains`/`excluded_domains` in the server tool); Exa supports both simultaneously in either API ^[raw/document/openrouter/openrouter-039-guides-features-plugins-web-search-2026-04-29.md]

## Related

- [[entities/openrouter]]
- [[entities/firecrawl]]
- [[entities/parallel]]
- [[concepts/web_search]]
- [[concepts/server_tools]]
- [[concepts/web_fetch]]
- [[summaries/openrouter-guides-features-plugins-web-search]]