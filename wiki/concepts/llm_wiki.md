---
title: "LLM Wiki"
summary: "A personalization pattern where an LLM incrementally builds a persistent, compounding wiki of knowledge, putting the user in full control of their data"
type: concept
sources:
  - raw/articles/farzapedia.md
  - raw/articles/karpathy-github-llm-wiki.md
  - raw/articles/karpathy-tweet-llm-wiki.md
tags:
  - llm-wiki
  - personalization
  - knowledge-management
  - architecture
created: "2026-05-01T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: merged
---

# LLM Wiki

A pattern for AI personalization and knowledge management where the LLM incrementally builds and maintains a persistent wiki of structured, interlinked markdown files -- rather than relying on per-query retrieval (RAG) or implicit learning. The wiki sits between the user and raw sources as a compounding artifact that grows richer with every source added. ^[raw/articles/karpathy-github-llm-wiki.md:11-13]

## Architecture

The pattern defines three distinct layers with clear ownership boundaries:

| Layer | Composition | Owner | Mutability |
|-------|-------------|-------|------------|
| **Raw sources** | Curated articles, papers, images, data files | Human-curated | Immutable (LLM reads, never writes) |
| **The wiki** | LLM-generated markdown: summaries, entity pages, concept pages, comparisons, index, log, synthesis | LLM-owned | LLM writes and maintains; human reads |
| **The schema** | Configuration (CLAUDE.md, AGENTS.md) defining structure, conventions, workflows | Co-evolved | Human + LLM update together |

^[raw/articles/karpathy-github-llm-wiki.md:29-35]

## Core Operations

### Ingest
When a new source is added to `raw/`, the LLM reads it, discusses key takeaways with the human, writes or updates a summary page, updates relevant entity and concept pages across the wiki, updates the index, and appends an entry to the log. A single source typically touches 10-15 wiki pages. Sources can be ingested singly (preferred for depth and human guidance) or in batches (for speed). ^[raw/articles/karpathy-github-llm-wiki.md:39]

### Query
The LLM searches the wiki, reads relevant pages, and synthesizes answers with citations. Key insight: good answers can be filed back into the wiki as new pages (comparisons, analyses, connections discovered during querying), so explorations compound in the knowledge base. ^[raw/articles/karpathy-github-llm-wiki.md:41] ^[raw/articles/karpathy-tweet-llm-wiki.md:16]

At ~100 articles and ~400K words, Karpathy reports that RAG is unnecessary -- the LLM navigates via auto-maintained index files and brief summaries. ^[raw/articles/karpathy-tweet-llm-wiki.md:13]

### Lint
Periodic health checks scan for: contradictions between pages, stale claims superseded by newer sources, orphan pages with no inbound links, important concepts lacking their own page, missing cross-references, and data gaps fillable via web search. The LLM also suggests new questions to investigate and new sources to look for. ^[raw/articles/karpathy-github-llm-wiki.md:43] ^[raw/articles/karpathy-tweet-llm-wiki.md:19]

## The Four Pillars of Personalization

Karpathy articulates four properties that make the LLM Wiki pattern superior to implicit AI personalization: ^[raw/articles/farzapedia.md:4-9]

| Pillar | Description |
|--------|-------------|
| **Explicit** | Knowledge artifacts are viewable and manageable -- not hidden in a black-box model |
| **Yours** | Data stays on the user's machine, extractable and portable |
| **File over App** | Data lives in universal formats (markdown, images), interoperable with any tool |
| **BYOAI** | Any AI model can be plugged in; finetuning can embed knowledge in weights |

## Why It Works

The pattern succeeds through division of labor: LLMs handle the bookkeeping that causes humans to abandon knowledge bases (updating cross-references, flagging contradictions, maintaining consistency across dozens of pages). Humans handle curation, direction, questioning, and analysis. The cost of maintenance is near zero for the human. ^[raw/articles/karpathy-github-llm-wiki.md:68-70]

The wiki is a git repository of markdown files, providing version history, branching, and collaboration for free. ^[raw/articles/karpathy-github-llm-wiki.md:64]

## Conceptual Predecessors

The idea is related to Vannevar Bush's Memex (1945) -- a personal, curated knowledge store with associative trails between documents. Bush's vision was closer to the LLM Wiki than to what the web became: private, actively curated, where connections between documents are as important as the documents themselves. The part Bush could not solve was who performs the maintenance -- the LLM handles that. ^[raw/articles/karpathy-github-llm-wiki.md:72]

## Future Directions

As the wiki grows, synthetic data generation and finetuning could embed knowledge in model weights rather than context windows, enabling the model to "know" the data permanently. ^[raw/articles/karpathy-tweet-llm-wiki.md:25] ^[raw/articles/farzapedia.md:9]

## Use Cases

- Personal tracking (goals, health, psychology, self-improvement)
- Deep research (papers, articles, evolving thesis over weeks/months)
- Book reading (character pages, themes, plot threads per chapter)
- Business/team wikis (Slack threads, meeting transcripts, project documents)
- Competitive analysis, due diligence, trip planning, course notes, hobby deep-dives

^[raw/articles/karpathy-github-llm-wiki.md:19-25]

## Related

- [[concepts/file_over_app]]
- [[concepts/byoai]]
- [[concepts/rag]]
- [[concepts/memex]]
- [[entities/obsidian]]
- [[entities/qmd]]
