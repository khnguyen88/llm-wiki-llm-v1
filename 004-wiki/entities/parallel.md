---
title: "Parallel"
summary: "A search API (parallel.ai) that integrates with OpenRouter's web search server tool, supporting domain filtering and context size control"
type: entity
sources:
  - raw/document/openrouter/openrouter-034-guides-features-server-tools-web-search-2026-04-29.md
  - raw/document/openrouter/openrouter-039-guides-features-plugins-web-search-2026-04-29.md
tags:
  - search-engine
  - openrouter
  - web-search
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Parallel

A search API (parallel.ai) that integrates with OpenRouter's web search server tool, supporting domain filtering and context size control. ^[raw/document/openrouter/openrouter-034-guides-features-server-tools-web-search-2026-04-29.md]

## Key Facts

- Selected with `engine: "parallel"` in the `openrouter:web_search` tool parameters ^[raw/document/openrouter/openrouter-034-guides-features-server-tools-web-search-2026-04-29.md]
- Supports both `allowed_domains` and `excluded_domains`, but they are mutually exclusive (only one can be used per request) ^[raw/document/openrouter/openrouter-034-guides-features-server-tools-web-search-2026-04-29.md]
- Supports `search_context_size` (`low`/`medium`/`high`) which controls total characters across all results (unlike Exa where it applies per result) ^[raw/document/openrouter/openrouter-034-guides-features-server-tools-web-search-2026-04-29.md]
- `max_results` applies per search call (1–25, default 5) ^[raw/document/openrouter/openrouter-034-guides-features-server-tools-web-search-2026-04-29.md]
- Pricing: $4 per 1,000 results using OpenRouter credits (same rate as Exa) ^[raw/document/openrouter/openrouter-034-guides-features-server-tools-web-search-2026-04-29.md]
- Does not support `user_location` for location-biased results ^[raw/document/openrouter/openrouter-034-guides-features-server-tools-web-search-2026-04-29.md]
- In the deprecated `web` plugin, domain filtering uses `include_domains` and `exclude_domains`; Parallel supports both but they are mutually exclusive (only one can be used per request) ^[raw/document/openrouter/openrouter-039-guides-features-plugins-web-search-2026-04-29.md]

## Related

- [[entities/openrouter]]
- [[entities/exa]]
- [[entities/firecrawl]]
- [[concepts/web_search]]
- [[concepts/server_tools]]
- [[summaries/openrouter-guides-features-plugins-web-search]]