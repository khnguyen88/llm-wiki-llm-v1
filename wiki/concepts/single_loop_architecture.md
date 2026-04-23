---
title: Single Loop Architecture
type: concept
date: 2026-04-23
sources:
  - raw/forum-thread/Best GitHub repos for Claude Code.md
tags:
  - claude-code
  - architecture
  - context
  - prompt-engineering
---

# Single Loop Architecture

An architectural pattern for single-agent LLM loops where a lean system prompt (sub-60 lines) contains only core "shape" directives, and domain-specific rules live in skill files that inject into context only when relevant.

## Origin

Term from internal discussion at a workplace using Claude Code. "SL" = Single Loop — one agent calling tools in a continuous loop, where all responses accumulate in one context.

## Core Problem

In a single-agent loop, everything accumulates in one continuous context. The further back core rules get pushed by accumulated tool responses and conversation, the less the LLM adheres to them. Past ~200 lines, instructions at the bottom of the system prompt lose reliability.

## The Fix

1. **Lean root prompt** — CLAUDE.md stays under 60 lines with only:
   - What the project is (identity)
   - Architecture shape (skeleton, not full tree)
   - Agent/skill dispatch table (when to invoke what)
   - Core conventions that apply to EVERY operation
   - On-demand detail pointers
2. **Skills load on demand** — Domain-specific rules ("doctrine", "domain" directives) live in skill files. They inject into context only when the relevant task arises.
3. **Keep skills focused** — 1-2 actions per skill, concise and explicit. Broad skills bloat context just like a fat CLAUDE.md would.

## Why It Works

- Core system directives stay closer to the "attention window" of the model
- Skills inject only the rules relevant to the current task
- Context drift is staved off because the shape directives aren't buried under accumulated tool output

## Related

- [[context_management]] — the broader strategy this pattern serves
- [[claude_code]] — the tool this pattern was developed for
- [[memory_flush]] — complementary hook-based knowledge capture