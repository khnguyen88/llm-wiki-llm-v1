# LLM Wiki — Pipelines

All pipelines that move data through the system, the agents that run them, and the tools they depend on.

---

## Pipeline Overview

```
                           EXTERNAL KB (→ 004-wiki/)
                           ========================

Chain A: 001a-raw/ PDFs ──→ Document Processing ──→ 003-processed/ ──→ Ingest ──→ 004-wiki/
Chain B: User query ──────→ AI Research ──────────→ 001b-ai-research/ ─→ Ingest ──→ 004-wiki/
Chain C: 001a-raw/ .md ───→ Ingest (direct) ──────→ 004-wiki/
Chain D: YouTube URL ──────→ Transcript ───────────→ 001a-raw/transcripts/ ─→ (Review) ─→ Ingest ──→ 004-wiki/

                           INTERNAL KB (→ knowledge/)
                           ========================

Chain E: Conversations ───→ Memory Compilation ────→ knowledge/

                           HORIZONTAL (support both KBs)
                           ============================

Web Search  ←── ephemeral answers for any caller (auto-remediation, research, review)
Lint+Repair ←── health checks + fixes for 004-wiki/ and knowledge/
Wiki Query  ←── index-guided Q&A against 004-wiki/
```

---

## Document Processing Pipeline

Converts binary documents (PDF, DOCX, PPTX) into segmented, approved markdown ready for wiki ingestion. Orchestrated by the `document-processor` agent.

```
001a-raw/{file}.pdf
  → document-converter   (docling-serve → 002-raw-preprocessed/{name}-{date}.md + sidecar)
  → ocr-remediator       (deepseek-ocr → fix formulas/tables/diagrams)
  → markdown-chunker     (segment by chapters → 003-processed/{name}-part-NNN-{date}.md)
  → auto-remediation     (LLM + web-search fallback for unresolved elements)
  → human review gate    (approve/reject remaining issues)
  → 003-processed/ approved segments
```

| Step | Agent | Input | Output | Key Tools |
|------|-------|-------|--------|------------|
| Convert | `document-converter` | PDF/DOCX/PPTX | `002-raw-preprocessed/{name}-{date}.md` + `.elements.json` sidecar | docling-serve Docker (port 5001), docx2pdf, pypdf, `scripts/sidecar.py` |
| OCR Fix | `ocr-remediator` | Raw markdown + sidecar | Updated markdown + updated sidecar | Ollama + deepseek-ocr, arrase/OCR CLI (pipx), OpenRouter API, `scripts/ocr_remediate.py` |
| Chunk | `markdown-chunker` | Cleaned markdown + sidecar | `003-processed/{subfolder}/{name}-part-NNN-{date}.md` | `scripts/sidecar.py` |
| Approve | `document-processor` | Chunked segments + sidecar | Approved segments with `pipeline_state.stage == "approved"` | OpenRouter API, `web-search` agent |

**Gate:** The `wiki-maintainer` agent refuses to ingest any document whose sidecar doesn't have `stage == "approved"`.

---

## Ingest Pipeline

Extracts entities, concepts, claims, and summaries from a source file into the external wiki. Run by the `wiki-maintainer` agent via subagent-driven dispatch (one fresh subagent per source).

```
Approved source (001a-raw/, 001b-ai-research/, or 003-processed/)
  → Read source + existing wiki index
  → Extract entities, concepts, claims, quotes
  → Write summary page       → 004-wiki/summaries/
  → Create/update entities   → 004-wiki/entities/
  → Create/update concepts   → 004-wiki/concepts/
  → Update index             → 004-wiki/index.md
  → Update source manifest   → 004-wiki/sources-manifest.md
  → Update log               → 004-wiki/log.md
  → Update synthesis         → 004-wiki/synthesis.md
  → Lint + repair if needed
```

**Entry points:**
- Small markdown files (≤3,000 words): ingest directly
- Large files or PDFs: must go through Document Processing Pipeline first
- AI-researched files: ingest from `001b-ai-research/web/`

**Tools:** None external. LLM reads/writes files within the project.

---

## AI Research Pipeline

Deep web research that persists results as source files ready for wiki ingestion. Run by the `ai-research` agent.

```
User query
  → vane_web_search --save  → 001b-ai-research/web/{slug}-{date}.md
  → crawl4ai deep dive      → append ## Deep Dive sections
  → lint.py                 → validate metadata + structure
  → sync-check agent        → verify cross-file consistency
  → Ready for ingest
```

| Step | Tool/Agent | Purpose |
|------|------------|---------|
| Search | Vane API (localhost:3000) via `vane_web_search` | AI-synthesized results with inline citations |
| Deep dive | crawl4ai MCP (localhost:11235) | Full-text crawl of top 3-5 source URLs |
| Validate | `uv run python scripts/lint.py` | Structural + metadata validation |
| Verify | `sync-check` agent | Cross-reference consistency with project config |

**Prune-and-replace:** If research on the same topic (slug match) already exists in `001b-ai-research/web/`, the old file is deleted before saving the new one.

---

## Transcript Pipeline

Extracts YouTube transcripts and optionally reviews them for speech-to-text errors. Two-stage: `youtube-transcript` → (optional) `transcript-reviewer`.

```
YouTube URL
  → youtube-transcript   (youtube-transcript-api → 001a-raw/transcripts/{channel}-{date}.md; ytscribe.io API as fallback)
  → transcript-reviewer  (web-verify suspect terms → corrections + audit trail)
  → Ready for ingest
```

| Step | Agent | Input | Output | Key Tools |
|------|-------|-------|--------|------------|
| Extract | `youtube-transcript` | YouTube URL | `001a-raw/transcripts/{channel-or-topic}-{YYYY-MM-DD}.md` | youtube-transcript-api (primary), ytscribe.io API (fallback), YouTube oEmbed, crawl4ai REST API |
| Review | `transcript-reviewer` | Transcript file path or URL | Corrected file with `reviewed_date` + `revisions` in metadata | Vane API (vane_web_search), WebSearch (fallback) |

---

## Memory Compilation Pipeline

Extracts knowledge from Claude Code conversations into structured knowledge articles. Automatic (hooks + background processes) with manual override.

```
Session ends / context compacts
  → session-end.py or pre-compact.py hook fires
  → flush.py (background, Claude Agent SDK)
      → Extracts: Context, Key Exchanges, Decisions, Lessons, Action Items
      → Appends to daily/{YYYY-MM-DD}.md
      → If past 6 PM: spawns compile.py (background)
          → Reads daily log + existing knowledge/ articles
          → Creates/updates knowledge/concepts/ + knowledge/connections/
          → Updates knowledge/index.md + knowledge/log.md
```

| Component | Type | Purpose | Key Tools |
|-----------|------|---------|------------|
| `session-end.py` | Hook | Capture transcript on session close, spawn flush.py | File I/O, subprocess |
| `pre-compact.py` | Hook | Capture context before auto-compaction | File I/O, subprocess |
| `flush.py` | Script | LLM extraction of memories from transcript | Claude Agent SDK |
| `compile.py` | Script | Compile daily logs → knowledge articles | Claude Agent SDK, `scripts/state.json` |

**Manual compile:** `uv run python scripts/compile.py [--all | --file <path> | --dry-run]`

---

## Lint + Repair Pipeline

Detects and fixes structural and semantic issues across both knowledge bases.

```
User triggers lint
  → wiki-linter agent (or knowledge-compiler for internal KB)
      → 14 checks: broken links, orphans, stale articles, missing backlinks,
        sparse articles, unsourced claims, missing summary, duplicate concepts,
        malformed citations, broken citations, contradictions (LLM),
        raw source metadata, filename convention, schema cross-links
  → wiki-repair agent (for external KB only)
      → 7 fixes: fix-broken-links, add-backlinks, resolve-orphans,
        prune-stubs, merge-duplicates, validate-sources, fix-naming
```

| Command | Scope |
|---------|-------|
| `uv run python scripts/lint.py` | Both KBs (12 structural + 1 LLM) |
| `uv run python scripts/lint.py --structural-only` | Structural checks only (no API calls) |
| `uv run python scripts/lint.py --kb external` | External KB (004-wiki/) only |
| `uv run python scripts/lint.py --kb internal` | Internal KB (knowledge/) only |

---

## Web Search Pipeline

Ephemeral web search returning results without persistence. Used by other agents (auto-remediation, research, transcript review) and directly by users.

```
User query
  → vane_get_providers   (discover available models)
  → vane_web_search      (AI-synthesized results with inline citations)
  → Optional: crawl4ai    (deep dive on top 3-5 URLs)
  → Fallback: WebSearch   (if Vane is unavailable)
```

| Tool | When |
|------|------|
| Vane API (localhost:3000) | Primary — AI-synthesized results with narrative + sources |
| crawl4ai MCP (localhost:11235) | Optional deep dive into source pages |
| Built-in WebSearch | Fallback when Vane is down (shallower results) |

---

## Wiki Query Pipeline

Answers questions by reading the wiki index and synthesizing across relevant pages.

```
User question
  → Read 004-wiki/index.md (identify relevant pages)
  → Read 3-10 relevant pages in full
  → Synthesize answer with [[wikilink]] citations
  → Optional: file answer to knowledge/qa/{question}.md
```

**Agent:** `wiki-query` — index-guided retrieval, no RAG needed.

---

## Tool Dependency Cross-Reference

| Tool | Pipelines |
|------|-----------|
| **docling-serve** Docker (port 5001) | Document Processing |
| **Ollama** + deepseek-ocr model | Document Processing |
| **arrase/OCR** CLI (pipx) | Document Processing |
| **OpenRouter** API | Document Processing (OCR fallback, vision, auto-remediation) |
| **Vane** Docker (localhost:3000) | AI Research, Web Search, Transcript Review |
| **crawl4ai** MCP (localhost:11235) | AI Research, Web Search (deep dive), Transcript (metadata fallback) |
| **ytscribe.io** API (free tier, https://ytscribe.io/api) | Transcript (fallback) |
| **Claude Agent SDK** | Memory Compilation (flush.py, compile.py) |
| **scripts/sidecar.py** | Document Processing (all stages) |
| **scripts/ocr_remediate.py** | Document Processing (OCR stage) |
| **scripts/lint.py** | Lint+Repair, AI Research (post-save validation) |
| **scripts/compile.py** | Memory Compilation |
| **scripts/flush.py** | Memory Compilation |
