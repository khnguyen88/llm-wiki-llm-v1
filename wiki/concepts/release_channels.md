---
title: "Release Channels"
summary: "Version delivery mechanism controlling whether Claude Code receives updates immediately on the latest channel or on a delayed stable channel, with auto-update, version pinning, and manual update options"
type: concept
sources:
  - raw/document/claude code/claude-code-102-setup-2026-04-29.md
tags:
  - claude-code
  - release-channels
  - auto-updates
  - versioning
  - deployment
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Release Channels

Release channels control which version track Claude Code follows for updates. The two channels — `"latest"` and `"stable"` — determine whether new features arrive immediately or on a delayed schedule that skips releases with major regressions. ^[raw/document/claude code/claude-code-102-setup-2026-04-29.md]

## Key Points

- `"latest"` (default) receives new features as soon as they are released; `"stable"` is typically about one week behind and skips releases with major regressions ^[raw/document/claude code/claude-code-102-setup-2026-04-29.md]
- Configured via the `autoUpdatesChannel` setting in settings.json or through `/config` → Auto-update channel; for enterprise deployments, enforce a consistent channel via [[concepts/managed_settings]] ^[raw/document/claude code/claude-code-102-setup-2026-04-29.md]
- Native installations auto-update: Claude Code checks for updates on startup and periodically while running, downloading and installing in the background; updates take effect on the next start ^[raw/document/claude code/claude-code-102-setup-2026-04-29.md]
- Homebrew, WinGet, and Linux package manager (apt, dnf, apk) installations do not auto-update; Homebrew cask choice determines channel: `claude-code` tracks stable and `claude-code@latest` tracks latest ^[raw/document/claude code/claude-code-102-setup-2026-04-29.md]
- `DISABLE_AUTOUPDATER=1` in `env` stops the background auto-update check but still allows `claude update` and `claude install`; `DISABLE_UPDATES` blocks all update paths including manual updates ^[raw/document/claude code/claude-code-102-setup-2026-04-29.md]
- The channel chosen at native install time becomes the default for auto-updates; it can be changed later via `autoUpdatesChannel` or `/config` ^[raw/document/claude code/claude-code-102-setup-2026-04-29.md]

## Details

### Minimum Version Pinning

The `minimumVersion` setting establishes a version floor. Background auto-updates and `claude update` refuse to install any version below this value, so moving to the stable channel does not downgrade an installation already on a newer latest build. In managed settings, this enforces an organization-wide minimum that user and project settings cannot override. ^[raw/document/claude code/claude-code-102-setup-2026-04-29.md]

Switching from `"latest"` to `"stable"` via `/config` prompts the user to either stay on the current version (which sets `minimumVersion` to that version) or allow the downgrade. Switching back to `"latest"` clears `minimumVersion`. ^[raw/document/claude code/claude-code-102-setup-2026-04-29.md]

### Manual Updates

`claude update` applies an update immediately without waiting for the next background check. For Homebrew, run `brew upgrade claude-code` or `brew upgrade claude-code@latest`. For WinGet, run `winget upgrade Anthropic.ClaudeCode`. Homebrew keeps old versions on disk; run `brew cleanup` periodically to reclaim space. ^[raw/document/claude code/claude-code-102-setup-2026-04-29.md]

A known issue exists where Claude Code may notify of updates before the new version is available in package managers (Homebrew, WinGet, apt, dnf, apk). If an upgrade fails, wait and try again later. ^[raw/document/claude code/claude-code-102-setup-2026-04-29.md]

## Related

- [[entities/claude_code]]
- [[concepts/managed_settings]]
- [[concepts/setting_sources]]