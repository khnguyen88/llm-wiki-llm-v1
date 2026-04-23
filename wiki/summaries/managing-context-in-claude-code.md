---
title: Managing Context in Claude Code
type: summary
date: 2026-04-23
sources:
  - raw/forum-thread/How are you guys managing context in Claude Code_ 200K just ain't cutting it..md
tags:
  - claude-code
  - context
  - community
  - reddit
---

# Managing Context in Claude Code

A Reddit thread on r/ClaudeAI where users share strategies for dealing with context window limits and compaction drift in Claude Code.

## The Problem

After Claude Code auto-compacts, responses subtly drift off-rails. Constraints from the original plan vanish. The 200K context window sounds large, but performance degrades past 100K and drops dramatically after 150K. Even 1M context windows (Codex) suffer quality degradation at scale.

## Top Strategies (by community consensus)

1. **CLAUDE.md as persistent memory** — Put core architecture, constraints, coding standards, and current plan in CLAUDE.md. Auto-loaded every session, survives compaction. Most upvoted solution.

2. **Subagent delegation** — Send subagents to do research or implement smaller pieces. They do the token-heavy work and report back concise summaries, keeping main context clean. Second most popular strategy.

3. **Work in smaller chunks** — One session per logical unit (implement auth middleware, then fresh conversation for auth routes). Don't let a single session grow large enough to require compaction.

4. **Handoff documents** — Before context fills up, have Claude create a summary of progress, decisions, and next steps. Start new session reading that handoff doc.

5. **Proactive compact** — Use `/compact` before Claude auto-compacts. Add instructions like "preserve the current implementation plan and all file paths discussed."

6. **File-based memory** — Use PLAN.md, TODO.md, CONTEXT.md as persistent memory. CLAUDE.md is the bootstrap — everything else chains from there.

## Key Quotes

> "The 200K limit is workable once you stop treating context as your primary memory and start treating files as memory instead." — [[restaurant_hefty322]]

> "After compaction, Claude loses the architectural constraints you set early in the conversation and starts making decisions that contradict your original plan." — ruso-0

> "Performance starts to drop after 100k, and it drops dramatically after 150k. Just because you have a 1M context window doesn't mean you should use all of it." — Ebi_Tendon

## Emerging Ideas

- **Knowledge graph approaches** — Typed connections between memories with temporal filtering, instead of flat markdown files (PenfieldLabs)
- **Dual-window workflow** — Claude Desktop for planning, Claude Code for execution, with MD files as the bridge
- **AI-format CLAUDE.md** — Keep a human-friendly version and a stripped-down AI-optimized version with no "niceties"
- **Context handoff skill** — Auto-trigger at 75% context, creates handoff doc, then start fresh session

## Source

`raw/forum-thread/How are you guys managing context in Claude Code_ 200K just ain't cutting it..md`