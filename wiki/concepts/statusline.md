---
title: "Statusline"
summary: "A customizable status bar in Claude Code that runs a user-defined shell script receiving JSON session data on stdin and displays the script's stdout output at the bottom of the terminal"
type: concept
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

# Statusline

A customizable status bar at the bottom of Claude Code that runs any shell script the user configures, receiving JSON session data on stdin and displaying whatever the script prints to stdout. It provides a persistent, at-a-glance view of context usage, costs, git status, and other session metrics. ^[raw/document/claude code/claude-code-105-statusline-2026-04-29.md]

## Key Points

- Configured via the `statusLine` field in `~/.claude/settings.json` (user) or project settings, with `type: "command"` and a `command` pointing to a script path or inline shell command ^[raw/document/claude code/claude-code-105-statusline-2026-04-29.md]
- The `/statusline` command accepts natural language descriptions and auto-generates a script file in `~/.claude/`, updating settings automatically ^[raw/document/claude code/claude-code-105-statusline-2026-04-29.md]
- Updates trigger after each assistant message, permission mode change, or vim mode toggle, debounced at 300ms; in-flight executions are cancelled when new updates arrive ^[raw/document/claude code/claude-code-105-statusline-2026-04-29.md]
- Optional `refreshInterval` re-runs the command every N seconds (minimum 1) to keep time-based or externally-sourced data current during idle periods ^[raw/document/claude code/claude-code-105-statusline-2026-04-29.md]
- Scripts can output multiple lines (each `echo`/`print` produces a separate row), ANSI escape codes for terminal colors, and OSC 8 escape sequences for clickable hyperlinks ^[raw/document/claude code/claude-code-105-statusline-2026-04-29.md]
- The `hideVimModeIndicator` field suppresses the built-in `-- INSERT --` text below the prompt when the script renders `vim.mode` itself ^[raw/document/claude code/claude-code-105-statusline-2026-04-29.md]
- The `subagentStatusLine` setting renders custom row bodies for subagents in the agent panel, receiving all visible subagent rows as a single JSON object on stdin ^[raw/document/claude code/claude-code-105-statusline-2026-04-29.md]

## Details

### How It Works

Claude Code runs the configured script and pipes JSON session data to it via stdin. The script reads the JSON, extracts the fields it needs, and prints text to stdout. Claude Code displays whatever the script prints. The status line runs locally and does not consume API tokens. It temporarily hides during autocomplete suggestions, the help menu, and permission prompts. ^[raw/document/claude code/claude-code-105-statusline-2026-04-29.md]

Update triggers can go quiet when the main session is idle (e.g., while a coordinator waits on background subagents). Setting `refreshInterval` ensures time-based or externally-sourced segments stay current during idle periods. ^[raw/document/claude code/claude-code-105-statusline-2026-04-29.md]

### Available JSON Data

The JSON input includes fields for: model (`model.id`, `model.display_name`), workspace (`workspace.current_dir`, `workspace.project_dir`, `workspace.added_dirs`, `workspace.git_worktree`), cost (`cost.total_cost_usd`, `cost.total_duration_ms`, `cost.total_api_duration_ms`, `cost.total_lines_added`, `cost.total_lines_removed`), context window (`context_window.total_input_tokens`, `context_window.total_output_tokens`, `context_window.context_window_size`, `context_window.used_percentage`, `context_window.remaining_percentage`, `context_window.current_usage`), effort level, thinking state, rate limits, session metadata, vim mode, agent name, and worktree details. Several fields may be absent depending on session state. ^[raw/document/claude code/claude-code-105-statusline-2026-04-29.md]

### Context Window Fields

The `context_window` object provides two tracking approaches: cumulative totals (`total_input_tokens`, `total_output_tokens`) for session-wide consumption, and `current_usage` for the most recent API call's token counts (`input_tokens`, `output_tokens`, `cache_creation_input_tokens`, `cache_read_input_tokens`). The `used_percentage` field is calculated from input tokens only (`input_tokens + cache_creation_input_tokens + cache_read_input_tokens`), excluding `output_tokens`. `current_usage` is `null` before the first API call. ^[raw/document/claude code/claude-code-105-statusline-2026-04-29.md]

### Rate Limit Fields

The `rate_limits` object contains `five_hour` (5-hour rolling window) and `seven_day` (weekly) windows, each providing `used_percentage` (0-100) and `resets_at` (Unix epoch seconds). This field only appears for Claude.ai subscribers (Pro/Max) after the first API response. Each window may be independently absent; use `jq -r '.rate_limits.five_hour.used_percentage // empty'` to handle absence gracefully. ^[raw/document/claude code/claude-code-105-statusline-2026-04-29.md]

### Caching Slow Operations

Scripts run frequently during active sessions. Commands like `git status` or `git diff` can be slow in large repositories. The recommended pattern caches git information to a temp file using `session_id` (stable per session, unique across sessions) as the cache key, refreshing only when the cache is older than a configurable threshold (e.g., 5 seconds). Process-based identifiers like `$$` or `os.getpid()` change on every invocation and defeat caching. ^[raw/document/claude code/claude-code-105-statusline-2026-04-29.md]

### Windows Configuration

On Windows, commands run through Git Bash when available, or through PowerShell when Git Bash is absent. PowerShell scripts are invoked via `powershell -NoProfile -File <path>`. ^[raw/document/claude code/claude-code-105-statusline-2026-04-29.md]

### Subagent Status Lines

The `subagentStatusLine` setting renders a custom row body for each subagent shown in the agent panel below the prompt. The command runs once per refresh tick with all visible subagent rows passed as a single JSON object on stdin, including base hook fields plus `columns` and a `tasks` array with `id`, `name`, `type`, `status`, `description`, `label`, `startTime`, `tokenCount`, `tokenSamples`, and `cwd`. Write one JSON line to stdout per row to override, using `{"id": "<task id>", "content": "<row body>"}`. Omit a task's `id` to keep default rendering; emit empty `content` to hide it. ^[raw/document/claude code/claude-code-105-statusline-2026-04-29.md]

## Related

- [[entities/claude_code]]
- [[concepts/context_window]]
- [[concepts/cost_tracking]]
- [[concepts/rate_limiting]]
- [[concepts/subagents]]
- [[concepts/sessions]]
- [[concepts/hooks]]
- [[summaries/claude-code-statusline]]