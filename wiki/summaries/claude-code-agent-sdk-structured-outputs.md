---
title: "Claude Code Agent Sdk Structured Outputs"
summary: "Agent SDK feature for returning validated JSON from agent workflows using JSON Schema, Zod, or Pydantic schemas with automatic re-prompting on validation failure"
type: summary
sources:
  - raw/document/claude code/claude-code-024-agent-sdk-structured-outputs-2026-04-29.md
tags:
  - agent-sdk
  - structured-output
  - json-schema
  - zod
  - pydantic
  - validation
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Claude Code Agent Sdk Structured Outputs

## Key Points

- Structured outputs let developers define the exact shape of data they want back from an agent via JSON Schema, with the SDK validating output against the schema and re-prompting on mismatch ^[raw/document/claude code/claude-code-024-agent-sdk-structured-outputs-2026-04-29.md]
- The `outputFormat` (TypeScript) / `output_format` (Python) option accepts a JSON Schema object; validated data appears in `message.structured_output` on the result message ^[raw/document/claude code/claude-code-024-agent-sdk-structured-outputs-2026-04-29.md]
- Zod (TypeScript) and Pydantic (Python) can define schemas with full type inference and runtime validation, then generate JSON Schema via `z.toJSONSchema()` or `.model_json_schema()` ^[raw/document/claude code/claude-code-024-agent-sdk-structured-outputs-2026-04-29.md]
- If validation fails within the retry limit, the result message has `subtype: "error_max_structured_output_retries"` instead of `"success"` ^[raw/document/claude code/claude-code-024-agent-sdk-structured-outputs-2026-04-29.md]
- The SDK supports standard JSON Schema features: all basic types, `enum`, `const`, `required`, nested objects, and `$ref` definitions ^[raw/document/claude code/claude-code-024-agent-sdk-structured-outputs-2026-04-29.md]
- Schemas should stay focused and match the task; making fields optional when information may be unavailable reduces validation failures ^[raw/document/claude code/claude-code-024-agent-sdk-structured-outputs-2026-04-29.md]
- Agents can use any tools during execution and still return structured output at the end — the schema constrains only the final response shape ^[raw/document/claude code/claude-code-024-agent-sdk-structured-outputs-2026-04-29.md]

## Quotes

> "Agents return free-form text by default, which works for chat but not when you need to use the output programmatically." ^[raw/document/claude code/claude-code-024-agent-sdk-structured-outputs-2026-04-29.md]

> "Keep schemas focused. Deeply nested schemas with many required fields are harder to satisfy. Start simple and add complexity as needed." ^[raw/document/claude code/claude-code-024-agent-sdk-structured-outputs-2026-04-29.md]

## Notes

- The TODO tracking agent example demonstrates structured outputs with multi-step tool use: the agent autonomously uses Grep and Bash tools, then returns a single structured response with optional fields for data that may not exist ^[raw/document/claude code/claude-code-024-agent-sdk-structured-outputs-2026-04-29.md]
- For full JSON Schema limitations, the source refers to the Anthropic platform documentation on structured outputs ^[raw/document/claude code/claude-code-024-agent-sdk-structured-outputs-2026-04-29.md]

## Related

- [[entities/agent_sdk]]
- [[concepts/structured_output]]
- [[entities/zod]]
- [[entities/pydantic]]
- [[concepts/streaming_output]]
- [[concepts/custom_tools]]