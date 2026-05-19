---
title: "Claude Code Agent Sdk Slash Commands"
summary: "Slash commands in the Agent SDK control sessions via built-in commands like /compact and custom markdown-defined commands, with discovery through the system init message"
type: summary
sources:
  - raw/document/claude code/claude-code-021-agent-sdk-slash-commands-2026-04-29.md
tags:
  - agent-sdk
  - slash-commands
  - skills
  - custom-commands
  - claude-code
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Claude Code Agent Sdk Slash Commands

## Key Points

- Available slash commands are listed in the `system` init message at session start (`message.slash_commands`); only commands that work without an interactive terminal are dispatchable through the SDK ^[raw/document/claude code/claude-code-021-agent-sdk-slash-commands-2026-04-29.md]
- Slash commands are sent by including them in the prompt string (e.g. `prompt: "/compact"`), the same way as regular text ^[raw/document/claude code/claude-code-021-agent-sdk-slash-commands-2026-04-29.md]
- The `/compact` command reduces conversation history size by summarizing older messages; completion is signaled by a `system` message with `subtype: "compact_boundary"` containing `compact_metadata` with `pre_tokens` and `trigger` fields ^[raw/document/claude code/claude-code-021-agent-sdk-slash-commands-2026-04-29.md]
- The interactive `/clear` command is not available in the SDK; each `query()` call starts a fresh conversation, so ending the current call and starting a new one achieves the same effect ^[raw/document/claude code/claude-code-021-agent-sdk-slash-commands-2026-04-29.md]
- Custom slash commands are markdown files at `.claude/commands/` (legacy) or `.claude/skills/<name>/SKILL.md` (recommended); the recommended format supports both slash-command invocation and autonomous invocation by Claude ^[raw/document/claude code/claude-code-021-agent-sdk-slash-commands-2026-04-29.md]
- Custom commands support YAML frontmatter (`description`, `allowed-tools`, `model`, `argument-hint`), dynamic arguments via `$1`/`$2` placeholders, bash command execution with `` !`command` `` syntax, and file references with `@filename` prefix ^[raw/document/claude code/claude-code-021-agent-sdk-slash-commands-2026-04-29.md]
- Subdirectories in `.claude/commands/` create namespace labels (e.g. `frontend/`, `backend/`) that appear in the command description but do not affect the command name ^[raw/document/claude code/claude-code-021-agent-sdk-slash-commands-2026-04-29.md]

## Quotes

- "Only commands that work without an interactive terminal are dispatchable through the SDK; the `system/init` message lists the ones available in your session." ^[raw/document/claude code/claude-code-021-agent-sdk-slash-commands-2026-04-29.md]
- "The `.claude/commands/` directory is the legacy format. The recommended format is `.claude/skills/<name>/SKILL.md`, which supports the same slash-command invocation (`/name`) plus autonomous invocation by Claude." ^[raw/document/claude code/claude-code-021-agent-sdk-slash-commands-2026-04-29.md]

## Notes

- Personal commands at `~/.claude/commands/` (legacy) or `~/.claude/skills/` (recommended) are available across all projects; project commands are scoped to the current project ^[raw/document/claude code/claude-code-021-agent-sdk-slash-commands-2026-04-29.md]
- The `$ARGUMENTS` placeholder in custom command files captures all arguments passed after the command name ^[raw/document/claude code/claude-code-021-agent-sdk-slash-commands-2026-04-29.md]

## Related

- [[entities/agent_sdk]]
- [[concepts/skills]]
- [[concepts/custom_tools]]
- [[concepts/subagents]]