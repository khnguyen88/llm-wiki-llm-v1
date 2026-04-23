---
title: Memory Flush
type: concept
date: 2026-04-22
sources:
  - raw/repos/claude-memory-compiler/AGENTS.md
  - raw/repos/claude-memory-compiler/scripts/flush.py
tags:
  - automation
  - hooks
  - claude-code
  - knowledge-base
---

# Memory Flush

The process of extracting important knowledge from a conversation transcript and appending it to the daily log. Spawned automatically by hooks when a session ends or when Claude Code auto-compacts mid-session.

## Mechanism

1. Hook (session-end or pre-compact) reads the JSONL transcript, extracts conversation context
2. Writes context to a temp `.md` file
3. Spawns `flush.py` as a detached background process
4. flush.py calls Claude Agent SDK with `allowed_tools=[]`, `max_turns=2`
5. LLM returns structured bullet points (decisions, lessons, actions) or `FLUSH_OK`
6. Result appended to `daily/YYYY-MM-DD.md`
7. If past 6 PM and today's log changed, auto-triggers `compile.py`

## Safety Guards

- **Recursion prevention**: `CLAUDE_INVOKED_BY` env var prevents flush from triggering its own hooks
- **Deduplication**: same session flushed within 60 seconds is skipped
- **PreCompact safety net**: captures context before auto-compaction discards it — critical for long sessions with multiple compactions

## Cost

~$0.02-0.05 per session (one brief Agent SDK call with no tools).

## Related

- [[claude-memory-compiler]] — the system this concept comes from
- [[llm_wiki]] — the architecture pattern
- [[headless_llm_execution]] — another automation pattern using background processes
- [[context_management]] — the broader context preservation strategy