---
title: "Agent Teams"
summary: "Multi-instance coordination pattern where one lead session spawns and manages independent Claude Code teammates with shared tasks and inter-agent messaging"
type: concept
sources:
  - raw/document/claude code/claude-code-031-agent-teams-2026-04-29.md
  - raw/document/claude code/claude-code-052-costs-2026-04-29.md
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

# Agent Teams

A multi-agent coordination pattern in Claude Code where one session acts as team lead, spawning and managing separate Claude Code instances (teammates) that work independently on assigned tasks, communicate directly with each other, and coordinate through a shared task list and mailbox messaging system. ^[raw/document/claude code/claude-code-031-agent-teams-2026-04-29.md]

## Key Points

- Agent teams consist of a team lead, teammates, a shared task list, and a mailbox messaging system; teammates are fully independent Claude Code instances, each with their own context window ^[raw/document/claude code/claude-code-031-agent-teams-2026-04-29.md]
- Unlike [[concepts/subagents|subagents]], teammates can message each other directly and users can interact with individual teammates without going through the lead ^[raw/document/claude code/claude-code-031-agent-teams-2026-04-29.md]
- Experimental feature requiring `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` environment variable and Claude Code v2.1.32+ ^[raw/document/claude code/claude-code-031-agent-teams-2026-04-29.md]
- Two display modes: in-process (single terminal, Shift+Down to cycle) and split panes (tmux or iTerm2, one pane per teammate) ^[raw/document/claude code/claude-code-031-agent-teams-2026-04-29.md]
- Task claiming uses file locking to prevent race conditions; tasks have three states (pending, in progress, completed) and support dependencies ^[raw/document/claude code/claude-code-031-agent-teams-2026-04-29.md]
- Agent teams use approximately 7x more tokens than standard sessions when teammates run in plan mode, because each teammate maintains its own context window and runs as a separate Claude instance ^[raw/document/claude code/claude-code-052-costs-2026-04-29.md]
- Token usage scales with the number of active teammates and how long each one runs; to manage costs, use Sonnet for teammates, keep teams small, keep spawn prompts focused, and clean up teams when work is done (active teammates continue consuming tokens even if idle) ^[raw/document/claude code/claude-code-052-costs-2026-04-29.md]
- Teammates can be spawned from subagent definitions, inheriting the definition's `tools` allowlist and `model`; team coordination tools (`SendMessage`, task management) are always available regardless of `tools` restrictions ^[raw/document/claude code/claude-code-031-agent-teams-2026-04-29.md]

## Details

The team lead creates the team, spawns teammates, assigns tasks, and synthesizes results. Teammates load the same project context as a regular session (CLAUDE.md, MCP servers, skills) but do not inherit the lead's conversation history. Communication happens through automatic message delivery, idle notifications, shared task lists, and direct teammate-to-teammate messaging by name. ^[raw/document/claude code/claude-code-031-agent-teams-2026-04-29.md]

Plan approval can be required for teammates on complex or risky tasks. The teammate works in read-only plan mode until the lead approves; if rejected, the teammate revises and resubmits. The lead makes approval decisions autonomously, but users can influence judgment by providing criteria in the prompt (e.g., "only approve plans that include test coverage"). ^[raw/document/claude code/claude-code-031-agent-teams-2026-04-29.md]

Quality gates can be enforced via hooks: `TeammateIdle` fires when a teammate is about to go idle (exit code 2 sends feedback and keeps the teammate working), `TaskCreated` fires when a task is created (exit code 2 prevents creation), and `TaskCompleted` fires when a task is marked complete (exit code 2 prevents completion). ^[raw/document/claude code/claude-code-031-agent-teams-2026-04-29.md]

Best practices recommend 3-5 teammates with 5-6 tasks per teammate, starting with research and review tasks before attempting parallel implementation, avoiding file conflicts by assigning distinct file ownership per teammate, and monitoring/steering the team rather than letting it run unattended. ^[raw/document/claude code/claude-code-031-agent-teams-2026-04-29.md]

Known limitations include: no session resumption with in-process teammates, task status lag, slow shutdown (teammates finish current request before stopping), one team per session, no nested teams, fixed lead role, permissions set at spawn time (all teammates inherit the lead's mode), and split panes requiring tmux or iTerm2 (not supported in VS Code terminal, Windows Terminal, or Ghostty). ^[raw/document/claude code/claude-code-031-agent-teams-2026-04-29.md]

## Related

- [[entities/claude_code]]
- [[concepts/subagents]]
- [[concepts/hooks]]
- [[concepts/permissions]]
- [[concepts/sessions]]
- [[concepts/skills]]
- [[summaries/claude-code-agent-teams]]
- [[concepts/token_optimization]]
- [[summaries/claude-code-costs]]