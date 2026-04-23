---
title: Context Management
type: concept
date: 2026-04-23
sources:
  - raw/forum-thread/Best GitHub repos for Claude Code.md
  - raw/forum-thread/How are you guys managing context in Claude Code_ 200K just ain't cutting it..md
tags:
  - claude-code
  - context
  - memory
  - workflow
---

# Context Management

Strategies for managing LLM context windows to prevent compaction drift, token waste, and lost constraints. The core insight: stop treating the context window as primary memory and start treating files as memory instead.

## The Compaction Problem

When Claude Code auto-compacts, responses subtly drift off-rails. Architectural constraints and plans set early in the conversation vanish. Performance degrades past 100K tokens and drops dramatically after 150K. Even 1M context windows suffer quality loss at scale ("lost in the middle" problem).

## Key Strategies

| Strategy | Mechanism | Survives Compaction? |
|----------|-----------|---------------------|
| CLAUDE.md | Auto-loaded every session, contains core rules | Yes |
| Subagent delegation | Subagents do token-heavy work, report summaries | N/A (reduces need) |
| Small sessions | One session per logical unit of work | N/A (avoids problem) |
| Handoff documents | Summary of progress/decisions/next steps | Yes (file on disk) |
| Proactive compact | `/compact` with preservation instructions | Partially |
| File-based memory | PLAN.md, TODO.md, CONTEXT.md | Yes |
| Lean system prompt | Sub-60 line CLAUDE.md, on-demand skill injection | Yes |

## The Lean Prompt Pattern

Keep CLAUDE.md under 40-60 lines with only "shape" directives. Domain-specific rules live in skill files that inject on demand. This is [[single_loop_architecture]] — keeping the active context slim is the primary lever for maintaining consistent behavior across long sessions.

## Tooling

- **ccusage** — Token spend per session (most "Claude is expensive" posts are from users who never measured)
- **OpenWolf** — Hooks for file index, learning memory, token ledger
- **context-mode** — MCP token bloat management
- **claude-context-optimizer** — Plugin claiming 65-70% context savings in real work

## Related

- [[claude_code]] — the tool these strategies apply to
- [[single_loop_architecture]] — lean prompt architecture
- [[memory_flush]] — automatic knowledge capture via hooks
- [[claude_code_ecosystem]] — community tools