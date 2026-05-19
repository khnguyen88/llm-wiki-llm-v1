---
title: "Claude Code Whats New 2026 W17"
summary: "Week 17 (April 20-24, 2026) release introducing ultrareview research preview, automatic session recaps, custom color themes, redesigned web interface, and multiple CLI improvements"
type: summary
sources:
  - raw/document/claude code/claude-code-122-whats-new-2026-w17-2026-04-29.md
tags:
  - claude-code
  - release-notes
  - ultrareview
  - themes
  - web-redesign
  - w17
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Claude Code Whats New 2026 W17

Releases v2.1.114 through v2.1.119, covering April 20-24, 2026.

## Key Points

- Ultrareview entered public research preview, running a fleet of bug-hunting agents against a branch or PR with findings returned to the CLI or Desktop automatically ^[raw/document/claude code/claude-code-122-whats-new-2026-w17-2026-04-29.md]
- Session recap provides automatic one-line summaries when returning to a terminal after switching focus away; `/recap` generates on demand and automatic recaps can be disabled via `/config` ^[raw/document/claude code/claude-code-122-whats-new-2026-w17-2026-04-29.md]
- Custom themes (v2.1.118) allow building and switching named color themes from `/theme` or editing JSON in `~/.claude/themes/`; plugins can also ship themes ^[raw/document/claude code/claude-code-122-whats-new-2026-w17-2026-04-29.md]
- Claude Code on the web received a redesign matching the desktop app with a sessions sidebar, drag-and-drop layout, and a refreshed routines view; key parts were rebuilt for quicker responses and more reliable experience ^[raw/document/claude code/claude-code-122-whats-new-2026-w17-2026-04-29.md]
- Vim visual mode adds `v` for character selection and `V` for line selection in the prompt input, with operators and visual feedback ^[raw/document/claude code/claude-code-122-whats-new-2026-w17-2026-04-29.md]
- Hooks can call MCP tools directly via `type: "mcp_tool"`, hitting an already-connected server without spawning a process ^[raw/document/claude code/claude-code-122-whats-new-2026-w17-2026-04-29.md]
- `/cost` and `/stats` merged into `/usage`; old names still work as typing shortcuts that open the relevant tab ^[raw/document/claude code/claude-code-122-whats-new-2026-w17-2026-04-29.md]
- `/config` changes (theme, editor mode, verbose, and similar) now persist to `~/.claude/settings.json` and follow the same project/local/policy precedence as other settings ^[raw/document/claude code/claude-code-122-whats-new-2026-w17-2026-04-29.md]
- Default effort level for Pro and Max subscribers on Opus 4.6 and Sonnet 4.6 is now `high` (was `medium`) ^[raw/document/claude code/claude-code-122-whats-new-2026-w17-2026-04-29.md]
- Native macOS and Linux builds replace `Glob` and `Grep` tools with embedded `bfs` and `ugrep` available through Bash for faster searches without a separate tool round-trip ^[raw/document/claude code/claude-code-122-whats-new-2026-w17-2026-04-29.md]
- Opus 4.7 sessions now compute against the model's native 1M context window, fixing inflated `/context` percentages and premature autocompaction; `/resume` on large sessions is up to 67% faster and offers to summarize stale sessions before re-reading them ^[raw/document/claude code/claude-code-122-whats-new-2026-w17-2026-04-29.md]
- Forked subagents can be enabled on external builds with `CLAUDE_CODE_FORK_SUBAGENT=1` ^[raw/document/claude code/claude-code-122-whats-new-2026-w17-2026-04-29.md]
- Auto mode supports `"$defaults"` in `autoMode.allow`, `soft_deny`, or `environment` to add custom rules alongside the built-in list instead of replacing it ^[raw/document/claude code/claude-code-122-whats-new-2026-w17-2026-04-29.md]
- `--from-pr` now accepts GitLab merge request, Bitbucket pull request, and GitHub Enterprise PR URLs in addition to github.com ^[raw/document/claude code/claude-code-122-whats-new-2026-w17-2026-04-29.md]
- New `claude plugin tag` command creates release git tags for plugins with version validation ^[raw/document/claude code/claude-code-122-whats-new-2026-w17-2026-04-29.md]

## Related

- [[entities/claude_code]]
- [[entities/claude_code_web]]
- [[concepts/ultrareview]]
- [[concepts/session_recap]]
- [[concepts/custom_themes]]
- [[concepts/hooks]]
- [[concepts/commands]]
- [[concepts/auto_mode]]
- [[concepts/plugins]]
- [[concepts/vim_editor_mode]]
- [[concepts/subagent_forking]]
- [[concepts/native_binaries]]
- [[concepts/context_window]]