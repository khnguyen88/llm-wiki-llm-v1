---
title: "Custom Tools"
summary: "User-defined functions that extend the Agent SDK via an in-process MCP server, with input schemas, handlers, annotations, and access control"
type: concept
sources:
  - raw/document/claude code/claude-code-005-agent-sdk-custom-tools-2026-04-29.md
  - raw/document/claude code/claude-code-009-agent-sdk-mcp-2026-04-29.md
  - raw/document/claude code/claude-code-027-agent-sdk-tool-search-2026-04-29.md
tags:
  - agent-sdk
  - custom-tools
  - mcp
  - tool-annotations
  - error-handling
  - tool-search
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Custom Tools

User-defined functions that extend the Agent SDK by letting Claude call application-specific logic, external APIs, databases, or any domain capability during a conversation. Custom tools are defined with the SDK's `@tool` (Python) or `tool()` (TypeScript) helper and registered through an in-process MCP server. ^[raw/document/claude code/claude-code-005-agent-sdk-custom-tools-2026-04-29.md]

## Key Points

- A custom tool requires four parts: **name** (unique identifier), **description** (Claude reads this to decide when to call it), **input schema** (Zod in TypeScript, dict or JSON Schema in Python), and **handler** (async function returning `{content: [...], isError?: boolean}`) ^[raw/document/claude code/claude-code-005-agent-sdk-custom-tools-2026-04-29.md]

- Tools are bundled into an MCP server with `create_sdk_mcp_server` (Python) / `createSdkMcpServer` (TypeScript), which runs in-process inside the application, not as a separate process ^[raw/document/claude code/claude-code-005-agent-sdk-custom-tools-2026-04-29.md]

- Tool names follow the format `mcp__{server_name}__{tool_name}` when exposed to Claude; the `server_name` comes from the key used in `mcpServers` passed to `query()` ^[raw/document/claude code/claude-code-005-agent-sdk-custom-tools-2026-04-29.md]

- Error handling has two paths: returning `isError: true` lets Claude see the failure and continue (retry, try another tool, explain); an uncaught exception stops the entire agent loop ^[raw/document/claude code/claude-code-005-agent-sdk-custom-tools-2026-04-29.md]

- Tool annotations are metadata hints — `readOnlyHint` (enables parallel batching), `destructiveHint`, `idempotentHint`, `openWorldHint` — that describe behavior but do not enforce it; a handler can still perform actions contradicting its annotations ^[raw/document/claude code/claude-code-005-agent-sdk-custom-tools-2026-04-29.md]

## Details

Custom tools use the Agent SDK's in-process MCP server to give Claude access to application-specific capabilities. The server wraps one or more tool definitions and is passed to `query()` via the `mcpServers` option. Each tool consumes context window space on every turn, so for large tool sets the source recommends using tool search to load them on demand instead of listing them all upfront. ^[raw/document/claude code/claude-code-005-agent-sdk-custom-tools-2026-04-29.md]

The `tools` option and the allowed/disallowed lists operate on separate layers. `tools` controls which built-in tools appear in Claude's context — unlisted built-ins are removed entirely so Claude never attempts them. Allowed and disallowed lists control whether tool calls are approved or denied after Claude attempts them. Omitting a built-in from `tools` is preferred over listing it in `disallowedTools`, because the latter leaves the tool visible and may cause Claude to waste a turn trying it. ^[raw/document/claude code/claude-code-005-agent-sdk-custom-tools-2026-04-29.md]

Tool content arrays support three block types: `text` (plain text), `image` (base64-encoded bytes with a required `mimeType` field — no `data:` URI prefix), and `resource` (content addressed by a URI label, with the actual content in a `text` or `blob` field). Resource URIs are labels for Claude to reference; the SDK does not read from those paths. These block shapes follow the MCP `CallToolResult` type specification. ^[raw/document/claude code/claude-code-005-agent-sdk-custom-tools-2026-04-29.md]

Custom tools defined via the SDK's in-process MCP server are one of three MCP transport types. When registered through `create_sdk_mcp_server`/`createSdkMcpServer`, they appear as SDK MCP servers rather than separate processes. External MCP servers (stdio and HTTP/SSE) are configured separately via `mcpServers` in `query()` or `.mcp.json`. ^[raw/document/claude code/claude-code-009-agent-sdk-mcp-2026-04-29.md]

## Related

- [[entities/agent_sdk]]
- [[concepts/agent_loop]]
- [[concepts/skills]]
- [[concepts/mcp]]
- [[concepts/tool_search]]