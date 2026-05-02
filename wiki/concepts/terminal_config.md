---
title: "Terminal Config"
summary: "Configuring terminal emulators to send correct key signals and notifications to Claude Code, including Shift+Enter, Option key, tmux passthrough, and fullscreen rendering"
type: concept
sources:
  - raw/document/claude code/claude-code-107-terminal-config-2026-04-29.md
tags:
  - claude-code
  - terminal
  - configuration
  - keybindings
  - notifications
  - tmux
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Terminal Config

Terminal configuration for Claude Code ensures that the terminal emulator sends the correct key signals (Shift+Enter, Option key) and forwards notifications and progress indicators. Claude Code works in any terminal without configuration, but specific terminals may need setup for full functionality. ^[raw/document/claude code/claude-code-107-terminal-config-2026-04-29.md]

## Key Points

- Pressing Enter submits the prompt; Ctrl+J or `\` then Enter always inserts a newline regardless of terminal; Shift+Enter works without setup in Ghostty, Kitty, iTerm2, WezTerm, Warp, and Apple Terminal ^[raw/document/claude code/claude-code-107-terminal-config-2026-04-29.md]
- `/terminal-setup` configures Shift+Enter and other keybindings in VS Code, Cursor, Windsurf, Alacritty, and Zed by writing to their terminal configuration files; it also sets `terminal.integrated.mouseWheelScrollSensitivity` in VS Code for smoother fullscreen scrolling ^[raw/document/claude code/claude-code-107-terminal-config-2026-04-29.md]
- On macOS, the Option key must be configured as Meta ("Use Option as Meta Key" or "Esc+") for shortcuts like Option+Enter and Option+P to work; the setting location varies by terminal (Apple Terminal: Profiles → Keyboard; iTerm2: Profiles → Keys → General; VS Code: `terminal.integrated.macOptionIsMeta`) ^[raw/document/claude code/claude-code-107-terminal-config-2026-04-29.md]
- Desktop notifications reach the OS natively in Ghostty and Kitty without setup; iTerm2 requires enabling "Notification Center Alerts" and "Send escape sequence-generated alerts" in its settings ^[raw/document/claude code/claude-code-107-terminal-config-2026-04-29.md]
- Tmux requires three settings in `~/.tmux.conf`: `allow-passthrough on` (for notifications and progress), `extended-keys on`, and `terminal-features 'xterm*:extkeys'` (for Shift+Enter); run `tmux source-file ~/.tmux.conf` to apply ^[raw/document/claude code/claude-code-107-terminal-config-2026-04-29.md]
- Pasting more than 10,000 characters collapses the input to a `[Pasted text]` placeholder while still sending the full content on submission; VS Code's integrated terminal can drop characters from very large pastes ^[raw/document/claude code/claude-code-107-terminal-config-2026-04-29.md]
- Windows Terminal, gnome-terminal, and JetBrains IDEs do not support Shift+Enter; users must use Ctrl+J or `\` then Enter for newlines ^[raw/document/claude code/claude-code-107-terminal-config-2026-04-29.md]

## Details

### Multiline Prompts

Enter submits the message by default. Three alternatives insert a newline without submitting: Ctrl+J (works everywhere), `\` followed by Enter (works everywhere), and Shift+Enter (works in most terminals, requires `/terminal-setup` in some). The `/terminal-setup` command writes keybindings to the terminal's configuration file and does not overwrite existing bindings. It should be run in the host terminal, not inside tmux or screen. When running inside tmux, Shift+Enter also requires the tmux passthrough configuration even if the outer terminal supports it. ^[raw/document/claude code/claude-code-107-terminal-config-2026-04-29.md]

### Option Key on macOS

Many Claude Code shortcuts use the Option key (Option+Enter for newline, Option+P to switch models). On macOS, most terminals do not send Option as a modifier by default. The terminal setting is usually labeled "Use Option as Meta Key." The historical Unix name for this key is Meta. Ghostty and Kitty have Option-as-Alt or Option-as-Meta settings in their configuration files. ^[raw/document/claude code/claude-code-107-terminal-config-2026-04-29.md]

### Notification Hooks

In terminals that do not receive desktop notifications natively (Warp, Apple Terminal, and others), a Notification hook in `settings.json` can play a sound or run a custom command when Claude finishes a task or pauses for a permission prompt. Hooks run alongside the native desktop notification and do not replace it. ^[raw/document/claude code/claude-code-107-terminal-config-2026-04-29.md]

### Tmux Integration

Inside tmux, two things break by default: Shift+Enter submits instead of inserting a newline, and desktop notifications and the progress bar never reach the outer terminal. The `allow-passthrough` setting lets escape sequences for notifications and progress reach the outer terminal (iTerm2, Ghostty, or Kitty). The `extended-keys` and `terminal-features` settings let tmux distinguish Shift+Enter from plain Enter. ^[raw/document/claude code/claude-code-107-terminal-config-2026-04-29.md]

### Fullscreen Rendering

Fullscreen rendering mode draws to a separate screen buffer that the terminal reserves for full-screen applications, instead of appending to normal scrollback. This keeps memory usage flat and adds mouse support for scrolling and selection. Switch to it with `/tui fullscreen` in the current session, or set `CLAUDE_CODE_NO_FLICKER=1` as an environment variable before starting Claude Code to make it the default. ^[raw/document/claude code/claude-code-107-terminal-config-2026-04-29.md]

## Related

- [[concepts/custom_themes]]
- [[concepts/vim_editor_mode]]
- [[concepts/hooks]]
- [[concepts/statusline]]
- [[entities/claude_code]]
- [[entities/tmux]]
- [[summaries/claude-code-terminal-config]]