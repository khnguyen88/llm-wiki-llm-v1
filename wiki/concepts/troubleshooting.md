---
title: "Troubleshooting"
summary: "Diagnostic procedures and recovery strategies for performance, stability, search, and installation issues in Claude Code"
type: concept
sources:
  - raw/document/claude code/claude-code-110-troubleshooting-2026-04-29.md
  - raw/document/claude code/claude-code-111-troubleshoot-install-2026-04-29.md
tags:
  - troubleshooting
  - diagnostics
  - performance
  - claude-code
  - installation
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: merged
---

# Troubleshooting

Diagnostic procedures for identifying and resolving performance, stability, search, and installation issues in Claude Code. The `/doctor` command provides an automated health check covering installation, settings, MCP configuration, and context usage; `claude doctor` runs the same check from the shell when Claude Code cannot start. ^[raw/document/claude code/claude-code-110-troubleshooting-2026-04-29.md] For installation and login errors specifically, see [[concepts/troubleshoot_install]].

## Key Points

- `/doctor` checks installation health, settings validity, MCP configuration, and context usage in one pass; `claude doctor` is the shell equivalent when the CLI cannot start ^[raw/document/claude code/claude-code-110-troubleshooting-2026-04-29.md]
- High resource usage can be mitigated with `/compact`, restarting between major tasks, and excluding large build directories via `.gitignore` ^[raw/document/claude code/claude-code-110-troubleshooting-2026-04-29.md]
- `/heapdump` writes a JavaScript heap snapshot and memory breakdown to `~/Desktop` (or `~/` on Linux without a Desktop folder) for diagnosing memory issues; the breakdown distinguishes JS heap growth from native memory growth ^[raw/document/claude code/claude-code-110-troubleshooting-2026-04-29.md]
- Auto-compaction thrashing means the context refilled to the limit immediately after compaction; the system stops retrying to avoid wasting API calls, and recovery requires reducing the oversized content ^[raw/document/claude code/claude-code-110-troubleshooting-2026-04-29.md]
- Search failures (missing files from Search tool, `@file`, custom agents, or custom skills) indicate the bundled ripgrep binary may be incompatible; install the platform's ripgrep package and set `USE_BUILTIN_RIPGREP=0` ^[raw/document/claude code/claude-code-110-troubleshooting-2026-04-29.md]

## Details

### High CPU or Memory Usage

Claude Code may consume significant resources when processing large codebases. The recommended mitigation sequence is: (1) use `/compact` regularly to reduce context size, (2) close and restart Claude Code between major tasks, (3) add large build directories to `.gitignore`. If memory usage remains high, `/heapdump` produces a `.heapsnapshot` file (openable in Chrome DevTools under Memory → Load) and a memory breakdown showing resident set size, JS heap, array buffers, and unaccounted native memory. Both files should be attached when reporting memory issues on GitHub. ^[raw/document/claude code/claude-code-110-troubleshooting-2026-04-29.md]

### Auto-Compaction Thrashing

When auto-compaction succeeds but a file or tool output immediately refills the context window several times in a row, Claude Code stops retrying and displays: `Autocompact is thrashing: the context refilled to the limit...`. Recovery strategies include: (1) reading oversized files in smaller chunks (specific line ranges or functions), (2) running `/compact` with a focus that drops the large output, (3) moving large-file work to a subagent running in a separate context window, or (4) running `/clear` if the earlier conversation is no longer needed. ^[raw/document/claude code/claude-code-110-troubleshooting-2026-04-29.md]

### WSL Search Performance

Disk read performance penalties when working across file systems on WSL result in fewer-than-expected search matches. `/doctor` reports Search as OK in this case. The three recommended solutions are: submit more specific searches (specify directories or file types), move the project to the Linux filesystem (`/home/`) rather than `/mnt/c/`, or run Claude Code natively on Windows instead. ^[raw/document/claude code/claude-code-110-troubleshooting-2026-04-29.md]

## Related

- [[entities/claude_code]]
- [[concepts/context_window]]
- [[concepts/commands]]
- [[concepts/sessions]]
- [[entities/ripgrep]]
- [[summaries/claude-code-troubleshooting]]
- [[concepts/troubleshoot_install]]
- [[summaries/claude-code-troubleshoot-install]]