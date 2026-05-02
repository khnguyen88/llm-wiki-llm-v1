---
title: "Channels"
summary: "MCP servers that push external events into a running Claude Code session, enabling two-way communication with messaging platforms and webhook receivers"
type: concept
sources:
  - raw/document/claude code/claude-code-039-channels-2026-04-29.md
  - raw/document/claude code/claude-code-040-channels-reference-2026-04-29.md
tags:
  - channels
  - mcp
  - plugins
  - automation
  - telegram
  - discord
  - imessage
  - enterprise
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: merged
---

# Channels

Channels are MCP servers that push events into a running Claude Code session from external sources, enabling Claude to react to things happening outside the terminal. Unlike standard MCP servers that Claude queries on-demand, channels push events in real time — a CI result, chat message, or monitoring alert arrives in the session immediately. ^[raw/document/claude code/claude-code-039-channels-2026-04-29.md]

## Key Points

- Channels are MCP servers installed as plugins that push events into a running session; they require the `--channels` flag at startup (e.g., `claude --channels plugin:telegram@claude-plugins-official`) ^[raw/document/claude code/claude-code-039-channels-2026-04-29.md]
- Channels can be two-way: Claude reads the inbound event and replies through the same channel, acting as a chat bridge; replies appear on the external platform, not in the terminal ^[raw/document/claude code/claude-code-039-channels-2026-04-29.md]
- Events only arrive while the session is open; for always-on operation, run Claude Code in a background process or persistent terminal ^[raw/document/claude code/claude-code-039-channels-2026-04-29.md]
- Security relies on sender allowlists: only approved sender IDs can push messages, and allowlist members who can reply through the channel can also approve or deny tool-use permission prompts via permission relay ^[raw/document/claude code/claude-code-039-channels-2026-04-29.md]
- Channel plugins require [Bun](https://bun.sh) and are installed via `/plugin install`; after installation, `/reload-plugins` activates the plugin's configure command ^[raw/document/claude code/claude-code-039-channels-2026-04-29.md]
- Research preview (requires Claude Code v2.1.80+, claude.ai login; console and API key auth not supported) with Telegram, Discord, and iMessage as the included plugins ^[raw/document/claude code/claude-code-039-channels-2026-04-29.md]
- Channel servers declare the `claude/channel` capability in their MCP Server constructor; the `instructions` field is added to Claude's system prompt and should describe expected events, whether to reply, and which tool/attribute to route replies through ^[raw/document/claude code/claude-code-040-channels-reference-2026-04-29.md]
- Notification payloads use method `notifications/claude/channel` with `content` (string, becomes `<channel>` tag body) and `meta` (optional `Record<string, string>`, each key becomes a tag attribute; keys must be identifiers — letters, digits, underscores only; hyphenated keys are silently dropped) ^[raw/document/claude code/claude-code-040-channels-reference-2026-04-29.md]
- Two-way channels expose an MCP tool (e.g., `reply`) with `capabilities.tools: {}` in the constructor so Claude Code discovers the tool; Claude calls the tool with arguments like `chat_id` and `text` to send messages back ^[raw/document/claude code/claude-code-040-channels-reference-2026-04-29.md]
- Sender gating is mandatory for any channel exposed to a chat platform or public endpoint; gate on sender identity (`message.from.id`), not room identity (`message.chat.id`), because anyone in an allowlisted group could inject messages ^[raw/document/claude code/claude-code-040-channels-reference-2026-04-29.md]
- Permission relay (v2.1.81+) lets two-way channels receive and respond to tool approval prompts remotely; declared via `capabilities.experimental['claude/channel/permission']`; the local terminal dialog stays open, and whichever answer arrives first (local or remote) is applied ^[raw/document/claude code/claude-code-040-channels-reference-2026-04-29.md]
- Custom channels require `--dangerously-load-development-channels` during the research preview because they are not on the approved allowlist; the bypass is per-entry and does not extend to `--channels` entries ^[raw/document/claude code/claude-code-040-channels-reference-2026-04-29.md]

## Details

### Supported Channels

The research preview includes three officially supported channel plugins, all requiring Bun:

**Telegram** — Create a bot via BotFather (`/newbot`), install the plugin (`/plugin install telegram@claude-plugins-official`), configure the token (`/telegram:configure <token>`), restart with `--channels`, and pair by messaging the bot then running `/telegram:access pair <code>` followed by `/telegram:access policy allowlist`. Tokens are stored in `~/.claude/channels/telegram/.env`. ^[raw/document/claude code/claude-code-039-channels-2026-04-29.md]

**Discord** — Create a bot in the Discord Developer Portal, enable Message Content Intent under Privileged Gateway Intents, invite the bot with appropriate permissions (View Channels, Send Messages, Send Messages in Threads, Read Message History, Attach Files, Add Reactions), install the plugin (`/plugin install discord@claude-plugins-official`), configure (`/discord:configure <token>`), restart with `--channels`, and pair by DMing the bot then running `/discord:access pair <code>` and `/discord:access policy allowlist`. Tokens are stored in `~/.claude/channels/discord/.env`. ^[raw/document/claude code/claude-code-039-channels-2026-04-29.md]

**iMessage** — macOS only; reads the Messages database directly at `~/Library/Messages/chat.db` and sends replies via AppleScript. Requires Full Disk Access granted to the terminal app. Self-chat bypasses access control automatically; other contacts are added via `/imessage:access allow +15551234567` using phone numbers in `+country` format or Apple ID emails. No bot token or external service is needed. ^[raw/document/claude code/claude-code-039-channels-2026-04-29.md]

### Security Model

Every approved channel plugin maintains a sender allowlist. Telegram and Discord use a pairing mechanism: message the bot, receive a pairing code, approve it in the Claude Code session. iMessage grants self-chat automatically and adds other contacts by handle. Being in `.mcp.json` is not enough — a server must also be named in `--channels` to push messages. The allowlist also gates permission relay: anyone who can reply through the channel can approve or deny tool use in the session. ^[raw/document/claude code/claude-code-039-channels-2026-04-29.md]

### Enterprise Controls

On Team and Enterprise plans, channels are off by default. Two managed settings control availability:

- `channelsEnabled` — master switch; must be `true` for any channel to deliver messages. Set via claude.ai admin console or managed settings. Blocks all channels including the development flag when off. ^[raw/document/claude code/claude-code-039-channels-2026-04-29.md]
- `allowedChannelPlugins` — restricts which plugins can register once channels are enabled. Each entry names a plugin and its marketplace (e.g., `{ "marketplace": "claude-plugins-official", "plugin": "telegram" }`). Replaces the Anthropic default list entirely when set; leave unset to fall back to defaults. An empty array blocks all channel plugins from the allowlist. Requires `channelsEnabled: true`. ^[raw/document/claude code/claude-code-039-channels-2026-04-29.md]

Pro and Max users without an organization skip these checks entirely; they opt in per session with `--channels`. ^[raw/document/claude code/claude-code-039-channels-2026-04-29.md]

### How Channels Compare

Channels fill a specific gap among Claude Code's external connectivity features. Claude Code on the web runs tasks in a fresh cloud sandbox. Claude in Slack spawns a web session from an `@Claude` mention. Standard MCP servers let Claude query external systems on-demand. Remote Control lets a user drive their local session from claude.ai or mobile. Channels are distinct: they push events from non-Claude sources into an already-running local session that has context about ongoing work. ^[raw/document/claude code/claude-code-039-channels-2026-04-29.md]

### Fakechat Demo

Fakechat is an officially supported demo channel that runs a chat UI on `localhost:8787` with no authentication or external service required. Install with `/plugin install fakechat@claude-plugins-official`, restart with `claude --channels plugin:fakechat@claude-plugins-official`, and type messages in the browser to see them arrive in the Claude Code session. ^[raw/document/claude code/claude-code-039-channels-2026-04-29.md]

### Channel Contract

The channel contract defines how MCP servers register as channels and exchange messages with Claude Code. ^[raw/document/claude code/claude-code-040-channels-reference-2026-04-29.md]

**Server capabilities** are set in the `Server` constructor:

| Field | Required | Purpose |
|-------|----------|---------|
| `capabilities.experimental['claude/channel']` | Yes | Registers the notification listener; always `{}` |
| `capabilities.experimental['claude/channel/permission']` | No | Opts in to permission relay (v2.1.81+); always `{}` |
| `capabilities.tools` | Two-way only | Enables tool discovery for reply tools; always `{}` |
| `instructions` | Recommended | Added to Claude's system prompt; describes expected events and reply routing |

^[raw/document/claude code/claude-code-040-channels-reference-2026-04-29.md]

**Notification format**: events are emitted via `mcp.notification()` with method `notifications/claude/channel`. The `content` param (string) becomes the `<channel>` tag body, and each `meta` entry (optional `Record<string, string>`) becomes a tag attribute. The `source` attribute is set automatically from the server's configured name. Meta keys must be identifiers (letters, digits, underscores); hyphenated or otherwise invalid keys are silently dropped. ^[raw/document/claude code/claude-code-040-channels-reference-2026-04-29.md]

### Sender Gating

An ungated channel is a prompt injection vector — anyone who can reach the endpoint can inject text into Claude's context. Channels must gate on sender identity, not room identity. In group chats, `message.from.id` (sender) and `message.chat.id` (room) differ; gating on the room would let any member of an allowlisted group inject messages. Telegram and Discord channels use a pairing mechanism for bootstrapping the allowlist; iMessage detects the user's own addresses from the Messages database at startup. ^[raw/document/claude code/claude-code-040-channels-reference-2026-04-29.md]

### Permission Relay

Permission relay (requires v2.1.81+) forwards tool approval prompts to a remote channel so a user can approve or deny tool use from another device. It covers tool-use approvals (Bash, Write, Edit) but not project trust or MCP server consent dialogs, which only appear in the local terminal. The relay loop has four steps: (1) Claude Code generates a five-letter request ID (lowercase, no `l`) and notifies the channel server; (2) the server forwards the prompt and ID to the chat app; (3) the remote user replies with yes/no and the ID; (4) the inbound handler parses the reply into a verdict and sends it back. The local terminal dialog stays open throughout; whichever answer arrives first is applied. ^[raw/document/claude code/claude-code-040-channels-reference-2026-04-29.md]

The outbound notification method is `notifications/claude/channel/permission_request` with four params: `request_id`, `tool_name`, `description`, and `input_preview` (tool args as JSON, truncated to ~200 characters). The verdict is sent back as `notifications/claude/channel/permission` with `request_id` and `behavior` set to `'allow'` or `'deny'`. Neither verdict affects future calls. ^[raw/document/claude code/claude-code-040-channels-reference-2026-04-29.md]

### Plugin Packaging

To make a channel installable and shareable, wrap it in a plugin and publish it to a marketplace. Users install with `/plugin install` and enable per session with `--channels plugin:<name>@<marketplace>`. During the research preview, channels not on the Anthropic allowlist still require `--dangerously-load-development-channels`. To get added to the allowlist, submit the plugin to the official marketplace; channel plugins undergo security review before approval. On Team and Enterprise plans, admins can use `allowedChannelPlugins` to replace the default allowlist entirely. ^[raw/document/claude code/claude-code-040-channels-reference-2026-04-29.md]

## Related

- [[concepts/mcp]]
- [[concepts/plugins]]
- [[concepts/permissions]]
- [[concepts/managed_settings]]
- [[concepts/sessions]]
- [[entities/claude_code]]