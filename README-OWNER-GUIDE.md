# LLM Wiki — Owner Guide

Internal reference for how the system works, what to maintain, and what to watch out for.

## Architecture at a Glance

```
+----------------------------------------------------------+
|                    External KB                            |
|                                                          |
|  001a-raw/ --> 002-raw-preprocessed/ --> 003-processed/ --> 004-wiki/                           |
|  (human)     (document conversion+OCR)  (LLM stage)       (LLM compiled)                |
|  001b-ai-research/ -------------+                             |
|  (LLM found, immutable)                                   |
|                                                          |
+----------------------------------------------------------+
|                    Internal KB                            |
|                                                          |
|  daily/ --> knowledge/                                   |
|  (hooks capture)  (LLM compiled)                         |
|                                                          |
|  Schema: AGENTS.md                                       |
|  Schema: schema/WIKI_*.md                                |
+----------------------------------------------------------+
```

**Ownership rule:** You curate `001a-raw/`. The LLM owns `004-wiki/`, `knowledge/`, `003-processed/`, and `daily/`. `001b-ai-research/` is LLM-discovered but immutable once saved.

## Data Flow

### External Ingest (raw -> wiki)

```
1. You add file to 001a-raw/ or 001b-ai-research/
2. If PDF/DOCX/PPTX -> document-converter converts to markdown in 002-raw-preprocessed/
3. If OCR issues -> ocr-remediator fixes formulas, tables, diagrams
4. If file >3000 words -> markdown-chunker segments to 003-processed/
5. wiki-maintainer processes source (subagent-driven dispatch)
6. Creates/updates: summary, entities, concepts in 004-wiki/
7. Updates: index.md, sources-manifest.md, log.md, synthesis.md
8. Lint + repair if needed
```

### Internal Compile (daily -> knowledge)

```
1. session-end hook fires -> flush.py extracts memories -> daily/YYYY-MM-DD.md
2. compile.py reads daily log + existing knowledge articles
3. Creates/updates: concepts, connections in knowledge/
4. Updates: knowledge/index.md, knowledge/log.md
5. Auto-compilation triggers after 6 PM if daily log changed
```

## File Ownership Map

| Who edits | Directories/Files |
|-----------|------------------|
| **You** | `001a-raw/` (add sources), `AGENTS.md` (schema), `CLAUDE.md` (project rules), `schema/WIKI_*.md` (config), `.claude/agents/*.md` (agent defs), `.claude/settings.json` (hooks), `pyproject.toml` (deps) |
| **LLM** | `004-wiki/` (compiled), `knowledge/` (compiled), `003-processed/` (staged), `002-raw-preprocessed/` (converted docs), `daily/` (conversation logs), `scripts/state.json` (tracking) |
| **Hooks** | `daily/` (created by session-end), `scripts/flush-context-*` (temp) |
| **Gitignored** | `daily/`, `knowledge/`, `reports/`, `scripts/state.json`, `scripts/last-flush.json`, `.claude/settings.local.json`, `.obsidian/` |

## Scripts Reference

| Script | Purpose | Key CLI Flags | State Files |
|--------|---------|---------------|-------------|
| `compile.py` | Compile daily logs -> knowledge articles | `--all`, `--file <path>`, `--dry-run` | `scripts/state.json` (hashes) |
| `query.py` | Index-guided KB query | `--file-back` (saves Q&A article) | `scripts/state.json` (query count) |
| `lint.py` | Health checks (12 structural + 1 LLM) | `--structural-only`, `--kb internal\|external\|both` | `scripts/state.json` (last lint), `reports/lint-*.md` |
| `flush.py` | Extract memories from conversations | (spawned by hooks, not manual) | `scripts/last-flush.json` (dedup) |
| `config.py` | Path constants and time helpers | (imported, not run directly) | — |
| `utils.py` | Shared helpers (slugify, frontmatter, etc.) | (imported, not run directly) | — |
| `ocr_remediate.py` | OCR remediation for problem pages | -- | — |
| `sidecar.py` | Sidecar file management for document pipeline | -- | — |

## Hooks Reference

| Hook | When | What it does |
|------|------|--------------|
| `session-start.py` | Every Claude Code session start | Reads `knowledge/index.md` + recent daily log, injects as context. Also injects a sync-check reminder. |
| `session-end.py` | Session close | Reads transcript JSON, spawns `flush.py` as detached background process. Windows: `CREATE_NO_WINDOW` flag. |
| `pre-compact.py` | Before auto-compaction | Same architecture as session-end. Captures context before summarization discards it. Critical for long sessions. |

**Hook config location:** `.claude/settings.json` — commands use `uv run python hooks/<name>.py`

**Flush deduplication:** `scripts/last-flush.json` tracks `(session_id, timestamp)` to prevent double-processing. Skips if same session was flushed within 60 seconds.

**Auto-compilation:** If it's past 6 PM local time and today's daily log has changed since last compilation (hash comparison), `flush.py` spawns `compile.py` as another detached background process.

## Agent Dispatch Rules

| Trigger phrase | Agent | What it does |
|----------------|-------|--------------|
| "Process this source" | `wiki-maintainer` | 10-step ingest of a source into 004-wiki/ |
| "Convert this document to markdown" | `document-converter` | Convert PDF/DOCX/PPTX to markdown via docling-serve |
| "Fix OCR issues in 002-raw-preprocessed" | `ocr-remediator` | Run deepseek-ocr on problem pages, fix formulas/tables |
| "Chunk this markdown into chapters" | `markdown-chunker` | Segment large markdown files into LLM-sized chapters |
| "Process this PDF", "Run the full pipeline on X" | `document-processor` | Full pipeline: convert → OCR remediate → chunk |
| "Compile daily logs" | `knowledge-compiler` | Compile daily/ -> knowledge/ |
| "Lint the wiki", "Run health check" | `wiki-linter` | 12 structural + 1 LLM checks |
| "Fix broken links", "Resolve orphans" | `wiki-repair` | 7 repair operations |
| Questions about compiled knowledge | `wiki-query` | 7-step query with optional file-back |
| "Search the web for X" | `web-search` | Ephemeral web search via Vane (vane_web_search shell tool) |
| "Research X and save it" | `ai-research` | Deep research: Vane + crawl4ai, saves to 001b-ai-research/web/ |
| "Get transcript for `<url>`" | `youtube-transcript` | Extract transcript via ytscribe.io, save to 001a-raw/transcripts/ |
| "Review transcript `<path>`" | `transcript-reviewer` | Verify/correct speech-to-text errors in transcripts |
| After structural changes | `sync-check` | 7 categories of consistency checks |
| "Load rules for X", "Audit CLAUDE.md" | `context-loader` | On-demand rule loading, prompt health |

## Schema Cross-References

| File | Defines |
|------|---------|
| `AGENTS.md` | Internal KB schema: compiler analogy, article formats, operations, conventions, project structure, hook system, script details |
| `schema/WIKI_AGENTS.md` | External KB agent role, three-layer architecture, file conventions |
| `schema/WIKI_SCHEMA.md` | External KB file formats: frontmatter, naming, citations, page templates, index/log format |
| `schema/WIKI_WORKFLOWS.md` | External KB workflows: Ingest (10 steps), Query (5 steps), Lint (8+1 checks), Research |
| `CLAUDE.md` | Project instructions: architecture table, key directories, agent dispatch, core conventions, on-demand details |

## Known Issues & Design Decisions

- **Lint checks**: 12 structural + 1 LLM = 13 total. All 12 structural checks are now implemented in lint.py.
- **`daily/` and `knowledge/` are gitignored**: They're regenerated by hooks and scripts. If you lose the local copies, re-run compilation from a backup of daily logs.
- **`001b-ai-research/` has web research content**: Contains AI-researched web sources saved by the ai-research agent.
- **`003-processed/` has segmented documents**: Contains segmented output from the document processing pipeline (document-converter → ocr-remediator → markdown-chunker).
- **`002-raw-preprocessed/` stores intermediate conversion output**: Files here are pre-chunking and may need OCR remediation before segmentation.
- **`knowledge/qa/` is currently empty**: No Q&A articles have been filed back yet.
- **Windows hooks**: Use `CREATE_NO_WINDOW` flag, not `DETACHED_PROCESS`. The latter breaks Agent SDK subprocess I/O.
- **Wiki frontmatter**: All wiki pages require `title`, `summary`, `type`, `sources`, `tags`, `created`, `updated`. Optional: `confidence`, `provenance`, `contradictedBy`, `orphaned`.

## Maintenance Tasks

| Task | When | How |
|------|------|-----|
| Run sync-check | Every session start (automatic via hook) | The session-start hook injects a reminder |
| Run lint | After batch ingestion, or weekly | `uv run python scripts/lint.py --structural-only` |
| Run full lint | Monthly or before releases | `uv run python scripts/lint.py` |
| Reset state | If state.json gets corrupted | `rm scripts/state.json scripts/last-flush.json` |
| Compile daily logs | After 6 PM (automatic), or manually | `uv run python scripts/compile.py` |
| Review lint reports | After running lint | Check `reports/lint-YYYY-MM-DD.md` |