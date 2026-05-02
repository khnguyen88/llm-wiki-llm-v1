---
title: "Tool Search"
summary: "A mechanism that dynamically discovers and loads only relevant tools on demand, enabling agents to scale to thousands of tools without overwhelming the context window; in the CLI, the ToolSearch tool provides this capability when tool search is enabled"
type: concept
sources:
  - raw/document/claude code/claude-code-027-agent-sdk-tool-search-2026-04-29.md
  - raw/document/claude code/claude-code-109-tools-reference-2026-04-29.md
tags:
  - agent-sdk
  - tool-search
  - context-window
  - mcp
  - cli
created: "2026-05-01T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: merged
---

# Tool Search

A mechanism in the Agent SDK that withholds tool definitions from the context window and provides the agent with a summary of available tools. When the agent needs a capability not already loaded, it searches the tool catalog and the 3-5 most relevant tools are injected into context for subsequent turns. ^[raw/document/claude code/claude-code-027-agent-sdk-tool-search-2026-04-29.md]

## Key Points

- Tool search is enabled by default; it can be controlled via the `ENABLE_TOOL_SEARCH` environment variable set in the `env` option on `query()` ^[raw/document/claude code/claude-code-027-agent-sdk-tool-search-2026-04-29.md]

- The `auto` mode compares the combined token count of all tool definitions against the model's context window; if they exceed 10%, tool search activates, otherwise all tools load normally ^[raw/document/claude code/claude-code-027-agent-sdk-tool-search-2026-04-29.md]

- Tool search adds one extra round-trip the first time a tool is discovered, but for large tool sets this is offset by smaller context on every turn ^[raw/document/claude code/claude-code-027-agent-sdk-tool-search-2026-04-29.md]

- When context compaction removes earlier messages, previously discovered tools may be removed and the agent searches again as needed ^[raw/document/claude code/claude-code-027-agent-sdk-tool-search-2026-04-29.md]

- The search mechanism matches queries against tool names and descriptions; descriptive names (e.g., `search_slack_messages`) and specific descriptions improve discoverability ^[raw/document/claude code/claude-code-027-agent-sdk-tool-search-2026-04-29.md]

## Details

Tool search addresses two challenges that emerge as tool libraries grow. First, tool definitions consume context window space — 50 tools can use 10-20K tokens, leaving less room for actual work. Second, tool selection accuracy degrades with more than 30-50 tools loaded at once. By withholding definitions and loading only what is needed, tool search keeps context efficient and selection accurate even with thousands of tools. ^[raw/document/claude code/claude-code-027-agent-sdk-tool-search-2026-04-29.md]

The `ENABLE_TOOL_SEARCH` variable accepts five values: unset or `true` (always on, default), `auto` (activates when tool definitions exceed 10% of the context window), `auto:N` (custom percentage threshold), and `false` (disables search, loads all definitions). When using `auto`, the threshold is based on the combined size of all tool definitions across all MCP servers. The variable is set in the `env` option on `query()`. ^[raw/document/claude code/claude-code-027-agent-sdk-tool-search-2026-04-29.md]

Tool search requires Claude Sonnet 4 or later, or Claude Opus 4 or later; Haiku models do not support it. The catalog supports up to 10,000 tools, and each search returns 3-5 of the most relevant results. ^[raw/document/claude code/claude-code-027-agent-sdk-tool-search-2026-04-29.md]

In the Claude Code CLI, tool search is accessible through the **ToolSearch** built-in tool, which searches for and loads deferred tools when tool search is enabled. The ToolSearch tool does not require explicit permission. ^[raw/document/claude code/claude-code-109-tools-reference-2026-04-29.md]

## Related

- [[entities/agent_sdk]]
- [[concepts/context_window]]
- [[concepts/custom_tools]]
- [[concepts/mcp]]