---
title: "OpenRouter Plugins Overview"
summary: "OpenRouter plugins extend model capabilities by injecting or mutating requests/responses; they always run once when enabled, unlike server tools which the model invokes 0-N times"
type: summary
sources:
  - raw/document/openrouter/openrouter-038-guides-features-plugins-overview-2026-04-29.md
tags:
  - openrouter
  - plugins
  - response-healing
  - context-compression
  - pdf
  - web-search
  - api
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# OpenRouter Plugins Overview

## Key Points

- Plugins extend model capabilities by injecting or mutating requests or responses, running exactly once per request when enabled — distinct from server tools, which the model calls 0-N times ^[raw/document/openrouter/openrouter-038-guides-features-plugins-overview-2026-04-29.md]
- Four plugins are available: Web Search (deprecated, replaced by `openrouter:web_search` server tool), PDF Inputs, Response Healing (auto-fixes malformed JSON), and Context Compression (middle-out truncation for prompts exceeding context windows) ^[raw/document/openrouter/openrouter-038-guides-features-plugins-overview-2026-04-29.md]
- Plugins are enabled via a `plugins` array in the chat completions request body, each identified by `id` with optional configuration parameters (e.g., `{ "id": "web", "max_results": 3 }`) ^[raw/document/openrouter/openrouter-038-guides-features-plugins-overview-2026-04-29.md]
- Multiple plugins can be enabled in a single request by adding multiple objects to the `plugins` array ^[raw/document/openrouter/openrouter-038-guides-features-plugins-overview-2026-04-29.md]
- Organization admins and individual users can configure default plugin settings via the Plugins settings page, including a "Prevent overrides" option that enforces org-wide policies ^[raw/document/openrouter/openrouter-038-guides-features-plugins-overview-2026-04-29.md]
- Plugin precedence: request-level settings override account defaults, unless "Prevent overrides" is enabled for the plugin in account settings ^[raw/document/openrouter/openrouter-038-guides-features-plugins-overview-2026-04-29.md]
- A default plugin can be disabled per-request by passing `{ "id": "web", "enabled": false }` in the `plugins` array ^[raw/document/openrouter/openrouter-038-guides-features-plugins-overview-2026-04-29.md]
- The `:online` model variant suffix is a deprecated shortcut for the `web` plugin; use the `openrouter:web_search` server tool instead ^[raw/document/openrouter/openrouter-038-guides-features-plugins-overview-2026-04-29.md]

## Quotes

> Plugins always run once when enabled. Unlike server tools (which the model can call 0-N times), plugins always run once when enabled. ^[raw/document/openrouter/openrouter-038-guides-features-plugins-overview-2026-04-29.md:7]

> When "Prevent overrides" is enabled for a plugin, individual API requests cannot disable or modify that plugin's configuration. This is useful for enforcing organization-wide policies. ^[raw/document/openrouter/openrouter-038-guides-features-plugins-overview-2026-04-29.md:60]

## Notes

- The Web Search plugin is deprecated; the `openrouter:web_search` server tool is the replacement, giving the model control over when and how often to search
- Plugin IDs used in examples: `web` (Web Search), `response-healing` (Response Healing)
- The source document demonstrates plugin configuration in TypeScript, Python, and cURL

## Related

- [[entities/openrouter]]
- [[concepts/plugins]]
- [[concepts/response_healing]]
- [[concepts/context_compression]]
- [[concepts/server_tools]]
- [[concepts/model_variants]]
- [[concepts/pdf_input]]
- [[concepts/web_search]]
- [[concepts/structured_output]]