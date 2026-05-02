---
title: "Managed Settings"
summary: "Policy delivery mechanism in Claude Code that enforces organization-wide rules with strict precedence over local developer configuration"
type: concept
sources:
  - raw/document/claude code/claude-code-001-admin-setup-2026-04-29.md
  - raw/document/claude code/claude-code-003-agent-sdk-claude-code-features-2026-04-29.md
  - raw/document/claude code/claude-code-035-auto-mode-config-2026-04-29.md
  - raw/document/claude code/claude-code-044-claude-directory-2026-04-29.md
tags:
  - claude-code
  - admin
  - policy
  - deployment
  - enterprise
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: merged
---

# Managed Settings

Managed settings define organization policy that takes precedence over local developer configuration in Claude Code. They control which tools, commands, servers, and network destinations Claude can reach, and are delivered through four mechanisms with strict precedence order. ^[raw/document/claude code/claude-code-001-admin-setup-2026-04-29.md]

## Key Points

- Four delivery mechanisms in priority order: server-managed (highest, from Claude.ai admin console), plist/registry policy (macOS `com.anthropic.claudecode` plist or Windows `HKLM\SOFTWARE\Policies\ClaudeCode`), file-based managed (platform-specific paths like `/etc/claude-code/managed-settings.json`), and Windows user registry (`HKCU\SOFTWARE\Policies\ClaudeCode`, lowest priority) ^[raw/document/claude code/claude-code-001-admin-setup-2026-04-29.md]
- Server-managed settings require a Claude for Teams or Enterprise plan; deployments on other providers must use file-based or OS-level mechanisms ^[raw/document/claude code/claude-code-001-admin-setup-2026-04-29.md]
- Array settings (`permissions.allow`, `permissions.deny`) merge entries from all sources — developers can extend managed lists but cannot remove entries from them ^[raw/document/claude code/claude-code-001-admin-setup-2026-04-29.md]
- Plist and HKLM registry locations require admin privileges to write, resisting tampering; HKCU is writable without elevation and should be treated as a convenience default rather than an enforcement channel ^[raw/document/claude code/claude-code-001-admin-setup-2026-04-29.md]
- By default, WSL reads only the Linux file path at `/etc/claude-code/managed-settings.json`; setting `wslInheritsWindowsSettings: true` in Windows admin-only sources extends Windows registry and `C:\Program Files\ClaudeCode` policy to WSL on the same machine ^[raw/document/claude code/claude-code-001-admin-setup-2026-04-29.md]
- In the Agent SDK, managed policy settings are always loaded regardless of `settingSources` configuration; they cannot be disabled via `settingSources: []` and can only be removed by deleting the managed settings file from the host ^[raw/document/claude code/claude-code-003-agent-sdk-claude-code-features-2026-04-29.md]
- The `~/.claude.json` global config and auto memory at `~/.claude/projects/<project>/memory/` are also read regardless of `settingSources`; for multi-tenant isolation, set `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1` in `env` ^[raw/document/claude code/claude-code-003-agent-sdk-claude-code-features-2026-04-29.md]
- In auto mode, managed settings provide the organization-wide scope for `autoMode` configuration; developers can extend `environment`, `allow`, and `soft_deny` but cannot remove entries that managed settings provide ^[raw/document/claude code/claude-code-035-auto-mode-config-2026-04-29.md]
- `managed-settings.json` lives at system level (location varies by OS) and is enterprise-enforced; it cannot be overridden by local developer configuration ^[raw/document/claude code/claude-code-044-claude-directory-2026-04-29.md]

## Details

### Control Surfaces

Managed settings can lock down tools, sandbox execution, restrict MCP servers and plugin sources, and control which hooks run. Permission rules allow, ask, or deny specific tools and commands via `permissions.allow` and `permissions.deny`. Permission lockdown (`allowManagedPermissionRulesOnly`) ensures only managed rules apply and disables `--dangerously-skip-permissions`. Sandboxing (`sandbox.enabled`, `sandbox.network.allowedDomains`) provides OS-level filesystem and network isolation with domain allowlists. ^[raw/document/claude code/claude-code-001-admin-setup-2026-04-29.md]

Permission rules and sandboxing address different layers: denying WebFetch blocks Claude's built-in fetch tool, but if Bash is allowed, `curl` and `wget` can still reach any URL. Sandboxing closes that gap with a network domain allowlist enforced at the OS level. ^[raw/document/claude code/claude-code-001-admin-setup-2026-04-29.md]

Additional controls include: managed policy CLAUDE.md (org-wide instructions that load in every session and cannot be excluded), MCP server control (`allowedMcpServers`, `deniedMcpServers`, `allowManagedMcpServersOnly`), plugin marketplace control (`strictKnownMarketplaces`, `blockedMarketplaces`), hook restrictions (`allowManagedHooksOnly`, `allowedHttpHookUrls`), and version floors (`minimumVersion`). ^[raw/document/claude code/claude-code-001-admin-setup-2026-04-29.md]

### Mixed-Provider Deployments

Organizations that mix providers should configure server-managed settings for Claude.ai users plus a file-based or plist/registry fallback so that users on other providers still receive managed policy. Server-managed settings reach devices at authentication time and refresh hourly during active sessions, with no endpoint infrastructure required. ^[raw/document/claude code/claude-code-001-admin-setup-2026-04-29.md]

## Related

- [[entities/claude_code]]
- [[entities/agent_sdk]]
- [[concepts/setting_sources]]
- [[concepts/auto_mode]]
- [[concepts/claude_directory]]