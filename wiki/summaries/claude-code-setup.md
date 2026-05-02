---
title: "Claude Code Setup"
summary: "System requirements, platform-specific installation, release channels, version management, binary verification, and uninstallation for Claude Code"
type: summary
sources:
  - raw/document/claude code/claude-code-102-setup-2026-04-29.md
tags:
  - claude-code
  - setup
  - installation
  - release-channels
  - code-signing
  - platform-support
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Claude Code Setup

## Key Points

- Supported platforms: macOS 13.0+, Windows 10 1809+/Server 2019+, Ubuntu 20.04+, Debian 10+, Alpine 3.19+; requires 4 GB+ RAM, x64 or ARM64 processor, internet connection, and Bash/Zsh/PowerShell/CMD shell ^[raw/document/claude code/claude-code-102-setup-2026-04-29.md]
- Native install is recommended: `curl -fsSL https://claude.ai/install.sh | bash` (macOS/Linux/WSL) or `irm https://claude.ai/install.ps1 | iex` (Windows PowerShell); native installations auto-update in the background ^[raw/document/claude code/claude-code-102-setup-2026-04-29.md]
- Windows has two modes: native (with Git for Windows recommended, no sandboxing) and WSL 2 (sandboxing supported, for Linux toolchains); WSL 1 is also supported but without sandboxing ^[raw/document/claude code/claude-code-102-setup-2026-04-29.md]
- Homebrew casks (`claude-code` for stable, `claude-code@latest` for rolling) and WinGet (`winget install Anthropic.ClaudeCode`) do not auto-update; Linux package manager installations (apt, dnf, apk) also require manual updates ^[raw/document/claude code/claude-code-102-setup-2026-04-29.md]
- Two release channels: `"latest"` (default, receives features immediately) and `"stable"` (about one week behind, skips releases with major regressions); configured via `autoUpdatesChannel` setting or `/config` ^[raw/document/claude code/claude-code-102-setup-2026-04-29.md]
- `minimumVersion` establishes a version floor that prevents downgrades; enforced in managed settings for organization-wide control; switching from latest to stable via `/config` prompts to either stay on the current version or allow the downgrade ^[raw/document/claude code/claude-code-102-setup-2026-04-29.md]
- Every release publishes a `manifest.json` with SHA256 checksums for all platform binaries, signed by the Anthropic GPG key (fingerprint `31DD DE24 DDFA B679 F42D 7BD2 BAA9 29FF 1A7E CACE`); macOS binaries are signed by "Anthropic PBC" and notarized by Apple, Windows binaries are signed by "Anthropic, PBC" ^[raw/document/claude code/claude-code-102-setup-2026-04-29.md]

## Notes

- The source covers installation, updates, and uninstallation comprehensively but does not describe runtime configuration (covered in other documents)
- Alpine and musl-based distributions require `libgcc`, `libstdc++`, and `ripgrep` packages plus `USE_BUILTIN_RIPGREP=0` in settings
- Authentication is covered briefly (Pro/Max/Team/Enterprise/Console account required); detailed credential sources are in the authentication concept page
- The npm package installs the same native binary via per-platform optional dependencies; it does not invoke Node at runtime

## Related

- [[entities/claude_code]]
- [[concepts/authentication]]
- [[concepts/release_channels]]
- [[concepts/binary_verification]]
- [[concepts/managed_settings]]
- [[concepts/setting_sources]]