---
title: "ripgrep"
summary: "A fast regex search tool bundled with Claude Code; when the bundled binary is incompatible, users must install ripgrep separately and set USE_BUILTIN_RIPGREP=0"
type: entity
sources:
  - raw/document/claude code/claude-code-110-troubleshooting-2026-04-29.md
tags:
  - ripgrep
  - search
  - claude-code
  - tools
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# ripgrep

A fast regex-based search tool (rg) that Claude Code bundles as its default file search backend. When the bundled binary does not run on a user's system, the Search tool, `@file` mentions, custom agents, and custom skills fail to find files. ^[raw/document/claude code/claude-code-110-troubleshooting-2026-04-29.md]

## Key Facts

- Claude Code ships a bundled ripgrep binary for file search operations; if it is incompatible with the system, search functionality silently fails ^[raw/document/claude code/claude-code-110-troubleshooting-2026-04-29.md]
- To use a system-installed ripgrep instead of the bundled binary, install ripgrep via the platform package manager and set `USE_BUILTIN_RIPGREP=0` in the environment ^[raw/document/claude code/claude-code-110-troubleshooting-2026-04-29.md]
- Platform install commands: `brew install ripgrep` (macOS), `sudo apt install ripgrep` (Ubuntu/Debian), `apk add ripgrep` (Alpine), `pacman -S ripgrep` (Arch), `winget install BurntSushi.ripgrep.MSVC` (Windows) ^[raw/document/claude code/claude-code-110-troubleshooting-2026-04-29.md]
- On Alpine and musl-based distributions, ripgrep must be installed separately and `USE_BUILTIN_RIPGREP=0` must be set; the bundled binary does not work on these platforms ^[raw/document/claude code/claude-code-110-troubleshooting-2026-04-29.md]

## Related

- [[entities/claude_code]]
- [[concepts/troubleshooting]]
- [[concepts/tool_search]]