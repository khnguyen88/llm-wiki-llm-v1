---
title: "Vim Editor Mode"
summary: "A Vim-style editing mode for the Claude Code prompt input supporting NORMAL and VISUAL mode motions, text objects, and operators"
type: concept
sources:
  - raw/document/claude code/claude-code-107-terminal-config-2026-04-29.md
tags:
  - claude-code
  - vim
  - editor
  - keybindings
  - input
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Vim Editor Mode

Claude Code includes a Vim-style editing mode for the prompt input that supports a subset of NORMAL and VISUAL mode motions, operators, and text objects. ^[raw/document/claude code/claude-code-107-terminal-config-2026-04-29.md]

## Key Points

- Enable Vim mode through `/config` → Editor mode, or by setting `editorMode` to `"vim"` in `~/.claude/settings.json`; set it back to `"normal"` to disable ^[raw/document/claude code/claude-code-107-terminal-config-2026-04-29.md]
- Supports `hjkl` navigation, `v`/`V` for visual selection, and `d`/`c`/`y` with text objects for delete, change, and yank operations ^[raw/document/claude code/claude-code-107-terminal-config-2026-04-29.md]
- Pressing Enter still submits the prompt in INSERT mode, unlike standard Vim; use `o` or `O` in NORMAL mode, or Ctrl+J, to insert a newline instead ^[raw/document/claude code/claude-code-107-terminal-config-2026-04-29.md]
- Vim motions are not remappable through the keybindings file ^[raw/document/claude code/claude-code-107-terminal-config-2026-04-29.md]
- The full key table for Vim editor mode is documented in the interactive mode reference, not the terminal config page ^[raw/document/claude code/claude-code-107-terminal-config-2026-04-29.md]

## Details

Vim editor mode is a prompt-input feature, not a full Vim emulation. It provides common NORMAL-mode motions (`h`, `j`, `k`, `l`), VISUAL-mode selection (`v` for character-wise, `V` for line-wise), and operators (`d`, `c`, `y`) with text objects. The key difference from standard Vim is that Enter submits the prompt rather than inserting a newline, which means users must use `o`/`O` in NORMAL mode or Ctrl+J to add line breaks. Vim motions cannot be remapped through the keybindings file, though other Claude Code shortcuts can be. ^[raw/document/claude code/claude-code-107-terminal-config-2026-04-29.md]

## Related

- [[concepts/terminal_config]]
- [[concepts/commands]]
- [[entities/claude_code]]
- [[summaries/claude-code-terminal-config]]