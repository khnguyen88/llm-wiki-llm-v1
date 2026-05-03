---
title: "Online Variant"
summary: "A deprecated OpenRouter model variant suffix (`:online`) that enabled real-time web search capabilities, replaced by the `openrouter:web_search` server tool"
type: concept
sources:
  - raw/document/openrouter/openrouter-024-guides-routing-model-variants-online-2026-04-29.md
  - raw/document/openrouter/openrouter-034-guides-features-server-tools-web-search-2026-04-29.md
  - raw/document/openrouter/openrouter-039-guides-features-plugins-web-search-2026-04-29.md
tags:
  - openrouter
  - model-variants
  - web-search
  - deprecated
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Online Variant

A deprecated OpenRouter model variant suffix (`:online`) that enabled real-time web search capabilities by incorporating web search results into model responses. It has been replaced by the `openrouter:web_search` server tool. ^[raw/document/openrouter/openrouter-024-guides-routing-model-variants-online-2026-04-29.md]

## Key Points

- The `:online` variant is deprecated; the recommended replacement is the `openrouter:web_search` server tool, which gives the model control over when and how often to search ^[raw/document/openrouter/openrouter-024-guides-routing-model-variants-online-2026-04-29.md]
- Usage was by appending `:online` to any model ID, e.g., `"openai/gpt-5.2:online"` ^[raw/document/openrouter/openrouter-024-guides-routing-model-variants-online-2026-04-29.md]
- The `:online` suffix was a shortcut for the `web` plugin, exactly equivalent to `{ "model": "openrouter/auto", "plugins": [{ "id": "web" }] }` ^[raw/document/openrouter/openrouter-024-guides-routing-model-variants-online-2026-04-29.md]
- Applications providing a `web_search` tool have it automatically hoisted to `openrouter:web_search`, so removing the `:online` suffix preserves web search functionality as long as the application exposes the tool ^[raw/document/openrouter/openrouter-024-guides-routing-model-variants-online-2026-04-29.md]
- The `:online` suffix can be combined with `:free` as `"model:free:online"` (e.g., `"openai/gpt-oss-20b:free:online"`); using web search incurs extra costs even with free models ^[raw/document/openrouter/openrouter-039-guides-features-plugins-web-search-2026-04-29.md]

## Details

The Online variant incorporated relevant web search results into model responses, providing access to real-time information and current events beyond the model's training data. This was particularly useful for queries requiring up-to-date information.

The server tool replacement (`openrouter:web_search`) is preferred because it gives the model agency over search behavior — the model decides when and how often to search — rather than unconditionally attaching search results to every request. ^[raw/document/openrouter/openrouter-024-guides-routing-model-variants-online-2026-04-29.md]

### Migration from `:online` to Web Search Server Tool

The key differences when migrating: the server tool uses `tools: [{ type: "openrouter:web_search" }]` instead of `plugins: [{ id: "web" }]`; the model decides when/whether to search (0 to N times) instead of always searching once; engine options now include `auto` (default); domain filtering uses `allowed_domains` instead of `include_domains`; context size control uses `search_context_size` instead of `web_search_options`; and `max_total_results` caps cumulative results across all searches in a request. ^[raw/document/openrouter/openrouter-034-guides-features-server-tools-web-search-2026-04-29.md]

## Related

- [[entities/openrouter]]
- [[concepts/model_variants]]
- [[concepts/plugins]]
- [[concepts/web_search]]
- [[summaries/openrouter-guides-routing-model-variants-online]]
- [[summaries/openrouter-guides-features-server-tools-web-search]]
- [[summaries/openrouter-guides-features-plugins-web-search]]