---
title: "Claude Code Whats New 2026 W15"
summary: "Week 15 (April 6-10, 2026) introduced Ultraplan research preview, Monitor tool with /loop self-pacing, /autofix-pr CLI command, and /team-onboarding"
type: summary
sources:
  - raw/document/claude code/claude-code-120-whats-new-2026-w15-2026-04-29.md
tags:
  - claude-code
  - release-notes
  - w15
  - ultraplan
  - monitor
  - auto-fix
  - onboarding
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Claude Code Whats New 2026 W15

Covers releases v2.1.92 through v2.1.101 (April 6-10, 2026). Four headline features shipped alongside quality-of-life improvements for permissions, cost visibility, and platform setup. ^[raw/document/claude code/claude-code-120-whats-new-2026-w15-2026-04-29.md]

## Key Points

- **Ultraplan** entered research preview: `/ultraplan` delegates planning from the CLI to a cloud-based web session; as of v2.1.101 the first run auto-creates a default cloud environment ^[raw/document/claude code/claude-code-120-whats-new-2026-w15-2026-04-29.md]
- **Monitor tool** (v2.1.98) spawns a background watcher that streams events into the conversation; pairs with `/loop` which now self-paces when the interval is omitted ^[raw/document/claude code/claude-code-120-whats-new-2026-w15-2026-04-29.md]
- **`/autofix-pr`** brings PR auto-fix to the CLI: infers the open PR for the current branch and enables auto-fix on Claude Code on the web in one step ^[raw/document/claude code/claude-code-120-whats-new-2026-w15-2026-04-29.md]
- **`/team-onboarding`** (v2.1.101) generates a teammate ramp-up guide from local Claude Code usage so new teammates can replay an experienced user's setup ^[raw/document/claude code/claude-code-120-whats-new-2026-w15-2026-04-29.md]
- **Focus view** (`Ctrl+O` in flicker-free mode) collapses the display to the last prompt, a one-line tool summary with diffstats, and Claude's final response ^[raw/document/claude code/claude-code-120-whats-new-2026-w15-2026-04-29.md]
- **Guided setup wizards** for Bedrock and Vertex AI appear on the login screen under "3rd-party platform", providing step-by-step auth, region, credential, and model pinning ^[raw/document/claude code/claude-code-120-whats-new-2026-w15-2026-04-29.md]
- Default effort level is now `high` for API-key, Bedrock, Vertex, Foundry, Team, and Enterprise users; `/cost` shows per-model and cache-hit breakdown for subscription users ^[raw/document/claude code/claude-code-120-whats-new-2026-w15-2026-04-29.md]

## Quotes

- "Tail a training run, babysit a PR's CI, or auto-fix a dev server crash the moment it happens, all without a Bash sleep loop holding the turn open." ^[raw/document/claude code/claude-code-120-whats-new-2026-w15-2026-04-29.md]
- "Push your branch, run the command, walk away; Claude watches CI and review comments and pushes fixes until it's green." ^[raw/document/claude code/claude-code-120-whats-new-2026-w15-2026-04-29.md]

## Notes

- Other improvements: `/agents` tabbed layout with Running tab, `CLAUDE_CODE_PERFORCE_MODE` makes Edit/Write fail on read-only files with a `p4 edit` hint, OS CA certificate store trusted by default (`CLAUDE_CODE_CERT_STORE=bundled` to opt out), hardened Bash tool permissions for backslash-escaped flags/env-var prefixes/`/dev/tcp` redirects/compound commands, `UserPromptSubmit` hooks can set session title via `hookSpecificOutput.sessionTitle`, statusline `refreshInterval` setting and `workspace.git_worktree` JSON input, Amazon Bedrock powered by Mantle (`CLAUDE_CODE_USE_MANTLE=1`)

## Related

- [[concepts/ultraplan]]
- [[concepts/monitor_tool]]
- [[concepts/auto_fix]]
- [[concepts/commands]]
- [[concepts/cost_tracking]]
- [[concepts/permissions]]
- [[concepts/hooks]]
- [[concepts/statusline]]
- [[entities/amazon_bedrock]]
- [[entities/google_vertex_ai]]
- [[entities/claude_code]]
- [[entities/claude_code_web]]