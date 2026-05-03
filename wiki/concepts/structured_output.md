---
title: "Structured Output"
summary: "Mechanism for constraining LLM responses to validated JSON schemas, enabling programmatic use of model output with type-safe objects — implemented in the Agent SDK with automatic re-prompting and on OpenRouter with JSON Schema enforcement via response_format"
type: concept
sources:
  - raw/document/claude code/claude-code-024-agent-sdk-structured-outputs-2026-04-29.md
  - raw/document/openrouter/openrouter-041-guides-features-structured-outputs-2026-04-29.md
tags:
  - agent-sdk
  - structured-output
  - json-schema
  - validation
  - output
  - openrouter
created: "2026-05-01T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: merged
---

# Structured Output

A mechanism for constraining LLM responses to match a defined JSON Schema, returning validated, type-safe data instead of free-form text. Implemented in two contexts: the Agent SDK (with automatic re-prompting on validation failure) and the OpenRouter API (with JSON Schema enforcement via `response_format`).

## Key Points

- In the Agent SDK, structured outputs are configured via the `outputFormat` / `output_format` option on `query()`, which accepts a JSON Schema describing the desired output shape; the SDK validates and re-prompts on failure ^[raw/document/claude code/claude-code-024-agent-sdk-structured-outputs-2026-04-29.md]
- On OpenRouter, structured outputs are enabled via `response_format` with `type: "json_schema"` and a `json_schema` object containing `name`, `strict`, and `schema` fields; the model returns a JSON object strictly following the provided schema ^[raw/document/openrouter/openrouter-041-guides-features-structured-outputs-2026-04-29.md]
- Zod (TypeScript) and Pydantic (Python) can define schemas with full type inference and runtime validation, generating JSON Schema via `z.toJSONSchema()` or `.model_json_schema()` ^[raw/document/claude code/claude-code-024-agent-sdk-structured-outputs-2026-04-29.md]
- On OpenRouter, supported providers include OpenAI (GPT-4o+), Google Gemini, Anthropic (Sonnet 4.5, Opus 4.1+), most open-source models, and all Fireworks-provided models ^[raw/document/openrouter/openrouter-041-guides-features-structured-outputs-2026-04-29.md]
- OpenRouter structured outputs support streaming (`stream: true`), delivering valid partial JSON that assembles into a complete schema-conformant response ^[raw/document/openrouter/openrouter-041-guides-features-structured-outputs-2026-04-29.md]
- On OpenRouter, set `strict: true` in the `json_schema` object and include clear `description` fields on schema properties as best practices ^[raw/document/openrouter/openrouter-041-guides-features-structured-outputs-2026-04-29.md]
- OpenRouter's Response Healing plugin can repair imperfect JSON formatting on non-streaming structured output requests ^[raw/document/openrouter/openrouter-041-guides-features-structured-outputs-2026-04-29.md]

## Details

### Agent SDK Implementation

Structured outputs solve the problem of programmatically consuming agent responses. Without them, agents return free-form text that requires manual parsing. With structured outputs, the developer defines the desired data shape up front, and the SDK ensures the final response conforms to that schema, enabling direct integration with application logic, databases, or UI components. ^[raw/document/claude code/claude-code-024-agent-sdk-structured-outputs-2026-04-29.md]

The validation-and-retry mechanism works as follows: after the agent completes its work, the SDK validates the output against the provided JSON Schema. If validation fails, the agent is re-prompted with the validation error, giving it another chance to produce conforming output. This continues until either validation succeeds (result `subtype: "success"`) or the retry limit is exhausted (result `subtype: "error_max_structured_output_retries"`). To minimize failures, schemas should be kept focused, fields that may not always be available should be optional, and prompts should clearly specify the expected output format. ^[raw/document/claude code/claude-code-024-agent-sdk-structured-outputs-2026-04-29.md]

For type safety, Zod schemas (TypeScript) and Pydantic models (Python) generate the JSON Schema automatically and provide strongly-typed objects after validation via `safeParse()` (Zod) or `model_validate()` (Pydantic). This enables autocomplete and type checking throughout the codebase. ^[raw/document/claude code/claude-code-024-agent-sdk-structured-outputs-2026-04-29.md]

### OpenRouter Implementation

On OpenRouter, structured outputs are configured through the `response_format` parameter in chat completion requests. The `json_schema` object requires a `name` (schema identifier), `strict: true` (ensures exact schema adherence), and a `schema` field containing the JSON Schema definition with `type`, `properties`, `required`, and `additionalProperties: false`. Two error scenarios exist: models that don't support structured outputs produce a request failure, and invalid JSON Schemas produce a validation error. ^[raw/document/openrouter/openrouter-041-guides-features-structured-outputs-2026-04-29.md]

To ensure only structured-output-capable models handle a request, check `supported_parameters` on the models page (filter: `structured_outputs`) and set `require_parameters: true` in provider preferences. ^[raw/document/openrouter/openrouter-041-guides-features-structured-outputs-2026-04-29.md]

## Related

- [[entities/agent_sdk]]
- [[entities/zod]]
- [[entities/pydantic]]
- [[entities/openrouter]]
- [[concepts/streaming_output]]
- [[concepts/custom_tools]]
- [[concepts/agent_loop]]
- [[concepts/response_healing]]
- [[concepts/provider_routing]]
- [[summaries/openrouter-guides-features-structured-outputs]]