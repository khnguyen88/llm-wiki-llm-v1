---
title: "Claude Code Agent Sdk Plugins"
summary: "How to load and use plugins in the Agent SDK to extend Claude Code with custom skills, agents, hooks, and MCP servers"
type: summary
sources:
  - raw/document/claude code/claude-code-015-agent-sdk-plugins-2026-04-29.md
tags:
  - agent-sdk
  - plugins
  - skills
  - extensibility
  - local-plugins
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Claude Code Agent Sdk Plugins

## Key Points

- Plugins are packages of Claude Code extensions that can include skills, agents, hooks, and MCP servers ^[raw/document/claude code/claude-code-015-agent-sdk-plugins-2026-04-29.md]
- Plugins are loaded programmatically via the `plugins` option in `query()`, requiring `type: "local"` and a filesystem path; the SDK does not accept remote or marketplace plugins directly ^[raw/document/claude code/claude-code-015-agent-sdk-plugins-2026-04-29.md]
- Plugin skills are namespaced with `plugin-name:skill-name` format when invoked as slash commands to avoid conflicts between plugins ^[raw/document/claude code/claude-code-015-agent-sdk-plugins-2026-04-29.md]
- A plugin directory must contain `.claude-plugin/plugin.json`; optional directories include `skills/`, `agents/`, `hooks/`, and `.mcp.json` ^[raw/document/claude code/claude-code-015-agent-sdk-plugins-2026-04-29.md]
- The `commands/` directory is a legacy format; use `skills/` for new plugins ^[raw/document/claude code/claude-code-015-agent-sdk-plugins-2026-04-29.md]
- Plugin loading is verified through the system init message, which exposes `message.plugins` and `message.slash_commands` ^[raw/document/claude code/claude-code-015-agent-sdk-plugins-2026-04-29.md]
- Path specifications support both relative (resolved from CWD) and absolute paths, and multiple plugins can be loaded from different locations simultaneously ^[raw/document/claude code/claude-code-015-agent-sdk-plugins-2026-04-29.md]

## Quotes

> "The `commands/` directory is a legacy format. Use `skills/` for new plugins." ^[raw/document/claude code/claude-code-015-agent-sdk-plugins-2026-04-29.md]

## Notes

- The SDK only accepts `type: "local"` for plugin loading; remote or marketplace plugins must be downloaded first and referenced by local path
- CLI-installed plugins (via `/plugin install`) can be reused in the SDK by providing their installation path from `~/.claude/plugins/`

## Related

- [[entities/agent_sdk]]
- [[concepts/plugins]]
- [[concepts/skills]]
- [[concepts/hooks]]
- [[concepts/mcp]]
- [[concepts/subagents]]