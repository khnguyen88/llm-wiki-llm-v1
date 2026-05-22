# CLAUDE.md

Two parallel knowledge bases implementing Karpathy's LLM Wiki pattern — no RAG, index-guided retrieval instead.

## Architecture

| KB       | Raw source                                    | Compiled to  | Schema             |
| -------- | --------------------------------------------- | ------------ | ------------------ |
| External | `001a-raw/` + `001b-ai-research/` → `003-processed/` → `004-wiki/` | `004-wiki/`      | `schema/WIKI_*.md` |
| Internal | `daily/` (conversation logs)                    | `knowledge/` | `AGENTS.md`        |

Core insight: the LLM incrementally builds a **persistent, compounding wiki** instead of rediscovering knowledge from scratch on every query.

## Key Directories

- `001a-raw/` — Source documents (human-curated, read-only for LLM)
- `001b-ai-research/` — AI-discovered web sources (LLM-writes, immutable once saved)
- `002-raw-preprocessed/` — Document conversion + OCR output (pre-chunking)
- `003-processed/` — Segmented markdown from large raw files (LLM-owned)
- `004-wiki/` — External KB (LLM-owned)
- `004-wiki/qanda/` — Q&A pages filed by wiki-query
- `004-wiki/connections/` — Cross-concept connection pages
- `daily/` — Conversation logs (immutable)
- `knowledge/` — Internal KB (LLM-owned)

Full directory tree: `schema/WIKI_SCHEMA.md` → Directory Structure

## Project Agents

Defined in `.claude/agents/`. Each agent file is self-contained with its own operations, conventions, and examples. Full trigger table: `AGENTS.md` → Agent Dispatch Rules.

**`web-search` vs `ai-research`**: When the user says "web-search agent" they mean the project's `web-search` agent (Vane-first, ephemeral). Do **not** substitute the built-in `WebSearch` tool. The `ai-research` agent always does deep search (Vane + crawl4ai) and saves to `001b-ai-research/web/`.

## Core Conventions

- LLM owns `004-wiki/`, `knowledge/`, and `003-processed/` — human curates `001a-raw/` and `daily/`; `001b-ai-research/` sources are LLM-discovered but immutable once saved
- Never invent claims — flag gaps in `## Open Questions`; don't invent operations — ask for clarification when outside defined rules
- Wikilinks: `[[path/to/article]]` (no `.md`); citations: `^[001a-raw/articles/source.md]` or `^[001a-raw/articles/source.md:42-58]` for paragraph-level provenance
- Frontmatter required: title, summary, type, sources, tags, created, updated; optional: confidence, provenance, contradictedBy, orphaned
- Naming: kebab-case for all wiki pages; dates: ISO 8601 with timestamps; style: encyclopedia-style, factual, concise
- Git commits: never include AI attribution (Co-Authored-By, Generated with, etc.)

## On-Demand Details

Operations, file formats, scripts, hooks, and Obsidian integration live in:

- **Workflows**: `schema/WIKI_WORKFLOWS.md` (ingest, query, lint, research, search)
- **File formats**: `schema/WIKI_SCHEMA.md`
- **Agent roles**: `schema/WIKI_AGENTS.md`
- **Internal KB**: `AGENTS.md`
- **Scripts**: `scripts/*.py` (run via `uv run python scripts/<name>.py`)
- **Hooks**: `.claude/settings.json`
- **Web search output**: `schema/WIKI_WORKFLOWS.md` → Search Workflow (Vane and built-in WebSearch conventions)

## Crawling Rules

Always use the crawl4ai MCP tool for any web crawling or scraping tasks.
Do not fall back to WebFetch or write custom crawl scripts unless crawl4ai
MCP is confirmed unavailable. The crawl4ai container runs on localhost:11235.
