---
title: "Claude Code Channels"
summary: "MCP servers that push external events into a running Claude Code session, enabling two-way communication with platforms like Telegram, Discord, and iMessage"
type: summary
sources:
  - raw/document/claude code/claude-code-039-channels-2026-04-29.md
tags:
  - channels
  - mcp
  - plugins
  - telegram
  - discord
  - imessage
  - automation
  - enterprise
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Claude Code Channels

## Key Points

- Channels are MCP servers that push events into a running Claude Code session, allowing Claude to react to external events while the user is away from the terminal ^[raw/document/claude code/claude-code-039-channels-2026-04-29.md]
- Channels can be two-way: Claude reads inbound events and replies back through the same channel, functioning as a chat bridge ^[raw/document/claude code/claude-code-039-channels-2026-04-29.md]
- Events only arrive while the session is open; for always-on usage, Claude Code must run in a background process or persistent terminal ^[raw/document/claude code/claude-code-039-channels-2026-04-29.md]
- The research preview (requires v2.1.80+) includes Telegram, Discord, and iMessage plugins; custom channels can be built using the Channels reference ^[raw/document/claude code/claude-code-039-channels-2026-04-29.md]
- Security uses sender allowlists with a pairing mechanism; only approved sender IDs can push messages, and anyone who can reply through a channel can also approve or deny tool use in the session ^[raw/document/claude code/claude-code-039-channels-2026-04-29.md]
- Team and Enterprise organizations have channels disabled by default; admins must enable them via `channelsEnabled` managed setting or the claude.ai admin console ^[raw/document/claude code/claude-code-039-channels-2026-04-29.md]
- The `--channels` flag enables specific channel plugins per session; being in `.mcp.json` is not sufficient — a server must also be named in `--channels` to push messages ^[raw/document/claude code/claude-code-039-channels-2026-04-29.md]

## Notes

- Channels differ from standard MCP servers (which Claude queries on-demand), Claude Code on the web (which runs in a fresh cloud sandbox), and Remote Control (which drives an existing session from claude.ai or mobile) — channels specifically push events from non-Claude sources into a local session that already has context ^[raw/document/claude code/claude-code-039-channels-2026-04-29.md]
- The `allowedChannelPlugins` managed setting replaces the Anthropic default allowlist entirely when set; an empty array blocks all channel plugins except those loaded with `--dangerously-load-development-channels` ^[raw/document/claude code/claude-code-039-channels-2026-04-29.md]

## Related

- [[concepts/channels]]
- [[concepts/mcp]]
- [[concepts/plugins]]
- [[concepts/permissions]]
- [[concepts/managed_settings]]
- [[entities/claude_code]]