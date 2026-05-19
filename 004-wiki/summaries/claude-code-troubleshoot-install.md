---
title: "Claude Code Troubleshoot Install"
summary: "Fixes for command not found, PATH, permission, network, binary incompatibility, and authentication errors when installing or signing in to Claude Code"
type: summary
sources:
  - raw/document/claude code/claude-code-111-troubleshoot-install-2026-04-29.md
tags:
  - troubleshooting
  - installation
  - authentication
  - claude-code
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Claude Code Troubleshoot Install

## Key Points

- Installation places the binary at `~/.local/bin/claude` (macOS/Linux) or `%USERPROFILE%\.local\bin\claude.exe` (Windows); if `claude` command is not found, add this directory to PATH ^[raw/document/claude code/claude-code-111-troubleshoot-install-2026-04-29.md]
- The installer downloads from `downloads.claude.ai`; if connectivity fails, set `HTTPS_PROXY`/`HTTP_PROXY` for corporate proxies or try Homebrew (`brew install --cask claude-code`) / WinGet (`winget install Anthropic.ClaudeCode`) as alternatives ^[raw/document/claude code/claude-code-111-troubleshoot-install-2026-04-29.md]
- Multiple installations (native, npm global, legacy `~/.claude/local/`, Homebrew) can cause version mismatches; the native installer at `~/.local/bin/claude` is recommended, remove others with `npm uninstall -g` or `rm -rf ~/.claude/local` ^[raw/document/claude code/claude-code-111-troubleshoot-install-2026-04-29.md]
- TLS/SSL errors (`unable to get local issuer certificate`, `SELF_SIGNED_CERT_IN_CHAIN`) from corporate proxies require pointing `curl --cacert` at the corporate CA bundle during install, then setting `NODE_EXTRA_CA_CERTS` for runtime API requests ^[raw/document/claude code/claude-code-111-troubleshoot-install-2026-04-29.md]
- Claude Code requires at least 4 GB of RAM; the Linux OOM killer terminates installs on low-memory VPS instances — add a 2 GB swap file as a workaround ^[raw/document/claude code/claude-code-111-troubleshoot-install-2026-04-29.md]
- Platform-specific issues: WSL1 produces `Exec format error` (fix by converting to WSL2 or using the dynamic linker wrapper); musl/glibc binary mismatches cause shared library errors; `Illegal instruction` indicates CPU architecture mismatch or missing AVX support; `dyld: cannot load` on macOS means the binary requires macOS 13.0+ ^[raw/document/claude code/claude-code-111-troubleshoot-install-2026-04-29.md]
- Authentication resets use `/logout` followed by restarting `claude`; if the browser doesn't open during OAuth, press `c` to copy the URL manually; `ANTHROPIC_API_KEY` overrides subscription OAuth and can cause 403 errors from disabled organizations ^[raw/document/claude code/claude-code-111-troubleshoot-install-2026-04-29.md]

## Notes

- The source document provides a comprehensive symptom-to-fix table at the top covering `command not found`, HTML install scripts, curl failures, TLS errors, OOM kills, platform mismatches, and authentication errors
- Docker installs can hang when run from `/` because the installer scans the entire filesystem; set `WORKDIR /tmp` before running the installer
- On Windows, older Claude Desktop versions register `Claude.exe` in `WindowsApps` that overrides the `claude` CLI on PATH; updating Claude Desktop resolves this

## Related

- [[entities/claude_code]]
- [[concepts/troubleshoot_install]]
- [[concepts/troubleshooting]]
- [[concepts/authentication]]
- [[entities/docker]]