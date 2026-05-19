---
title: "Zod"
summary: "TypeScript-first schema validation library used with the Agent SDK to define structured output schemas with full type inference and runtime validation"
type: entity
sources:
  - raw/document/claude code/claude-code-024-agent-sdk-structured-outputs-2026-04-29.md
  - raw/document/claude code/claude-code-040-channels-reference-2026-04-29.md
tags:
  - typescript
  - validation
  - schema
  - agent-sdk
  - structured-output
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: merged
---

# Zod

A TypeScript-first schema validation library that integrates with the Agent SDK for defining structured output schemas. Zod schemas generate JSON Schema via `z.toJSONSchema()` and provide runtime validation with `safeParse()`, returning fully typed objects with autocomplete and type checking support. ^[raw/document/claude code/claude-code-024-agent-sdk-structured-outputs-2026-04-29.md]

## Key Facts

- Used with the Agent SDK's `outputFormat` option to define structured output schemas in TypeScript ^[raw/document/claude code/claude-code-024-agent-sdk-structured-outputs-2026-04-29.md]
- `z.toJSONSchema()` converts a Zod schema to a JSON Schema object suitable for the `outputFormat.schema` field ^[raw/document/claude code/claude-code-024-agent-sdk-structured-outputs-2026-04-29.md]
- `safeParse()` validates the `structured_output` data at runtime, enabling type-safe access to the parsed result ^[raw/document/claude code/claude-code-024-agent-sdk-structured-outputs-2026-04-29.md]
- Supports composable, reusable schemas with features like `z.enum()` for constrained string values and `z.array()` for nested object structures ^[raw/document/claude code/claude-code-024-agent-sdk-structured-outputs-2026-04-29.md]
- `z.infer<typeof Schema>` derives TypeScript types from Zod schemas for use throughout the codebase ^[raw/document/claude code/claude-code-024-agent-sdk-structured-outputs-2026-04-29.md]
- Used in channel servers to define the `PermissionRequestSchema` for notification handler routing: `z.object({ method: z.literal('notifications/claude/channel/permission_request'), params: z.object({ request_id: z.string(), tool_name: z.string(), description: z.string(), input_preview: z.string() }) })` ^[raw/document/claude code/claude-code-040-channels-reference-2026-04-29.md]

## Related

- [[concepts/structured_output]]
- [[entities/agent_sdk]]
- [[entities/pydantic]]
- [[concepts/channels]]