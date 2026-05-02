---
title: "Cloud Environment"
summary: "Anthropic-managed VMs that host Claude Code on the Web sessions, with pre-installed runtimes, configurable setup scripts, and environment caching for fast startup"
type: concept
sources:
  - raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md
tags:
  - claude-code
  - cloud
  - vm
  - setup
  - caching
  - environment
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Cloud Environment

Each Claude Code on the Web session runs in a fresh Anthropic-managed VM with the user's repository cloned. The cloud environment determines what's available at session start and how it can be customized. ^[raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md]

## Key Points

- Repositories are cloned from GitHub; anything committed to the repo is available, but local-only configuration (user `~/.claude/CLAUDE.md`, user-scoped plugins, `claude mcp add` servers, API tokens) is not ^[raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md]
- Pre-installed runtimes include Python 3.x, Node.js 20/21/22, Ruby 3.1-3.3, PHP 8.4, OpenJDK 21, Go, Rust, C/C++ (GCC, Clang), Docker, PostgreSQL 16, and Redis 7.0 ^[raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md]
- Setup scripts are Bash scripts that run before Claude Code launches on the first session; after completion, the filesystem is snapshotted and reused, so later sessions skip the script ^[raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md]
- Environment caching reuses the snapshot for roughly seven days or until the setup script or network settings change; resuming an existing session never re-runs the setup script ^[raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md]
- Setup scripts run as root on Ubuntu 24.04 and need network access to reach registries; they fail under "None" network access; append `|| true` to non-critical commands to avoid blocking the session ^[raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md]
- PostgreSQL and Redis are pre-installed but not running by default; ask Claude to start them with `service postgresql start` or `service redis-server start` ^[raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md]

## Details

The cloud environment is configured per environment, not per session. Environments control network access, environment variables, and the setup script. Environment variables use `.env` format (one `KEY=value` pair per line, no quotes around values). Plugins declared in the repo's `.claude/settings.json` are installed at session start from the declared marketplace, requiring network access to reach the marketplace source.

Setup scripts differ from [[concepts/hooks|SessionStart hooks]] in scope and timing. Setup scripts are attached to the cloud environment, configured in the cloud environment UI, and run before Claude Code launches only when no cached environment is available. SessionStart hooks are attached to the repository, configured in `.claude/settings.json`, and run after Claude Code launches on every session including resumed ones. To run cloud-only dependency installation, check the `CLAUDE_CODE_REMOTE` environment variable in a SessionStart hook script. The `CLAUDE_CODE_REMOTE` variable is set to `true` in cloud sessions.

Mid-session package installs do not carry over to other sessions. To persist packages across sessions, add them to the setup script. To persist environment variables for subsequent Bash commands, write to the file at `$CLAUDE_ENV_FILE`.

## Related

- [[entities/claude_code_web]]
- [[concepts/network_access]]
- [[concepts/sessions]]
- [[concepts/hooks]]