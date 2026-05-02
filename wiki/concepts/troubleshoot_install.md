---
title: "Troubleshoot Install"
summary: "Diagnostic and resolution procedures for installation, PATH, permission, binary incompatibility, and authentication errors when setting up Claude Code"
type: concept
sources:
  - raw/document/claude code/claude-code-111-troubleshoot-install-2026-04-29.md
tags:
  - troubleshooting
  - installation
  - authentication
  - claude-code
  - diagnostics
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Troubleshoot Install

Procedures for diagnosing and fixing installation, PATH, permission, binary compatibility, and authentication errors when installing or signing in to Claude Code. For runtime issues after Claude Code is working, see [[concepts/troubleshooting]]. ^[raw/document/claude code/claude-code-111-troubleshoot-install-2026-04-29.md]

## Key Points

- The installer places the binary at `~/.local/bin/claude` (macOS/Linux) or `%USERPROFILE%\.local\bin\claude.exe` (Windows); `command not found` after install means this directory is not on PATH ^[raw/document/claude code/claude-code-111-troubleshoot-install-2026-04-29.md]
- Multiple installations (native, npm `-g`, legacy `~/.claude/local/`, Homebrew cask, WinGet) can conflict; keep only the native install and remove others ^[raw/document/claude code/claude-code-111-troubleshoot-install-2026-04-29.md]
- The installer requires write access to `~/.local/bin/` and `~/.claude/`; use `sudo chown -R $(whoami) ~/.local` if permissions are wrong ^[raw/document/claude code/claude-code-111-troubleshoot-install-2026-04-29.md]
- Claude Code requires at least 4 GB RAM; the Linux OOM killer terminates installs on low-memory servers, fixed by adding 2 GB swap ^[raw/document/claude code/claude-code-111-troubleshoot-install-2026-04-29.md]
- `ANTHROPIC_API_KEY` overrides subscription OAuth and can cause "This organization has been disabled" 403 errors from stale keys; unset it and remove it from shell profiles to use subscription authentication ^[raw/document/claude code/claude-code-111-troubleshoot-install-2026-04-29.md]

## Details

### Network and Connectivity

The installer downloads from `downloads.claude.ai`. If `curl -sI https://downloads.claude.ai/claude-code-releases/latest` returns no output, a connection timeout, or `Could not resolve host`, the network is blocking the download. Corporate firewalls and proxies are the most common cause. Set `HTTP_PROXY` and `HTTPS_PROXY` environment variables before running the installer. Alternative install methods (Homebrew on macOS, WinGet on Windows) bypass the shell installer entirely. ^[raw/document/claude code/claude-code-111-troubleshoot-install-2026-04-29.md]

TLS/SSL handshake failures (`curl: (35) TLS connect error`, `schannel` errors, `unable to get local issuer certificate`) indicate CA certificate or proxy issues. Solutions include updating system CA certificates (`sudo apt-get install ca-certificates` on Debian/Ubuntu), enabling TLS 1.2 in PowerShell (`[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12`), and pointing curl at a corporate CA bundle with `--cacert`. For runtime API requests after install, set `NODE_EXTRA_CA_CERTS` to the same CA bundle path. On Windows, certificate revocation check failures (`CRYPT_E_NO_REVOCATION_CHECK`, `CRYPT_E_REVOCATION_OFFLINE`) behind corporate firewalls can be bypassed with `curl --ssl-revoke-best-effort`. ^[raw/document/claude code/claude-code-111-troubleshoot-install-2026-04-29.md]

### Binary and Platform Issues

If the install script returns HTML instead of a shell script (errors like `syntax error near unexpected token '<'` or PowerShell `Invoke-Expression: Missing argument in parameter list`), the install URL returned an HTML page, possibly because Claude Code is unavailable in the user's country. On Windows, using the wrong shell command (CMD vs PowerShell vs bash) produces distinct errors: `'irm' is not recognized` in CMD, `The token '&&' is not valid` in PowerShell with the CMD command, and `'bash' is not recognized` when running the macOS/Linux command. ^[raw/document/claude code/claude-code-111-troubleshoot-install-2026-04-29.md]

Platform-specific binary issues: WSL1 produces `Exec format error` (fix by converting to WSL2 with `wsl --set-version <DistroName> 2`, or invoke via the dynamic linker `/lib64/ld-linux-x86-64.so.2`); musl/glibc mismatches cause `Error loading shared library` (Alpine requires `apk add libgcc libstdc++ ripgrep`); `Illegal instruction` means CPU lacks required instructions (AVX, ~pre-2013 Intel/AMD); `dyld: cannot load` on macOS means the binary requires macOS 13.0+. Claude Code does not support 32-bit Windows. On Windows, older Claude Desktop versions register a `Claude.exe` in `WindowsApps` that takes PATH priority over the CLI. ^[raw/document/claude code/claude-code-111-troubleshoot-install-2026-04-29.md]

Docker installs hang when run from `/` because the installer scans the entire filesystem; set `WORKDIR /tmp` before running the installer or increase Docker memory limits to 4 GB. npm install errors in WSL occur when WSL picks up the Windows `npm` binary (`/mnt/c/` paths); fix by installing Node via the Linux package manager or nvm. The npm package delivers the native binary through per-platform optional dependencies (`@anthropic-ai/claude-code-darwin-arm64`, etc.); if these are skipped with `--omit=optional` or `--no-optional`, the binary is not available. ^[raw/document/claude code/claude-code-111-troubleshoot-install-2026-04-29.md]

### Authentication Troubleshooting

Login failures resolve in most cases by running `/logout`, closing Claude Code, and restarting with `claude`. If the browser doesn't open during OAuth, press `c` to copy the URL to the clipboard and paste it manually. OAuth `Invalid code` errors mean the login code expired or was truncated; press Enter to retry and complete login quickly. In WSL2, if the browser won't open, set the `BROWSER` environment variable to the Windows browser path; if pasting the code doesn't work in the terminal, use `claude auth login` as a fallback. ^[raw/document/claude code/claude-code-111-troubleshoot-install-2026-04-29.md]

A 403 Forbidden error after login means either the subscription is inactive (check at claude.ai/settings), the Anthropic Console account lacks the "Claude Code" or "Developer" role (admins assign this under Settings → Members), or a corporate proxy is interfering. When `ANTHROPIC_API_KEY` is set in the environment, it overrides subscription OAuth credentials, producing "This organization has been disabled" errors if the key belongs to a disabled organization. On macOS, login can fail when the Keychain is locked or its password is out of sync; run `security unlock-keychain ~/Library/Keychains/login.keychain-db` or resync via Keychain Access. ^[raw/document/claude code/claude-code-111-troubleshoot-install-2026-04-29.md]

Cloud provider credentials (Bedrock, Vertex, Foundry) that fail with `Could not load the default credentials` or `ChainedTokenCredential authentication failed` typically mean the cloud CLI is not authenticated in the current shell. For Bedrock, run `aws sts get-caller-identity`; for Vertex, set `ANTHROPIC_VERTEX_PROJECT_ID` and `CLOUD_ML_REGION` then run `gcloud auth application-default login`; for Foundry, set `ANTHROPIC_FOUNDRY_API_KEY` or run `az login`. If credentials work in the terminal but not in VS Code or JetBrains, the IDE process didn't inherit the shell environment. ^[raw/document/claude code/claude-code-111-troubleshoot-install-2026-04-29.md]

## Related

- [[entities/claude_code]]
- [[concepts/troubleshooting]]
- [[concepts/authentication]]
- [[entities/docker]]
- [[summaries/claude-code-troubleshoot-install]]