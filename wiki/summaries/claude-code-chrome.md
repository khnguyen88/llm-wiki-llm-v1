---
title: "Claude Code Chrome"
summary: "Chrome browser extension integration for Claude Code, enabling browser automation, live debugging, form filling, data extraction, and session recording from the CLI or VS Code"
type: summary
sources:
  - raw/document/claude code/claude-code-042-chrome-2026-04-29.md
tags:
  - claude-code
  - chrome
  - browser-automation
  - extension
  - beta
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Claude Code Chrome

## Key Points

- Claude Code connects to the Claude in Chrome browser extension to provide browser automation capabilities from the CLI or VS Code extension, chaining browser actions with coding tasks in a single workflow ^[raw/document/claude code/claude-code-042-chrome-2026-04-29.md]
- The integration is in beta and currently supports Google Chrome and Microsoft Edge only; Brave, Arc, and other Chromium-based browsers are not yet supported, and WSL is also not supported ^[raw/document/claude code/claude-code-042-chrome-2026-04-29.md]
- Prerequisites: Chrome extension v1.0.36+, Claude Code v2.0.73+, and a direct Anthropic plan (Pro, Max, Team, or Enterprise); not available through third-party providers (Bedrock, Vertex AI, Foundry) ^[raw/document/claude code/claude-code-042-chrome-2026-04-29.md]
- Enable via `claude --chrome` flag or `/chrome` command within a session; can be set as default by running `/chrome` and selecting "Enabled by default" (increases context usage since browser tools are always loaded) ^[raw/document/claude code/claude-code-042-chrome-2026-04-29.md]
- Capabilities include live debugging, design verification, web app testing, authenticated web app interaction (shares browser login state), data extraction, task automation, and session recording as GIFs ^[raw/document/claude code/claude-code-042-chrome-2026-04-29.md]
- When encountering a login page or CAPTCHA, Claude pauses and asks the user to handle it manually; browser actions run in a visible Chrome window in real time ^[raw/document/claude code/claude-code-042-chrome-2026-04-29.md]
- Troubleshooting includes reconnecting via `/chrome`, checking native messaging host config files, dismissing modal dialogs that block browser events, and handling Windows named pipe conflicts (EADDRINUSE) ^[raw/document/claude code/claude-code-042-chrome-2026-04-29.md]

## Quotes

- "Claude opens new tabs for browser tasks and shares your browser's login state, so it can access any site you're already signed into." ^[raw/document/claude code/claude-code-042-chrome-2026-04-29.md]
- "Chrome integration is not available through third-party providers like Amazon Bedrock, Google Cloud Vertex AI, or Microsoft Foundry." ^[raw/document/claude code/claude-code-042-chrome-2026-04-29.md]
- "Enabling Chrome by default in the CLI increases context usage since browser tools are always loaded." ^[raw/document/claude code/claude-code-042-chrome-2026-04-29.md]

## Notes

- The Chrome extension uses a native messaging host to communicate with Claude Code; on first enable, a native messaging host configuration file is installed, and Chrome must be restarted to read it ^[raw/document/claude code/claude-code-042-chrome-2026-04-29.md]
- Site-level permissions are managed through the Chrome extension settings, not within Claude Code itself ^[raw/document/claude code/claude-code-042-chrome-2026-04-29.md]
- The extension's service worker can go idle during extended sessions, breaking the connection; `/chrome` → "Reconnect extension" resolves this ^[raw/document/claude code/claude-code-042-chrome-2026-04-29.md]

## Related

- [[entities/chrome_extension]]
- [[entities/claude_code]]
- [[concepts/browser_automation]]
- [[concepts/mcp]]
- [[concepts/permissions]]