---
title: "Claude Code Claude Code On The Web"
summary: "Claude Code on the Web runs coding tasks on Anthropic-managed cloud VMs with GitHub integration, environment caching, network access controls, and session portability between web and terminal"
type: summary
sources:
  - raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md
tags:
  - claude-code
  - cloud
  - web
  - sessions
  - github
  - remote
  - teleport
  - auto-fix
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Claude Code Claude Code On The Web

## Key Points

- Claude Code on the Web (research preview for Pro, Max, Team, and Enterprise with premium seats) runs tasks on Anthropic-managed cloud VMs at claude.ai/code; sessions persist even if the browser is closed ^[raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md]
- Two GitHub authentication methods: the GitHub App (per-repo scoping, required for auto-fix) and `/web-setup` (syncs local `gh` token, suited for individual developers) ^[raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md]
- Cloud sessions start in fresh VMs with pre-installed runtimes (Python, Node.js, Ruby, PHP, Java, Go, Rust, C/C++, Docker, PostgreSQL, Redis) and 4 vCPU / 16 GB RAM / 30 GB disk limits ^[raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md]
- Setup scripts run before Claude launches on first session; the filesystem is snapshotted and reused for subsequent sessions, keeping startup fast even with large dependency installs ^[raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md]
- Network access has four levels (None, Trusted, Full, Custom) with a default Trusted allowlist covering major package registries, GitHub, cloud SDKs, and container registries; all outbound traffic passes through a security proxy ^[raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md]
- `--remote` creates new cloud sessions from the terminal; `--teleport` pulls cloud sessions into a local terminal; sessions can also be sent from the Desktop app's "Continue in" menu ^[raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md]
- Auto-fix watches PRs for CI failures and review comments, pushing fixes when confident; requires the Claude GitHub App and can be enabled from the web UI, CLI (`/autofix-pr`), or mobile app ^[raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md]

## Quotes

- "Each session runs in a fresh Anthropic-managed VM with your repository cloned." ^[raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md]
- "The setup script runs the first time you start a session in an environment. After it completes, Anthropic snapshots the filesystem and reuses that snapshot as the starting point for later sessions." ^[raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md]
- "Sensitive credentials such as git credentials or signing keys are never inside the sandbox with Claude Code. Authentication is handled through a secure proxy using scoped credentials." ^[raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md]

## Notes

- Zero Data Retention organizations cannot use `/web-setup` or other cloud session features
- Organizations with IP allowlisting will see authentication errors from cloud sessions since traffic originates from Anthropic infrastructure, not the organization's network
- Repositories without GitHub can be bundled and uploaded directly (under 100 MB), but sessions cannot push results back to the remote

## Related

- [[entities/claude_code]]
- [[entities/claude_code_web]]
- [[entities/github]]
- [[entities/docker]]
- [[concepts/cloud_environment]]
- [[concepts/network_access]]
- [[concepts/teleport]]
- [[concepts/auto_fix]]
- [[concepts/sessions]]
- [[concepts/hooks]]