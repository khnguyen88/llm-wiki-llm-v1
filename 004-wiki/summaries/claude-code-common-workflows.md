---
title: "Claude Code Common Workflows"
summary: "Step-by-step guides for everyday development tasks with Claude Code: exploring codebases, debugging, refactoring, testing, creating PRs, managing sessions, and using advanced features like Plan Mode, worktrees, and extended thinking"
type: summary
sources:
  - raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md
tags:
  - claude-code
  - workflows
  - debugging
  - refactoring
  - testing
  - plan-mode
  - worktrees
  - sessions
  - extended-thinking
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Claude Code Common Workflows

Step-by-step guides for exploring codebases, debugging, refactoring, testing, creating PRs, and managing sessions, covering Plan Mode, worktrees, extended thinking, and unix-style integration. ^[001a-raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]

## Key Points

- Start with broad questions to explore a codebase, then narrow down; install a code intelligence plugin for precise "go to definition" and "find references" navigation ^[001a-raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]
- Plan Mode uses read-only operations for safe code analysis; enter with Shift+Tab or `--permission-mode plan`, view/edit plans with Ctrl+G ^[001a-raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]
- Git worktrees create isolated working directories for parallel sessions via `claude --worktree`; subagents can also use worktrees with `isolation: worktree` in agent frontmatter ^[001a-raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]
- Extended thinking is enabled by default and uses adaptive reasoning on supported models, dynamically allocating thinking tokens based on effort level; configure via `/effort`, `CLAUDE_CODE_EFFORT_LEVEL`, or `MAX_THINKING_TOKENS` ^[001a-raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]
- Session resumption supports `--continue` (most recent), `--resume` (by name or picker), and `--from-pr <number>` (linked to a PR); the session picker offers search, preview, rename, and branch filtering ^[001a-raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]
- Use `@` to reference files or directories in prompts; `@file.js` includes full file content, `@src/components` provides a directory listing, and `@server:resource` fetches MCP resources ^[001a-raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]
- Notification hooks fire on `permission_prompt`, `idle_prompt`, `auth_success`, `elicitation_dialog`, `elicitation_complete`, and `elicitation_response` events; configure in `settings.json` with platform-specific commands ^[001a-raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]

## Quotes

> "Extended thinking is enabled by default, giving Claude space to reason through complex problems step-by-step before responding." ^[001a-raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]

> "When working on multiple tasks at once, you need each Claude session to have its own copy of the codebase so changes don't collide. Git worktrees solve this by creating separate working directories that each have their own files and branch." ^[001a-raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]

## Notes

- The source document also covers image analysis (drag/drop, paste, or path reference), working in non-code directories, and asking Claude about its own capabilities
- Subagent workflow usage is described: automatic delegation for appropriate tasks, explicit requests with `/agents`, and custom subagent creation in `.claude/agents/`
- Running Claude on a schedule offers four options: Routines (Anthropic-managed), Desktop scheduled tasks, GitHub Actions, and `/loop` (current CLI session)

## Related

- [[004-wiki/entities/claude_code]]
- [[004-wiki/concepts/plan_mode]]
- [[004-wiki/concepts/extended_thinking]]
- [[004-wiki/concepts/worktrees]]
- [[004-wiki/concepts/sessions]]
- [[004-wiki/concepts/parallel_sessions]]
- [[004-wiki/concepts/subagents]]
- [[004-wiki/concepts/hooks]]
- [[004-wiki/concepts/non_interactive_mode]]
- [[004-wiki/concepts/scheduled_tasks]]
- [[004-wiki/concepts/permissions]]
- [[004-wiki/concepts/context_window]]