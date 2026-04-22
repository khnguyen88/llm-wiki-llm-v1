---
title: coleam00
type: entity
date: 2026-04-22
sources:
  - raw/repos/claude-memory-compiler/README.md
tags:
  - people
  - open-source
  - claude-code
  - knowledge-base
---

# coleam00

Open-source developer who created [[claude-memory-compiler]], the reference implementation of the Karpathy LLM Wiki pattern for compiling AI conversations into a personal knowledge base.

## Key Contributions

- Adapted Karpathy's LLM Wiki architecture from external-article ingestion to conversation-based compilation
- Built the hook system (session-start, session-end, pre-compact) for automatic knowledge capture
- Implemented the compiler pipeline: flush -> daily log -> compile -> knowledge articles
- Made it work with Claude Code's built-in credentials (no separate API key)

## Related

- [[summaries/claude-memory-compiler]] — detailed summary of the tool
- [[andrej_karpathy]] — originator of the LLM Wiki pattern that coleam00 adapted