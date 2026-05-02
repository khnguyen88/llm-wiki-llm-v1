---
title: "Server Managed Settings"
summary: "Server-delivered configuration for Claude Code organizations that delivers policy from Anthropic's servers at authentication time, with strict precedence over local settings and caching for offline resilience"
type: concept
sources:
  - raw/document/claude code/claude-code-100-server-managed-settings-2026-04-29.md
tags:
  - claude-code
  - admin
  - settings
  - deployment
  - enterprise
  - security
  - caching
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Server Managed Settings

Server-managed settings deliver organization-wide Claude Code configuration from Anthropic's servers through a web-based admin console on Claude.ai. Clients automatically receive these settings when users authenticate with their organization credentials, eliminating the need for device management infrastructure. ^[raw/document/claude code/claude-code-100-server-managed-settings-2026-04-29.md]

## Key Points

- Available for Claude for Teams (v2.1.38+) and Claude for Enterprise (v2.1.30+); requires network access to `api.anthropic.com` ^[raw/document/claude code/claude-code-100-server-managed-settings-2026-04-29.md]
- Server-managed and endpoint-managed settings both occupy the highest precedence tier; the first source that delivers a non-empty configuration wins — server-managed is checked first, then endpoint-managed; sources do not merge ^[raw/document/claude code/claude-code-100-server-managed-settings-2026-04-29.md]
- Configured in Claude.ai under **Admin Settings > Claude Code > Managed settings** as JSON; supports all `settings.json` keys including hooks, environment variables, and managed-only settings ^[raw/document/claude code/claude-code-100-server-managed-settings-2026-04-29.md]
- Fetched at startup and polled hourly during active sessions; cached settings persist through network failures and apply immediately on subsequent launches ^[raw/document/claude code/claude-code-100-server-managed-settings-2026-04-29.md]
- `forceRemoteSettingsRefresh: true` enforces fail-closed startup: CLI blocks until a fresh fetch completes and exits rather than proceeding without policy if the fetch fails ^[raw/document/claude code/claude-code-100-server-managed-settings-2026-04-29.md]
- Shell command settings, custom environment variables (not on the known safe allowlist), and hook configurations trigger a security approval dialog; rejecting exits Claude Code; non-interactive mode (`-p`) skips the dialog ^[raw/document/claude code/claude-code-100-server-managed-settings-2026-04-29.md]

## Details

### Delivery and Caching

On first launch without cached settings, Claude Code fetches settings asynchronously, creating a brief window where restrictions are not yet enforced. On subsequent launches, cached settings apply immediately while fresh settings are fetched in the background. Most settings updates take effect automatically without a restart; OpenTelemetry configuration is an exception requiring a full restart. ^[raw/document/claude code/claude-code-100-server-managed-settings-2026-04-29.md]

If a user clears the server-managed configuration in the admin console intending to fall back to endpoint-managed settings, cached settings persist on client machines until the next successful fetch. The `/status` command shows which managed source is active. ^[raw/document/claude code/claude-code-100-server-managed-settings-2026-04-29.md]

### Fail-Closed Startup

For environments where the brief unenforced window on first launch is unacceptable, `forceRemoteSettingsRefresh: true` forces the CLI to block at startup until remote settings are freshly fetched. If the fetch fails, the CLI exits rather than proceeding without policy. This setting self-perpetuates: once delivered from the server, it is also cached locally so subsequent startups enforce the same behavior even before the first successful fetch of a new session. Network policies must allow connectivity to `api.anthropic.com` when this setting is enabled. ^[raw/document/claude code/claude-code-100-server-managed-settings-2026-04-29.md]

### Security Considerations

Server-managed settings provide centralized policy enforcement but operate as a client-side control. On unmanaged devices, users with admin or sudo access can modify the Claude Code binary, filesystem, or network configuration. If a user edits the cached settings file, tampered settings apply at startup but correct settings restore on the next server fetch. If a user deletes the cached settings file, first-launch behavior occurs with its asynchronous fetch window. If the API is unavailable, cached settings apply if available; otherwise managed settings are not enforced until the next successful fetch. ^[raw/document/claude code/claude-code-100-server-managed-settings-2026-04-29.md]

Server-managed settings are bypassed when users authenticate with a different organization or configure a third-party model provider (`CLAUDE_CODE_USE_BEDROCK`, `CLAUDE_CODE_USE_MANTLE`, `CLAUDE_CODE_USE_VERTEX`, `CLAUDE_CODE_USE_FOUNDRY`, or a non-default `ANTHROPIC_BASE_URL`). For stronger enforcement guarantees on managed devices, endpoint-managed settings deployed through MDM provide OS-level protection against user modification. ^[raw/document/claude code/claude-code-100-server-managed-settings-2026-04-29.md]

### Access Control and Limitations

Only Primary Owner and Owner roles can manage server-managed settings. Settings apply uniformly to all users in the organization; per-group configurations are not yet supported. MCP server configurations cannot be distributed through server-managed settings. ^[raw/document/claude code/claude-code-100-server-managed-settings-2026-04-29.md]

### Audit Logging

Audit log events for settings changes are available through the compliance API or audit log export (contact Anthropic account team for access). Events include the action type, account and device that performed the action, and references to previous and new values. ^[raw/document/claude code/claude-code-100-server-managed-settings-2026-04-29.md]

## Related

- [[entities/claude_code]]
- [[concepts/managed_settings]]
- [[concepts/setting_sources]]
- [[concepts/authentication]]
- [[concepts/permissions]]
- [[concepts/hooks]]
- [[concepts/auto_mode]]
- [[concepts/non_interactive_mode]]
- [[summaries/claude-code-server-managed-settings]]