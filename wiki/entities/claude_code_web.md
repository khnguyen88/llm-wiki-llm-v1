---
title: "Claude Code on the Web"
summary: "Anthropic's cloud-hosted Claude Code platform that runs coding tasks on managed VMs at claude.ai/code with session persistence, environment caching, and GitHub integration"
type: entity
sources:
  - raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md
  - raw/document/claude code/claude-code-047-commands-2026-04-29.md
tags:
  - claude-code
  - cloud
  - web
  - anthropic
  - sessions
  - commands
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Claude Code on the Web

A research preview of Claude Code (available for Pro, Max, Team, and Enterprise with premium or Chat+Code seats) that runs coding tasks on Anthropic-managed cloud infrastructure at claude.ai/code. Sessions persist even if the browser is closed and can be monitored from the Claude mobile app. ^[raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md]

## Key Facts

- Cloud sessions run in isolated Anthropic-managed VMs with the repository cloned from GitHub ^[raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md]
- Two GitHub authentication methods: GitHub App (per-repo scoping) and `/web-setup` (syncs local `gh` CLI token); the GitHub App is required for auto-fix PR functionality ^[raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md]
- Team and Enterprise admins can disable `/web-setup` with the Quick web setup toggle at claude.ai/admin-settings/claude-code ^[raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md]
- Each session has a transcript URL on claude.ai and exposes its ID via the `CLAUDE_CODE_REMOTE_SESSION_ID` environment variable for linking artifacts back to the session ^[raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md]
- Repos are cloned from GitHub (not the local machine) when using `--remote`; push local commits first to include them ^[raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md]
- Repositories without GitHub can be bundled and uploaded directly using `CCR_FORCE_BUNDLE=1`; bundles must be under 100 MB and untracked files are not included ^[raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md]
- Sessions can be shared (Team visibility for Enterprise/Team, Public visibility for Max/Pro), archived, or permanently deleted ^[raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md]
- The `check-tools` command (cloud sessions only) lists exact pre-installed tool versions ^[raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md]
- Resource limits per session: 4 vCPUs, 16 GB RAM, 30 GB disk ^[raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md]
- `/desktop` (macOS/Windows only) continues the current terminal session in the Claude Code Desktop app; `/teleport` (alias /tp) pulls a web session into the terminal ^[raw/document/claude code/claude-code-047-commands-2026-04-29.md]

## Related

- [[entities/claude_code]]
- [[entities/github]]
- [[entities/docker]]
- [[concepts/cloud_environment]]
- [[concepts/network_access]]
- [[concepts/teleport]]
- [[concepts/auto_fix]]
- [[concepts/sessions]]
- [[concepts/commands]]