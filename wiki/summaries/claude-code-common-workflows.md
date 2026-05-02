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

Step-by-step guides for exploring codebases, debugging, refactoring, testing, creating PRs, and managing sessions, covering Plan Mode, worktrees, extended thinking, and unix-style integration. ^[raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]

## Key Points

- Start with broad questions to explore a codebase, then narrow down; install a code intelligence plugin for precise "go to definition" and "find references" navigation ^[raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]
- Plan Mode uses read-only operations for safe code analysis; enter with Shift+Tab or `--permission-mode plan`, view/edit plans with Ctrl+G ^[raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]
- Git worktrees create isolated working directories for parallel sessions via `claude --worktree`; subagents can also use worktrees with `isolation: worktree` in agent frontmatter ^[raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]
- Extended thinking is enabled by default and uses adaptive reasoning on supported models, dynamically allocating thinking tokens based on effort level; configure via `/effort`, `CLAUDE_CODE_EFFORT_LEVEL`, or `MAX_THINKING_TOKENS` ^[raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]
- Session resumption supports `--continue` (most recent), `--resume` (by name or picker), and `--from-pr <number>` (linked to a PR); the session picker offers search, preview, rename, and branch filtering ^[raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]
- Use `@` to reference files or directories in prompts; `@file.js` includes full file content, `@src/components` provides a directory listing, and `@server:resource` fetches MCP resources ^[raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]
- Notification hooks fire on `permission_prompt`, `idle_prompt`, `auth_success`, `elicitation_dialog`, `elicitation_complete`, and `elicitation_response` events; configure in `settings.json` with platform-specific commands ^[raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]

## Quotes

> "Extended thinking is enabled by default, giving Claude space to reason through complex problems step-by-step before responding." ^[raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]

> "When working on multiple tasks at once, you need each Claude session to have its own copy of the codebase so changes don't collide. Git worktrees solve this by creating separate working directories that each have their own files and branch." ^[raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]

## Notes

- The source document also covers image analysis (drag/drop, paste, or path reference), working in non-code directories, and asking Claude about its own capabilities
- Subagent workflow usage is described: automatic delegation for appropriate tasks, explicit requests with `/agents`, and custom subagent creation in `.claude/agents/`
- Running Claude on a schedule offers four options: Routines (Anthropic-managed), Desktop scheduled tasks, GitHub Actions, and `/loop` (current CLI session)

## Related

- [[entities/claude_code]]
- [[concepts/plan_mode]]
- [[concepts/extended_thinking]]
- [[concepts/worktrees]]
- [[concepts/sessions]]
- [[concepts/parallel_sessions]]
- [[concepts/subagents]]
- [[concepts/hooks]]
- [[concepts/non_interactive_mode]]
- [[concepts/scheduled_tasks]]
- [[concepts/permissions]]
- [[concepts/context_window]]