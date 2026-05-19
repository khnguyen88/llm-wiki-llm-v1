---
title: "Custom Themes"
summary: "Claude Code's theme system with built-in presets, auto-detection, and user-defined JSON themes that override individual color tokens"
type: concept
sources:
  - raw/document/claude code/claude-code-107-terminal-config-2026-04-29.md
tags:
  - claude-code
  - themes
  - customization
  - terminal
  - color
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Custom Themes

Claude Code's theme system lets users select from built-in presets, auto-detect light/dark mode, or create custom JSON themes that override individual color tokens. Custom themes require Claude Code v2.1.118 or later. ^[raw/document/claude code/claude-code-107-terminal-config-2026-04-29.md]

## Key Points

- Use `/theme` or the theme picker in `/config` to select a theme; the auto option detects the terminal's light or dark background and follows OS appearance changes ^[raw/document/claude code/claude-code-107-terminal-config-2026-04-29.md]
- Custom themes are JSON files in `~/.claude/themes/`; the filename without `.json` becomes the theme slug, stored as `custom:<slug>` in preferences ^[raw/document/claude code/claude-code-107-terminal-config-2026-04-29.md]
- Each custom theme has three optional fields: `name` (display label, defaults to filename slug), `base` (built-in preset to start from: `dark`, `light`, `dark-daltonized`, `light-daltonized`, `dark-ansi`, `light-ansi`; defaults to `dark`), and `overrides` (map of color token names to color values) ^[raw/document/claude code/claude-code-107-terminal-config-2026-04-29.md]
- Color values accept `#rrggbb`, `#rgb`, `rgb(r,g,b)`, `ansi256(n)`, or `ansi:<name>` (16 standard ANSI color names); unknown tokens and invalid values are ignored ^[raw/document/claude code/claude-code-107-terminal-config-2026-04-29.md]
- Claude Code watches `~/.claude/themes/` and reloads when a file changes, so edits in an editor apply to a running session without restart ^[raw/document/claude code/claude-code-107-terminal-config-2026-04-29.md]
- Several color tokens have paired `Shimmer` variants (e.g., `claudeShimmer`, `warningShimmer`) that supply the lighter color used in the spinner's animated gradient ^[raw/document/claude code/claude-code-107-terminal-config-2026-04-29.md]
- Subagents use eight named colors (`red`, `blue`, `green`, `yellow`, `purple`, `orange`, `pink`, `cyan`) following the token pattern `<color>_FOR_SUBAGENTS_ONLY` ^[raw/document/claude code/claude-code-107-terminal-config-2026-04-29.md]

## Details

### Color Token Groups

**Text and accent colors** control the primary brand and text shades: `claude` (brand accent, spinner, assistant label), `text` (default foreground), `inverseText` (text on colored backgrounds), `inactive` (secondary text, hints, timestamps), `subtle` (faint borders, de-emphasized text), `permission` (dialog borders), `remember` (memory and CLAUDE.md indicators). ^[raw/document/claude code/claude-code-107-terminal-config-2026-04-29.md]

**Status colors** signal states: `success` (passing checks), `error` (failures), `warning` (caution, auto mode border), `merged` (merged PR status). ^[raw/document/claude code/claude-code-107-terminal-config-2026-04-29.md]

**Input box and mode indicators** set borders and accents: `promptBorder` (default input border), `planMode` (plan mode accent and border), `autoAccept` (accept-edits mode), `bashBorder` (shell command input), `ide` (IDE connection indicator), `fastMode` (fast mode indicator). ^[raw/document/claude code/claude-code-107-terminal-config-2026-04-29.md]

**Diff rendering** colors code changes: `diffAdded`, `diffRemoved` (background of changed lines), `diffAddedDimmed`, `diffRemovedDimmed` (unchanged context near changes), `diffAddedWord`, `diffRemovedWord` (word-level highlights). ^[raw/document/claude code/claude-code-107-terminal-config-2026-04-29.md]

**Fullscreen mode** tokens apply only when using fullscreen rendering: `userMessageBackground` (background behind user messages), `selectionBg` (mouse selection background). ^[raw/document/claude code/claude-code-107-terminal-config-2026-04-29.md]

### Creating a Theme

Select "New custom theme..." at the end of the `/theme` list to create one interactively: name the theme, then pick individual color tokens to override. Press `Ctrl+E` while a custom theme is highlighted to edit it. The interactive editor shows all tokens with a live preview, including internal tokens not covered in the documentation. ^[raw/document/claude code/claude-code-107-terminal-config-2026-04-29.md]

Plugins can also contribute themes, which appear in the `/theme` list alongside built-in presets and custom themes. ^[raw/document/claude code/claude-code-107-terminal-config-2026-04-29.md]

## Related

- [[concepts/terminal_config]]
- [[concepts/statusline]]
- [[entities/claude_code]]
- [[summaries/claude-code-terminal-config]]