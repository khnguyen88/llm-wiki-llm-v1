---
title: "Subagent Forking"
summary: "Experimental feature where a subagent inherits the entire conversation so far instead of starting fresh, sharing the parent's prompt cache for cheaper context reuse while keeping the fork's own tool calls out of the main context"
type: concept
sources:
  - raw/document/claude code/claude-code-106-sub-agents-2026-04-29.md
  - raw/document/claude code/claude-code-122-whats-new-2026-w17-2026-04-29.md
tags:
  - subagents
  - forking
  - context-management
  - experimental
  - prompt-caching
  - claude-code
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Subagent Forking

Forked subagents inherit the full conversation so far instead of starting with a fresh context, enabling side tasks that need the same background without re-explaining the situation. Forking is experimental and requires Claude Code v2.1.117 or later, enabled via the `CLAUDE_CODE_FORK_SUBAGENT` environment variable set to `1`. ^[raw/document/claude code/claude-code-106-sub-agents-2026-04-29.md] On external builds (Agent SDK), forked subagents can be enabled with the same `CLAUDE_CODE_FORK_SUBAGENT=1` environment variable. ^[raw/document/claude code/claude-code-122-whats-new-2026-w17-2026-04-29.md]

## Key Points

- A fork inherits the same system prompt, tools, model, and message history as the main session, dropping the input isolation that named subagents provide ^[raw/document/claude code/claude-code-106-sub-agents-2026-04-29.md]
- The fork's own tool calls stay out of the main conversation; only its final result comes back, keeping the main context window clean ^[raw/document/claude code/claude-code-106-sub-agents-2026-04-29.md]
- Because a fork's system prompt and tool definitions are identical to the parent, its first request reuses the parent's prompt cache, making forking cheaper than spawning a fresh subagent for tasks needing the same context ^[raw/document/claude code/claude-code-106-sub-agents-2026-04-29.md]
- Enabling fork mode causes Claude to spawn a fork whenever it would otherwise use the general-purpose subagent; named subagents like Explore still spawn as before ^[raw/document/claude code/claude-code-106-sub-agents-2026-04-29.md]
- When fork mode is enabled, every subagent spawn runs in the background regardless of the `background` field; set `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS` to `1` to keep spawns synchronous ^[raw/document/claude code/claude-code-106-sub-agents-2026-04-29.md]
- The `/fork` command spawns a fork followed by a directive; forks cannot spawn further forks ^[raw/document/claude code/claude-code-106-sub-agents-2026-04-29.md]

## Details

Forking differs from named subagents in several key dimensions. Named subagents start from their own definition with a fresh context and a custom system prompt, while forks inherit everything the main session has at the moment they spawn. Named subagents use the model from their `model` field, while forks use the same model as the main session. Named subagents pre-approve permissions before launch then auto-deny anything not pre-approved, while forks surface permission prompts in the terminal as they occur. ^[raw/document/claude code/claude-code-106-sub-agents-2026-04-29.md]

Forks are best used when a named subagent would need too much background to be useful, or when trying several approaches in parallel from the same starting point. Named subagents are preferred when the task is self-contained, produces verbose output, or needs specific tool restrictions or a focused system prompt. ^[raw/document/claude code/claude-code-106-sub-agents-2026-04-29.md]

Running forks appear in a panel below the prompt input. Navigation keys include up/down arrows to move between rows, Enter to open a fork's transcript and send follow-up messages, `x` to dismiss a finished fork or stop a running one, and Esc to return focus to the prompt input. ^[raw/document/claude code/claude-code-106-sub-agents-2026-04-29.md]

When Claude spawns a fork through the Agent tool, it can pass `isolation: "worktree"` so the fork's file edits are written to a separate git worktree instead of the main checkout. ^[raw/document/claude code/claude-code-106-sub-agents-2026-04-29.md]

## Related

- [[concepts/subagents]]
- [[concepts/context_window]]
- [[concepts/worktrees]]
- [[concepts/prompt_caching]]
- [[summaries/claude-code-sub-agents]]