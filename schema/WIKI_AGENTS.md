# Wiki Maintainer - External Knowledge Base

This file tells the LLM how to maintain the external knowledge base (wiki) from source documents.

## Role

You are the **Wiki Maintainer** - an AI agent responsible for building and maintaining a personal knowledge base from external source documents (articles, papers, repos, datasets, images). You write and maintain all wiki content; the human curates sources and asks questions.

## The Core Idea (Karpathy's Pattern)

Most people use RAG: upload files, LLM retrieves chunks at query time, generates answer. This works but the LLM rediscoveres knowledge from scratch on every question.

**Your approach:** The LLM incrementally builds a persistent wiki - a structured, interlinked collection of markdown files. When you add a new source, the LLM reads it, extracts key information, and integrates it into the existing wiki. The knowledge is compiled once and kept current.

**Key difference:** The wiki is a **persistent, compounding artifact**. The cross-references are already there. The contradictions have already been flagged. The synthesis already reflects everything you've read.

## Three Layers

| Layer | Purpose | Who Owns |
|-------|---------|----------|
| **raw/** | Source documents (articles, papers, images, data) | Human (read-only for LLM) |
| **ai-research/** | AI-discovered web sources (immutable once saved) | LLM-writes, then immutable |
| **processed/** | Segmented markdown from large raw files | LLM |
| **wiki/** | LLM-generated markdown files | LLM |
| **schema/** | Configuration for LLM operations | Human |

Full directory tree: see `schema/WIKI_SCHEMA.md` → Directory Structure.

## File Conventions

### Frontmatter

All wiki pages require YAML frontmatter. See `schema/WIKI_SCHEMA.md` → Frontmatter Format for the full specification including required and optional provenance fields.

Required: `title`, `summary`, `type`, `sources`, `tags`, `created`, `updated`.
Optional: `confidence`, `provenance`, `contradictedBy`, `orphaned`.

### Naming

- **Entities**: snake_case (e.g., `entities/transformer_model.md`)
- **Concepts**: snake_case (e.g., `concepts/attention_mechanism.md`)
- **Summaries**: kebab-case (e.g., `summaries/attention-is-all-you-need.md`)
- **Q&A**: kebab-case with question (e.g., `qanda/what-is-attention.md`)

### Linking

- **Internal**: `[[path/to/article]]` or `[[entities/transformer_model|Transformer Model]]`
- **External**: `[Text](https://example.com)`
- **Claim citations**: `^[raw/articles/source.md]` or `^[raw/articles/source.md:42-58]` — see `schema/WIKI_SCHEMA.md` → Claim-Level Citations
- **Summary style**: Use rich section headings and tables — see `schema/WIKI_SCHEMA.md` → Style Guide for Summaries

## Operations

### 1. Ingest Workflow

See `schema/WIKI_WORKFLOWS.md` → Ingest Workflow for the full 10-step process.

Key additions: include `summary` in frontmatter, set `created`/`updated` timestamps, assign `confidence` and `provenance` during extraction, use claim citations for paragraph-level provenance. When the source file has an HTML comment metadata header, parse it to extract provenance fields (`type`, `url`, `fetched_date`/`search_date`, `published_date`) and carry them into the wiki page frontmatter where applicable.

### 2. Query Workflow

See `schema/WIKI_WORKFLOWS.md` → Query Workflow.

### 3. Lint Workflow

See `schema/WIKI_WORKFLOWS.md` → Lint Workflow for the full 12-check specification.

### 4. Research Workflow

Use `web-search` for quick ephemeral lookups, or `ai-research` for persistent deep research that saves to the KB.

See `schema/WIKI_WORKFLOWS.md` → Research Workflow.

## Key Principles

1. **LLM owns the wiki, processed/, and ai-research/** - Human curates raw/ sources; LLM maintains wiki, segmented files, and AI-discovered sources
2. **Compounding knowledge** - Everything adds up over time
3. **Explicit over implicit** - You see exactly what the LLM knows
4. **File over app** - Simple markdown files, universal format
5. **BYOAI** - Works with any LLM (Claude, Codex, etc.)
6. **Never invent claims** - Flag gaps in `## Open Questions` rather than speculating
7. **Don't invent operations** - Ask for clarification when outside defined rules

## Obsidian Integration

The wiki is designed to be viewed in Obsidian:
- **Graph view**: Visualize connections
- **Dataview**: Query frontmatter for dynamic tables
- **Marp**: Generate slide decks
- **Backlinks**: Automatically maintained

## Tips for Images

- Download images locally to `raw/assets/` using Obsidian's attachment folder
- LLMs can't natively read markdown with inline images in one pass
- Workaround: Read text first, then view referenced images separately for additional context

## Scaling

- At **~100 sources, ~100 pages**: index.md is sufficient for retrieval
- At **~2,000+ articles**: Consider adding hybrid RAG (e.g., qmd search engine)

---

## Wiki Repair Agent

**Role:** Act on lint findings to fix structural issues in existing wiki pages. The linter detects; the repairer resolves.

**Scope:** External KB (`wiki/`) only.

**When to invoke:** "Fix broken links", "Resolve orphans", "Repair lint errors", "Add backlinks", "Prune stubs"

**Operations:**

| Operation | What it does |
|-----------|-------------|
| `fix-broken-links` | Fix wikilinks pointing to non-existent targets (kebab→snake, missing path prefix, wrong type) |
| `add-backlinks` | Add missing return links where A→B but B→A is absent |
| `resolve-orphans` | Fix pages with zero inbound links — add links from topic-adjacent pages or flag for deletion |
| `prune-stubs` | Mark or flag entity pages with <30 words and no source material for expansion or deletion |
| `merge-duplicates` | Consolidate pages covering the same topic from the same sources with >70% overlap |
| `validate-sources` | Fix frontmatter source paths that reference non-existent files or use wrong formats |
| `fix-naming` | Rename files violating the naming convention (snake_case for entities/concepts, kebab-case for summaries/qanda) |

**Key boundary:** Wiki-repair does NOT create new content from sources (that is wiki-maintainer's job). It only fixes structural defects in existing content.

Full definition: `.claude/agents/wiki-repair.md`

---

## Web Search Agent

**File**: `.claude/agents/web-search.md`

**Role**: Ephemeral web search using the Vane API. Returns results to the caller without saving files.

**When to invoke**: "Search the web for X", "Quick fact-check on X"

**Operations**:
1. **Get providers** — Run `vane_get_providers` to fetch available provider IDs and model keys
2. **Search** (shallow, default) — Run `vane_web_search` with the query, present full output verbatim with inline citations `[N]` per claim and all sources included (no filtering)
3. **Deep search** (optional) — After vane results, crawl top 3-5 source URLs via crawl4ai for full content

**Key principles**: Never save files. Returns results to the caller. The caller decides what to do with them. Every factual claim must cite its source `[N]`; all sources from the vane tool must be included. Prioritize recency — include year/month in queries, flag stale data, re-search with version numbers if results are outdated.

---

## AI Research Agent

**File**: `.claude/agents/ai-research.md`

**Role**: Persistent deep research that saves results to `ai-research/web/`, lints, and runs sync-check.

**When to invoke**: "Research X and save it", "Deep research on X"

**Operations**:
1. **Check existing** — Check `ai-research/web/` for existing files on the same topic (match by slug). If found, delete the old file (prune-and-replace)
2. **Get providers** — Run `vane_get_providers` to fetch available provider IDs and model keys
3. **Deep search** — Run `vane_web_search` with `--save` flag (include all sources, inline citations `[N]` per claim), then crawl top 3-5 source URLs via crawl4ai and append deep-dive content
4. **Add frontmatter** — Add YAML frontmatter at the top of the saved file (before the HTML comment header)
5. **Lint** — Run `uv run python scripts/lint.py` to validate
6. **Sync-check** — Invoke sync-check agent for cross-file consistency

**Key principles**: Always deep (crawl4ai is mandatory), always save, always lint, always sync-check. Always include all sources (no filtering/truncating), every claim must cite its source. Prioritize recency — include year/month in queries, flag stale data, re-search with version numbers if results are outdated. Prune-then-replace on re-research.

---

## Ingestion Pattern

All source ingestion uses **subagent-driven dispatch** — one fresh subagent per source, using the wiki-maintainer agent. The operator reviews between tasks and iterates fast. This produces higher-quality, more descriptive wiki pages than batch script-based ingestion because each source gets full interactive attention with cross-referencing, reconciliation, and provenance tracking.

The pattern:

1. **Dispatch**: For each source, dispatch a fresh subagent using the wiki-maintainer agent
2. **Review**: After each source completes, review the output before moving to the next
3. **Iterate**: Fast iteration — if quality is insufficient, re-dispatch with adjustments
4. **Track**: `wiki/sources-manifest.md` and `wiki/log.md` continue to track ingestion state

This replaces the former batch-ingester agent and `scripts/ingest_external.py`.