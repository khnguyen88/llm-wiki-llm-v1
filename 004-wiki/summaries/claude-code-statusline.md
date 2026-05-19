---
title: "Claude Code Statusline"
summary: "Customizable status bar at the bottom of Claude Code that runs a user-defined shell script receiving JSON session data on stdin and displaying the script's stdout output"
type: summary
sources:
  - raw/document/claude code/claude-code-105-statusline-2026-04-29.md
tags:
  - statusline
  - claude-code
  - terminal-ui
  - configuration
  - context-window
  - cost-tracking
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Claude Code Statusline

## Key Points

- The status line is a customizable bar at the bottom of Claude Code that runs any shell script configured by the user, receiving JSON session data on stdin and displaying whatever the script prints to stdout ^[raw/document/claude code/claude-code-105-statusline-2026-04-29.md]
- Configured via `statusLine` field in `~/.claude/settings.json` (user) or project settings, with `type: "command"` and a `command` path or inline shell command ^[raw/document/claude code/claude-code-105-statusline-2026-04-29.md]
- The `/statusline` command accepts natural language descriptions and auto-generates a script file in `~/.claude/` with settings updated automatically ^[raw/document/claude code/claude-code-105-statusline-2026-04-29.md]
- Updates are triggered after each assistant message, permission mode change, or vim mode toggle, debounced at 300ms; a `refreshInterval` setting adds periodic re-runs for time-based data ^[raw/document/claude code/claude-code-105-statusline-2026-04-29.md]
- Scripts can output multiple lines, ANSI escape codes for colors, and OSC 8 escape sequences for clickable hyperlinks ^[raw/document/claude code/claude-code-105-statusline-2026-04-29.md]
- JSON data includes model info, workspace paths, cost/duration tracking, context window usage, rate limits, session metadata, vim mode, effort level, thinking state, and worktree details ^[raw/document/claude code/claude-code-105-statusline-2026-04-29.md]
- A separate `subagentStatusLine` setting renders custom row bodies for subagents in the agent panel, receiving all visible subagent rows as a single JSON object on stdin ^[raw/document/claude code/claude-code-105-statusline-2026-04-29.md]

## Notes

- The status line runs locally and does not consume API tokens
- It temporarily hides during autocomplete suggestions, the help menu, and permission prompts
- On Windows, commands run through Git Bash when available, or PowerShell otherwise; PowerShell scripts are invoked via `powershell -NoProfile -File`
- Process-based identifiers (`$$`, `os.getpid()`, `process.pid`) change on every invocation and defeat caching; use `session_id` from JSON input for stable cache keys
- The `hideVimModeIndicator` field suppresses the built-in `-- INSERT --` text when the script renders `vim.mode` itself

## Related

- [[entities/claude_code]]
- [[concepts/statusline]]
- [[concepts/context_window]]
- [[concepts/cost_tracking]]
- [[concepts/rate_limiting]]
- [[concepts/subagents]]
- [[concepts/sessions]]