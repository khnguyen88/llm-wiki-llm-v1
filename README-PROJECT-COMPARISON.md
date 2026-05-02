# Project Comparison & Origin Tracing

This project is a fusion of four sources, each contributing distinct architectural ideas. This document traces every major feature back to its origin, documents what was modified or omitted, and highlights this project's own original contributions.

## Sources

| # | Source | Author | Type | Core Contribution |
|---|--------|--------|------|-------------------|
| 1 | [LLM Wiki Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) | Andrej Karpathy | Blog post / Gist | Foundational raw→wiki pipeline, index-guided retrieval, no RAG |
| 2 | [claude-memory-compiler](https://github.com/coleam00/claude-memory-compiler) | Cole Medin | GitHub repo | daily→knowledge pipeline, hooks, flush, Agent SDK scripts |
| 3 | [llm-wiki-compiler](https://github.com/atomicmemory/llm-wiki-compiler) | Atomic Memory | GitHub repo | Enhanced frontmatter, claim citations, lint rules, multi-provider |
| 4 | [karpathy-obsidian-vault](https://github.com/joshpocock/karpathy-obsidian-vault) | Josh Pocock | GitHub repo | ai-research directory, Obsidian integration, example templates |

---

## Feature Matrix

Legend: **A** = adopted as-is, **M** = modified, **O** = omitted, **—** = not present, **N** = new (this project's own)

| Feature | Karpathy Gist | Cole Medin | Atomic Memory | Josh Pocock | This Project |
|---------|:---:|:---:|:---:|:---:|:---:|
| **Directory Structure** | | | | | |
| `raw/` (human-curated sources) | A | — | A | A | A |
| `wiki/` (LLM-owned KB) | A | — | A | A | A |
| `daily/` (conversation logs) | — | A | — | — | A |
| `knowledge/` (compiled internal KB) | — | A | — | — | A |
| `ai-research/` (AI-discovered sources) | — | — | — | A | A |
| `processed/` (segmented large files) | — | — | — | — | N |
| `output/` (ephemeral artifacts) | — | — | — | A | O |
| `.llmwiki/` (internal state) | — | — | A | — | O (use `scripts/state.json`) |
| **Schema & Configuration** | | | | | |
| Schema as a separate doc (CLAUDE.md) | A | — | — | A | A |
| AGENTS.md as compiler specification | — | A | — | — | M (dual-purpose: schema + reference) |
| YAML frontmatter on wiki pages | — | A | M | — | M (merged both systems) |
| Provenance fields (confidence, provenance) | — | — | A | — | A |
| Page kinds (concept, entity, comparison, overview) | — | — | A | — | M (added summary, qanda, synthesis) |
| Schema JSON for page-kind rules | — | — | A | — | O (convention-based instead) |
| **Citation System** | | | | | |
| Source traceability (every claim → source) | A | — | A | A | A |
| `^[file.md]` paragraph-level citations | — | — | A | — | A |
| `^[file.md:42-58]` claim-level citations | — | — | A | — | A |
| `**Source:**` line per article | — | — | — | A | M (in frontmatter, not inline) |
| **Hooks** | | | | | |
| SessionStart context injection | — | A | — | — | A |
| SessionEnd transcript capture | — | A | — | — | A |
| PreCompact safety net | — | A | — | — | A |
| Git hooks (husky pre-commit/pre-push) | — | — | A | — | O |
| **Scripts** | | | | | |
| compile.py (daily→knowledge) | — | A | — | — | A |
| query.py (index-guided retrieval) | — | A | A | — | M (queries both KBs) |
| lint.py (health checks) | — | A | A | — | M (merged both lint systems) |
| flush.py (memory extraction) | — | A | — | — | A |
| ~~ingest_external.py~~ (removed) | — | — | — | — | R |
| config.py / utils.py (shared helpers) | — | A | — | — | A |
| Full TypeScript compiler pipeline | — | — | A | — | O (Python chosen instead) |
| MCP server | — | — | A | — | O (crawl4ai MCP instead) |
| **Lint System** | | | | | |
| Broken wikilinks | A | A | A | A | A |
| Orphan pages | A | A | A | A | A |
| Stale articles (hash-based) | — | A | — | — | M |
| Missing backlinks | — | A | — | — | A |
| Sparse articles | — | A | — | — | A |
| Contradictions (LLM check) | A | A | — | A | A |
| Broken/malformed citations | — | — | A | — | A |
| Low confidence / contradicted pages | — | — | A | — | A |
| Duplicate concepts | — | — | A | — | A |
| Missing summary | — | — | A | — | A |
| Excess inferred paragraphs | — | — | A | — | A |
| Schema cross-link minimum | — | — | A | — | O |
| Missing concepts (mentioned 3+ times) | — | — | — | A | M (flagged by wiki-linter) |
| Unsourced claims | — | — | — | A | A |
| **Agents** | | | | | |
| wiki-maintainer | — | — | — | A | M (formalized as agent file) |
| document-processor | — | — | — | — | N |
| knowledge-compiler | — | A | — | — | M (formalized as agent file) |
| wiki-linter | — | — | — | A | M (formalized + expanded) |
| wiki-repair | — | — | — | — | N |
| wiki-query | — | — | — | A | M (formalized, dual-KB) |
| sync-check | — | — | — | — | N |
| context-loader | — | — | — | — | N |
| ~~batch-ingester~~ (removed) | — | — | — | — | R |
| **Tools & Integrations** | | | | | |
| Obsidian as read-only IDE | A | — | — | A | A |
| Obsidian Web Clipper | A | — | — | A | A |
| Dataview plugin | A | — | — | A | A |
| Marp (slide decks) | A | — | — | — | O |
| Graph view | A | — | — | A | A |
| crawl4ai MCP server | — | — | — | — | N |
| Claude Agent SDK | — | A | — | — | A |
| Multiple LLM providers | — | — | A | — | O (Anthropic-only via Agent SDK) |
| qmd search tool | A | — | — | A | O |
| **Operations** | | | | | |
| Ingest (raw→wiki) | A | — | A | A | A |
| Query (index-guided) | A | A | A | A | M (queries both KBs) |
| Lint (health check) | A | A | A | A | M (merged + expanded) |
| Research (web→ai-research) | — | — | — | A | A |
| Compile (daily→knowledge) | — | A | — | — | A |
| Flush (auto-extract conversations) | — | A | — | — | A |
| Repair (fix structural issues) | — | — | — | — | N |
| Batch ingest | A | — | A | — | M (Agent SDK-based) |
| **Naming Conventions** | | | | | |
| snake_case for entities/concepts | — | — | — | — | N (from Atomic Memory's slug logic) |
| kebab-case for summaries/qanda | — | — | — | — | N |
| Lowercase hyphenated (Josh Pocock) | — | — | — | A | M (split by page type) |
| ISO 8601 dates with timestamps | — | A | — | — | A |
| Wikilinks `[[path/to/article]]` | A | A | A | A | A |

---

## Source Narratives

### 1. Karpathy's LLM Wiki Gist

The foundational concept document. Karpathy described the pattern abstractly — three layers (raw → wiki → schema), three operations (Ingest, Query, Lint), and two navigation files (index.md, log.md). The insight: "the wiki is a persistent, compounding artifact" where knowledge is compiled once and kept current.

**Core concepts adopted:**
- Three-layer architecture (raw sources → wiki → schema)
- Index-guided retrieval instead of RAG (index.md as the primary navigation mechanism)
- LLM owns the wiki; human curates sources
- Ingest/Query/Lint as the three core operations
- Obsidian as the "IDE" for browsing the wiki
- `index.md` and `log.md` as the two special navigation files
- "Never invent claims" principle
- The compounding knowledge loop: file answers back into the wiki

**What was modified:**
- Karpathy's schema is intentionally abstract ("this document describes the idea, not a specific implementation"). This project instantiated it with concrete file formats, naming conventions, and agent roles.
- The three layers became five (added `daily/` + `knowledge/` from Cole Medin, and `ai-research/` from Josh Pocock).
- Lint expanded from Karpathy's informal list to 12+1 formalized checks.
- Query expanded to search both KBs (external wiki + internal knowledge), not just the wiki.

**What was omitted:**
- Marp (slide deck generation) — not needed for this project's use case
- qmd (local search engine) — the index file is sufficient at current scale
- The "business/team" and "reading a book" use cases — this project focuses on personal research
- RAG/embedding discussion — this project firmly chose index-guided retrieval and doesn't plan to add RAG

---

### 2. Cole Medin's claude-memory-compiler

The "internal KB" system. Cole Medin adapted Karpathy's pattern to compile Claude Code conversations (instead of web articles) into a structured knowledge base. The compiler analogy — daily logs are source code, the LLM is the compiler, knowledge articles are the executable — is the core framing.

**Core concepts adopted:**
- `daily/` directory for conversation logs (immutable, append-only)
- `knowledge/` directory for compiled articles (concepts, connections, qa)
- The compiler analogy and its three-layer model
- Three hooks: session-start.py (context injection), session-end.py (transcript capture + spawn flush), pre-compact.py (safety net before auto-compaction)
- flush.py: automatic memory extraction from conversations via Agent SDK
- compile.py: Agent SDK-based compilation with tool access (Read, Write, Edit, Glob, Grep)
- query.py: index-guided retrieval loading the full KB into context
- lint.py: structural + LLM-based health checks
- End-of-day auto-compilation (6 PM trigger)
- State tracking via state.json (hashes, costs, timestamps)
- Incremental compilation (hash-based change detection)
- Claude Agent SDK with `permission_mode="acceptEdits"` and `max_turns=30`
- Cost tracking per operation
- Cross-platform support (Windows CREATE_NO_WINDOW, backslash escaping)

**What was modified:**
- Cole Medin's AGENTS.md serves as the sole schema. This project split the schema into AGENTS.md (internal KB) + CLAUDE.md (project-level lean config) + schema/ files (external KB). The intent: CLAUDE.md stays under 60 lines for fast context loading.
- Frontmatter was expanded from Cole Medin's minimal set (title, sources, created, updated) to include Atomic Memory's provenance fields (confidence, provenance, contradictedBy, orphaned).
- Lint checks expanded from 7 (6 structural + 1 LLM) to 12+1 by merging Atomic Memory's checks.
- The `connections/` article type was kept but `qa/` was aligned with the external wiki's `qanda/` naming convention.
- Scripts were extended: added `ingest_external.py` for the raw→wiki pipeline that Cole Medin doesn't have.
- Hook timeouts were tuned for the dual-KB context.

**What was omitted:**
- Cole Medin has no external wiki (raw→wiki). His system is purely internal (daily→knowledge). This project added the external pipeline from other sources.
- No separate `reports/` directory — this project added it for lint output (gitignored).
- Cole Medin's lint auto-fixable flag — not implemented; repair is a separate agent (wiki-repair).

---

### 3. Atomic Memory's llm-wiki-compiler

The most engineering-heavy source. A full TypeScript/Node.js compiler with 4 LLM providers, MCP server, two-phase compilation pipeline, review queue, and 11 lint rules. It targets the raw→wiki pipeline with sophisticated citation tracking and provenance metadata.

**Core concepts adopted:**
- Enhanced frontmatter with provenance fields: `confidence` (0-1), `provenanceState` (extracted/merged/inferred/ambiguous), `contradictedBy`, `orphaned`
- Claim-level citations: `^[file.md]` (paragraph) and `^[file.md:42-58]` (line-range)
- Page kinds: concept, entity, comparison, overview
- Multiple lint rules beyond basic broken-links/orphans: broken-citation, malformed-claim-citation, low-confidence, contradicted-page, duplicate-concept, missing-summary, excess-inferred-paragraphs
- Two-phase compilation concept (extract from all sources first, then generate pages)
- Incremental compilation (hash-based change detection)
- Cross-source dependency tracking (when source A and B both produce concept X)
- Compounding queries (file answers back into wiki)
- Atomic file writes (write to .tmp then rename)
- Prompt budget enforcement for large source sets
- Claude settings fallback for API credentials

**What was modified:**
- TypeScript → Python. The entire codebase was reimplemented in Python to match Cole Medin's script ecosystem and avoid a Node.js dependency.
- Page kinds expanded: added `summary`, `qanda`, `synthesis` types. Removed `overview` (replaced by `synthesis`).
- MCP server was not adopted (crawl4ai MCP used instead for web research).
- Review queue (candidate approval flow) was not adopted — this project ingests directly, trusting the schema and lint to catch issues.
- Frozen slug protection and cross-source dependency tracking were not implemented — the wiki is small enough that full re-ingestion is feasible.
- Embeddings/BM25 retrieval was not adopted — index-guided retrieval is sufficient at current scale.
- Multi-provider support was not adopted — this project uses Anthropic exclusively via the Agent SDK.
- Export formats (llms.txt, JSON, GraphML, Marp, JSON-LD) were not adopted.
- Session history adapters (Claude/Codex/Cursor) were not adopted — the flush.py system covers Claude Code sessions.
- Schema JSON configuration was not adopted — conventions are defined in AGENTS.md and schema/ markdown files instead.

**What was omitted (significant):**
- The entire TypeScript toolchain (tsup, vitest, husky, fallow)
- The MCP server with 7 tools + 5 resources
- The 4-provider abstraction layer (Anthropic, OpenAI, Ollama, MiniMax)
- The review queue and candidate approval system
- The chunked retrieval with BM25 reranking
- The 6 export formats
- The compilation lock (PID-based)
- The source collision handling (duplicate slugification)
- The output language control (--lang flag)

---

### 4. Josh Pocock's karpathy-obsidian-vault

The most minimal implementation. A pure prompt-driven architecture where the entire system is a single CLAUDE.md file with no scripts, no hooks, no MCP servers, and no automation. The LLM does everything by following the prompt.

**Core concepts adopted:**
- `ai-research/` directory for AI-discovered web sources (separate from human `raw/`)
- The `raw/` vs `ai-research/` ownership split: human curates raw/, LLM discovers ai-research/, both immutable once saved
- "One source, one file" in ai-research/ with frontmatter (url, fetched, summary)
- Obsidian as the read-only IDE with bundled plugins (Dataview, Local Images Plus)
- Graph view configured to show orphans
- 3-level index navigation (master-index → topic _index → articles)
- Example templates for entity, concept, and source-summary pages
- Lint as a first-class operation with 7 dimensions (contradictions, stale, orphans, missing concepts, missing cross-links, unsourced, suggested)
- `**Source:**` traceability line per article
- `## Open Questions` section for gaps instead of speculation
- The "cardinal rule": never invent claims

**What was modified:**
- Josh Pocock's CLAUDE.md is the sole governing document (~8.8KB, everything in one file). This project split it into a lean CLAUDE.md (~70 lines), AGENTS.md (~640 lines), and three schema/ files. The context-loader agent enforces CLAUDE.md stays under 60 lines.
- The 3-level index (master → topic → article) was simplified to a flat `wiki/index.md` with categories. Topic subfolders were not adopted.
- `output/` directory for ephemeral artifacts was not adopted — lint reports go to `reports/` (gitignored), query results go to `qanda/` (permanent).
- The pure prompt-driven approach (no scripts, no hooks) was replaced with programmatic automation (hooks + Agent SDK scripts).
- Example templates in `wiki/_examples/` were not adopted — conventions are documented in `schema/WIKI_SCHEMA.md` instead.
- Lint is automated and scriptable (scripts/lint.py) rather than purely manual.

**What was omitted:**
- The entire pure-prompt approach — this project adds hooks, scripts, and agents for mechanical enforcement.
- `output/` directory — not needed; reports are gitignored, queries are permanent.
- 3-level index hierarchy — flat index is simpler and sufficient.
- Example template files — schema docs serve this purpose.
- The Obsidianite theme and visual configuration — this project uses default Obsidian.
- Bundled Obsidian plugins in the repo — this project references them but doesn't commit plugin binaries.

---

## Original Contributions

Features that none of the four sources had — purely this project's own additions:

### Architecture

| Feature | Description |
|---------|-------------|
| **Dual KB architecture** | Two parallel knowledge bases (external wiki for web sources, internal knowledge for conversations) that share the same tooling conventions but serve different data flows. No source had both pipelines in one project. |
| **5-layer directory model** | `raw/` + `ai-research/` + `processed/` + `wiki/` + `knowledge/` — more granular than any single source's 2-3 layer model. |
| **`processed/` directory** | Intermediate segmentation layer for large files (PDFs, long articles). Files >3,000 words get split into processed/ before wiki ingestion. No source had this. |

### Agents

| Feature | Description |
|---------|-------------|
| **9 specialized agents** | Formalized agent files in `.claude/agents/` with distinct roles, boundaries, and operations. Cole Medin had no agents (prompt-only). Josh Pocock had operations in CLAUDE.md. Atomic Memory had a CLI, not agents. |
| **wiki-repair agent** | 7 structural repair operations (fix-broken-links, add-backlinks, resolve-orphans, prune-stubs, merge-duplicates, validate-sources, fix-naming). No source had a dedicated repair subsystem. |
| **sync-check agent** | Verifies consistency across config files, schemas, and agents. No source had cross-file consistency checking. |
| **context-loader agent** | On-demand rule loading with Guard (enforce CLAUDE.md < 60 lines) and Audit (find duplicated/orphaned/missing rules). No source had prompt health management. |
| **batch-ingester agent** | Agent SDK-based wrapper for bulk ingestion. Karpathy mentioned batch-ingest; this project implemented it. |
| **document-processor agent** | Dedicated agent for segmenting large files into processed/. No source had this. |

### Lint System

| Feature | Description |
|---------|-------------|
| **12+1 merged lint checks** | Combined the best of Cole Medin's 7 checks, Atomic Memory's 11 checks, and Josh Pocock's 7-point lint report into a single 12-check structural + 1 LLM contradiction check. |
| **Lint severity levels with auto-fixable flag** | Errors (broken links, duplicate concepts, citations), warnings (orphans, stale, contradictions), suggestions (sparse, missing backlinks). Wiki-repair agent handles auto-fixable items. |

### Scripts

| Feature | Description |
|---------|-------------|
| **ingest_external.py** | Bulk ingestion of raw/ and ai-research/ sources into wiki/. Uses Agent SDK with `max_turns=30`. No source had a separate bulk-ingest script (Atomic Memory uses the CLI compile command). |
| **Dual-KB query** | query.py searches both `wiki/` and `knowledge/` in a single operation. No source had a unified query across two KBs. |

### Documentation

| Feature | Description |
|---------|-------------|
| **Split documentation model** | CLAUDE.md (lean project instructions, ~70 lines), AGENTS.md (internal KB schema), schema/WIKI_*.md (external KB formats, workflows, agents), README-OWNER-GUIDE.md, README-USER-GUIDE.md. No source split docs this way — they either put everything in CLAUDE.md or AGENTS.md. |
| **README-OWNER-GUIDE.md** | Internal maintenance reference with architecture, data flow, ownership map, scripts reference, hooks reference. No source had an owner-specific guide. |

---

## Key Modifications

Where this project significantly diverged from any source's approach:

| Area | Source Approach | This Project's Approach | Why |
|------|----------------|------------------------|-----|
| **Language** | Atomic Memory: TypeScript/Node.js | Python | Consistency with Cole Medin's scripts; Agent SDK is Python-native; avoids Node.js dependency |
| **Automation** | Josh Pocock: pure prompt (no scripts/hooks) | Hooks + Agent SDK scripts | Mechanical enforcement is more reliable than prompt-only instructions; flush system needs background processes |
| **Lint** | Cole Medin: 7 checks; Atomic Memory: 11 checks; Josh Pocock: 7-point manual report | Merged 12+1 checks | Take the strongest structural checks from each source; add one LLM contradiction check |
| **Schema storage** | Atomic Memory: `.llmwiki/schema.json`; Josh Pocock: single CLAUDE.md | Convention-based (AGENTS.md + schema/*.md) | Markdown is easier for the LLM to read and edit than JSON; matches the wiki's own format |
| **Page kinds** | Atomic Memory: concept, entity, comparison, overview | concept, entity, summary, qanda, synthesis | Different page taxonomy: `summary` for source-level summaries (from Josh Pocock), `qanda` for filed queries (from Cole Medin), `synthesis` for the evolving thesis (unique) |
| **Frontmatter** | Cole Medin: minimal (title, sources, created, updated); Atomic Memory: full provenance | Merged: required (title, summary, type, sources, tags, created, updated) + optional provenance (confidence, provenance, contradictedBy, orphaned) | Best of both: required fields ensure minimum quality, optional provenance enables epistemic tracking |
| **Ingestion** | Josh Pocock: manual (human says "compile"); Atomic Memory: CLI command | Agent SDK scripts (ingest_external.py, compile.py) + batch-ingester agent | Automation reduces human effort; Agent SDK gives the LLM direct file I/O tools |
| **Query** | All sources: single-KB query | Dual-KB query (wiki + knowledge) | Both KBs may contain relevant information; unified query avoids the user deciding which KB to search |
| **Context injection** | Cole Medin: knowledge/index.md only | Knowledge index + daily log + sync-check reminder | More context at session start; sync-check catches drift early |
| **Citations** | Josh Pocock: `**Source:**` inline; Atomic Memory: `^[file.md]` footnote | `^[raw/articles/source.md]` or `^[raw/articles/source.md:42-58]` in footnote style with full path | Full path enables lint to verify source existence; line ranges enable paragraph-level provenance |
| **Index navigation** | Josh Pocock: 3-level (master → topic → article); Atomic Memory: auto-generated TOC + MOC | Flat `wiki/index.md` with categories + `wiki/sources-manifest.md` for source tracking | Simpler structure; sources-manifest tracks what's been ingested (no source had this) |

---

## What Was Deliberately Left Out

| Feature | Source | Why Omitted |
|---------|--------|-------------|
| MCP server (7 tools + 5 resources) | Atomic Memory | crawl4ai MCP handles web research; Agent SDK scripts handle the rest. Adding a second MCP adds complexity without clear benefit. |
| Multi-provider support (OpenAI, Ollama, MiniMax) | Atomic Memory | This project uses Anthropic exclusively via Agent SDK. Multi-provider adds abstraction layers not needed. |
| Review queue / candidate approval flow | Atomic Memory | Trust the schema + lint to catch issues. A review queue adds latency without proportionate quality gain at current scale. |
| Embeddings / BM25 retrieval | Atomic Memory | Index-guided retrieval is sufficient at 50-500 articles. Embeddings add infrastructure cost with no benefit until ~2,000 articles. |
| 6 export formats (llms.txt, JSON, JSON-LD, GraphML, Marp, full) | Atomic Memory | No current use case. Can be added later if needed. |
| Husky git hooks (pre-commit type check, pre-push build) | Atomic Memory | This project has no TypeScript build step. Claude Code hooks serve a different purpose (session lifecycle, not code quality). |
| Compilation lock (PID-based) | Atomic Memory | Single-user project; concurrent compilation is unlikely. Can be added if scale demands it. |
| Session history adapters (Claude, Codex, Cursor) | Atomic Memory | flush.py handles Claude Code sessions. Other editors are not in scope. |
| Marp slide deck generation | Karpathy | Not needed for personal research wiki. |
| qmd local search engine | Karpathy, Josh Pocock | Index file is sufficient at current scale. |
| 3-level index hierarchy | Josh Pocock | Flat index with categories is simpler and sufficient for current article count. |
| Obsidianite theme | Josh Pocock | Default Obsidian theme is fine. Visual customization is low priority. |
| Bundled Obsidian plugins in repo | Josh Pocock | Plugin binaries in git is a maintenance burden; this project references them in README instead. |
| Output language control (--lang flag) | Atomic Memory | English-only is sufficient. |

---

## Lineage Summary

```
Karpathy Gist (concept)
  ├── raw/ → wiki/ pipeline
  ├── index.md + log.md navigation
  ├── Ingest / Query / Lint operations
  ├── "No RAG" index-guided retrieval
  ├── Obsidian as IDE
  └── Compounding knowledge loop
        │
        ├── Cole Medin (internal KB + automation)
        │     ├── daily/ → knowledge/ pipeline
        │     ├── 3 hooks (session-start, session-end, pre-compact)
        │     ├── flush.py (memory extraction)
        │     ├── compile.py (Agent SDK-based)
        │     ├── query.py + lint.py
        │     ├── End-of-day auto-compilation
        │     └── State tracking + cost tracking
        │
        ├── Atomic Memory (epistemic rigor + scale features)
        │     ├── Provenance frontmatter (confidence, provenance, contradictedBy)
        │     ├── Claim-level citations ^[file.md:42-58]
        │     ├── 11 structural lint rules
        │     ├── Page kinds (concept, entity, comparison, overview)
        │     ├── Two-phase compilation concept
        │     └── Incremental compilation
        │
        └── Josh Pocock (AI research + Obsidian)
              ├── ai-research/ directory convention
              ├── raw/ vs ai-research/ ownership split
              ├── Obsidian plugin integration (Dataview, Local Images)
              ├── Example templates (entity, concept, source-summary)
              ├── 7-point lint report
              └── "Never invent claims" cardinal rule
                    │
                    ▼
              THIS PROJECT
              ├── Dual KB architecture (unique)
              ├── 9 specialized agents (unique)
              ├── 12+1 merged lint checks (merged from all)
              ├── Agent SDK batch ingestion (unique)
              ├── Split documentation model (unique)
              ├── processed/ directory (unique)
              ├── sync-check + context-loader agents (unique)
              └── Python implementation (choice)
```