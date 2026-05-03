---
title: "Response Healing"
summary: "An OpenRouter plugin that automatically fixes malformed JSON responses from LLMs"
type: concept
sources:
  - raw/document/openrouter/openrouter-038-guides-features-plugins-overview-2026-04-29.md
  - raw/document/openrouter/openrouter-040-guides-features-plugins-response-healing-2026-04-29.md
tags:
  - openrouter
  - plugins
  - json
  - structured-output
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: merged
---

# Response Healing

An OpenRouter plugin that automatically fixes malformed JSON responses from LLMs. It is enabled by adding `{ "id": "response-healing" }` to the `plugins` array in a chat completions request. ^[raw/document/openrouter/openrouter-038-guides-features-plugins-overview-2026-04-29.md]

## Key Points

- Response Healing is one of four OpenRouter plugins; it runs exactly once per request when enabled, unlike server tools which the model invokes 0-N times ^[raw/document/openrouter/openrouter-038-guides-features-plugins-overview-2026-04-29.md]
- Enabled via the `plugins` array with `{ "id": "response-healing" }` ^[raw/document/openrouter/openrouter-038-guides-features-plugins-overview-04-29.md]
- Can be combined with other plugins in a single request, such as the web search plugin ^[raw/document/openrouter/openrouter-038-guides-features-plugins-overview-2026-04-29.md]
- Can be configured as a default plugin in account settings and optionally enforced with "Prevent overrides" ^[raw/document/openrouter/openrouter-038-guides-features-plugins-overview-2026-04-29.md]
- Activates only for non-streaming requests when `response_format` uses `type: "json_schema"` or `type: "json_object"` and the plugin is included in the `plugins` array ^[raw/document/openrouter/openrouter-040-guides-features-plugins-response-healing-2026-04-29.md]
- Fixes five categories of JSON errors: missing closing brackets, markdown code block extraction, mixed text/JSON extraction, trailing comma removal, and unquoted key quoting ^[raw/document/openrouter/openrouter-040-guides-features-plugins-response-healing-2026-04-29.md]
- Cannot repair all malformed JSON; responses truncated by `max_tokens` are specifically unrepairable ^[raw/document/openrouter/openrouter-040-guides-features-plugins-response-healing-2026-04-29.md]
- Only applies to non-streaming requests ^[raw/document/openrouter/openrouter-040-guides-features-plugins-response-healing-2026-04-29.md]

## Details

Response Healing is particularly useful when using `response_format` with `json_schema` to request structured JSON output, as LLMs can sometimes produce malformed JSON that fails parsing. The plugin intercepts the response and repairs JSON syntax errors before returning the result to the caller.

The plugin handles these specific repair categories: missing closing brackets (e.g., `{"name": "Alice"` → `{"name": "Alice"}`), extraction of JSON from markdown code blocks (e.g., `` ```json\n{...}\n``` ``), extraction of JSON mixed with surrounding text, removal of trailing commas (e.g., `{"name": "David",}` → `{"name": "David"}`), and quoting of unquoted JavaScript-style keys (e.g., `{name: "Eve"}` → `{"name": "Eve"}`). ^[raw/document/openrouter/openrouter-040-guides-features-plugins-response-healing-2026-04-29.md]

## Related

- [[entities/openrouter]]
- [[concepts/plugins]]
- [[concepts/structured_output]]
- [[summaries/openrouter-guides-features-plugins-overview]]
- [[summaries/openrouter-guides-features-plugins-response-healing]]