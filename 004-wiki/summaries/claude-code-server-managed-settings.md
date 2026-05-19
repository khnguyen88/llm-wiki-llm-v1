---
title: "Claude Code Server Managed Settings"
summary: "Server-managed settings deliver organization-wide Claude Code configuration from Anthropic's servers at authentication time, with strict precedence over local settings and optional fail-closed startup"
type: summary
sources:
  - raw/document/claude code/claude-code-100-server-managed-settings-2026-04-29.md
tags:
  - claude-code
  - admin
  - settings
  - deployment
  - enterprise
  - security
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Claude Code Server Managed Settings

## Key Points

- Server-managed settings allow administrators to centrally configure Claude Code through a web-based interface on Claude.ai; clients receive settings automatically at authentication time without requiring device management infrastructure ^[raw/document/claude code/claude-code-100-server-managed-settings-2026-04-29.md]
- Available for Claude for Teams (v2.1.38+) and Claude for Enterprise (v2.1.30+); requires network access to `api.anthropic.com` ^[raw/document/claude code/claude-code-100-server-managed-settings-2026-04-29.md]
- Server-managed and endpoint-managed settings both occupy the highest tier in the settings hierarchy; no other settings level can override them, including command-line arguments; the first source that delivers a non-empty configuration wins (server-managed is checked first) ^[raw/document/claude code/claude-code-100-server-managed-settings-2026-04-29.md]
- Settings are fetched at startup and polled hourly during active sessions; first launch without cached settings loads asynchronously with a brief unenforced window; cached settings apply immediately on subsequent launches ^[raw/document/claude code/claude-code-100-server-managed-settings-2026-04-29.md]
- `forceRemoteSettingsRefresh: true` enforces fail-closed startup: the CLI blocks until fresh settings are fetched, and exits if the fetch fails rather than proceeding without policy ^[raw/document/claude code/claude-code-100-server-managed-settings-2026-04-29.md]
- Shell command settings, custom environment variables (not on the known safe allowlist), and hook configurations trigger a security approval dialog that users must accept; rejecting exits Claude Code; in non-interactive mode (`-p`), security dialogs are skipped and settings applied without approval ^[raw/document/claude code/claude-code-100-server-managed-settings-2026-04-29.md]
- Not available when using third-party model providers (Amazon Bedrock, Google Vertex AI, Microsoft Foundry, or custom `ANTHROPIC_BASE_URL`); settings are bypassed entirely in those configurations ^[raw/document/claude code/claude-code-100-server-managed-settings-2026-04-29.md]

## Quotes

> Settings delivered from Anthropic's servers at authentication time ^[raw/document/claude code/claude-code-100-server-managed-settings-2026-04-29.md]

> Sources do not merge: if server-managed settings deliver any keys at all, endpoint-managed settings are ignored entirely. ^[raw/document/claude code/claude-code-100-server-managed-settings-2026-04-29.md]

> On unmanaged devices, users with admin or sudo access can modify the Claude Code binary, filesystem, or network configuration. ^[raw/document/claude code/claude-code-100-server-managed-settings-2026-04-29.md]

## Notes

- Only Primary Owner and Owner roles can manage server-managed settings; changes apply to all users in the organization uniformly (per-group configurations not yet supported) ^[raw/document/claude code/claude-code-100-server-managed-settings-2026-04-29.md]
- MCP server configurations cannot be distributed through server-managed settings ^[raw/document/claude code/claude-code-100-server-managed-settings-2026-04-29.md]
- Audit log events for settings changes are available through the compliance API or audit log export ^[raw/document/claude code/claude-code-100-server-managed-settings-2026-04-29.md]
- `ConfigChange` hooks can detect runtime configuration changes for logging or blocking unauthorized modifications ^[raw/document/claude code/claude-code-100-server-managed-settings-2026-04-29.md]
- Advanced settings like OpenTelemetry configuration require a full restart to take effect, even though most settings update automatically ^[raw/document/claude code/claude-code-100-server-managed-settings-2026-04-29.md]

## Related

- [[entities/claude_code]]
- [[concepts/managed_settings]]
- [[concepts/server_managed_settings]]
- [[concepts/setting_sources]]
- [[concepts/authentication]]
- [[concepts/permissions]]
- [[concepts/hooks]]
- [[concepts/auto_mode]]
- [[concepts/non_interactive_mode]]