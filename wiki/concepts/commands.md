---
title: "Commands"
summary: "Slash commands that control Claude Code from inside a session, providing quick access to model switching, session management, code review, permissions, and workflow automation"
type: concept
sources:
  - raw/document/claude code/claude-code-047-commands-2026-04-29.md
  - raw/document/claude code/claude-code-051-context-window-2026-04-29.md
tags:
  - claude-code
  - commands
  - cli
  - sessions
  - skills
  - context-management
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.95
provenance: extracted
---

# Commands

Slash commands control Claude Code from inside a session, providing quick access to model switching, session management, code review, permissions, and workflow automation. Type `/` to see every available command, or `/` followed by letters to filter. ^[raw/document/claude code/claude-code-047-commands-2026-04-29.md]

## Key Points

- Two command categories: built-in commands (coded into the CLI) and bundled skills (prompt-based, using the same mechanism as user-written skills) ^[raw/document/claude code/claude-code-047-commands-2026-04-29.md]
- Availability varies by platform, plan, and environment; some commands are only visible under specific conditions (e.g., /setup-bedrock requires CLAUDE_CODE_USE_BEDROCK=1, /desktop is macOS/Windows only) ^[raw/document/claude code/claude-code-047-commands-2026-04-29.md]
- Required arguments are denoted `<arg>` and optional arguments `[arg]` ^[raw/document/claude code/claude-code-047-commands-2026-04-29.md]
- MCP servers expose prompts as commands in the format `/mcp__<server>__<prompt>`, dynamically discovered from connected servers ^[raw/document/claude code/claude-code-047-commands-2026-04-29.md]
- Custom commands are created through [[concepts/skills|skills]] at `.claude/skills/<name>/SKILL.md` ^[raw/document/claude code/claude-code-047-commands-2026-04-29.md]

## Details

Built-in commands implement their behavior directly in the CLI codebase. They cover core functionality including session management (/compact, /clear, /resume, /branch), model configuration (/model, /effort, /fast), code review (/review, /ultrareview, /security-review), permissions (/permissions, /sandbox), observability (/context, /diff, /doctor, /usage), and cloud/web integration (/desktop, /teleport, /remote-control, /web-setup). Several commands have aliases: /branch (/fork), /clear (/reset, /new), /config (/settings), /resume (/continue), /remote-control (/rc), /desktop (/app). ^[raw/document/claude code/claude-code-047-commands-2026-04-29.md]

The `/context` command shows a live breakdown of context usage by category with optimization suggestions, helping identify which components consume the most tokens. ^[raw/document/claude code/claude-code-051-context-window-2026-04-29.md] The `/memory` command shows which CLAUDE.md and auto memory files loaded at startup. ^[raw/document/claude code/claude-code-051-context-window-2026-04-29.md]

Bundled skills are invoked the same way as built-in commands but execute by passing a prompt to Claude. They include /batch (large-scale change orchestration via git worktrees), /claude-api (API reference and migration), /debug (logging and troubleshooting), /fewer-permission-prompts (allowlist generation), /loop (repeated execution), and /simplify (code quality review). ^[raw/document/claude code/claude-code-047-commands-2026-04-29.md]

## Related

- [[entities/claude_code]]
- [[concepts/skills]]
- [[concepts/sessions]]
- [[concepts/context_window]]
- [[concepts/subagents]]
- [[concepts/permissions]]
- [[concepts/hooks]]
- [[concepts/mcp]]
- [[concepts/code_review]]
- [[concepts/auto_fix]]
- [[concepts/cost_tracking]]
- [[concepts/file_checkpointing]]
- [[concepts/plugins]]
- [[entities/claude_code_web]]
- [[entities/amazon_bedrock]]
- [[entities/google_vertex_ai]]
- [[entities/github]]
- [[entities/managed_agents]]