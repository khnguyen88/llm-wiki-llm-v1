---
title: "MCP (Model Context Protocol)"
summary: "An open standard for connecting AI agents to external tools and data sources, enabling database queries, API integrations, and service connections without custom tool code"
type: concept
sources:
  - raw/document/claude code/claude-code-009-agent-sdk-mcp-2026-04-29.md
  - raw/document/claude code/claude-code-039-channels-2026-04-29.md
  - raw/document/claude code/claude-code-040-channels-reference-2026-04-29.md
  - raw/document/claude code/claude-code-050-computer-use-2026-04-29.md
  - raw/document/claude code/claude-code-115-vs-code-2026-04-29.md
  - raw/document/claude code/claude-code-117-whats-new-2026-04-29.md
  - raw/document/claude code/claude-code-119-whats-new-2026-w14-2026-04-29.md
tags:
  - mcp
  - agent-sdk
  - tools
  - integration
  - protocol
  - channels
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# MCP (Model Context Protocol)

An open standard for connecting AI agents to external tools and data sources. With MCP, an agent can query databases, integrate with APIs like Slack and GitHub, and connect to other services without writing custom tool implementations. ^[raw/document/claude code/claude-code-009-agent-sdk-mcp-2026-04-29.md]

## Key Points

- MCP servers can run as local processes (stdio), connect over HTTP/SSE for remote access, or execute directly within an SDK application as in-process servers ^[raw/document/claude code/claude-code-009-agent-sdk-mcp-2026-04-29.md]
- Tool names follow the naming pattern `mcp__<server-name>__<tool-name>`; for example, a GitHub server named `"github"` with a `list_issues` tool becomes `mcp__github__list_issues` ^[raw/document/claude code/claude-code-009-agent-sdk-mcp-2026-04-29.md]
- MCP tools require explicit permission via `allowedTools` before Claude can use them; without permission, Claude sees tools are available but cannot call them ^[raw/document/claude code/claude-code-009-agent-sdk-mcp-2026-04-29.md]
- Wildcards (`*`) in `allowedTools` grant access to all tools from a specific server (e.g., `mcp__github__*`) without listing each tool individually ^[raw/document/claude code/claude-code-009-agent-sdk-mcp-2026-04-29.md]
- Tool search is enabled by default and withholds tool definitions from context, loading only the ones Claude needs for each turn, reducing context window consumption for large tool sets ^[raw/document/claude code/claude-code-009-agent-sdk-mcp-2026-04-29.md]
- The default connection timeout is 60 seconds; servers that need more startup time will fail unless pre-warmed or optimized ^[raw/document/claude code/claude-code-009-agent-sdk-mcp-2026-04-29.md]
- Channels are a specialized type of MCP server that pushes events into a running session rather than being queried on-demand; they require the `--channels` flag and are installed as plugins ^[raw/document/claude code/claude-code-039-channels-2026-04-29.md]
- Channel servers communicate over stdio transport (Claude Code spawns the server as a subprocess) and use the `@modelcontextprotocol/sdk` npm package; Node.js, Bun, and Deno runtimes are all supported ^[raw/document/claude code/claude-code-040-channels-reference-2026-04-29.md]
- Channel servers declare `capabilities.experimental['claude/channel']` to register as a channel and optionally `capabilities.experimental['claude/channel/permission']` to opt in to permission relay; two-way channels also declare `capabilities.tools: {}` ^[raw/document/claude code/claude-code-040-channels-reference-2026-04-29.md]
- `computer-use` is a built-in MCP server for screen control on macOS; disabled by default, enabled per project via `/mcp`, requires Pro/Max plan and interactive session ^[raw/document/claude code/claude-code-050-computer-use-2026-04-29.md]
- In VS Code, MCP servers are added via `claude mcp add` in the integrated terminal and managed with `/mcp` in the chat panel; the management dialog lets users enable/disable servers, reconnect, and manage OAuth authentication ^[raw/document/claude code/claude-code-115-vs-code-2026-04-29.md]
- The VS Code extension runs a built-in IDE MCP server (named `ide`, hidden from `/mcp`) that provides `mcp__ide__getDiagnostics` (read language-server errors) and `mcp__ide__executeCode` (run Jupyter cells with user confirmation); the server binds to `127.0.0.1` with per-activation random auth tokens ^[raw/document/claude code/claude-code-115-vs-code-2026-04-29.md]
- A per-tool MCP result-size override allows individual MCP tool calls to return results up to 500K, bypassing the default result size limit ^[raw/document/claude code/claude-code-117-whats-new-2026-04-29.md]
- MCP server authors can set `anthropic/maxResultSizeChars` in a tool's `_meta` field within the `tools/list` response to raise the truncation cap up to 500K characters; previously the limit was global, so tools returning inherently large payloads (database schemas, full file trees) were persisted to disk with a file reference ^[raw/document/claude code/claude-code-119-whats-new-2026-w14-2026-04-29.md]

## Details

### Transport Types

MCP servers communicate via three transport protocols. The transport type is determined by what the server's documentation provides: a command to run indicates stdio, a URL indicates HTTP or SSE, and tools defined in application code use SDK MCP servers. ^[raw/document/claude code/claude-code-009-agent-sdk-mcp-2026-04-29.md]

**stdio servers** run as local processes communicating via stdin/stdout. They are configured with a `command` and `args` array, plus an optional `env` field for environment variables. This is suitable for MCP servers running on the same machine. ^[raw/document/claude code/claude-code-009-agent-sdk-mcp-2026-04-29.md]

**HTTP/SSE servers** connect to cloud-hosted or remote MCP servers. HTTP (non-streaming) uses `"type": "http"` and SSE (streaming) uses `"type": "sse"`, both requiring a `url` field. Authentication headers are passed via the `headers` field. ^[raw/document/claude code/claude-code-009-agent-sdk-mcp-2026-04-29.md]

**SDK MCP servers** define custom tools directly in application code as in-process servers rather than separate processes, described in the custom tools documentation. ^[raw/document/claude code/claude-code-009-agent-sdk-mcp-2026-04-29.md]

### Configuration

MCP servers can be configured in two ways: inline in code via the `mcpServers` option passed to `query()`, or in a `.mcp.json` file at the project root. The `.mcp.json` file is picked up when the `project` setting source is enabled (which is the default for `query()`). If `settingSources` is set explicitly, `"project"` must be included for this file to load. ^[raw/document/claude code/claude-code-009-agent-sdk-mcp-2026-04-29.md]

### Authentication

Credentials are passed through environment variables using the `env` field for stdio servers, or through the `headers` field for HTTP/SSE servers. In `.mcp.json` files, the `${VAR_NAME}` syntax expands environment variables at runtime. The SDK does not handle OAuth flows automatically; access tokens obtained from an external OAuth flow are passed via the `Authorization` header. ^[raw/document/claude code/claude-code-009-agent-sdk-mcp-2026-04-29.md]

### Error Handling

The SDK emits a `system` message with subtype `init` at the start of each query, containing connection status for each MCP server. Servers with `status: "failed"` indicate connection problems. Common failure causes include missing environment variables, uninstalled server packages (verify `npx` commands and Node.js availability), invalid connection strings, and network reachability issues. ^[raw/document/claude code/claude-code-009-agent-sdk-mcp-2026-04-29.md]

## Related

- [[entities/agent_sdk]]
- [[entities/claude_code]]
- [[concepts/custom_tools]]
- [[concepts/agent_loop]]
- [[concepts/setting_sources]]
- [[concepts/computer_use]]
- [[concepts/channels]]
- [[entities/vs_code_extension]]
- [[concepts/ide_mcp_server]]