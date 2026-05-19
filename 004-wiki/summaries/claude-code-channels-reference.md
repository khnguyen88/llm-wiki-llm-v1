---
title: "Claude Code Channels Reference"
summary: "Reference specification for the channel contract: server capabilities, notification events, reply tools, sender gating, and permission relay for building MCP-based channels that push events into Claude Code sessions"
type: summary
sources:
  - raw/document/claude code/claude-code-040-channels-reference-2026-04-29.md
tags:
  - channels
  - mcp
  - reference
  - permissions
  - plugins
  - security
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Claude Code Channels Reference

## Key Points

- Channels are MCP servers that declare `capabilities.experimental['claude/channel']` in the Server constructor; this capability registers a notification listener with Claude Code and makes the server a channel rather than a standard MCP server ^[raw/document/claude code/claude-code-040-channels-reference-2026-04-29.md]
- One-way channels forward alerts and webhooks into the session; two-way channels also expose an MCP tool (e.g., `reply`) so Claude can send messages back to the external platform ^[raw/document/claude code/claude-code-040-channels-reference-2026-04-29.md]
- The notification payload uses method `notifications/claude/channel` with `content` (string, becomes the `<channel>` tag body) and `meta` (optional `Record<string, string>`, each entry becomes a tag attribute) ^[raw/document/claude code/claude-code-040-channels-reference-2026-04-29.md]
- Sender gating is critical: ungated channels are prompt injection vectors; channels must check sender identity against an allowlist before emitting notifications, gating on `message.from.id` (sender) rather than `message.chat.id` (room) ^[raw/document/claude code/claude-code-040-channels-reference-2026-04-29.md]
- Permission relay (v2.1.81+) lets two-way channels receive and respond to tool approval prompts remotely; declared via `capabilities.experimental['claude/channel/permission']` and uses request IDs composed of five lowercase letters from `a`-`z` excluding `l` ^[raw/document/claude code/claude-code-040-channels-reference-2026-04-29.md]
- Custom channels require `--dangerously-load-development-channels` during the research preview because they are not on the approved allowlist; the bypass is per-entry and does not extend to `--channels` entries ^[raw/document/claude code/claude-code-040-channels-reference-2026-04-29.md]
- The `instructions` field in the Server constructor is added to Claude's system prompt and should specify what events to expect, whether to reply, and which tool and attribute to use for routing replies ^[raw/document/claude code/claude-code-040-channels-reference-2026-04-29.md]

## Quotes

- "A channel is an MCP server that pushes events into a Claude Code session so Claude can react to things happening outside the terminal." ^[raw/document/claude code/claude-code-040-channels-reference-2026-04-29.md]
- "An ungated channel is a prompt injection vector. Anyone who can reach your endpoint can put text in front of Claude." ^[raw/document/claude code/claude-code-040-channels-reference-2026-04-29.md]
- "Gate on the sender's identity, not the chat or room identity." ^[raw/document/claude code/claude-code-040-channels-reference-2026-04-29.md]

## Notes

- The reference document provides complete code examples for building webhook receivers, adding reply tools, implementing sender gating, and adding permission relay to two-way chat bridges.
- Permission relay covers tool-use approvals (Bash, Write, Edit) but not project trust or MCP server consent dialogs, which only appear in the local terminal.
- During research preview, channel plugins submitted to the official marketplace undergo security review before being added to the Anthropic allowlist.

## Related

- [[concepts/channels]]
- [[concepts/mcp]]
- [[concepts/permissions]]
- [[concepts/plugins]]
- [[entities/claude_code]]