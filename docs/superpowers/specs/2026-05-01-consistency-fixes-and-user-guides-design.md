# Design Spec: Consistency Fixes + README-USER-GUIDE & README-OWNER-GUIDE

Date: 2026-05-01

## Overview

Fix 20+ inconsistencies between project documentation, schema files, agent definitions, scripts, and actual code state. Then create two new guide documents:

- **README-USER-GUIDE.md** — for new users/adopters wanting to understand and set up the system
- **README-OWNER-GUIDE.md** — for the project owner (future self) needing quick reference on internals

---

## Part 1: Consistency Fixes

### 1.1 Documentation Fixes (AGENTS.md)

| # | Fix | Detail |
|---|-----|--------|
| 1 | Remove duplicate `wiki-repair.md` entry | Line ~338 lists wiki-repair.md twice in `.claude/agents/` |
| 2 | Fix Python version | Change "Python 3.12+" to "Python >=3.11" to match pyproject.toml |
| 3 | Add `context-loader.md` to agents listing | Present on disk and in CLAUDE.md agent table but missing from AGENTS.md project tree |
| 4 | Fix Windows hook creation flags | Change `DETACHED_PROCESS` to `CREATE_NO_WINDOW` to match actual code |
| 5 | Add `tools_scripts/` to project structure | Directory exists on disk but not documented |
| 6 | Fix sources-manifest.md comment | Change `raw/processed` to `raw/ai-research/processed` in project tree comment |
| 7 | Fix frontmatter examples to use ISO 8601 timestamps | Change date-only format (e.g., `2026-04-01`) to timestamp format (e.g., `"2026-04-01T12:00:00Z"`) |
| 8 | Add `summary`, `type`, `tags` as required frontmatter for internal KB | Currently only lists `title, sources, created, updated` — CLAUDE.md declares these as universally required |
| 9 | Document session-start.py sync-check injection | session-start.py injects a sync-check reminder — this behavior is not mentioned in AGENTS.md hook section |
| 10 | Update lint check count from 12 to 8 | Remove the 4 unimplemented checks (missing summary, duplicate concept, malformed citation, broken citation) from the documented list |
| 11 | Update --max-words default from 3000 to 30000 | The script default is 30000; CI workflow already overrides to 3000 explicitly |

### 1.2 Documentation Fixes (Other Files)

| # | File | Fix |
|---|------|-----|
| 12 | `.claude/settings.json` | Change `python` to `uv run python` in all 3 hook commands |
| 13 | `CLAUDE.md` | Add `schema/WIKI_AGENTS.md` to On-Demand Details section |
| 14 | `schema/WIKI_SCHEMA.md` | Fix `[[Page Name]]` bare format to `[[path/to/article]]` to match CLAUDE.md convention |
| 15 | `schema/WIKI_WORKFLOWS.md` | Update lint check count from 12 to 8; remove the 4 unimplemented checks from the list |
| 16 | `.claude/agents/wiki-linter.md` | Update check count from 12 to 8; remove the 4 unimplemented checks |
| 17 | `.claude/agents/knowledge-compiler.md` | Add `summary`, `type`, `tags` to frontmatter required fields list |
| 18 | `.claude/agents/batch-ingester.md` | Update --max-words default from 3000 to 30000 |
| 19 | `README.md` | Fix sources-manifest.md comment to include ai-research/; add tools_scripts/ to project structure |

### 1.3 Wiki Frontmatter Fixes

| # | File | Fix |
|---|------|-----|
| 20 | `wiki/index.md` | Add `summary` field; change `date` to `created`/`updated` with ISO 8601 timestamps |
| 21 | `wiki/sources-manifest.md` | Add `summary`, `sources`, `tags`, `created`, `updated` fields; change `date` to `created`/`updated` |

### 1.4 Code Fix

| # | Fix | Detail |
|---|-----|--------|
| 22 | Implement synthesis.md update in `ingest_external.py` | Add a `update_wiki_synthesis()` function that updates `wiki/synthesis.md` after ingest, completing the documented step 10 of the ingest workflow. The function should append new source references and update the frontmatter `updated` timestamp. |

### 1.5 Cleanup

| # | Action | Detail |
|---|--------|---------|
| 23 | Delete `.agents/` directory | Empty directory with broken symlink. Add `.agents/` to `.gitignore` |
| 24 | Gitignore `compound-knowledge.md` | Nearly empty placeholder file, only referenced as a naming example in wiki-repair.md |
| 25 | Gitignore `_useful_tools.md` | Personal scratch file, not referenced by any workflow |

---

## Part 2: README-USER-GUIDE.md

**Audience:** New users and potential adopters who want to understand or set up the system.

**Structure:**

1. **What is LLM Wiki?** — One-paragraph explanation of the pattern: persistent wiki instead of RAG, index-guided retrieval, two knowledge bases
2. **Quick Start** — Prerequisites (Python >=3.11, uv, Anthropic API key), clone/install, first ingest command
3. **The Two Knowledge Bases** — Diagram showing the three-layer pipeline:
   - External KB: raw/ -> processed/ -> wiki/
   - Internal KB: daily/ -> knowledge/
4. **Directory Map** — Full directory tree with descriptions, split into:
   - Wiki content directories (raw/, ai-research/, processed/, wiki/) — what you curate vs what the LLM owns
   - Project infrastructure (scripts/, hooks/, schema/, .claude/, daily/, knowledge/) — how the system works
   - Supporting files (pyproject.toml, .gitignore, etc.)
5. **Core Commands** — Table of `uv run python scripts/<name>.py` commands with flags
6. **Using the Agents** — Table of 9 agents with invocation triggers
7. **Obsidian Integration** — Opening wiki/ as an Obsidian vault
8. **Crawling Docs** — crawl4ai MCP, REST API fallback

**Key convention for directory ownership descriptions:**
- `raw/` — human-curated (you add sources here)
- `ai-research/` — LLM-discovered, human-approved, immutable once saved
- `processed/` — LLM-owned staging (segmented from large raw files)
- `daily/` — LLM-curated from human conversations
- `wiki/` — LLM-owned (compiled knowledge articles)
- `knowledge/` — LLM-owned (compiled internal knowledge)

---

## Part 3: README-OWNER-GUIDE.md

**Audience:** Project owner (future self) needing quick reference on internals.

**Structure:**

1. **Architecture at a Glance** — Two-KB diagram with ownership annotations
2. **Data Flow** — How a source becomes a wiki article (10-step ingest); how a conversation becomes a knowledge article (flush -> compile)
3. **File Ownership Map** — Which directories/files the human edits vs which the LLM edits
4. **Scripts Reference** — Each script's purpose, key functions, CLI flags, state files
5. **Hooks Reference** — What each hook does, when it fires, what it spawns
6. **Agent Dispatch Rules** — When to invoke each agent, trigger phrases
7. **Schema Cross-References** — What each schema file defines and where it's referenced
8. **Known Issues & Design Decisions** — Current limitations and intentional choices
9. **Maintenance Tasks** — sync-check cadence, lint frequency, state file locations, how to reset

---

## Out of Scope

- Implementing the 4 missing lint checks (removed from docs instead)
- Refactoring existing scripts or workflows beyond the synthesis.md fix
- Changing the CI workflow's --max-words override (3000 is intentional for cost control)
- Adding new agents or workflows
- Populating ai-research/, processed/, or knowledge/qa/ directories