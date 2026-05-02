---
title: "Claude Code Commands"
summary: "Complete reference for slash commands in Claude Code, covering 50+ built-in and skill-based commands for session management, model switching, code review, permissions, and more"
type: summary
sources:
  - raw/document/claude code/claude-code-047-commands-2026-04-29.md
tags:
  - claude-code
  - commands
  - cli
  - reference
  - skills
  - sessions
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.95
provenance: extracted
---

# Claude Code Commands

## Key Points

- Claude Code provides 50+ slash commands for controlling sessions, switching models, managing permissions, running workflows, and more ^[raw/document/claude code/claude-code-047-commands-2026-04-29.md]
- Commands fall into two categories: built-in commands (coded into the CLI) and bundled skills (prompt-based, marked [Skill]) ^[raw/document/claude code/claude-code-047-commands-2026-04-29.md]
- Availability depends on platform, plan, and environment; e.g., /desktop (macOS/Windows only), /upgrade (Pro/Max), /setup-bedrock (CLAUDE_CODE_USE_BEDROCK=1) ^[raw/document/claude code/claude-code-047-commands-2026-04-29.md]
- /compact summarizes conversation history to free context (optionally with focus instructions); /clear starts a fresh conversation ^[raw/document/claude code/claude-code-047-commands-2026-04-29.md]
- /batch orchestrates large-scale changes by decomposing work into 5-30 units, each handled by a background agent in an isolated git worktree ^[raw/document/claude code/claude-code-047-commands-2026-04-29.md]
- /autofix-pr spawns a Claude Code on the Web session that watches the current branch's PR and pushes fixes for CI failures and review comments; accepts an optional prompt for custom instructions ^[raw/document/claude code/claude-code-047-commands-2026-04-29.md]
- MCP servers expose prompts as commands in the /mcp__<server>__<prompt> format, dynamically discovered from connected servers ^[raw/document/claude code/claude-code-047-commands-2026-04-29.md]

## Quotes

No notable direct quotes from this reference document.

## Notes

- Several commands have aliases: /branch (/fork), /clear (/reset, /new), /config (/settings), /resume (/continue), /remote-control (/rc), /desktop (/app), /exit (/quit), /feedback (/bug), /rewind (/checkpoint, /undo), /usage (/cost, /stats)
- /pr-comments was removed in v2.1.91; ask Claude directly to view PR comments instead
- /vim was removed in v2.1.92; use /config → Editor mode to toggle between Vim and Normal editing
- The complete documentation index is available at https://code.claude.com/docs/llms.txt

## Related

- [[concepts/commands]]
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
- [[entities/claude_code]]
- [[entities/claude_code_web]]
- [[entities/amazon_bedrock]]
- [[entities/google_vertex_ai]]
- [[entities/github]]
- [[entities/managed_agents]]