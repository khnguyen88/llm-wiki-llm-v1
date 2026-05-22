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
| **001a-raw/** | Source documents (articles, papers, images, data) | Human (read-only for LLM) |
| **001b-ai-research/** | AI-discovered web sources (immutable once saved) | LLM-writes, then immutable |
| **003-processed/** | Segmented markdown from large raw files | LLM |
| **004-wiki/** | LLM-generated markdown files | LLM |
| **schema/** | Configuration for LLM operations | Human |

Full directory tree: see `schema/WIKI_SCHEMA.md` → Directory Structure.

## File Conventions

### Frontmatter

All wiki pages require YAML frontmatter. See `schema/WIKI_SCHEMA.md` → Frontmatter Format for the full specification including required and optional provenance fields.

Required: `title`, `summary`, `type`, `sources`, `tags`, `created`, `updated`.
Optional: `confidence`, `provenance`, `contradictedBy`, `orphaned`.

### Naming

- **Entities**: kebab-case (e.g., `entities/transformer-model.md`)
- **Concepts**: kebab-case (e.g., `concepts/attention-mechanism.md`)
- **Summaries**: kebab-case (e.g., `summaries/attention-is-all-you-need.md`)
- **Q&A**: kebab-case (e.g., `qanda/why-is-x-important.md`)
- **Connections**: kebab-case (e.g., `connections/agent-loop-and-context-window.md`)

### Linking

- **Internal**: `[[path/to/article]]` or `[[entities/transformer_model|Transformer Model]]`
- **External**: `[Text](https://example.com)`
- **Claim citations**: `^[001a-raw/articles/source.md]` or `^[001a-raw/articles/source.md:42-58]` — see `schema/WIKI_SCHEMA.md` → Claim-Level Citations
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

1. **LLM owns the wiki, 003-processed/, and 001b-ai-research/** - Human curates 001a-raw/ sources; LLM maintains wiki, segmented files, and AI-discovered sources
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

- Download images locally to `001a-raw/assets/` using Obsidian's attachment folder
- LLMs can't natively read markdown with inline images in one pass
- Workaround: Read text first, then view referenced images separately for additional context

## Scaling

- At **~100 sources, ~100 pages**: index.md is sufficient for retrieval
- At **~2,000+ articles**: Consider adding hybrid RAG (e.g., qmd search engine)

---

## Wiki Repair Agent

**Role:** Act on lint findings to fix structural issues in existing wiki pages. The linter detects; the repairer resolves.

**Scope:** External KB (`004-wiki/`) only.

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
| `fix-naming` | Rename files violating the naming convention (kebab-case for all wiki pages) |

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

**Role**: Persistent deep research that saves results to `001b-ai-research/web/`, lints, and runs sync-check.

**When to invoke**: "Research X and save it", "Deep research on X"

**Operations**:
1. **Check existing** — Check `001b-ai-research/web/` for existing files on the same topic (match by slug). If found, delete the old file (prune-and-replace)
2. **Get providers** — Run `vane_get_providers` to fetch available provider IDs and model keys
3. **Deep search** — Run `vane_web_search` with `--save` flag (include all sources, inline citations `[N]` per claim), then crawl top 3-5 source URLs via crawl4ai and append deep-dive content
4. **Add frontmatter** — Add YAML frontmatter at the top of the saved file (before the HTML comment header)
5. **Lint** — Run `uv run python scripts/lint.py` to validate
6. **Sync-check** — Invoke sync-check agent for cross-file consistency

**Key principles**: Always deep (crawl4ai is mandatory), always save, always lint, always sync-check. Always include all sources (no filtering/truncating), every claim must cite its source. Prioritize recency — include year/month in queries, flag stale data, re-search with version numbers if results are outdated. Prune-then-replace on re-research.

---

## YouTube Transcript Agent

**File**: `.claude/agents/youtube-transcript.md`

**Role**: Ephemeral extraction agent that fetches YouTube transcripts via youtube-transcript-api (primary), with ytscribe.io API as fallback. Merges timestamps into paragraphs, resolves metadata through cascading fallbacks (oEmbed, WebSearch, crawl4ai, user prompt), and saves to `001a-raw/transcripts/`.

**When to invoke**: "Get transcript for `<url>`", "Extract transcript from `<url>`"

**Operations**:
1. **Parse video ID** — Extract 11-character YouTube video ID from URL (supports watch, shorts, live, youtu.be, raw ID)
2. **Fetch transcript (primary)** — `youtube-transcript-api` Python library → raw timestamped segments
3. **Fallback** — If primary fails, use ytscribe.io API with key from `.ytscribe.env` → paragraph + timestamped views
4. **Merge timestamps** — Group segments into paragraphs, prepend each paragraph with its first segment's timestamp
5. **Fetch metadata** — Cascading fallback: oEmbed → WebSearch → crawl4ai → prompt user
6. **Determine filename** — `001a-raw/transcripts/{channel-or-topic}-{YYYY-MM-DD}.md`, increment suffix if exists
7. **Write output** — Save with `video-transcript-llm` HTML comment metadata header and per-paragraph timestamps

**Key principles**: Try free youtube-transcript-api first, fall back to ytscribe.io only on failure. Preserve original paragraph text from the extraction source. Cascading metadata fallback. Schema-compliant output. No wiki modification — only writes to `001a-raw/transcripts/`. Idempotent filenames (increment suffix, never overwrite).

---

## Transcript Reviewer Agent

**File**: `.claude/agents/transcript-reviewer.md`

**Role**: Ephemeral review agent that reads a `001a-raw/transcripts/` file, identifies mistranscribed/mispelled terms using context + web verification, applies corrections, and writes a revision summary.

**When to invoke**: "Review transcript `<path-or-url>`", "Review this transcript for errors"

**Operations**:
1. **Resolve input** — Accept a file path or YouTube URL; if URL, search `001a-raw/transcripts/` for matching file by URL in metadata header
2. **Check for prior review** — If `reviewed_date` exists in metadata, warn user and ask whether to re-review
3. **Extract context clues** — Read metadata header for channel name, video title, topic keywords for disambiguation
4. **Paragraph-by-paragraph review** — For each paragraph, identify suspicious terms, web-verify each via Vane (fall back to built-in WebSearch), record verified corrections
5. **Apply corrections** — Replace all verified terms consistently across the entire file, preserving timestamps and formatting
6. **Update metadata** — Add/replace `reviewed_date` and `revisions` fields in the HTML comment metadata header
7. **Print summary** — Report unique corrections, total replacements, uncertain terms, and revert instructions

**Key principles**: Verify don't guess (web-search confirmation required). Context-aware disambiguation. Preserve original formatting. Consistent corrections across the file. Case-sensitive casing from web results. Only writes to `001a-raw/transcripts/`. Idempotent on re-review.

---

## Document Converter Agent

**File**: `.claude/agents/document-converter.md`

**Role**: Converts documents (PDF, DOCX, PPTX) to raw markdown via docling-serve.

**When to invoke**: "Convert this document to markdown", first stage of document processing pipeline

**Operations**:
1. **Pre-process** — DOCX → PDF via docx2pdf; PDFs > 25 pages split via pypdf
2. **Convert** — docling-serve Docker API, parallel conversion for split PDFs, concatenate output
3. **Write output** — `002-raw-preprocessed/{name}-{date}.md` + `{name}-{date}.sidecar.json`

**Key principles**: Sidecar is the contract — always write it. Never segment (that's markdown-chunker's job). OCR remediation is handled by the separate ocr-remediator stage.

## OCR Remediator Agent

**File**: `.claude/agents/ocr-remediator.md`

**Role**: Fixes docling OCR gaps by running deepseek-ocr on pages with placeholder comments or low-confidence elements.

**When to invoke**: "Fix OCR issues in 002-raw-preprocessed", second stage of document processing pipeline

**Operations**:
1. **Scan** — Find `<!-- formula-not-decoded -->` and similar placeholders + low-confidence sidecar elements
2. **Convert source** — If not already PDF, convert to PDF (DOCX via docx2pdf, PPTX via LibreOffice)
3. **Run deepseek-ocr** — `ocr --include <problem-pages>` on the PDF
4. **Splice fixes** — Replace placeholders with actual formulas, upgrade low-confidence sections
5. **Update sidecar** — Mark resolved elements with `ocr_method: "arrase-deepseek"`
6. **Optional OpenRouter** — If `OPENROUTER_API_KEY` is set and deepseek-ocr fails, attempt OpenRouter vision

**Key principles**: Best-effort — never blocks the pipeline. Only runs on pages that need it. Produces same format it received.

---

## Markdown Chunker Agent

**File**: `.claude/agents/markdown-chunker.md`

**Role**: Partitions raw markdown into chapter/section-based chunks in `003-processed/`, using TOC as the structure guide.

**When to invoke**: "Chunk this markdown into chapters", third stage of document processing pipeline

**Operations**:
1. **Detect structure** — Parse TOC, H1/H2/H3 hierarchy; identify copyright/boilerplate pages
2. **Extract TOC** — Standalone chunk-000 with segment map
3. **Partition** — Chunk by H1-H2 sections; word count is safety check, not driver
4. **Assign elements** — Map each sidecar element to its owning chunk by page number
5. **Write chunks** — `003-processed/{subfolder}/{name}-part-NNN-{date}.md` with full metadata headers and navigation links

**Key principles**: TOC is the chunking map. Never orphan an element. Navigation links on every chunk.

---

## Document Processor Agent

**File**: `.claude/agents/document-processor.md`

**Role**: Breaks large raw files (PDFs, long reports, files >3,000 words) into segmented markdown in `003-processed/` so they can be ingested into the wiki within LLM context limits.

**When to invoke**: "Process this PDF", "Segment this document", files >3,000 words

**Operations**:
1. **Read** — Read the document (page-by-page for PDFs, full file for markdown)
2. **Identify structure** — Parse TOC, headers, chapter breaks, logical section boundaries
3. **Plan segments** — Target ~500–1,500 words per segment; group thin sections, split oversized ones
4. **Convert to markdown** — Preserve heading hierarchy, convert tables, save complex images to `001a-raw/assets/`
5. **Write metadata headers** — Each segment gets a `processed-segment` HTML comment header per `schema/WIKI_SCHEMA.md`; raw source metadata header goes on the first segment only
6. **Write segments** — Save to `003-processed/{subfolder}/` with naming convention `{base-name}-part-{###}[-{chapter-##|section-slug}]-{YYYY-MM-DD}.md`
7. **Delete original** — Remove from `001a-raw/` after all segments confirmed (optional — keep if reprocessing may be needed)

**Key principles**: Preserve heading hierarchy. Navigation links between sibling segments. Segment map in first segment. Only writes to `003-processed/` and `001a-raw/assets/`.

---

## Wiki Linter Agent

**File**: `.claude/agents/wiki-linter.md`

**Role**: Runs health checks across both the external (`004-wiki/`) and internal (`knowledge/`) knowledge bases.

**When to invoke**: "Lint the wiki", "Run health check"

**Operations**: 14 checks across three severity levels:
- **Errors**: broken links, duplicate concepts, malformed citations, broken citations, raw source metadata validation
- **Warnings**: orphan pages, stale articles, sparse articles (<50 chars body), missing recommended metadata fields
- **Suggestions**: orphan sources (unprocessed), missing backlinks, sparse articles (<200 words), missing summary, filename conventions

**CLI**: `uv run python scripts/lint.py` (all checks), `--structural-only` (skip contradiction check), `--kb internal|external`

Reports save to `reports/lint-YYYY-MM-DD.md`.

**Key principles**: Actionable findings, not style nits. Prioritize errors > warnings > suggestions. Never invent claims.

---

## Wiki Query Agent

**File**: `.claude/agents/wiki-query.md`

**Role**: Answers questions against both the external (`004-wiki/`) and internal (`knowledge/`) knowledge bases.

**When to invoke**: Questions about compiled knowledge

**Operations**:
1. **Read index** — Start with `004-wiki/index.md` and/or `knowledge/index.md`
2. **Select relevant pages** — Identify 3–10 relevant articles
3. **Read in full** — Drill into summaries first, then entities/concepts for detail
4. **Follow links** — Read referenced articles if relevant
5. **Synthesize** — Combine information from multiple pages into a coherent answer with `[[wikilinks]]`
6. **Identify gaps** — Note what the KB doesn't cover; offer `web-search` or `ai-research` to fill gaps

**CLI**: `uv run python scripts/query.py "question"`, `--file-back` to save answer back to KB

**Key principles**: Always start from the index. Distinguish KB knowledge from general knowledge. Never invent claims. Offer to invoke `web-search` or `ai-research` when gaps are detected.

---

## Knowledge Compiler Agent

**File**: `.claude/agents/knowledge-compiler.md`

**Role**: Compiles daily conversation logs into the internal knowledge base at `knowledge/`.

**When to invoke**: "Compile daily logs"

**Operations**:
1. **Compile** — Read daily log, read `knowledge/index.md`, update existing concepts or create new ones, write connections articles, update index and log
2. **Query** — Read index, identify relevant articles, synthesize answer with citations
3. **Lint** — 12 health checks for the internal KB (broken links, orphans, stale articles, etc.)

**Key principles**: Owns `knowledge/` directory. Prefers updating existing articles over creating near-duplicates. Never invent claims.

---

## Sync Check Agent

**File**: `.claude/agents/sync-check.md`

**Role**: Verifies cross-file consistency across project configuration files (directories, agents, schemas, scripts, conventions).

**When to invoke**: After structural changes to dirs/schemas/agents

**Operations**: Checks 8 categories of consistency:
1. Directory references — all files defining project structure agree on dirs/subdirs
2. Agent cross-references — every agent references correct dirs, schemas, scripts
3. Script names — CLI commands match actual scripts in `scripts/`
4. Conventions — naming, frontmatter, citations consistent across all files
5. Processed/ pipeline — `003-processed/` referenced alongside `001a-raw/` and `001b-ai-research/`
6. Source manifest — listed in all relevant files
7. Wiki directory naming — `summaries/` not `sources/`
8. Raw source metadata — 8 source types and field tiers match across schema, linter, maintainer, workflows

**Output**: Markdown checklist of inconsistencies found and items verified.

---

## Context Loader Agent

**File**: `.claude/agents/context-loader.md`

**Role**: Loads domain-specific rules on demand and enforces that `CLAUDE.md` stays lean (under 60 lines).

**When to invoke**: "Load rules for X", "Audit CLAUDE.md", "Guard prompt health"

**Operations**:
1. **Load** — Inject domain rules on demand by reading the relevant source file and presenting exact rules (no summarizing)
2. **Guard** — Enforce CLAUDE.md leanness: under 60 lines, no domain rules in root, no duplication, pointers over inlining
3. **Audit** — Check rule distribution across the project for duplication, orphaned rules, missing rules, stale pointers

**Key principles**: Never load rules proactively — only on demand. Loading speculatively bloats context. No duplication — rules live in ONE place.

---

## Ingestion Pattern

All source ingestion uses **subagent-driven dispatch** — one fresh subagent per source, using the wiki-maintainer agent. The operator reviews between tasks and iterates fast. This produces higher-quality, more descriptive wiki pages than batch script-based ingestion because each source gets full interactive attention with cross-referencing, reconciliation, and provenance tracking.

The pattern:

1. **Dispatch**: For each source, dispatch a fresh subagent using the wiki-maintainer agent
2. **Review**: After each source completes, review the output before moving to the next
3. **Iterate**: Fast iteration — if quality is insufficient, re-dispatch with adjustments
4. **Track**: `004-wiki/sources-manifest.md` and `004-wiki/log.md` continue to track ingestion state

This replaces the former batch-ingester agent and `scripts/ingest_external.py`.