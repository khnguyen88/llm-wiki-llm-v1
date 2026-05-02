---
title: "Plugins"
summary: "Packages of Claude Code extensions loaded into Agent SDK sessions to add custom skills, agents, hooks, and MCP servers"
type: concept
sources:
  - raw/document/claude code/claude-code-015-agent-sdk-plugins-2026-04-29.md
  - raw/document/claude code/claude-code-039-channels-2026-04-29.md
  - raw/document/claude code/claude-code-040-channels-reference-2026-04-29.md
  - raw/document/claude code/claude-code-115-vs-code-2026-04-29.md
  - raw/document/claude code/claude-code-117-whats-new-2026-04-29.md
tags:
  - agent-sdk
  - plugins
  - extensibility
  - skills
  - hooks
  - mcp
  - channels
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Plugins

Plugins are packages of Claude Code extensions that can be shared across projects and loaded into Agent SDK sessions to add custom slash commands, agents, skills, hooks, and MCP servers. ^[raw/document/claude code/claude-code-015-agent-sdk-plugins-2026-04-29.md]

## Key Points

- Plugins contain four types of extensions: skills (model-invoked capabilities), agents (specialized subagents), hooks (event handlers), and MCP servers (external tool integrations) ^[raw/document/claude code/claude-code-015-agent-sdk-plugins-2026-04-29.md]
- Plugins are loaded via the `plugins` option in `query()` with `type: "local"` and a filesystem path; the SDK only accepts local paths, not remote or marketplace references ^[raw/document/claude code/claude-code-015-agent-sdk-plugins-2026-04-29.md]
- Plugin skills are automatically namespaced as `plugin-name:skill-name` when invoked as slash commands to prevent naming conflicts between plugins ^[raw/document/claude code/claude-code-015-agent-sdk-plugins-2026-04-29.md]
- A plugin directory must contain a `.claude-plugin/plugin.json` manifest file at its root ^[raw/document/claude code/claude-code-015-agent-sdk-plugins-2026-04-29.md]
- The `commands/` directory is a legacy format; new plugins should use `skills/` instead ^[raw/document/claude code/claude-code-015-agent-sdk-plugins-2026-04-29.md]
- Channel plugins are MCP servers that push external events into a running session; they are installed via `/plugin install` (e.g., `telegram@claude-plugins-official`), activated with `/reload-plugins`, and enabled per session with `claude --channels plugin:<name>@<marketplace>` ^[raw/document/claude code/claude-code-039-channels-2026-04-29.md]
- Channel plugins published to a marketplace still require `--dangerously-load-development-channels` during the research preview unless they are on the Anthropic allowlist; to get added, submit the plugin to the official marketplace for security review ^[raw/document/claude code/claude-code-040-channels-reference-2026-04-29.md]
- On Team and Enterprise plans, admins can use `allowedChannelPlugins` to replace the default Anthropic allowlist entirely with an organization-specific list of approved channel plugins ^[raw/document/claude code/claude-code-040-channels-reference-2026-04-29.md]

## Details

Plugin paths can be relative (resolved from the current working directory) or absolute. The path must point to the plugin root directory containing `.claude-plugin/plugin.json`. Multiple plugins from different locations can be loaded in a single session. ^[raw/document/claude code/claude-code-015-agent-sdk-plugins-2026-04-29.md]

Successful plugin loading is verified through the system init message (`message.type === "system" && message.subtype === "init"`), which exposes `message.plugins` (loaded plugin list) and `message.slash_commands` (available commands including namespaced plugin skills). ^[raw/document/claude code/claude-code-015-agent-sdk-plugins-2026-04-29.md]

The plugin directory structure includes `.claude-plugin/plugin.json` (required), and optional `skills/`, `commands/` (legacy), `agents/`, `hooks/`, and `.mcp.json` directories/files. Each skill must have its own subdirectory under `skills/` with a `SKILL.md` file (e.g., `skills/my-skill/SKILL.md`). ^[raw/document/claude code/claude-code-015-agent-sdk-plugins-2026-04-29.md]

- In the VS Code extension, `/plugins` opens a graphical dialog with Plugins (installed/available with search and toggle switches) and Marketplaces (add/remove sources) tabs; plugins installed from the extension use the same CLI commands under the hood and configurations are shared ^[raw/document/claude code/claude-code-115-vs-code-2026-04-29.md]
- VS Code plugin installation offers three scopes: "Install for you" (user scope, all projects), "Install for this project" (project scope, shared with collaborators), "Install locally" (local scope, only you, only this repository) ^[raw/document/claude code/claude-code-115-vs-code-2026-04-29.md]
- Plugin marketplaces in VS Code accept GitHub repos, URLs, or local paths; clicking the refresh icon updates the plugin list and the trash icon removes a marketplace; changes prompt a Claude Code restart ^[raw/document/claude code/claude-code-115-vs-code-2026-04-29.md]
- Plugin executables are available on the Bash tool's PATH, allowing plugin-provided commands to be invoked directly from shell commands ^[raw/document/claude code/claude-code-117-whats-new-2026-04-29.md]
- Plugins can contribute custom themes that appear in the `/theme` list alongside built-in presets and user-created themes ^[raw/document/claude code/claude-code-117-whats-new-2026-04-29.md]

## Related

- [[entities/agent_sdk]]
- [[entities/vs_code_extension]]
- [[concepts/skills]]
- [[concepts/hooks]]
- [[concepts/mcp]]
- [[concepts/subagents]]
- [[concepts/setting_sources]]
- [[concepts/channels]]