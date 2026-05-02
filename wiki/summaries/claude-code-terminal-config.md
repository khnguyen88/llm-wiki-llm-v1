---
title: "Claude Code Terminal Config"
summary: "How to configure terminal emulators, keybindings, themes, notifications, tmux, and Vim mode for Claude Code"
type: summary
sources:
  - raw/document/claude code/claude-code-107-terminal-config-2026-04-29.md
tags:
  - claude-code
  - terminal
  - configuration
  - themes
  - vim
  - tmux
  - notifications
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Claude Code Terminal Config

## Key Points

- Shift+Enter inserts a newline in most terminals; in VS Code, Alacritty, Zed, Cursor, and Windsurf, run `/terminal-setup` once to enable it; Windows Terminal and gnome-terminal do not support Shift+Enter and require Ctrl+J or `\` then Enter ^[raw/document/claude code/claude-code-107-terminal-config-2026-04-29.md]
- macOS Option key must be configured as Meta (Esc+) in terminal settings for Claude Code shortcuts like Option+Enter and Option+P to work ^[raw/document/claude code/claude-code-107-terminal-config-2026-04-29.md]
- Desktop notifications work natively in Ghostty, Kitty, and iTerm2; other terminals require a Notification hook configured in `settings.json` ^[raw/document/claude code/claude-code-107-terminal-config-2026-04-29.md]
- Tmux requires `allow-passthrough on`, `extended-keys on`, and `terminal-features 'xterm*:extkeys'` in `~/.tmux.conf` for notifications and Shift+Enter to work ^[raw/document/claude code/claude-code-107-terminal-config-2026-04-29.md]
- Custom themes are JSON files in `~/.claude/themes/` with `name`, `base` (preset to extend), and `overrides` (color token map); supports `#rrggbb`, `#rgb`, `rgb(r,g,b)`, `ansi256(n)`, and `ansi:<name>` color values ^[raw/document/claude code/claude-code-107-terminal-config-2026-04-29.md]
- Fullscreen rendering mode (`/tui fullscreen` or `CLAUDE_CODE_NO_FLICKER=1`) draws to a separate screen buffer to fix flicker and scroll jumps ^[raw/document/claude code/claude-code-107-terminal-config-2026-04-29.md]
- Vim editor mode enables hjkl navigation, visual selection, and text objects in the prompt input; Enter still submits in INSERT mode, use `o`/`O` or Ctrl+J for newlines ^[raw/document/claude code/claude-code-107-terminal-config-2026-04-29.md]

## Quotes

- "Claude Code works in any terminal without configuration. This page is for when something specific is not behaving the way you expect." ^[raw/document/claude code/claude-code-107-terminal-config-2026-04-29.md]

## Notes

- The source distinguishes terminal configuration (sending the right signals to Claude Code) from keybindings (which keys Claude Code itself responds to), pointing to the keybindings page for the latter
- Pasting over 10,000 characters collapses to a `[Pasted text]` placeholder; the full content is still sent on submission
- `/terminal-setup` should be run in the host terminal, not inside tmux or screen

## Related

- [[concepts/terminal_config]]
- [[concepts/custom_themes]]
- [[concepts/vim_editor_mode]]
- [[concepts/hooks]]
- [[concepts/statusline]]
- [[entities/claude_code]]
- [[entities/tmux]]