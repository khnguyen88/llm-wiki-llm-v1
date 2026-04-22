# CLAUDE.md

Two parallel knowledge bases implementing Karpathy's LLM Wiki pattern — no RAG, index-guided retrieval instead.

## Architecture

| KB | Raw source | Compiled to | Schema |
|----|-----------|-------------|--------|
| External | `raw/` → `processed/` → `wiki/` | `wiki/` | `schema/WIKI_*.md` |
| Internal | `daily/` (conversation logs) | `knowledge/` | `AGENTS.md` |

Core insight: the LLM incrementally builds a **persistent, compounding wiki** instead of rediscovering knowledge from scratch on every query.

## Directory Layout

- `raw/` — Source documents (human-curated, read-only for LLM): `articles/`, `papers/`, `repos/`, `datasets/`, `assets/`, `document/` (papers, PDFs, datasets), `web/` (articles, repos, tweets)
- `processed/` — Segmented markdown from large raw files: `articles/`, `papers/`, `repos/`, `datasets/`, `assets/`, `document/`, `web/`
- `wiki/` — External KB (LLM-owned): index.md, sources-manifest.md, log.md, synthesis.md, entities/, concepts/, summaries/, qanda/
- `daily/` — Conversation logs (immutable)
- `knowledge/` — Internal KB (LLM-owned): index.md, log.md, concepts/, connections/, qa/
- `schema/` — WIKI_AGENTS.md, WIKI_SCHEMA.md, WIKI_WORKFLOWS.md
- `AGENTS.md` — Internal KB compiler specification
- `scripts/` — compile.py, query.py, lint.py, flush.py
- `hooks/` — session-start.py, session-end.py, pre-compact.py
- `reports/` — Lint reports (gitignored)

## Operations

**External KB** — Large files in `raw/` get segmented into `processed/` first (PDF → markdown parts, then delete PDF). Sources are organized as `raw/document/` (papers, datasets) or `raw/web/` (articles, repos). Ingest into wiki pages, update index.md + log.md. Query via index.md first, drill into relevant pages. Lint for broken links, orphans, contradictions.

**Internal KB** — Compile daily logs into knowledge articles. Query via index.md. Lint: 7 checks (broken links, orphans, orphan sources, stale, missing backlinks, sparse, contradictions).

## Project Agents

Defined in `.claude/agents/`:

| Agent | Purpose |
|-------|---------|
| `wiki-maintainer` | Ingests sources from `raw/` and `processed/` (all subfolders) into `wiki/`, creates entities/concepts/summaries, updates index + log |
| `document-processor` | Segments large raw files into `processed/` (matching subfolder), handles tables/images |
| `knowledge-compiler` | Compiles `daily/` logs into `knowledge/` concepts, connections, qa articles |
| `wiki-linter` | Health checks across both KBs: broken links, orphans, contradictions, stale articles |
| `wiki-query` | Index-guided retrieval against both KBs, files valuable answers back |
| `sync-check` | Verifies all config files, schemas, and agents stay consistent with each other |

## Conventions

- LLM owns `wiki/` and `knowledge/` — human curates `raw/` and `daily/`
- Wikilinks: `[[path/to/article]]` (no `.md`)
- Frontmatter required on all wiki pages (title, type, date, sources, tags)
- Naming: snake_case for entities/concepts, kebab-case for summaries/qanda
- Processed files: `processed/{subfolder}/{base-name}-{YYYY-MM-DD}-part-{###}[-{chapter-##|section-slug}].md`
- Dates: ISO 8601 (YYYY-MM-DD)
- Style: encyclopedia-style, factual, concise

## Scripts

All via `uv run python scripts/<name>.py`:
- `compile.py` — daily logs → knowledge (`--all`, `--file`, `--dry-run`)
- `query.py` — ask a KB (`--file-back` saves answer)
- `lint.py` — health checks (`--structural-only` skips LLM judgment)
- `flush.py` — extract from conversations (background, spawned by hooks)

## Hooks

Configured in `.claude/settings.json`:
- **SessionStart**: injects KB index into session context
- **PreCompact**: captures context before compaction discards it
- **SessionEnd**: extracts conversation → daily log, spawns background flush

## Obsidian

Both KBs work natively — graph view, backlinks, Dataview, Marp slides.