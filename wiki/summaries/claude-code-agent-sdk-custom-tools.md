---
title: "Claude Code Agent Sdk Custom Tools"
summary: "How to define, register, and control custom tools in the Claude Agent SDK using its in-process MCP server, including input schemas, tool annotations, access control, error handling, and non-text content"
type: summary
sources:
  - raw/document/claude code/claude-code-005-agent-sdk-custom-tools-2026-04-29.md
tags:
  - agent-sdk
  - custom-tools
  - mcp
  - tool-annotations
  - error-handling
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Claude Code Agent Sdk Custom Tools

## Key Points

- Custom tools are defined with four parts — name, description, input schema, and async handler — using `@tool` (Python) or `tool()` (TypeScript), then wrapped in an in-process MCP server via `create_sdk_mcp_server`/`createSdkMcpServer` ^[raw/document/claude code/claude-code-005-agent-sdk-custom-tools-2026-04-29.md]

- In TypeScript, input schemas use Zod and the handler's `args` are typed from the schema automatically; in Python, the dict schema (`{"latitude": float}`) is converted to JSON Schema, and a full JSON Schema dict is needed for enums, ranges, optional fields, or nested objects ^[raw/document/claude code/claude-code-005-agent-sdk-custom-tools-2026-04-29.md]

- Tool names follow the pattern `mcp__{server_name}__{tool_name}` when exposed to Claude; the server name comes from the key in `mcpServers` passed to `query()` ^[raw/document/claude code/claude-code-005-agent-sdk-custom-tools-2026-04-29.md]

- The `tools` option and allowed/disallowed lists operate on separate layers: `tools` controls which built-in tools appear in Claude's context (removing unlisted ones entirely), while allowed/disallowed lists control whether tool calls are approved or denied after Claude attempts them ^[raw/document/claude code/claude-code-005-agent-sdk-custom-tools-2026-04-29.md]

- Handlers should return `isError: true` (Python: `is_error: True`) instead of throwing exceptions — uncaught exceptions stop the entire agent loop, while `isError` results let Claude react and continue ^[raw/document/claude code/claude-code-005-agent-sdk-custom-tools-2026-04-29.md]

- Tool content arrays accept `text`, `image` (base64-encoded bytes with required `mimeType`), and `resource` (content addressed by URI label) block types, following the MCP `CallToolResult` specification ^[raw/document/claude code/claude-code-005-agent-sdk-custom-tools-2026-04-29.md]

- Tool annotations are optional metadata hints — `readOnlyHint` (enables parallel calls), `destructiveHint`, `idempotentHint`, `openWorldHint` — and are descriptive, not enforced; a tool marked `readOnlyHint: true` can still write to disk if the handler does so ^[raw/document/claude code/claude-code-005-agent-sdk-custom-tools-2026-04-29.md]

## Quotes

- "Using the SDK's in-process MCP server, you can give Claude access to databases, external APIs, domain-specific logic, or any other capability your application needs." ^[raw/document/claude code/claude-code-005-agent-sdk-custom-tools-2026-04-29.md]

- "The server runs in-process inside your application, not as a separate process." ^[raw/document/claude code/claude-code-005-agent-sdk-custom-tools-2026-04-29.md]

- "Omitting a tool from `tools` removes it from context so Claude never attempts it; listing it in `disallowedTools` blocks the call but leaves the tool visible, so Claude may waste a turn trying it." ^[raw/document/claude code/claude-code-005-agent-sdk-custom-tools-2026-04-29.md]

- "Annotations are metadata, not enforcement. A tool marked `readOnlyHint: true` can still write to disk if that's what the handler does." ^[raw/document/claude code/claude-code-005-agent-sdk-custom-tools-2026-04-29.md]

## Notes

- The wildcard pattern `mcp__weather__*` can be used in `allowedTools` to cover every tool a server exposes without listing each individually ^[raw/document/claude code/claude-code-005-agent-sdk-custom-tools-2026-04-29.md]

- Every tool in a server's `tools` array consumes context window space on every turn; for dozens of tools, the source recommends using tool search to load them on demand instead ^[raw/document/claude code/claude-code-005-agent-sdk-custom-tools-2026-04-29.md]

- Optional parameters in Python are handled by omitting the parameter from the dict schema, mentioning it in the description, and reading it with `args.get()` in the handler; in TypeScript, `.default()` on the Zod field makes a parameter optional ^[raw/document/claude code/claude-code-005-agent-sdk-custom-tools-2026-04-29.md]

- Resource blocks use a URI as a label for Claude to reference later; the SDK does not read from that path — the actual content rides in the block's `text` or `blob` field ^[raw/document/claude code/claude-code-005-agent-sdk-custom-tools-2026-04-29.md]

## Related

- [[entities/agent_sdk]]
- [[concepts/custom_tools]]
- [[concepts/agent_loop]]