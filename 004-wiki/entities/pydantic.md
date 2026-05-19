---
title: "Pydantic"
summary: "Python data validation library used with the Agent SDK to define structured output schemas with type hints and runtime validation via model_json_schema()"
type: entity
sources:
  - raw/document/claude code/claude-code-024-agent-sdk-structured-outputs-2026-04-29.md
tags:
  - python
  - validation
  - schema
  - agent-sdk
  - structured-output
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Pydantic

A Python data validation library that integrates with the Agent SDK for defining structured output schemas. Pydantic models generate JSON Schema via `.model_json_schema()` and provide runtime validation with `model_validate()`, returning objects with full type hints. ^[raw/document/claude code/claude-code-024-agent-sdk-structured-outputs-2026-04-29.md]

## Key Facts

- Used with the Agent SDK's `output_format` option to define structured output schemas in Python ^[raw/document/claude code/claude-code-024-agent-sdk-structured-outputs-2026-04-29.md]
- `.model_json_schema()` converts a Pydantic model to a JSON Schema object suitable for the `output_format` schema field ^[raw/document/claude code/claude-code-024-agent-sdk-structured-outputs-2026-04-29.md]
- `model_validate()` validates the `structured_output` data at runtime, enabling type-safe access to parsed results ^[raw/document/claude code/claude-code-024-agent-sdk-structured-outputs-2026-04-29.md]
- Supports composable schemas with features like `enum` constrained values and nested model structures ^[raw/document/claude code/claude-code-024-agent-sdk-structured-outputs-2026-04-29.md]
- Provides better error messages than raw JSON Schema validation when structured output validation fails ^[raw/document/claude code/claude-code-024-agent-sdk-structured-outputs-2026-04-29.md]

## Related

- [[concepts/structured_output]]
- [[entities/agent_sdk]]
- [[entities/zod]]