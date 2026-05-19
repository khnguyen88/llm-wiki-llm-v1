---
title: "Claude Code Troubleshooting"
summary: "Diagnostic procedures for performance, stability, and search issues in Claude Code, including high resource usage, auto-compaction thrashing, hangs, and ripgrep configuration"
type: summary
sources:
  - raw/document/claude code/claude-code-110-troubleshooting-2026-04-29.md
tags:
  - troubleshooting
  - performance
  - diagnostics
  - claude-code
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Claude Code Troubleshooting

## Key Points

- Claude Code may consume significant resources on large codebases; use `/compact` regularly, restart between major tasks, and add large build directories to `.gitignore` ^[raw/document/claude code/claude-code-110-troubleshooting-2026-04-29.md]
- Auto-compaction thrashing occurs when a file or tool output immediately refills the context window after compaction; recover by reading files in smaller chunks, using `/compact` with a focus filter, moving large-file work to a subagent, or running `/clear` ^[raw/document/claude code/claude-code-110-troubleshooting-2026-04-29.md]
- If Claude Code hangs or freezes, press Ctrl+C to cancel; if unresponsive, close the terminal and restart with `claude --resume` to pick up the session ^[raw/document/claude code/claude-code-110-troubleshooting-2026-04-29.md]
- Search, `@file` mentions, custom agents, and custom skills failing to find files may indicate the bundled ripgrep binary is incompatible with the system; install the platform's ripgrep package and set `USE_BUILTIN_RIPGREP=0` ^[raw/document/claude code/claude-code-110-troubleshooting-2026-04-29.md]
- WSL cross-filesystem access degrades search performance; solutions include more specific searches, moving projects to the Linux filesystem (`/home/`), or running Claude Code natively on Windows ^[raw/document/claude code/claude-code-110-troubleshooting-2026-04-29.md]
- `/heapdump` writes a JavaScript heap snapshot and memory breakdown to `~/Desktop` (or home directory on Linux without Desktop); the breakdown shows resident set size, JS heap, array buffers, and unaccounted native memory ^[raw/document/claude code/claude-code-110-troubleshooting-2026-04-29.md]
- `/doctor` runs an automated check of installation, settings, MCP servers, and context usage; `claude doctor` is available from the shell when Claude Code won't start ^[raw/document/claude code/claude-code-110-troubleshooting-2026-04-29.md]

## Notes

- The troubleshooting page provides a symptom-to-page routing table directing users to specialized pages for installation issues, login/authentication errors, configuration problems, API errors, model access issues, and IDE integration problems.

## Related

- [[entities/claude_code]]
- [[concepts/troubleshooting]]
- [[concepts/context_window]]
- [[concepts/sessions]]
- [[concepts/commands]]
- [[entities/ripgrep]]