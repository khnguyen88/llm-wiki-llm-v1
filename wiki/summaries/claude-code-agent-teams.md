---
title: "Claude Code Agent Teams"
summary: "Feature for coordinating multiple Claude Code instances as a team with shared tasks, inter-agent messaging, and centralized management"
type: summary
sources:
  - raw/document/claude code/claude-code-031-agent-teams-2026-04-29.md
tags:
  - claude-code
  - agent-teams
  - multi-agent
  - coordination
  - parallel-work
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Claude Code Agent Teams

## Key Points

- Agent teams coordinate multiple Claude Code instances: one session acts as team lead, spawning and managing teammates that work independently with their own context windows ^[raw/document/claude code/claude-code-031-agent-teams-2026-04-29.md]
- Unlike subagents, teammates communicate directly with each other and can be interacted with without going through the lead ^[raw/document/claude code/claude-code-031-agent-teams-2026-04-29.md]
- Experimental feature, disabled by default; requires `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` environment variable set to `1` and Claude Code v2.1.32+ ^[raw/document/claude code/claude-code-031-agent-teams-2026-04-29.md]
- Best use cases: parallel research/review, independent module development, debugging with competing hypotheses, and cross-layer coordination ^[raw/document/claude code/claude-code-031-agent-teams-2026-04-29.md]
- Two display modes: in-process (all teammates in one terminal, cycle with Shift+Down) and split panes (each teammate gets its own pane, requires tmux or iTerm2) ^[raw/document/claude code/claude-code-031-agent-teams-2026-04-29.md]
- Architecture consists of team lead, teammates, shared task list (with file-locking for race conditions), and mailbox messaging system ^[raw/document/claude code/claude-code-031-agent-teams-2026-04-29.md]
- Significant token consumption: each teammate has its own context window; recommended 3-5 teammates with 5-6 tasks per teammate ^[raw/document/claude code/claude-code-031-agent-teams-2026-04-29.md]

## Quotes

- "Use subagents when you need quick, focused workers that report back. Use agent teams when teammates need to share findings, challenge each other, and coordinate on their own." ^[raw/document/claude code/claude-code-031-agent-teams-2026-04-29.md]
- "Three focused teammates often outperform five scattered ones." ^[raw/document/claude code/claude-code-031-agent-teams-2026-04-29.md]

## Notes

- Agent teams have known limitations: no session resumption with in-process teammates, task status can lag, shutdown can be slow, one team per session, no nested teams, and lead is fixed for the team's lifetime
- Split-pane mode is not supported in VS Code's integrated terminal, Windows Terminal, or Ghostty
- Team config stored at `~/.claude/teams/{team-name}/config.json`; task list at `~/.claude/tasks/{team-name}/`; these are auto-generated and should not be hand-edited

## Related

- [[entities/claude_code]]
- [[concepts/agent_teams]]
- [[concepts/subagents]]
- [[concepts/hooks]]
- [[concepts/permissions]]
- [[concepts/sessions]]