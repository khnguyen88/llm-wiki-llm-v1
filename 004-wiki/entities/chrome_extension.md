---
title: "Claude in Chrome Extension"
summary: "Browser extension connecting Claude Code to Chrome for browser automation, debugging, and data extraction"
type: entity
sources:
  - raw/document/claude code/claude-code-042-chrome-2026-04-29.md
  - raw/document/claude code/claude-code-115-vs-code-2026-04-29.md
tags:
  - claude-code
  - chrome
  - browser
  - extension
  - automation
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Claude in Chrome Extension

A Chrome Web Store extension (also compatible with Microsoft Edge) that connects Claude Code to the browser, enabling real-time browser automation from the CLI or VS Code extension. ^[001a-raw/document/claude code/claude-code-042-chrome-2026-04-29.md]

## Key Facts

- Available in the Chrome Web Store for both Google Chrome and Microsoft Edge ^[001a-raw/document/claude code/claude-code-042-chrome-2026-04-29.md]
- Requires version 1.0.36 or higher ^[001a-raw/document/claude code/claude-code-042-chrome-2026-04-29.md]
- Shares the browser's login state, allowing Claude to access any site the user is already signed into without API connectors ^[001a-raw/document/claude code/claude-code-042-chrome-2026-04-29.md]
- Communicates with Claude Code via a native messaging host; on first enable, Claude Code installs a native messaging host configuration file that Chrome reads on startup ^[001a-raw/document/claude code/claude-code-042-chrome-2026-04-29.md]
- Native messaging host config locations differ by browser and OS: Chrome uses `~/Library/Application Support/Google/Chrome/NativeMessagingHosts/` (macOS), `~/.config/google-chrome/NativeMessagingHosts/` (Linux), or `HKCU\Software\Google\Chrome\NativeMessagingHosts\` in the Windows Registry; Edge uses corresponding `Microsoft Edge` paths ^[001a-raw/document/claude code/claude-code-042-chrome-2026-04-29.md]
- Site-level permissions are managed through the Chrome extension settings, controlling which sites Claude can browse, click, and type on ^[001a-raw/document/claude code/claude-code-042-chrome-2026-04-29.md]
- The extension's service worker can go idle during extended sessions, breaking the connection; `/chrome` → "Reconnect extension" re-establishes it ^[001a-raw/document/claude code/claude-code-042-chrome-2026-04-29.md]
- Not supported on Brave, Arc, or other Chromium-based browsers; WSL is also not supported ^[001a-raw/document/claude code/claude-code-042-chrome-2026-04-29.md]
- Not available through third-party API providers (Amazon Bedrock, Google Cloud Vertex AI, Microsoft Foundry); requires a direct Anthropic plan (Pro, Max, Team, or Enterprise) ^[001a-raw/document/claude code/claude-code-042-chrome-2026-04-29.md]
- In VS Code, the Chrome extension is referenced via `@browser` in the prompt box; Claude opens new tabs for browser tasks and shares the browser's login state ^[001a-raw/document/claude code/claude-code-115-vs-code-2026-04-29.md]

## Related

- [[004-wiki/entities/claude_code]]
- [[004-wiki/concepts/browser_automation]]
- [[004-wiki/concepts/permissions]]
- [[004-wiki/concepts/mcp]]
- [[004-wiki/entities/vs_code_extension]]