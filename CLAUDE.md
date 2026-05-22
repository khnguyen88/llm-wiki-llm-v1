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

Full directory tree with all subfolders: see `schema/WIKI_SCHEMA.md` → Directory Structure

## Project Agents

Defined in `.claude/agents/`. Each agent file is self-contained with its own operations, conventions, and examples. Invoke by name; don't inline their rules here.

| Agent                | When to invoke                                               |
| -------------------- | ------------------------------------------------------------ |
| `wiki-maintainer`    | "Process this source", "Ingest X"                            |
| `document-converter`  | "Convert this document to markdown"                         |
| `ocr-remediator`      | "Fix OCR issues in 002-raw-preprocessed", "Run deepseek-ocr on problem pages" |
| `markdown-chunker`    | "Chunk this markdown into chapters"                         |
| `document-processor` | "Process this source", "Run the full pipeline on X", "Approve document for wiki" |
| `knowledge-compiler` | "Compile daily logs"                                         |
| `wiki-linter`        | "Lint the wiki", "Run health check"                          |
| `wiki-repair`        | "Fix broken links", "Resolve orphans", "Repair lint errors"  |
| `wiki-query`         | Questions about compiled knowledge                           |
| `web-search`         | "Search the web for X", "Quick fact-check on X" — **ephemeral**: uses `vane_web_search` shell tool, returns results to caller, never saves files |
| `ai-research`        | "Research X and save it", "Deep research on X" — **persistent**: deep Vane search + crawl4ai follow-up, saves to `001b-ai-research/web/`, always lints and sync-checks |
| `youtube-transcript` | "Get transcript for `<url>`", "Extract transcript from `<url>`" — **ephemeral**: uses youtube-transcript-api (primary), ytscribe.io API key from `.ytscribe.env` (fallback), saves to `001a-raw/transcripts/`, never modifies wiki |
| `transcript-reviewer` | "Review transcript `<path-or-url>`", "Review this transcript for errors" — **ephemeral**: verifies and corrects speech-to-text errors in `001a-raw/transcripts/`, records revisions in metadata |
| `sync-check`         | After structural changes to dirs/schemas/agents              |
| `context-loader`     | "Load rules for X", "Audit CLAUDE.md", "Guard prompt health" |

**`web-search` vs `ai-research`**: When the user says "web-search agent" they mean the project's `web-search` agent (Vane-first, ephemeral). Do **not** substitute the built-in `WebSearch` tool. The `ai-research` agent is for when the user wants results persisted as wiki source files — it always does deep search (Vane + crawl4ai) and saves to `001b-ai-research/web/`.

## Core Conventions

- LLM owns `004-wiki/` and `knowledge/` — human curates `001a-raw/` and `daily/`
- `001b-ai-research/` sources are LLM-discovered but immutable once saved
- Never invent claims — flag gaps in `## Open Questions` instead
- Don't invent operations — ask for clarification when outside defined rules
- Wikilinks: `[[path/to/article]]` (no `.md`)
- Claim citations: `^[001a-raw/articles/source.md]` or `^[001a-raw/articles/source.md:42-58]` for paragraph-level provenance
- Frontmatter required on all wiki pages (title, summary, type, sources, tags, created, updated)
- Optional provenance fields: confidence, provenance, contradictedBy, orphaned
- Naming: kebab-case for all wiki pages (concepts, entities, summaries, qanda, connections)
- Dates: ISO 8601 with timestamps (`"2026-04-05T12:00:00Z"`)
- Style: encyclopedia-style, factual, concise
- Git commits: never include AI attribution (Co-Authored-By, Generated with, etc.) — commit messages must be AI-free

## On-Demand Details

Operations, file formats, scripts, hooks, and Obsidian integration live in:

- **Workflows**: `schema/WIKI_WORKFLOWS.md`
- **File formats**: `schema/WIKI_SCHEMA.md`
- **Agent roles**: `schema/WIKI_AGENTS.md`
- **Internal KB**: `AGENTS.md`
- **Scripts**: `scripts/*.py` (run via `uv run python scripts/<name>.py`)
- **Hooks**: `.claude/settings.json`

## Web Search Output Convention

### Vane (`vane_web_search`)
When using the Vane web search tool, the output follows the
`ai-research-multi` schema from `schema/WIKI_SCHEMA.md`. Always present the
full output verbatim — schema header, message body, and **all** Sources (do not
filter or truncate the Sources list). Do not summarize, reformat, or abstract
away any part. **Every factual claim must include an inline citation `[N]`
referencing the numbered source it came from** — a bare Sources section at the
end is insufficient. To save results as wiki source files, use `--save` which
writes to `001b-ai-research/web/{slug}-{date}.md`.

### Built-in WebSearch
When using the built-in `WebSearch` tool, always include a **Sources** section
at the end with all result URLs as markdown hyperlinks. Every factual claim in
the response must include an inline citation `[N]` referencing the numbered
source it came from — a bare Sources section at the end is insufficient. Do not
omit or truncate any source from the search results.

## Crawling Rules

Always use the crawl4ai MCP tool for any web crawling or scraping tasks.
Do not fall back to WebFetch or write custom crawl scripts unless crawl4ai
MCP is confirmed unavailable. The crawl4ai container runs on localhost:11235.
