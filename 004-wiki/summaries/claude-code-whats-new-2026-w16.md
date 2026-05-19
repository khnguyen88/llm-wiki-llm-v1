---
title: "Claude Code Whats New 2026 W16"
summary: "Week 16 (Apr 13-17, 2026): Claude Opus 4.7 with xhigh effort level, Routines on the web, /usage breakdown, /ultrareview cloud review, and native binaries replacing bundled JavaScript"
type: summary
sources:
  - raw/document/claude code/claude-code-121-whats-new-2026-w16-2026-04-29.md
tags:
  - claude-code
  - whats-new
  - release-notes
  - opus-4.7
  - routines
  - ultrareview
  - native-binaries
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Claude Code Whats New 2026 W16

Releases v2.1.105 through v2.1.113, covering April 13-17, 2026. Five major features and multiple incremental improvements. ^[raw/document/claude code/claude-code-121-whats-new-2026-w16-2026-04-29.md]

## Key Points

- Claude Opus 4.7 released as default on Max and Team Premium, available elsewhere via `/model`; adds `xhigh` effort level between `high` and `max`, set as default on first switch to 4.7 ^[raw/document/claude code/claude-code-121-whats-new-2026-w16-2026-04-29.md]
- `/effort` now opens an interactive arrow-key slider when called without arguments, allowing adjustment without remembering level names ^[raw/document/claude code/claude-code-121-whats-new-2026-w16-2026-04-29.md]
- Routines on Claude Code on the web: templated cloud agents triggered by schedule, GitHub event, or API call; each routine gets a tokened `/fire` endpoint for external systems ^[raw/document/claude code/claude-code-121-whats-new-2026-w16-2026-04-29.md]
- `/usage` breakdown shows what drives limits (parallel sessions, subagents, cache misses, long context) with percentage breakdowns for the last 24 hours; press `d` or `w` to switch between day and week views ^[raw/document/claude code/claude-code-121-whats-new-2026-w16-2026-04-29.md]
- `/ultrareview` v2.1.111 fans the branch across parallel cloud reviewers, runs an adversarial critique pass, and returns a verified findings report; the launch dialog now shows a diffstat ^[raw/document/claude code/claude-code-121-whats-new-2026-w16-2026-04-29.md]
- Native binaries (v2.1.113): the `claude` CLI spawns a per-platform native binary instead of bundled JavaScript; the npm package pulls the right binary via optional dependencies like `@anthropic-ai/claude-code-darwin-arm64` ^[raw/document/claude code/claude-code-121-whats-new-2026-w16-2026-04-29.md]
- Auto mode available for Max subscribers on Opus 4.7 without the `--enable-auto-mode` flag ^[raw/document/claude code/claude-code-121-whats-new-2026-w16-2026-04-29.md]

## Notes

Other improvements in this release cycle:

- Session recap shows a one-line summary of what happened while away; `/recap` on demand, toggle via `/config` ^[raw/document/claude code/claude-code-121-whats-new-2026-w16-2026-04-29.md]
- New `/tui` command and `tui` setting switch between classic and flicker-free rendering mid-conversation; focus view moved from `Ctrl+O` to `/focus` ^[raw/document/claude code/claude-code-121-whats-new-2026-w16-2026-04-29.md]
- Push notification tool pings the user's phone via Remote Control when Claude decides it needs attention ^[raw/document/claude code/claude-code-121-whats-new-2026-w16-2026-04-29.md]
- Plugins can ship background watchers via a `monitors` manifest key that auto-arms at session start or on skill invoke ^[raw/document/claude code/claude-code-121-whats-new-2026-w16-2026-04-29.md]
- "Auto (match terminal)" option in `/theme` follows the terminal's dark/light mode ^[raw/document/claude code/claude-code-121-whats-new-2026-w16-2026-04-29.md]
- `/fewer-permission-prompts` scans transcripts for common read-only Bash and MCP calls and proposes an allowlist ^[raw/document/claude code/claude-code-121-whats-new-2026-w16-2026-04-29.md]
- Claude can discover and run built-in commands like `/init`, `/review`, and `/security-review` via the Skill tool ^[raw/document/claude code/claude-code-121-whats-new-2026-w16-2026-04-29.md]
- `PreCompact` hooks can block compaction by exiting with code 2 or returning `"decision":"block"` ^[raw/document/claude code/claude-code-121-whats-new-2026-w16-2026-04-29.md]
- `ENABLE_PROMPT_CACHING_1H` opts API key, Bedrock, Vertex, and Foundry users into 1-hour prompt cache TTL ^[raw/document/claude code/claude-code-121-whats-new-2026-w16-2026-04-29.md]
- `sandbox.network.deniedDomains` setting carves specific domains out of a broader `allowedDomains` wildcard ^[raw/document/claude code/claude-code-121-whats-new-2026-w16-2026-04-29.md]
- `/undo` is now an alias for `/rewind`, and `/proactive` is an alias for `/loop` ^[raw/document/claude code/claude-code-121-whats-new-2026-w16-2026-04-29.md]
- Hardened Bash permissions: deny rules now match through `env`/`sudo`/`watch` wrappers, and `Bash(find:*)` allow rules no longer auto-approve `-exec` or `-delete` ^[raw/document/claude code/claude-code-121-whats-new-2026-w16-2026-04-29.md]

## Related

- [[entities/claude_code]]
- [[entities/claude_code_web]]
- [[concepts/routines]]
- [[concepts/ultrareview]]
- [[concepts/native_binaries]]
- [[concepts/auto_mode]]
- [[concepts/commands]]
- [[concepts/permissions]]
- [[concepts/hooks]]
- [[concepts/plugins]]
- [[concepts/prompt_caching]]
- [[concepts/skills]]
- [[concepts/session_recap]]
- [[summaries/claude-code-whats-new]]