---
title: "Browser Automation"
summary: "Claude Code's ability to control a Chrome browser via the Claude in Chrome extension, enabling live debugging, form filling, data extraction, and multi-site workflows"
type: concept
sources:
  - raw/document/claude code/claude-code-042-chrome-2026-04-29.md
  - raw/document/claude code/claude-code-050-computer-use-2026-04-29.md
tags:
  - claude-code
  - chrome
  - browser
  - automation
  - testing
  - debugging
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Browser Automation

The ability of Claude Code to control a Chrome browser through the Claude in Chrome extension, chaining browser actions with coding tasks in a single workflow. Browser actions execute in a visible Chrome window in real time, and Claude shares the user's browser login state. ^[raw/document/claude code/claude-code-042-chrome-2026-04-29.md]

## Key Points

- Activated via `claude --chrome` flag or `/chrome` command; can be set as default but increases context usage since browser tools are always loaded ^[raw/document/claude code/claude-code-042-chrome-2026-04-29.md]
- Supports six capability categories: live debugging (console errors + DOM state), design verification, web app testing, authenticated web app interaction, data extraction, and task automation ^[raw/document/claude code/claude-code-042-chrome-2026-04-29.md]
- Also supports session recording: Claude can record browser interactions as GIF files ^[raw/document/claude code/claude-code-042-chrome-2026-04-29.md]
- When encountering a login page or CAPTCHA, Claude pauses and asks the user to handle it manually ^[raw/document/claude code/claude-code-042-chrome-2026-04-29.md]
- Currently in beta; supports Google Chrome and Microsoft Edge only (not Brave, Arc, or other Chromium browsers, and not WSL) ^[raw/document/claude code/claude-code-042-chrome-2026-04-29.md]
- Browser automation is preferred over computer use for web-based tasks: Claude tries MCP servers first, then Bash, then Chrome extension, and only falls back to computer use (screen control) for native apps, simulators, and tools without an API ^[raw/document/claude code/claude-code-050-computer-use-2026-04-29.md]

## Details

Browser automation uses a native messaging host to bridge Claude Code and the Chrome extension. On first enable, Claude Code installs a configuration file that Chrome reads on startup; if the extension is not detected on the first attempt, restarting Chrome picks up the new configuration. ^[raw/document/claude code/claude-code-042-chrome-2026-04-29.md]

Common troubleshooting scenarios include: JavaScript modal dialogs (alert, confirm, prompt) blocking browser events (dismiss manually then continue), the extension service worker going idle during long sessions (run `/chrome` → "Reconnect extension"), and Windows named pipe conflicts (EADDRINUSE, resolved by closing other Claude Code sessions using Chrome). ^[raw/document/claude code/claude-code-042-chrome-2026-04-29.md]

## Related

- [[entities/chrome_extension]]
- [[entities/claude_code]]
- [[concepts/mcp]]
- [[concepts/computer_use]]
- [[concepts/permissions]]