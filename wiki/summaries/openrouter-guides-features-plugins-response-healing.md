---
title: "OpenRouter Response Healing Plugin"
summary: "Detailed guide for the Response Healing plugin that automatically repairs malformed JSON from LLM responses, including the types of errors it fixes and its limitations"
type: summary
sources:
  - raw/document/openrouter/openrouter-040-guides-features-plugins-response-healing-2026-04-29.md
tags:
  - openrouter
  - plugins
  - json
  - structured-output
  - response-healing
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# OpenRouter Response Healing Plugin

## Key Points

- Response Healing automatically repairs malformed JSON in LLM responses, fixing missing brackets, trailing commas, unquoted keys, markdown wrappers, and mixed text/JSON ^[raw/document/openrouter/openrouter-040-guides-features-plugins-response-healing-2026-04-29.md]
- Activates only for non-streaming requests when `response_format` uses `type: "json_schema"` or `type: "json_object"` and the plugin is included in the `plugins` array ^[raw/document/openrouter/openrouter-040-guides-features-plugins-response-healing-2026-04-29.md]
- Fixes five categories of JSON errors: missing closing brackets, markdown code block extraction, mixed text and JSON extraction, trailing comma removal, and unquoted key quoting ^[raw/document/openrouter/openrouter-040-guides-features-plugins-response-healing-2026-04-29.md]
- Cannot repair all malformed JSON — responses truncated by `max_tokens` are specifically called out as unrepairable ^[raw/document/openrouter/openrouter-040-guides-features-plugins-response-healing-2026-04-29.md]
- Works only on non-streaming requests; streaming requests are not eligible for healing ^[raw/document/openrouter/openrouter-040-guides-features-plugins-response-healing-2026-04-29.md]

## Notes

- The plugin identifier is `{ "id": "response-healing" }` in the `plugins` array
- Example usage demonstrates the plugin with `response_format.type: "json_schema"` and a `Product` schema containing `name` (string), `price` (number), and `description` (string) fields ^[raw/document/openrouter/openrouter-040-guides-features-plugins-response-healing-2026-04-29.md]

## Related

- [[entities/openrouter]]
- [[concepts/response_healing]]
- [[concepts/plugins]]
- [[concepts/structured_output]]