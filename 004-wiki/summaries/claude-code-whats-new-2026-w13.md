---
title: "Claude Code Whats New 2026 W13"
summary: "Week 13 (March 23-27, 2026) introduced auto mode, computer use on Desktop, PR auto-fix, transcript search, PowerShell tool, and conditional hooks across releases v2.1.83-85"
type: summary
sources:
  - raw/document/claude code/claude-code-118-whats-new-2026-w13-2026-04-29.md
tags:
  - claude-code
  - whats-new
  - release-notes
  - w13
  - auto-mode
  - computer-use
  - auto-fix
  - powershell
  - hooks
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Claude Code Whats New 2026 W13

Releases v2.1.83 through v2.1.85, covering March 23-27, 2026. Six features shipped plus a batch of smaller improvements. ^[raw/document/claude code/claude-code-118-whats-new-2026-w13-2026-04-29.md]

## Key Points

- **Auto mode** (research preview) routes permission prompts to a classifier; safe edits and commands run without interruption while destructive or suspicious actions are blocked and surfaced — positioned as the middle ground between approving every file write and `--dangerously-skip-permissions` ^[raw/document/claude code/claude-code-118-whats-new-2026-w13-2026-04-29.md]
- **Computer use on Desktop** lets Claude control the actual desktop from the Claude Code Desktop app: open native apps, click through the iOS simulator, drive hardware control panels, and verify changes on screen; disabled by default, asks before each action ^[raw/document/claude code/claude-code-118-whats-new-2026-w13-2026-04-29.md]
- **PR auto-fix on the web** watches CI after a PR is opened, fixes failures and nits, and pushes until green; toggle Auto fix in the CI panel after creating a PR on Claude Code web ^[raw/document/claude code/claude-code-118-whats-new-2026-w13-2026-04-29.md]
- **Transcript search** (v2.1.83) adds `/` search in transcript mode with `n`/`N` to step through matches ^[raw/document/claude code/claude-code-118-whats-new-2026-w13-2026-04-29.md]
- **PowerShell tool** (preview, v2.1.84) provides native cmdlet, pipeline, and path support on Windows alongside Bash; opt in with `CLAUDE_CODE_USE_POWERSHELL_TOOL=1` ^[raw/document/claude code/claude-code-118-whats-new-2026-w13-2026-04-29.md]
- **Conditional hooks** (v2.1.85) add an `if` field using permission rule syntax so hooks fire only for matching tool calls (e.g., `Bash(git commit *)`), cutting process overhead on busy sessions ^[raw/document/claude code/claude-code-118-whats-new-2026-w13-2026-04-29.md]

## Notes

Other improvements in this release cycle:

- Plugin `userConfig` is now public: prompts for settings at enable time with keychain-backed secrets
- Pasted images insert `[Image #N]` chips you can reference positionally
- `managed-settings.d/` drop-in directory for layered policy fragments
- `CwdChanged` and `FileChanged` hook events for direnv-style setups
- Agents can declare `initialPrompt` in frontmatter to auto-submit a first turn
- `Ctrl+X Ctrl+E` opens external editor, matching readline convention
- Interrupting before any response restores your input automatically
- `/status` now works while Claude is responding
- Deep links open in your preferred terminal, not the first-detected one
- Idle-return nudge to `/clear` after 75+ minutes away

^[raw/document/claude code/claude-code-118-whats-new-2026-w13-2026-04-29.md]

## Related

- [[concepts/auto_mode]]
- [[concepts/computer_use]]
- [[concepts/auto_fix]]
- [[concepts/transcript_search]]
- [[concepts/powershell_tool]]
- [[concepts/hooks]]
- [[entities/claude_code]]
- [[entities/claude_code_web]]
- [[concepts/managed_settings]]
- [[concepts/plugins]]
- [[concepts/sessions]]