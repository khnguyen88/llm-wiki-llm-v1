---
title: "Claude Code Computer Use"
summary: "Computer use lets Claude Code control the user's screen on macOS — opening apps, clicking, typing, and taking screenshots — to handle GUI-only tasks that no other tool can reach"
type: summary
sources:
  - raw/document/claude code/claude-code-050-computer-use-2026-04-29.md
tags:
  - claude-code
  - computer-use
  - gui
  - macos
  - mcp
  - permissions
  - accessibility
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Claude Code Computer Use

## Key Points

- Computer use is a research preview on macOS that requires a Pro or Max plan, Claude Code v2.1.85+, and an interactive session (not available with `-p` flag) ^[raw/document/claude code/claude-code-050-computer-use-2026-04-29.md]
- Enabled as a built-in MCP server called `computer-use` via the `/mcp` menu; the setting persists per project ^[raw/document/claude code/claude-code-050-computer-use-2026-04-29.md]
- Requires two macOS permissions: Accessibility (click, type, scroll) and Screen Recording (see the screen); macOS may require a restart after granting Screen Recording ^[raw/document/claude code/claude-code-050-computer-use-2026-04-29.md]
- Claude uses the most precise tool available: MCP servers first, then Bash, then Chrome extension, then computer use as a fallback for GUI-only tasks ^[raw/document/claude code/claude-code-050-computer-use-2026-04-29.md]
- Per-session app approval: the first time Claude needs a specific app, a prompt shows which apps it wants to control, extra permissions requested, and how many other apps will be hidden ^[raw/document/claude code/claude-code-050-computer-use-2026-04-29.md]
- Apps with broad access show sentinel warnings: Terminal/IDEs are "equivalent to shell access," Finder is "can read or write any file," System Settings is "can change system settings" ^[raw/document/claude code/claude-code-050-computer-use-2026-04-29.md]
- Screenshots are automatically downscaled (e.g., 3456×2234 → ~1372×887) to fit the model's input; there is no setting to change the target size ^[raw/document/claude code/claude-code-050-computer-use-2026-04-29.md]

## Quotes

- "Computer use lets Claude open apps, control your screen, and work on your machine the way you would." ^[raw/document/claude code/claude-code-050-computer-use-2026-04-29.md]
- "Screen control is reserved for things nothing else can reach: native apps, simulators, and tools without an API." ^[raw/document/claude code/claude-code-050-computer-use-2026-04-29.md]

## Notes

- Computer use holds a machine-wide lock; only one session can control the screen at a time
- Other visible apps are hidden while Claude works; the terminal window stays visible and is excluded from screenshots
- Pressing `Esc` anywhere aborts the current action immediately; a macOS notification appears when Claude acquires and releases the lock
- The Esc key press is consumed so prompt injection cannot use it to dismiss dialogs
- On Windows, computer use is only available in the Desktop app, not the CLI
- Not available for Team/Enterprise plans or third-party providers (Bedrock, Vertex AI, Foundry)

## Related

- [[concepts/computer_use]]
- [[entities/claude_code]]
- [[concepts/mcp]]
- [[concepts/permissions]]
- [[concepts/browser_automation]]
- [[concepts/non_interactive_mode]]