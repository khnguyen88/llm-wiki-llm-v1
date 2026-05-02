---
title: "Claude Code Whats New 2026 W14"
summary: "Week 14 release notes (v2.1.86-91): computer use in CLI, /powerup interactive lessons, flicker-free rendering, per-tool MCP result-size overrides, and plugin executables on PATH"
type: summary
sources:
  - raw/document/claude code/claude-code-119-whats-new-2026-w14-2026-04-29.md
tags:
  - claude-code
  - release-notes
  - computer-use
  - mcp
  - plugins
  - rendering
  - hooks
  - voice
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Claude Code Whats New 2026 W14

Releases v2.1.86 through v2.1.91, covering March 30 -- April 3, 2026. ^[raw/document/claude code/claude-code-119-whats-new-2026-w14-2026-04-29.md]

## Key Points

- Computer use expanded from Desktop to CLI (research preview): Claude can open native apps, click through UI, test changes, and fix what breaks from the terminal; best for closing the loop on apps without an API ^[raw/document/claude code/claude-code-119-whats-new-2026-w14-2026-04-29.md]
- `/powerup` (v2.1.90) provides interactive lessons that teach Claude Code features through animated demos inside the terminal ^[raw/document/claude code/claude-code-119-whats-new-2026-w14-2026-04-29.md]
- Flicker-free rendering (v2.1.89): opt into an alt-screen renderer with virtualized scrollback via `CLAUDE_CODE_NO_FLICKER=1`; the prompt input stays pinned to the bottom and mouse selection works across long conversations ^[raw/document/claude code/claude-code-119-whats-new-2026-w14-2026-04-29.md]
- MCP result-size override (v2.1.91): per-tool `anthropic/maxResultSizeChars` in `_meta` of the `tools/list` entry raises the truncation cap up to 500K characters, keeping large payloads like database schemas inline ^[raw/document/claude code/claude-code-119-whats-new-2026-w14-2026-04-29.md]
- Plugin executables on PATH (v2.1.91): a `bin/` directory at the plugin root is added to the Bash tool's PATH while the plugin is enabled, allowing bare command invocation without absolute paths ^[raw/document/claude code/claude-code-119-whats-new-2026-w14-2026-04-29.md]
- New `PermissionDenied` hook fires on classifier denials; `retry: true` lets Claude try a different approach; `/permissions` -> Recent lets users retry manually with `r` ^[raw/document/claude code/claude-code-119-whats-new-2026-w14-2026-04-29.md]
- New `defer` value for `permissionDecision` in `PreToolUse` hooks: `-p` sessions pause at a tool call and exit with a `deferred_tool_use` payload so an SDK app or custom UI can surface it, then resume with `--resume` ^[raw/document/claude code/claude-code-119-whats-new-2026-w14-2026-04-29.md]

## Notes

- `disableSkillShellExecution` setting blocks inline shell execution from skills, slash commands, and plugin commands ^[raw/document/claude code/claude-code-119-whats-new-2026-w14-2026-04-29.md]
- Edit tool now works on files viewed via `cat` or `sed -n` without requiring a separate Read first ^[raw/document/claude code/claude-code-119-whats-new-2026-w14-2026-04-29.md]
- Hook output over 50K characters is saved to disk with a path and preview instead of injected into context ^[raw/document/claude code/claude-code-119-whats-new-2026-w14-2026-04-29.md]
- Thinking summaries are off by default in interactive sessions; set `showThinkingSummaries: true` to restore ^[raw/document/claude code/claude-code-119-whats-new-2026-w14-2026-04-29.md]
- Voice mode updates: push-to-talk modifier combos, Windows WebSocket support, macOS Apple Silicon mic permission handling ^[raw/document/claude code/claude-code-119-whats-new-2026-w14-2026-04-29.md]
- `claude-cli://` deep links now accept multi-line prompts encoded with `%0A` ^[raw/document/claude code/claude-code-119-whats-new-2026-w14-2026-04-29.md]
- `/buddy` hatches a small creature that watches you code (April 1st feature) ^[raw/document/claude code/claude-code-119-whats-new-2026-w14-2026-04-29.md]

## Related

- [[entities/claude_code]]
- [[concepts/computer_use]]
- [[concepts/commands]]
- [[concepts/mcp]]
- [[concepts/plugins]]
- [[concepts/hooks]]
- [[concepts/permissions]]
- [[concepts/voice_dictation]]
- [[concepts/terminal_config]]
- [[concepts/skills]]