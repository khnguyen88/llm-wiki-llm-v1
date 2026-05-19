# Directory Renumbering — Design

## Summary

Add numeric prefixes to pipeline directories so the processing order is visible in a flat directory listing. Non-pipeline directories stay unnumbered.

## Target Layout

```
Pipeline (numbered):
  001a-raw/              Source acquisition — human-curated docs
  001b-ai-research/      Source acquisition — AI-discovered web
  002-raw-preprocessed/  Document conversion + OCR output (pre-chunking)
  003-processed/         Chunked/segmented documents
  004-wiki/              External KB

Non-pipeline (unnumbered):
  knowledge/             Internal KB (fed by daily/)
  daily/                 Conversation logs
  schema/                Schema docs
  scripts/               Python scripts
  tools_scripts/         Tool scripts
  docs/                  Project documentation
  hooks/                 Git hooks
  reports/               Reports
  .claude/               Claude config
```

Pipeline flow:
- `001a-raw/` → `002-raw-preprocessed/` → `003-processed/` → `004-wiki/` (documents)
- `001b-ai-research/` → `004-wiki/` directly (web content, no conversion needed)
- `daily/` → `knowledge/` (separate internal KB pipeline, both unnumbered)

## Migration Plan

### Execution order

1. Rename directories on disk (`git mv`)
2. Update all text references (two tiers below)
3. Run wiki-linter to verify no broken links
4. Commit

### Tier 1 — Mechanical find-and-replace

Straight string replacements for directory names in config files, scripts, schema docs, agent definitions, and READMEs:

| Old | New |
|-----|-----|
| `raw/` | `001a-raw/` |
| `ai-research/` | `001b-ai-research/` |
| `raw-markdown/` | `002-raw-preprocessed/` |
| `processed/` | `003-processed/` |
| `wiki/` | `004-wiki/` (config/docs only, not wikilinks) |

Files affected:
- `CLAUDE.md` — Architecture table, Key Directories
- `schema/WIKI_SCHEMA.md` — Directory Structure tree, all path references
- `schema/WIKI_AGENTS.md` — Pipeline stage references
- `schema/WIKI_WORKFLOWS.md` — Workflow path references
- `AGENTS.md` — Internal KB directory references
- `.claude/agents/*.md` — All agent definitions
- `scripts/*.py` — Hardcoded directory paths
- `.gitignore` — Directory patterns
- `README.md`, `README-OWNER-GUIDE.md`, `README-USER-GUIDE.md`, `README-PROJECT-COMPARISON.md`
- `wiki/index.md`, `wiki/sources-manifest.md`
- `.claude/settings.json` — Hook paths
- `docs/superpowers/specs/*.md` — Existing spec/plan files

### Tier 2 — Wikilink rewrites

All path-based wikilinks referencing wiki subdirectories need prefixing:

| Old pattern | New pattern |
|-------------|-------------|
| `[[concepts/X]]` | `[[004-wiki/concepts/X]]` |
| `[[entities/X]]` | `[[004-wiki/entities/X]]` |
| `[[summaries/X]]` | `[[004-wiki/summaries/X]]` |
| `[[qanda/X]]` | `[[004-wiki/qanda/X]]` |
| `[[synthesis]]` | `[[004-wiki/synthesis]]` |
| `[[index]]` | `[[004-wiki/index]]` |
| `[[sources-manifest]]` | `[[004-wiki/sources-manifest]]` |

Files affected: all `.md` files inside `004-wiki/`, plus any wikilinks in `AGENTS.md`, `CLAUDE.md`, and agent definitions.

Pipe syntax variants (`[[concepts/X|Display Text]]`) must also be handled.

### What doesn't change

- Inline claim citations (`^[raw/articles/source.md]`) — these are relative paths INSIDE the raw directory; the raw directory name change is handled by Tier 1
- `knowledge/` directory name — stays unnumbered
- `daily/` directory name — stays unnumbered
- All non-pipeline directories — no changes
- Wikilinks to non-wiki pages (e.g., `[[daily/2026-05-19]]`) — no change

## Verification

After migration:
1. `wiki-linter` agent — scan for broken wikilinks and orphaned pages
2. `sync-check` agent — verify schema and agent consistency
3. Manual spot-check — open a few wiki pages in Obsidian, confirm links resolve
