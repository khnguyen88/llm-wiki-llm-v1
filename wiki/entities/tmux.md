---
title: "tmux"
summary: "Terminal multiplexer that requires specific configuration for Claude Code features like Shift+Enter and desktop notifications to work correctly inside its sessions"
type: entity
sources:
  - raw/document/claude code/claude-code-107-terminal-config-2026-04-29.md
tags:
  - terminal
  - multiplexer
  - configuration
  - claude-code
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# tmux

A terminal multiplexer that, by default, breaks two Claude Code features: Shift+Enter (which submits instead of inserting a newline) and desktop notifications plus the progress bar (which never reach the outer terminal). ^[raw/document/claude code/claude-code-107-terminal-config-2026-04-29.md]

## Key Facts

- Three settings in `~/.tmux.conf` are required for Claude Code: `set -g allow-passthrough on` (lets notifications and progress reach the outer terminal), `set -s extended-keys on`, and `set -as terminal-features 'xterm*:extkeys'` (both let tmux distinguish Shift+Enter from plain Enter) ^[raw/document/claude code/claude-code-107-terminal-config-2026-04-29.md]
- After modifying `~/.tmux.conf`, run `tmux source-file ~/.tmux.conf` to apply changes to the running server ^[raw/document/claude code/claude-code-107-terminal-config-2026-04-29.md]
- Shift+Enter inside tmux requires the `extended-keys` and `terminal-features` settings even when the outer terminal supports Shift+Enter natively ^[raw/document/claude code/claude-code-107-terminal-config-2026-04-29.md]
- The `allow-passthrough` setting enables escape sequences from Claude Code to pass through tmux to the outer terminal (iTerm2, Ghostty, or Kitty) for notifications and progress updates ^[raw/document/claude code/claude-code-107-terminal-config-2026-04-29.md]
- `/terminal-setup` should be run in the host terminal rather than inside tmux, since it needs to write to the host terminal's configuration ^[raw/document/claude code/claude-code-107-terminal-config-2026-04-29.md]

## Related

- [[concepts/terminal_config]]
- [[entities/claude_code]]
- [[summaries/claude-code-terminal-config]]