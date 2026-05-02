---
title: "Claude Code CLI Reference"
summary: "Complete reference for Claude Code CLI commands and flags, covering session management, non-interactive mode, system prompt customization, permission control, and configuration options"
type: summary
sources:
  - raw/document/claude code/claude-code-045-cli-reference-2026-04-29.md
tags:
  - cli
  - claude-code
  - commands
  - flags
  - reference
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.95
provenance: extracted
---

# Claude Code CLI Reference

## Key Points

- Claude Code provides commands for session management (`claude`, `claude -p`, `claude -c`, `claude -r`), authentication (`claude auth login/logout/status`), updates (`claude update`, `claude install`), and subcommands for agents, MCP, and plugins ^[raw/document/claude code/claude-code-045-cli-reference-2026-04-29.md]
- The `--print` / `-p` flag enables non-interactive mode for scripting and CI, with output formats (`text`, `json`, `stream-json`), cost limits (`--max-budget-usd`), turn limits (`--max-turns`), and structured output (`--json-schema`) ^[raw/document/claude code/claude-code-045-cli-reference-2026-04-29.md]
- Four system prompt flags control customization: `--system-prompt` and `--system-prompt-file` replace the default prompt; `--append-system-prompt` and `--append-system-prompt-file` add to it; append flags can combine with replacement flags ^[raw/document/claude code/claude-code-045-cli-reference-2026-04-29.md]
- Permission modes are set via `--permission-mode` (accepts `default`, `acceptEdits`, `plan`, `auto`, `dontAsk`, `bypassPermissions`); `--allowedTools` pre-approves specific tools, `--disallowedTools` removes tools from context ^[raw/document/claude code/claude-code-045-cli-reference-2026-04-29.md]
- Bare mode (`--bare`) strips auto-discovery for faster scripted startup: no hooks, skills, plugins, MCP servers, auto memory, or CLAUDE.md; only Bash, Read, and Edit tools available ^[raw/document/claude code/claude-code-045-cli-reference-2026-04-29.md]
- Session management flags include `--continue` / `-c` (resume most recent), `--resume` / `-r` (resume by ID or name), `--fork-session` (branch a resumed session), `--name` / `-n` (display name), `--session-id` (UUID), and `--from-pr` (resume sessions linked to a PR) ^[raw/document/claude code/claude-code-045-cli-reference-2026-04-29.md]
- If a subcommand is mistyped, Claude Code suggests the closest match and exits without starting a session (e.g., `claude udpate` suggests `claude update`) ^[raw/document/claude code/claude-code-045-cli-reference-2026-04-29.md]

## Quotes

> "claude --help does not list every flag, so a flag's absence from --help does not mean it is unavailable." ^[raw/document/claude code/claude-code-045-cli-reference-2026-04-29.md]

> "For most use cases, use an append flag. Appending preserves Claude Code's built-in capabilities while adding your requirements. Use a replacement flag only when you need complete control over the system prompt." ^[raw/document/claude code/claude-code-045-cli-reference-2026-04-29.md]

## Notes

- The `--exclude-dynamic-system-prompt-sections` flag moves per-machine context (working directory, environment info, memory paths, git status) from the system prompt into the first user message, improving prompt-cache reuse across different users and machines ^[raw/document/claude code/claude-code-045-cli-reference-2026-04-29.md]
- `--fallback-model` enables automatic model fallback when the default model is overloaded (print mode only) ^[raw/document/claude code/claude-code-045-cli-reference-2026-04-29.md]
- `--effort` accepts `low`, `medium`, `high`, `xhigh`, or `max`; available levels depend on the model and the setting is session-scoped ^[raw/document/claude code/claude-code-045-cli-reference-2026-04-29.md]

## Related

- [[entities/claude_code]]
- [[concepts/non_interactive_mode]]
- [[concepts/sessions]]
- [[concepts/system_prompt]]
- [[concepts/permissions]]
- [[concepts/subagents]]
- [[concepts/bare_mode]]
- [[concepts/channels]]
- [[concepts/plugins]]
- [[concepts/mcp]]
- [[concepts/structured_output]]
- [[concepts/parallel_sessions]]