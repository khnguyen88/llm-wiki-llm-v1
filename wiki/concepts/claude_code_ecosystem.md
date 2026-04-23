---
title: Claude Code Ecosystem
type: concept
date: 2026-04-23
sources:
  - raw/forum-thread/Best GitHub repos for Claude Code.md
  - raw/forum-thread/How are you guys managing context in Claude Code_ 200K just ain't cutting it..md
tags:
  - claude-code
  - tools
  - community
---

# Claude Code Ecosystem

The ecosystem of community-built tools, repos, and plugins extending Claude Code beyond its default capabilities. Organized by function.

## Skill & Framework Collections

| Repo | Purpose |
|------|---------|
| awesome-claude-skills (ComposioHQ, 55.5k) | Canonical skills directory |
| awesome-claude-code (jqueryscript, 40k) | Broader curated list |
| awesome-claude-plugins (ComposioHQ, 1.4k) | Plugin collection |
| SuperClaude_Framework (22.4k) | Full framework |
| Superpowers (pcvelz) | Skills/agents for daily development |
| armory (Mathews-Tom) | Day-to-day skills/agents/hooks |
| claude-code-system-prompts (Piebald-AI, 9.3k) | Reverse-engineered system prompts |

## Context & Token Management

| Repo | Purpose |
|------|---------|
| ccusage (ryoppippi, 13.2k) | Token spend per session |
| context-mode (mksglu, 8.8k) | MCP token bloat management |
| OpenWolf (cytostack) | Hooks: file index, learning memory, token ledger |
| claude-context-optimizer (egorfdrv) | Context optimization plugin |
| claudectl (mercurialsolo) | Auto-pilot with local brain |

## Workflow & Orchestration

| Repo | Purpose |
|------|---------|
| GSD (gsd-build) | Phase-based planning and execution |
| agent-orchestrator (ComposioHQ, 6.4k) | Parallel sessions across git worktrees |
| repomix (yamadashy, 23.7k) | Packs repo into one readable file |
| Phaselock (infinri) | Phase-based workflow |
| claude-octopus (nyldn) | Delegates work to Codex |
| compound-engineering-plugin (EveryInc) | Compound engineering workflow |

## Patterns

- **Curated lists** (awesome-*) are the entry point; most users install 3-4 tools max
- **Context management** tools have the highest retention rate (ccusage, repomix)
- **Phase-based frameworks** (GSD, Phaselock) replace ad-hoc planning but add token overhead
- **Hooks-based tools** (OpenWolf, claudectl) are "invisible" — init once, then automatic
- **Tiny global defaults + repo-local rules beat giant universal setups** (tensorfish's principle)

## Related

- [[claude_code]] — the platform this ecosystem extends
- [[context_management]] — the problem most tools address
- [[model_routing]] — alternative multi-model approach