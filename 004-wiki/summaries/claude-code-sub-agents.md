---
title: "Claude Code Sub Agents"
summary: "Comprehensive guide to defining, configuring, and using specialized subagents in Claude Code CLI — including built-in agents, YAML frontmatter configuration, tool restriction, MCP scoping, persistent memory, hooks, forked subagents, and best practices for context management"
type: summary
sources:
  - raw/document/claude code/claude-code-106-sub-agents-2026-04-29.md
tags:
  - subagents
  - claude-code
  - delegation
  - context-management
  - hooks
  - permissions
  - forking
  - agent-configuration
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Claude Code Sub Agents

## Key Points

- Subagents run in their own context window with a custom system prompt, specific tool access, and independent permissions, returning only a summary to the main conversation ^[raw/document/claude code/claude-code-106-sub-agents-2026-04-29.md]
- Built-in subagents include Explore (Haiku, read-only), Plan (inherits model, read-only), General-purpose (inherits model, all tools), statusline-setup (Sonnet), and Claude Code Guide (Haiku) ^[raw/document/claude code/claude-code-106-sub-agents-2026-04-29.md]
- Subagent scope priority: managed settings (1, highest), `--agents` CLI flag (2), `.claude/agents/` project (3), `~/.claude/agents/` user (4), plugin agents/ (5, lowest) ^[raw/document/claude code/claude-code-106-sub-agents-2026-04-29.md]
- YAML frontmatter fields include `name`, `description`, `tools`, `disallowedTools`, `model`, `permissionMode`, `maxTurns`, `skills`, `mcpServers`, `hooks`, `memory`, `background`, `effort`, `isolation`, `color`, and `initialPrompt` ^[raw/document/claude code/claude-code-106-sub-agents-2026-04-29.md]
- Model resolution order: `CLAUDE_CODE_SUBAGENT_MODEL` env var → per-invocation `model` parameter → subagent definition's `model` frontmatter → main conversation's model ^[raw/document/claude code/claude-code-106-sub-agents-2026-04-29.md]
- Forked subagents (experimental, v2.1.117+) inherit the full conversation so far instead of starting fresh, sharing the parent's prompt cache for cheaper context reuse ^[raw/document/claude code/claude-code-106-sub-agents-2026-04-29.md]
- Three invocation patterns: natural language (Claude decides delegation), @-mention (guaranteed delegation for one task), `--agent` flag or `agent` setting (entire session uses that subagent's configuration) ^[raw/document/claude code/claude-code-106-sub-agents-2026-04-29.md]
- Persistent memory (`memory` field) gives subagents a directory that survives across conversations, with `user`, `project`, and `local` scope options ^[raw/document/claude code/claude-code-106-sub-agents-2026-04-29.md]

## Quotes

- "Use one when a side task would flood your main conversation with search results, logs, or file contents you won't reference again: the subagent does that work in its own context and returns only the summary." ^[raw/document/claude code/claude-code-106-sub-agents-2026-04-29.md]
- "A fork is a subagent that inherits the entire conversation so far instead of starting fresh. This drops the input isolation that subagents otherwise provide: a fork sees the same system prompt, tools, model, and message history as the main session, so you can hand it a side task without re-explaining the situation." ^[raw/document/claude code/claude-code-106-sub-agents-2026-04-29.md]
- "Subagents cannot spawn other subagents. If your workflow requires nested delegation, use Skills or chain subagents from the main conversation." ^[raw/document/claude code/claude-code-106-sub-agents-2026-04-29.md]

## Notes

- Plugin subagents do not support `hooks`, `mcpServers`, or `permissionMode` frontmatter fields for security reasons; these fields are ignored when loading agents from a plugin ^[raw/document/claude code/claude-code-106-sub-agents-2026-04-29.md]
- The `/agents` command provides a tabbed interface for managing subagents; the Library tab supports creation with guided setup or Claude generation ^[raw/document/claude code/claude-code-106-sub-agents-2026-04-29.md]
- Subagents support auto-compaction using the same logic as the main conversation, defaulting at ~95% capacity and configurable via `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` ^[raw/document/claude code/claude-code-106-sub-agents-2026-04-29.md]
- `disallowedTools` is applied before `tools` resolution; a tool listed in both is removed ^[raw/document/claude code/claude-code-106-sub-agents-2026-04-29.md]
- `isolation: worktree` gives a subagent an isolated git worktree copy; the worktree is automatically cleaned up if the subagent makes no changes ^[raw/document/claude code/claude-code-106-sub-agents-2026-04-29.md]
- `initialPrompt` is auto-submitted as the first user turn when an agent runs as the main session agent via `--agent` or the `agent` setting ^[raw/document/claude code/claude-code-106-sub-agents-2026-04-29.md]

## Related

- [[concepts/subagents]]
- [[concepts/subagent_forking]]
- [[concepts/hooks]]
- [[concepts/permissions]]
- [[concepts/skills]]
- [[concepts/mcp]]
- [[concepts/agent_teams]]
- [[concepts/worktrees]]
- [[entities/claude_code]]