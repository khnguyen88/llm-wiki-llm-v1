---
title: "Web Search"
summary: "An OpenRouter server tool (`openrouter:web_search`) that gives any model real-time web information with configurable engines, domain filtering, and cost controls"
type: concept
sources:
  - raw/document/openrouter/openrouter-034-guides-features-server-tools-web-search-2026-04-29.md
  - raw/document/openrouter/openrouter-039-guides-features-plugins-web-search-2026-04-29.md
tags:
  - openrouter
  - server-tools
  - web-search
  - search-engine
  - domain-filtering
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
provenance: merged
confidence: 0.9
provenance: extracted
---

# Web Search

The `openrouter:web_search` server tool gives any model on OpenRouter access to real-time web information. When the model determines it needs current information, it calls the tool with a search query; OpenRouter executes the search and returns results (URLs, titles, and content snippets) that the model uses to formulate a grounded, cited response. ^[raw/document/openrouter/openrouter-034-guides-features-server-tools-web-search-2026-04-29.md]

## Key Points

- Enabled by including `{ "type": "openrouter:web_search" }` in the `tools` array; the model decides when and whether to search, and may search multiple times in a single request ^[raw/document/openrouter/openrouter-034-guides-features-server-tools-web-search-2026-04-29.md]
- Five engine options: `auto` (default, uses native provider search or falls back to Exa), `native` (forces provider's built-in search), `exa` (Exa's keyword + embeddings search), `firecrawl` (BYOK, uses your Firecrawl credits), and `parallel` (Parallel's search API) ^[raw/document/openrouter/openrouter-034-guides-features-server-tools-web-search-2026-04-29.md]
- Configuration parameters: `engine`, `max_results` (1–25, default 5), `max_total_results` (caps cumulative results across all searches in a request), `search_context_size` (`low`/`medium`/`high`), `allowed_domains`, `excluded_domains`, and `user_location` ^[raw/document/openrouter/openrouter-034-guides-features-server-tools-web-search-2026-04-29.md]
- Domain filtering behavior varies by engine: Exa supports both `allowed_domains` and `excluded_domains` simultaneously; Parallel supports both but they are mutually exclusive; Firecrawl returns an error if domain filters are set; native providers vary ^[raw/document/openrouter/openrouter-034-guides-features-server-tools-web-search-2026-04-29.md]
- Usage is tracked in the response `usage.server_tool_use.web_search_requests` field ^[raw/document/openrouter/openrouter-034-guides-features-server-tools-web-search-2026-04-29.md]
- The deprecated `web` plugin always runs exactly once per request, unlike the server tool where the model decides when/whether to search; the plugin uses `include_domains`/`exclude_domains` (vs. `allowed_domains`/`excluded_domains` in the server tool) and supports a `search_prompt` parameter for customizing how results are attached ^[raw/document/openrouter/openrouter-039-guides-features-plugins-web-search-2026-04-29.md]
- Web search results for all models (including native-only providers) are standardized in the API response via the `message.annotations` array using `url_citation` type with `url`, `title`, `content`, `start_index`, and `end_index` fields ^[raw/document/openrouter/openrouter-039-guides-features-plugins-web-search-2026-04-29.md]
- The plugin's `engine` parameter accepts `"native"`, `"exa"`, `"firecrawl"`, `"parallel"`, or `undefined` (default: native when available, Exa fallback); the server tool adds `"auto"` as the default instead of `undefined` ^[raw/document/openrouter/openrouter-039-guides-features-plugins-web-search-2026-04-29.md]
- xAI models with web search enabled automatically receive an `x_search` tool alongside `web_search`, controlled by the top-level `x_search_filter` parameter with `allowed_x_handles`, `excluded_x_handles` (mutually exclusive, max 10 each), `from_date`, `to_date`, `enable_image_understanding`, and `enable_video_understanding` ^[raw/document/openrouter/openrouter-039-guides-features-plugins-web-search-2026-04-29.md]

## Details

### Engine Capabilities

| Feature | Exa | Firecrawl | Parallel | Native |
|---------|-----|-----------|----------|--------|
| Domain filtering | Yes (both simultaneously) | No (returns error) | Yes (mutually exclusive) | Varies by provider |
| Context size control | Yes (per result) | No | Yes (total across results) | No |
| API key | Server-side | BYOK (your key) | Server-side | Provider-handled |

`user_location` biases results geographically but is only supported by native provider search; it is ignored by Exa, Firecrawl, and Parallel. ^[raw/document/openrouter/openrouter-034-guides-features-server-tools-web-search-2026-04-29.md]

### Controlling Total Results

`max_total_results` caps the cumulative number of results across all search calls in a single request. Once the limit is reached, subsequent search calls return a message telling the model the limit was hit instead of performing another search. This is useful for controlling cost and context window usage in agentic loops. ^[raw/document/openrouter/openrouter-034-guides-features-server-tools-web-search-2026-04-29.md]

### Migration from Web Search Plugin

The web search plugin (`plugins: [{ id: "web" }]`) and `:online` model variant are deprecated. The server tool replaces both with key differences: the model decides when/whether to search (vs. always searching once), supports 0 to N calls per request, offers `max_total_results` for cost control, and uses `search_context_size` instead of `web_search_options`. ^[raw/document/openrouter/openrouter-034-guides-features-server-tools-web-search-2026-04-29.md]

### Web Search Result Format

All web search results (including native-only providers like Perplexity and OpenAI Online) are standardized by OpenRouter in the API response via the `message.annotations` array using the `url_citation` type. Each annotation includes: `url` (source URL), `title` (page title), `content` (search result content, added by OpenRouter if available), `start_index` (character index where the citation begins in the message), and `end_index` (character index where the citation ends). This follows the OpenAI Chat Completion Message type schema. ^[raw/document/openrouter/openrouter-039-guides-features-plugins-web-search-2026-04-29.md]

### Plugin Configuration (Deprecated)

The deprecated `web` plugin accepts these configuration parameters: `id` (`"web"`), `engine` (`"native"`, `"exa"`, `"firecrawl"`, `"parallel"`, or undefined for default behavior), `max_results` (defaults to 5), `search_prompt` (custom prompt text for attaching results), `include_domains` (whitelist), and `exclude_domains` (blacklist). The default search prompt instructs the model to cite sources using markdown links named by domain. ^[raw/document/openrouter/openrouter-039-guides-features-plugins-web-search-2026-04-29.md]

### Domain Filtering Differences

Domain filtering behavior varies between the plugin and server tool, and across engines. In the plugin, `include_domains` and `exclude_domains` accept wildcards (`*.substack.com`) and path filtering (`openai.com/blog`). Engine compatibility:

| Engine | `include_domains` | `exclude_domains` | Notes |
|--------|:-:|:-:|-------|
| **Exa** | Yes | Yes | Both can be used simultaneously |
| **Parallel** | Yes | Yes | Mutually exclusive |
| **Native** | Varies | Varies | See provider-specific notes |
| **Firecrawl** | No | No | Returns 400 if domain filters are set |

Native provider behavior for domain filters: Anthropic supports both but mutually exclusively; OpenAI supports `include_domains` only (silently ignores `exclude_domains`); xAI supports both but mutually exclusively with a 5-domain maximum. ^[raw/document/openrouter/openrouter-039-guides-features-plugins-web-search-2026-04-29.md]

### X Search Filters (xAI)

When using xAI models with web search, OpenRouter automatically adds the `x_search` tool alongside `web_search`. The top-level `x_search_filter` parameter controls X/Twitter search results with: `allowed_x_handles` (max 10, mutually exclusive with `excluded_x_handles`), `excluded_x_handles` (max 10), `from_date` and `to_date` (ISO 8601 date strings), `enable_image_understanding` (boolean), and `enable_video_understanding` (boolean). If validation fails, the filter is silently dropped and a basic `x_search` tool is used instead. ^[raw/document/openrouter/openrouter-039-guides-features-plugins-web-search-2026-04-29.md]

### Pricing

Exa and Parallel both cost $4 per 1,000 results using OpenRouter credits. Firecrawl uses your Firecrawl credits directly with no OpenRouter charge. Native provider pricing is passed through from the underlying provider. All pricing is in addition to standard LLM token costs. ^[raw/document/openrouter/openrouter-034-guides-features-server-tools-web-search-2026-04-29.md]

For the deprecated plugin, native search pricing is controlled via `web_search_options.search_context_size` (`low`, `medium`, `high`), which determines how much search data is retrieved. Refer to each provider's documentation for native pricing: OpenAI, Anthropic, Perplexity, and xAI each have their own pricing. Exa search in the plugin costs $4 per 1,000 results (default 5 results = max $0.02/request) using OpenRouter credits. ^[raw/document/openrouter/openrouter-039-guides-features-plugins-web-search-2026-04-29.md]

## Related

- [[entities/openrouter]]
- [[entities/exa]]
- [[entities/firecrawl]]
- [[entities/parallel]]
- [[concepts/server_tools]]
- [[concepts/online_variant]]
- [[concepts/tool_calling]]
- [[summaries/openrouter-guides-features-server-tools-web-search]]
- [[summaries/openrouter-guides-features-plugins-web-search]]