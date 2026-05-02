---
title: "Claude Code on the Web"
summary: "Anthropic's cloud-hosted Claude Code platform that runs coding tasks on managed VMs at claude.ai/code with session persistence, environment caching, and GitHub integration"
type: entity
sources:
  - raw/document/claude code/claude-code-043-claude-code-on-the-web-2026-04-29.md
  - raw/document/claude code/claude-code-047-commands-2026-04-29.md
  - raw/document/claude code/claude-code-104-slack-2026-04-29.md
  - raw/document/claude code/claude-code-112-ultraplan-2026-04-29.md
  - raw/document/claude code/claude-code-113-ultrareview-2026-04-29.md
  - raw/document/claude code/claude-code-116-web-quickstart-2026-04-29.md
  - raw/document/claude code/claude-code-117-whats-new-2026-04-29.md
  - raw/document/claude code/claude-code-118-whats-new-2026-w13-2026-04-29.md
tags:
  - claude-code
  - cloud
  - web
  - anthropic
  - sessions
  - commands
  - slack
  - quickstart
  - comparison
created: "2026-05-01T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
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
- Slack-initiated @Claude mentions create Claude Code sessions on the web; sessions are accessible in Claude Code history and, for Enterprise/Team accounts, automatically visible to the organization ^[raw/document/claude code/claude-code-104-slack-2026-04-29.md]
- Ultraplan (research preview, v2.1.91+) delegates planning from the CLI to a cloud web session in plan mode; the user reviews the plan in the browser with inline comments and emoji reactions, then chooses to execute on the web or teleport back to the terminal ^[raw/document/claude code/claude-code-112-ultraplan-2026-04-29.md]
- Ultrareview (research preview, v2.1.86+) runs deep multi-agent code reviews in the cloud sandbox; findings are independently reproduced and verified before being returned, and the review runs entirely remotely so the local terminal stays free ^[raw/document/claude code/claude-code-113-ultrareview-2026-04-29.md]
- Web sessions are best for parallel tasks (each gets its own session and branch), repos not available locally, well-defined tasks needing minimal steering, and code exploration without a local checkout; for work needing local config, tools, or environment, Remote Control or local CLI is a better fit ^[raw/document/claude code/claude-code-116-web-quickstart-2026-04-29.md]
- Comparison of run modes: web (cloud VM, chat from claude.ai/mobile, no local config, requires GitHub, persists after disconnect, Auto accept edits or Plan modes only, configurable network), Remote Control (local machine, chat from claude.ai/mobile, uses local config, no GitHub required, runs while terminal is open, Ask/Auto accept edits/Plan modes, local network), Terminal CLI (local machine, chat from terminal, uses local config, no GitHub required, stops on disconnect, all permission modes, local network), Desktop app (local or cloud VM, Desktop UI, config depends on session type, GitHub only for cloud sessions, persistence depends on session type, modes depend on session type, network depends on session type) ^[raw/document/claude code/claude-code-116-web-quickstart-2026-04-29.md]
- Review workflow: diff view shows lines added/removed across the session; inline comments on specific lines queue until the next message, then bundle with it so Claude sees file and line context without the user describing where the problem is; PR creation offers full PR, draft, or jumping to GitHub's compose page ^[raw/document/claude code/claude-code-116-web-quickstart-2026-04-29.md]
- Web sessions follow a lifecycle: clone and prepare → configure network → work (analyze, make changes, run tests, self-check) → push branch; the session stays live after the branch push so PR creation and further edits happen within the same conversation ^[raw/document/claude code/claude-code-116-web-quickstart-2026-04-29.md]
- `/web-setup` (CLI) syncs the local `gh` token to the Claude account and creates a default cloud environment with Trusted network access if none exists; requires CLI v2.1.80+ and claude.ai subscription auth; not available for organizations with Zero Data Retention enabled ^[raw/document/claude code/claude-code-116-web-quickstart-2026-04-29.md]
- Cloud sessions only support Auto accept edits and Plan permission modes; Ask, Auto, and Bypass are not available ^[raw/document/claude code/claude-code-116-web-quickstart-2026-04-29.md]
- The web interface received a redesign in Week 17 (v2.1.114-119) with a new sessions sidebar and drag-and-drop layout ^[raw/document/claude code/claude-code-117-whats-new-2026-04-29.md]
- Auto-fix on the web includes a CI panel toggle that enables Claude to watch CI, fix failures and nits, and push until the PR is green ^[raw/document/claude code/claude-code-118-whats-new-2026-w13-2026-04-29.md]

## Related

- [[entities/claude_code]]
- [[entities/github]]
- [[entities/docker]]
- [[concepts/cloud_environment]]
- [[concepts/network_access]]
- [[concepts/teleport]]
- [[concepts/auto_fix]]
- [[concepts/sessions]]
- [[entities/slack]]
- [[concepts/routing_mode]]
- [[concepts/commands]]
- [[concepts/ultraplan]]
- [[concepts/ultrareview]]
- [[summaries/claude-code-ultrareview]]
- [[summaries/claude-code-web-quickstart]]
- [[concepts/session_prefill]]
- [[concepts/permissions]]
- [[concepts/parallel_sessions]]
- [[summaries/claude-code-whats-new-2026-w13]]