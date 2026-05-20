---
title: "Openrouter Guides Features Structured Outputs"
summary: "OpenRouter supports structured outputs via JSON Schema, enabling models to return validated, type-safe JSON objects instead of free-form text"
type: summary
sources:
  - raw/document/openrouter/openrouter-041-guides-features-structured-outputs-2026-04-29.md
tags:
  - openrouter
  - structured-output
  - json-schema
  - api
  - streaming
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Openrouter Guides Features Structured Outputs

## Key Points

- Structured outputs enforce JSON Schema validation on model responses via the `response_format` parameter with `type: "json_schema"` and a `json_schema` object containing the schema definition ^[001a-raw/document/openrouter/openrouter-041-guides-features-structured-outputs-2026-04-29.md]
- The `json_schema` object requires three fields: `name` (schema identifier), `strict` (set to `true` for exact schema adherence), and `schema` (the JSON Schema definition with `type`, `properties`, `required`, and `additionalProperties: false`) ^[001a-raw/document/openrouter/openrouter-041-guides-features-structured-outputs-2026-04-29.md]
- Supported model providers include OpenAI (GPT-4o+), Google Gemini, Anthropic (Sonnet 4.5, Opus 4.1+), most open-source models, and all Fireworks-provided models ^[001a-raw/document/openrouter/openrouter-041-guides-features-structured-outputs-2026-04-29.md]
- Model support can be verified by checking `supported_parameters` on the models page and setting `require_parameters: true` in provider preferences to ensure only structured-output-capable models are used ^[001a-raw/document/openrouter/openrouter-041-guides-features-structured-outputs-2026-04-29.md]
- Structured outputs work with streaming responses (`stream: true`); the model streams valid partial JSON that assembles into a complete, schema-conformant response ^[001a-raw/document/openrouter/openrouter-041-guides-features-structured-outputs-2026-04-29.md]
- Two error scenarios exist: models that don't support structured outputs produce a request failure, and invalid JSON Schemas produce a schema validation error ^[001a-raw/document/openrouter/openrouter-041-guides-features-structured-outputs-2026-04-29.md]
- The [[004-wiki/concepts/response_healing|Response Healing]] plugin can be enabled for non-streaming structured output requests to repair imperfect JSON formatting from models ^[001a-raw/document/openrouter/openrouter-041-guides-features-structured-outputs-2026-04-29.md]

## Notes

- The source provides complete code examples in TypeScript SDK, Python (requests), and TypeScript (fetch) demonstrating the `response_format` parameter structure.
- Best practices from the source: include clear `description` fields on schema properties to guide the model, and always set `strict: true` to ensure exact schema adherence.

## Related

- [[004-wiki/entities/openrouter]]
- [[004-wiki/concepts/structured_output]]
- [[004-wiki/concepts/streaming_output]]
- [[004-wiki/concepts/response_healing]]
- [[004-wiki/concepts/provider_routing]]