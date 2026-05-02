---
title: "Structured Output"
summary: "Agent SDK feature that constrains agent responses to validated JSON schemas, enabling programmatic use of agent output with type-safe objects and automatic re-prompting on validation failure"
type: concept
sources:
  - raw/document/claude code/claude-code-024-agent-sdk-structured-outputs-2026-04-29.md
tags:
  - agent-sdk
  - structured-output
  - json-schema
  - validation
  - output
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Structured Output

A mechanism in the Agent SDK that constrains agent responses to match a defined JSON Schema, returning validated, typed data instead of free-form text. Structured outputs are configured via the `outputFormat` (TypeScript) or `output_format` (Python) option on `query()`, which accepts a JSON Schema describing the desired output shape. The SDK validates the agent's final response against the schema and re-prompts the agent if validation fails. ^[raw/document/claude code/claude-code-024-agent-sdk-structured-outputs-2026-04-29.md]

## Key Points

- The `outputFormat` / `output_format` option accepts `type: "json_schema"` with a `schema` field containing a JSON Schema object; validated data appears in `message.structured_output` on the result message ^[raw/document/claude code/claude-code-024-agent-sdk-structured-outputs-2026-04-29.md]
- Zod (TypeScript) and Pydantic (Python) can define schemas with full type inference and runtime validation, generating JSON Schema via `z.toJSONSchema()` or `.model_json_schema()` ^[raw/document/claude code/claude-code-024-agent-sdk-structured-outputs-2026-04-29.md]
- On validation success, the result message has `subtype: "success"` with populated `structured_output`; on retry exhaustion, `subtype: "error_max_structured_output_retries"` ^[raw/document/claude code/claude-code-024-agent-sdk-structured-outputs-2026-04-29.md]
- The SDK supports standard JSON Schema features including all basic types, `enum`, `const`, `required`, nested objects, and `$ref` definitions ^[raw/document/claude code/claude-code-024-agent-sdk-structured-outputs-2026-04-29.md]
- Agents can use any tools during execution and still return structured output at the end; the schema constrains only the final response shape, not the agent's tool-use behavior ^[raw/document/claude code/claude-code-024-agent-sdk-structured-outputs-2026-04-29.md]

## Details

Structured outputs solve the problem of programmatically consuming agent responses. Without them, agents return free-form text that requires manual parsing. With structured outputs, the developer defines the desired data shape up front, and the SDK ensures the final response conforms to that schema, enabling direct integration with application logic, databases, or UI components. ^[raw/document/claude code/claude-code-024-agent-sdk-structured-outputs-2026-04-29.md]

The validation-and-retry mechanism works as follows: after the agent completes its work, the SDK validates the output against the provided JSON Schema. If validation fails, the agent is re-prompted with the validation error, giving it another chance to produce conforming output. This continues until either validation succeeds (result `subtype: "success"`) or the retry limit is exhausted (result `subtype: "error_max_structured_output_retries"`). To minimize failures, schemas should be kept focused, fields that may not always be available should be optional, and prompts should clearly specify the expected output format. ^[raw/document/claude code/claude-code-024-agent-sdk-structured-outputs-2026-04-29.md]

For type safety, Zod schemas (TypeScript) and Pydantic models (Python) generate the JSON Schema automatically and provide strongly-typed objects after validation via `safeParse()` (Zod) or `model_validate()` (Pydantic). This enables autocomplete and type checking throughout the codebase. ^[raw/document/claude code/claude-code-024-agent-sdk-structured-outputs-2026-04-29.md]

## Related

- [[entities/agent_sdk]]
- [[entities/zod]]
- [[entities/pydantic]]
- [[concepts/streaming_output]]
- [[concepts/custom_tools]]
- [[concepts/agent_loop]]