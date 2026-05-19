---
title: "Claude Code Agent SDK MCP"
summary: "Configuring MCP servers in the Agent SDK to connect agents to external tools and data sources via stdio, HTTP/SSE, or in-process transports"
type: summary
sources:
  - raw/document/claude code/claude-code-009-agent-sdk-mcp-2026-04-29.md
tags:
  - agent-sdk
  - mcp
  - tools
  - authentication
  - configuration
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Claude Code Agent SDK MCP

## Key Points

- MCP (Model Context Protocol) is an open standard for connecting AI agents to external tools and data sources without writing custom tool implementations ^[raw/document/claude code/claude-code-009-agent-sdk-mcp-2026-04-29.md]
- MCP servers are configured via the `mcpServers` option in code or in a `.mcp.json` file at the project root; the config file is loaded when the `project` setting source is enabled ^[raw/document/claude code/claude-code-009-agent-sdk-mcp-2026-04-29.md]
- MCP tools require explicit permission via `allowedTools` before Claude can use them; the naming convention is `mcp__<server-name>__<tool-name>` ^[raw/document/claude code/claude-code-009-agent-sdk-mcp-2026-04-29.md]
- Three transport types are supported: stdio (local processes via stdin/stdout), HTTP/SSE (remote cloud-hosted servers), and SDK MCP servers (in-process custom tools) ^[raw/document/claude code/claude-code-009-agent-sdk-mcp-2026-04-29.md]
- Authentication is handled via environment variables (`env` field), HTTP headers for remote servers, or OAuth2 access tokens passed in headers after completing the OAuth flow externally ^[raw/document/claude code/claude-code-009-agent-sdk-mcp-2026-04-29.md]
- Tool search is enabled by default and withholds tool definitions from context, loading only the ones Claude needs per turn to reduce context window consumption ^[raw/document/claude code/claude-code-009-agent-sdk-mcp-2026-04-29.md]
- `allowedTools` is preferred over `permissionMode: "bypassPermissions"` for MCP access because it grants exactly the needed permissions without disabling all safety prompts ^[raw/document/claude code/claude-code-009-agent-sdk-mcp-2026-04-29.md]

## Quotes

- "MCP tools require explicit permission before Claude can use them. Without permission, Claude will see that tools are available but won't be able to call them." ^[raw/document/claude code/claude-code-009-agent-sdk-mcp-2026-04-29.md]
- "Prefer `allowedTools` over permission modes for MCP access. `permissionMode: 'acceptEdits'` does not auto-approve MCP tools (only file edits and filesystem Bash commands). `permissionMode: 'bypassPermissions'` does auto-approve MCP tools but also disables all other safety prompts, which is broader than necessary." ^[raw/document/claude code/claude-code-009-agent-sdk-mcp-2026-04-29.md]

## Notes

- The default MCP connection timeout is 60 seconds; servers that take longer to start will fail to connect
- The `system` init message includes connection status for each MCP server, enabling programmatic detection of failed connections
- Environment variable expansion syntax `${VAR_NAME}` in `.mcp.json` is resolved at runtime

## Related

- [[entities/agent_sdk]]
- [[entities/claude_code]]
- [[concepts/mcp]]
- [[concepts/custom_tools]]
- [[concepts/agent_loop]]