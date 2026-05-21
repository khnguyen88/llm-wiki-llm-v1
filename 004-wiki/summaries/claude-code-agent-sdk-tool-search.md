---
title: "Claude Code Agent Sdk Tool Search"
summary: "Tool search lets the Agent SDK dynamically discover and load tools on demand instead of injecting all tool definitions into context, enabling agents to scale to thousands of tools"
type: summary
sources:
  - raw/document/claude code/claude-code-027-agent-sdk-tool-search-2026-04-29.md
tags:
  - agent-sdk
  - tool-search
  - context-window
  - mcp
  - custom-tools
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Claude Code Agent Sdk Tool Search

## Key Points

- Tool search withholds tool definitions from the context window and provides a summary of available tools; the agent searches for relevant ones on demand, loading 3-5 at a time ^[001a-raw/document/claude code/claude-code-027-agent-sdk-tool-search-2026-04-29.md]
- Tool search solves two scaling problems: context efficiency (50 tools can consume 10-20K tokens) and tool selection accuracy (degrades with more than 30-50 tools loaded at once) ^[001a-raw/document/claude code/claude-code-027-agent-sdk-tool-search-2026-04-29.md]
- Tool search adds one extra round-trip on first discovery but offsets this with smaller context on every turn for large tool sets; with fewer than ~10 tools, loading everything upfront is typically faster ^[001a-raw/document/claude code/claude-code-027-agent-sdk-tool-search-2026-04-29.md]
- When the SDK compacts earlier messages to free space, previously discovered tools may be removed and the agent searches again as needed ^[001a-raw/document/claude code/claude-code-027-agent-sdk-tool-search-2026-04-29.md]
- Controlled via `ENABLE_TOOL_SEARCH` environment variable: unset/`true` (always on), `auto` (activates when tools exceed 10% of context), `auto:N` (custom percentage), `false` (off, all tools loaded) ^[001a-raw/document/claude code/claude-code-027-agent-sdk-tool-search-2026-04-29.md]
- Tool search applies to all registered tools whether from remote MCP servers or custom SDK MCP servers ^[001a-raw/document/claude code/claude-code-027-agent-sdk-tool-search-2026-04-29.md]
- Requires Claude Sonnet 4 or later, or Claude Opus 4 or later; Haiku models do not support tool search ^[001a-raw/document/claude code/claude-code-027-agent-sdk-tool-search-2026-04-29.md]

## Quotes

- "Tool definitions can consume large portions of the context window (50 tools can use 10-20K tokens), leaving less room for actual work." ^[001a-raw/document/claude code/claude-code-027-agent-sdk-tool-search-2026-04-29.md]

- "Names like `search_slack_messages` surface for a wider range of requests than `query_slack`. Descriptions with specific keywords ('Search Slack messages by keyword, channel, or date range') match more queries than generic ones ('Query Slack')." ^[001a-raw/document/claude code/claude-code-027-agent-sdk-tool-search-2026-04-29.md]

## Notes

- The `auto:N` threshold is based on the combined size of all tool definitions across all servers, not per-server ^[001a-raw/document/claude code/claude-code-027-agent-sdk-tool-search-2026-04-29.md]

- The search mechanism matches queries against tool names and descriptions; adding a system prompt section listing available tool categories improves discoverability ^[001a-raw/document/claude code/claude-code-027-agent-sdk-tool-search-2026-04-29.md]

## Related

- [[004-wiki/entities/agent-sdk]]
- [[004-wiki/concepts/tool-search]]
- [[004-wiki/concepts/context-window]]
- [[004-wiki/concepts/custom-tools]]
- [[004-wiki/concepts/mcp]]