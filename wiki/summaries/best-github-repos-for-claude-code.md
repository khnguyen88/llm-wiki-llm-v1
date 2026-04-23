---
title: Best GitHub Repos for Claude Code
type: summary
date: 2026-04-23
sources:
  - raw/forum-thread/Best GitHub repos for Claude Code.md
tags:
  - claude-code
  - tools
  - community
  - reddit
---

# Best GitHub Repos for Claude Code

A Reddit thread on r/ClaudeCode where users share the GitHub repos that stuck after trying 40+ skills, plugins, and helpers.

## Top Repos Mentioned

| Repo | Author | Stars | Purpose |
|------|--------|-------|---------|
| awesome-claude-skills | ComposioHQ | 55.5k | Canonical Claude Skills list (PDF/Word/Excel/PPT, CSV, brand voice, SaaS integrations) |
| repomix | yamadashy | 23.7k | Packs a repo into one file Claude can read |
| agent-orchestrator | ComposioHQ | 6.4k | Parallel Claude Code sessions across git worktrees |
| ccusage | ryoppippi | 13.2k | CLI that prints token spend per session |
| Superpowers | pcvelz | — | Skills/agents for everyday development |
| GSD | gsd-build | — | Breaks work into digestible phases with planning |
| OpenWolf | cytostack | — | 6 hooks: file index, learning memory, token ledger |
| awesome-claude-code | jqueryscript | 40k | Broader curated list |
| context-mode | mksglu | 8.8k | MCP token bloat management |
| claude-code-system-prompts | Piebald-AI | 9.3k | Reverse-engineered system prompts |
| armory | Mathews-Tom | — | Skills/agents/hooks for daily use |
| SuperClaude_Framework | SuperClaude-Org | 22.4k | Framework for Claude Code |

## Key Insight: Lean System Prompts

The thread's most-discussed technical insight: keep CLAUDE.md under 40-60 lines and load domain rules on demand via skills. This is [[single_loop_architecture]] — a lean root prompt with shape directives only, skills injecting domain rules when relevant. Past ~200 lines, Claude stops reliably following instructions at the bottom.

## Community Patterns

- **ccusage + repomix** are the most consistently kept tools
- **Superpowers** and **GSD** are the top skill/framework picks; GSD preferred for its phase-based planning discipline
- **OpenWolf** fills a niche: invisible hooks that reduce how fast you hit token limits
- Most "Claude is expensive" posts come from users who never measured their token spend

## Source

`raw/forum-thread/Best GitHub repos for Claude Code.md`