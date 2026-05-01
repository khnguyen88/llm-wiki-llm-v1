# LLM Wiki — Owner Guide

Internal reference for how the system works, what to maintain, and what to watch out for.

## Architecture at a Glance

```
+----------------------------------------------------------+
|                    External KB                            |
|                                                          |
|  raw/ --> processed/ --> wiki/                           |
|  (human)    (LLM stage)    (LLM compiled)                |
|  ai-research/ -------------+                             |
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

**Ownership rule:** You curate `raw/`. The LLM owns `wiki/`, `knowledge/`, `processed/`, and `daily/`. `ai-research/` is LLM-discovered but immutable once saved.

## Data Flow

### External Ingest (raw -> wiki)

```
1. You add file to raw/ or ai-research/
2. If file >3000 words -> document-processor segments to processed/
3. wiki-maintainer (or ingest_external.py) processes source
4. Creates/updates: summary, entities, concepts in wiki/
5. Updates: index.md, sources-manifest.md, log.md, synthesis.md
6. Lint + repair if batch ingesting
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
| **You** | `raw/` (add sources), `AGENTS.md` (schema), `CLAUDE.md` (project rules), `schema/WIKI_*.md` (config), `.claude/agents/*.md` (agent defs), `.claude/settings.json` (hooks), `pyproject.toml` (deps) |
| **LLM** | `wiki/` (compiled), `knowledge/` (compiled), `processed/` (staged), `daily/` (conversation logs), `scripts/state.json` (tracking) |
| **Hooks** | `daily/` (created by session-end), `scripts/flush-context-*` (temp) |
| **Gitignored** | `daily/`, `knowledge/`, `reports/`, `scripts/state.json`, `scripts/last-flush.json`, `.claude/settings.local.json`, `.obsidian/` |

## Scripts Reference

| Script | Purpose | Key CLI Flags | State Files |
|--------|---------|---------------|-------------|
| `compile.py` | Compile daily logs -> knowledge articles | `--all`, `--file <path>`, `--dry-run` | `scripts/state.json` (hashes) |
| `query.py` | Index-guided KB query | `--file-back` (saves Q&A article) | `scripts/state.json` (query count) |
| `lint.py` | Health checks (12 structural + 1 LLM) | `--structural-only`, `--kb internal\|external\|both` | `scripts/state.json` (last lint), `reports/lint-*.md` |
| `flush.py` | Extract memories from conversations | (spawned by hooks, not manual) | `scripts/last-flush.json` (dedup) |
| `ingest_external.py` | Bulk ingest raw/ai-research -> wiki | `--all`, `--file <path>`, `--dry-run`, `--max-words N`, `--workers N` | `scripts/state.json` (ingestion tracking) |
| `config.py` | Path constants and time helpers | (imported, not run directly) | — |
| `utils.py` | Shared helpers (slugify, frontmatter, etc.) | (imported, not run directly) | — |

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
| "Process this source" | `wiki-maintainer` | 10-step ingest of a source into wiki/ |
| Files >3,000 words or PDFs | `document-processor` | Segment large files into processed/ |
| "Compile daily logs" | `knowledge-compiler` | Compile daily/ -> knowledge/ |
| "Lint the wiki", "Run health check" | `wiki-linter` | 12 structural + 1 LLM checks |
| "Fix broken links", "Resolve orphans" | `wiki-repair` | 7 repair operations |
| Questions about compiled knowledge | `wiki-query` | 7-step query with optional file-back |
| After structural changes | `sync-check` | 7 categories of consistency checks |
| "Load rules for X", "Audit CLAUDE.md" | `context-loader` | On-demand rule loading, prompt health |
| "Ingest all pending sources" | `batch-ingester` | Run ingest_external.py, then lint + repair |

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
- **`--max-words` default**: Script default is 30000. The GitHub Actions workflow overrides to 3000 for cost control. The batch-ingester agent doc matches the script at 30000.
- **`daily/` and `knowledge/` are gitignored**: They're regenerated by hooks and scripts. If you lose the local copies, re-run compilation from a backup of daily logs.
- **`ai-research/` is currently empty**: The Research workflow has never been executed. All current wiki content comes from `raw/` sources.
- **`processed/` is currently empty**: No large files have been segmented yet.
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
| Check ingestion status | Anytime | `uv run python scripts/ingest_external.py --dry-run` |
| Compile daily logs | After 6 PM (automatic), or manually | `uv run python scripts/compile.py` |
| Review lint reports | After running lint | Check `reports/lint-YYYY-MM-DD.md` |