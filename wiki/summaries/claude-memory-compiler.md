---
title: Claude Memory Compiler
type: summary
date: 2026-04-22
sources:
  - raw/repos/claude-memory-compiler/README.md
  - raw/repos/claude-memory-compiler/AGENTS.md
tags:
  - tool
  - knowledge-base
  - claude-code
  - hooks
  - automation
---

# Claude Memory Compiler

An open-source tool by coleam00 that compiles AI conversations into a structured, searchable knowledge base. Adapted from [[llm_wiki]] — but instead of clipping web articles, the raw data is your own Claude Code conversations.

## Architecture (Compiler Analogy)

| Layer | Analog | Content |
|-------|--------|---------|
| `daily/` | Source code | Conversation logs (immutable, append-only) |
| LLM | Compiler | Extracts and organizes knowledge |
| `knowledge/` | Executable | Structured, queryable knowledge base |
| lint | Test suite | Health checks for consistency |
| queries | Runtime | Using the knowledge |

## How It Works

1. **Hooks** capture conversations automatically (SessionEnd + PreCompact safety net)
2. **flush.py** calls the Claude Agent SDK to decide what's worth saving, appends to `daily/YYYY-MM-DD.md`
3. **compile.py** turns daily logs into organized concept articles with cross-references (triggered automatically after 6 PM, or manually)
4. **query.py** answers questions using index-guided retrieval (no RAG)
5. **lint.py** runs 7 health checks (broken links, orphans, contradictions, staleness, backlinks, sparse, orphan sources)
6. **SessionStart hook** injects the knowledge index into every new session — the cycle repeats

## Key Scripts

| Script | Purpose | Cost |
|--------|---------|------|
| `compile.py` | daily logs -> knowledge articles (~$0.45-0.65/log) | Paid |
| `query.py` | ask the KB, optionally file answer back (~$0.15-0.40) | Paid |
| `lint.py` | 7 health checks (`--structural-only` is free) | Free/Paid |
| `flush.py` | extract from conversations (background, spawned by hooks) | ~$0.02-0.05/session |

## Key Design Decisions

- **No API key needed** — uses Claude Code's built-in credentials at `~/.claude/.credentials.json`
- **Personal use covered by subscription** (Max, Team, Enterprise) — no separate API billing
- **Incremental compilation** — tracks SHA-256 hashes of daily logs in `state.json`, skips unchanged files
- **End-of-day auto-compilation** — flush.py triggers compile.py after 6 PM if today's log changed
- **Deduplication** — same session flushed within 60 seconds is skipped
- **Background processes** — flush.py and compile.py spawn detached (survive parent exit)

## Knowledge Base Structure

- `knowledge/index.md` — master catalog (primary retrieval mechanism)
- `knowledge/log.md` — append-only build log
- `knowledge/concepts/` — atomic knowledge articles
- `knowledge/connections/` — cross-cutting insights linking 2+ concepts
- `knowledge/qa/` — filed query answers (compounding knowledge)

## Relationship to This Project

This project (`llm-wiki-llm-v1`) uses the same architecture but extends it with an **external KB** (`wiki/`) alongside the **internal KB** (`knowledge/`). The scripts and hooks in this project are adapted from claude-memory-compiler's originals.

## Source

`raw/repos/claude-memory-compiler/`