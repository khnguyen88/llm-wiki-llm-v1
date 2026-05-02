---
title: "Karpathy Github Llm Wiki"
summary: "Karpathy's original design document for the LLM Wiki pattern — a persistent, compounding wiki built and maintained by an LLM from curated sources, contrasting with RAG's per-query retrieval"
type: summary
sources:
  - raw/articles/karpathy-github-llm-wiki.md
tags:
  - llm-wiki
  - architecture
  - knowledge-management
  - rag
created: "2026-05-01T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 1.0
provenance: reingested
---

# Karpathy Github Llm Wiki

## Summary

Karpathy's gist is the canonical design document for the LLM Wiki pattern. It describes a three-layer architecture (raw sources, LLM-generated wiki, schema) and three core operations (ingest, query, lint) that replace traditional RAG with a persistent, compounding knowledge artifact. The key insight is that LLMs eliminate the bookkeeping burden that causes humans to abandon knowledge bases, enabling a wiki that grows richer with every source. ^[raw/articles/karpathy-github-llm-wiki.md:9-15]

## Architecture: Three-Layer Model

| Layer | Description | Ownership | Mutability |
|-------|-------------|-----------|------------|
| Raw sources | Curated collection of source documents (articles, papers, images, data) | Human-curated | Immutable |
| The wiki | Directory of LLM-generated markdown files (summaries, entities, concepts, synthesis) | LLM-owned | LLM-writes, human-reads |
| The schema | Configuration document (e.g., CLAUDE.md) defining structure, conventions, workflows | Co-evolved by human + LLM | Updated as needs evolve |

^[raw/articles/karpathy-github-llm-wiki.md:29-35]

## Core Operations

| Operation | Description | Typical Scope |
|-----------|-------------|---------------|
| **Ingest** | LLM reads a new source, discusses with human, writes summary, updates index, updates entities/concepts, appends log | 10-15 wiki pages per source |
| **Query** | LLM searches wiki, reads relevant pages, synthesizes answer with citations; good answers filed back as new pages | Varies by question |
| **Lint** | Periodic health check for contradictions, stale claims, orphans, missing cross-references, data gaps | Full wiki scan |

^[raw/articles/karpathy-github-llm-wiki.md:39-43]

## Navigation: Index and Log

Two special files replace the need for embedding-based RAG infrastructure at moderate scale (~100 sources, ~hundreds of pages):

- **index.md** -- Content-oriented catalog of every page with one-line summaries, organized by category. The LLM reads it first to find relevant pages, then drills in. ^[raw/articles/karpathy-github-llm-wiki.md:49]
- **log.md** -- Chronological, append-only record of ingests, queries, lint passes. Entries start with a consistent prefix (e.g., `## [YYYY-MM-DD]`) making the file parseable with Unix tools. ^[raw/articles/karpathy-github-llm-wiki.md:51]

## Why It Works

The pattern succeeds because of a fundamental division of labor:

- **LLM handles** all bookkeeping: updating cross-references, keeping summaries current, noting contradictions, maintaining consistency across dozens of pages. Cost of maintenance is near zero. ^[raw/articles/karpathy-github-llm-wiki.md:68]
- **Human handles** curation, direction, questioning, and analysis. ^[raw/articles/karpathy-github-llm-wiki.md:70]

The concept is related in spirit to Vannevar Bush's Memex (1945) -- a personal curated knowledge store with associative trails. The critical difference: the LLM solves the maintenance problem that Bush could not. ^[raw/articles/karpathy-github-llm-wiki.md:72]

## Use Cases

| Domain | Example Applications |
|--------|---------------------|
| Personal | Goals, health, psychology, self-improvement, journal entries |
| Research | Papers, articles, reports with evolving thesis over weeks/months |
| Book reading | Character pages, themes, plot threads per chapter |
| Business/team | Internal wiki from Slack threads, transcripts, project docs |
| Other | Competitive analysis, due diligence, trip planning, course notes, hobbies |

^[raw/articles/karpathy-github-llm-wiki.md:19-25]

## Key Quotes

> "The wiki is a persistent, compounding artifact." ^[raw/articles/karpathy-github-llm-wiki.md:15]

> "Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase." ^[raw/articles/karpathy-github-llm-wiki.md:17]

> "Good answers can be filed back into the wiki as new pages." ^[raw/articles/karpathy-github-llm-wiki.md:41]

> "Humans abandon wikis because the maintenance burden grows faster than the value. LLMs don't get bored, don't forget to update a cross-reference, and can touch 15 files in one pass." ^[raw/articles/karpathy-github-llm-wiki.md:68]

## Related

- [[concepts/llm_wiki]]
- [[entities/obsidian]]
- [[concepts/rag]]
- [[concepts/memex]]
- [[concepts/file_over_app]]
- [[concepts/byoai]]
