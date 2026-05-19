---
title: "Claude Code Tools Reference"
summary: "Comprehensive reference for Claude Code's 30+ built-in tools, their permission requirements, and specific behaviors for Bash, LSP, Monitor, and PowerShell"
type: summary
sources:
  - raw/document/claude code/claude-code-109-tools-reference-2026-04-29.md
tags:
  - claude-code
  - tools
  - permissions
  - reference
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Claude Code Tools Reference

## Key Points

- Claude Code provides 30+ built-in tools; tool names are the exact strings used in permission rules, subagent tool lists, and hook matchers; tools requiring explicit permission are Bash, Edit, ExitPlanMode, Monitor, NotebookEdit, PowerShell, Skill, WebFetch, WebSearch, and Write; all others operate without prompting ^[raw/document/claude code/claude-code-109-tools-reference-2026-04-29.md]

- To disable a tool entirely, add its name to the `deny` array in permission settings; to add custom tools, connect an MCP server; skills extend Claude through the existing Skill tool rather than adding new tool entries ^[raw/document/claude code/claude-code-109-tools-reference-2026-04-29.md]

- The Bash tool persists working directory changes across commands within the project directory (or additional working directories via `--add-dir`), but environment variables do not persist between commands; use `CLAUDE_ENV_FILE` or a SessionStart hook for persistent env vars, or `CLAUDE_BASH_MAINTAIN_PROJECT_WORKING_DIR=1` to disable directory carry-over ^[raw/document/claude code/claude-code-109-tools-reference-2026-04-29.md]

- The LSP tool provides code intelligence (jump to definition, find references, type information, symbol listing, implementation finding, call hierarchy tracing) but is inactive until a code intelligence plugin is installed for the target language ^[raw/document/claude code/claude-code-109-tools-reference-2026-04-29.md]

- The Monitor tool (v2.1.98+) runs background scripts and feeds each output line to Claude mid-conversation; not available on Amazon Bedrock, Google Vertex AI, or Microsoft Foundry, or when `DISABLE_TELEMETRY` or `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` is set ^[raw/document/claude code/claude-code-109-tools-reference-2026-04-29.md]

- The PowerShell tool runs commands natively on Windows instead of routing through Git Bash; auto-enabled on Windows without Git Bash, progressively rolling out on Windows with Git Bash, and opt-in on Linux/macOS/WSL via `CLAUDE_CODE_USE_POWERSHELL_TOOL=1` ^[raw/document/claude code/claude-code-109-tools-reference-2026-04-29.md]

- CronCreate, CronDelete, and CronList manage session-scoped scheduled prompts; tasks are restored on `--resume` or `--continue` if unexpired ^[raw/document/claude code/claude-code-109-tools-reference-2026-04-29.md]

## Quotes

> To disable a tool entirely, add its name to the `deny` array in your permission settings. To add custom tools, connect an MCP server. To extend Claude with reusable prompt-based workflows, write a skill, which runs through the existing `Skill` tool rather than adding a new tool entry. ^[raw/document/claude code/claude-code-109-tools-reference-2026-04-29.md]

> The LSP tool is inactive until you install a code intelligence plugin for your language. The plugin bundles the language server configuration, and you install the server binary separately. ^[raw/document/claude code/claude-code-109-tools-reference-2026-04-29.md]

> The Monitor tool lets Claude watch something in the background and react when it changes, without pausing the conversation. ^[raw/document/claude code/claude-code-109-tools-reference-2026-04-29.md]

## Notes

- Agent team tools (SendMessage, TeamCreate, TeamDelete) require `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`
- TodoWrite is used in non-interactive mode and the Agent SDK; interactive sessions use TaskCreate/TaskGet/TaskList/TaskUpdate instead
- TaskOutput is deprecated in favor of reading the task's output file path
- EnterWorktree and ExitWorktree are not available to subagents
- The exact tool set available depends on provider, platform, and settings; ask Claude directly or run `/mcp` for MCP tool names

## Related

- [[entities/claude_code]]
- [[concepts/permissions]]
- [[concepts/lsp_tool]]
- [[concepts/monitor_tool]]
- [[concepts/powershell_tool]]
- [[concepts/scheduled_tasks]]
- [[concepts/tool_search]]
- [[concepts/subagents]]
- [[concepts/mcp]]
- [[concepts/skills]]
- [[concepts/worktrees]]
- [[concepts/agent_teams]]