---
title: "Non-Interactive Mode"
summary: "Running Claude Code without an interactive session via claude -p for CI pipelines, pre-commit hooks, and automated workflows"
type: concept
sources:
  - raw/document/claude code/claude-code-036-best-practices-2026-04-29.md
  - raw/document/claude code/claude-code-045-cli-reference-2026-04-29.md
  - raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md
  - raw/document/claude code/claude-code-050-computer-use-2026-04-29.md
  - raw/document/claude code/claude-code-100-server-managed-settings-2026-04-29.md
tags:
  - claude-code
  - automation
  - ci
  - non-interactive
  - cli
  - print-mode
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: merged
---

# Non-Interactive Mode

Running Claude Code without an interactive session using `claude -p "prompt"`, enabling integration into CI pipelines, pre-commit hooks, and automated workflows. Output formats support programmatic parsing: plain text, JSON, and streaming JSON. ^[raw/document/claude code/claude-code-036-best-practices-2026-04-29.md]

## Key Points

- Use `claude -p "prompt"` to run Claude non-interactively without a session ^[raw/document/claude code/claude-code-036-best-practices-2026-04-29.md]
- Output formats include plain text (default), `--output-format json` for structured output, and `--output-format stream-json` for streaming JSON ^[raw/document/claude code/claude-code-036-best-practices-2026-04-29.md]
- The `--allowedTools` flag restricts what Claude can do, which matters for unattended batch operations ^[raw/document/claude code/claude-code-036-best-practices-2026-04-29.md]
- In non-interactive mode with auto mode, the classifier aborts if it repeatedly blocks actions since there is no user to fall back to ^[raw/document/claude code/claude-code-036-best-practices-2026-04-29.md]
- Can be piped into other commands: `claude -p "<prompt>" --output-format json | your_command` ^[raw/document/claude code/claude-code-036-best-practices-2026-04-29.md]
- `--output-format` accepts `text` (default), `json`, or `stream-json`; `--input-format` accepts `text` or `stream-json` for print mode ^[raw/document/claude code/claude-code-045-cli-reference-2026-04-29.md]
- `--max-budget-usd` sets a maximum dollar amount for API calls and `--max-turns` limits agentic turns; both are print-mode only and the run exits with an error when the turn limit is reached ^[raw/document/claude code/claude-code-045-cli-reference-2026-04-29.md]
- `--fallback-model` enables automatic fallback to a specified model when the default model is overloaded (print mode only) ^[raw/document/claude code/claude-code-045-cli-reference-2026-04-29.md]
- `--json-schema` constrains print-mode output to a specified JSON Schema; the agent completes its workflow and returns validated structured output (see [[concepts/structured_output]]) ^[raw/document/claude code/claude-code-045-cli-reference-2026-04-29.md]
- `--no-session-persistence` disables session saving to disk so sessions cannot be resumed (print mode only) ^[raw/document/claude code/claude-code-045-cli-reference-2026-04-29.md]
- `--init` runs Setup hooks before the session; `--maintenance` runs Setup hooks with the `maintenance` matcher; both are print-mode only ^[raw/document/claude code/claude-code-045-cli-reference-2026-04-29.md]
- `--include-partial-messages` includes streaming events in output and `--include-hook-events` includes hook lifecycle events; both require `--print` and `--output-format stream-json` ^[raw/document/claude code/claude-code-045-cli-reference-2026-04-29.md]
- `--replay-user-messages` re-emits user messages from stdin back on stdout for acknowledgment; requires `--input-format stream-json` and `--output-format stream-json` ^[raw/document/claude code/claude-code-045-cli-reference-2026-04-29.md]
- `--bare` skips auto-discovery of hooks, skills, plugins, MCP servers, auto memory, and CLAUDE.md for faster scripted startup; only Bash, Read, and Edit tools are available (see [[concepts/bare_mode]]) ^[raw/document/claude code/claude-code-045-cli-reference-2026-04-29.md]
- `--permission-prompt-tool` specifies an MCP tool to handle permission prompts in non-interactive mode ^[raw/document/claude code/claude-code-045-cli-reference-2026-04-29.md]
- Use `claude -p` as a unix-style utility: pipe data in with `cat error.txt | claude -p 'explain this'`, pipe output out with `> result.txt`, and integrate into build scripts (e.g., `"lint:claude": "claude -p 'you are a linter...'"`) ^[raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]
- Use `@` in prompts to include files or directories without waiting for Claude to read them: `claude -p 'Explain @src/utils/auth.js'` includes full file content; `@src/components` provides a directory listing; `@server:resource` fetches MCP resources ^[raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]
- Computer use (screen control) is not available in non-interactive mode; it requires an interactive session ^[raw/document/claude code/claude-code-050-computer-use-2026-04-29.md]
- In non-interactive mode with the `-p` flag, server-managed security approval dialogs for shell commands, custom environment variables, and hook configurations are skipped and settings are applied without user approval ^[raw/document/claude code/claude-code-100-server-managed-settings-2026-04-29.md]

## Details

Non-interactive mode is the primary integration point for automation. It allows Claude Code to be embedded in shell scripts, CI pipelines, and other automated workflows. The `--output-format` flag enables structured output for downstream processing. The `--allowedTools` flag is critical for safety in unattended runs: it restricts Claude's capabilities to only the tools specified, preventing unintended side effects during batch operations. ^[raw/document/claude code/claude-code-036-best-practices-2026-04-29.md]

When combining non-interactive mode with auto mode (`claude --permission-mode auto -p "prompt"`), the classifier model reviews commands before they run. If the classifier repeatedly blocks actions, the run aborts because there is no human to approve denied operations. This is a safety mechanism that prevents runaway automated processes. ^[raw/document/claude code/claude-code-036-best-practices-2026-04-29.md]

Use `--verbose` for debugging during development and disable it in production. ^[raw/document/claude code/claude-code-036-best-practices-2026-04-29.md]

## Related

- [[entities/claude_code]]
- [[concepts/auto_mode]]
- [[concepts/permissions]]
- [[concepts/parallel_sessions]]
- [[concepts/fan_out]]
- [[concepts/bare_mode]]
- [[concepts/structured_output]]
- [[summaries/claude-code-common-workflows]]
- [[concepts/computer_use]]
- [[summaries/claude-code-cli-reference]]