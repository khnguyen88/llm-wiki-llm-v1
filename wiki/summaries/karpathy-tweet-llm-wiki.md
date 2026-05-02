---
title: "Karpathy Tweet Llm Wiki"
summary: "Karpathy describes his LLM Wiki workflow: ingesting sources into raw/, compiling a .md wiki, using Obsidian as the IDE, querying without RAG at moderate scale, and iteratively enhancing the knowledge base"
type: summary
sources:
  - raw/articles/karpathy-tweet-llm-wiki.md
tags:
  - llm-wiki
  - knowledge-management
  - workflow
created: "2026-05-01T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: reingested
---

# Karpathy Tweet Llm Wiki

## Summary

In this tweet thread, Karpathy describes his practical LLM Wiki workflow in a condensed, six-step format. He reports shifting his token throughput from manipulating code to manipulating knowledge stored as markdown and images. The tweet serves as the practical companion to the architectural design document (see [[summaries/karpathy-github-llm-wiki]]), emphasizing "how it works in practice" over "what the architecture is." ^[raw/articles/karpathy-tweet-llm-wiki.md:4]

## Six-Step Workflow

| Step | Activity | Key Details |
|------|----------|-------------|
| 1. Data Ingest | Collect sources into raw/, LLM compiles wiki | Obsidian Web Clipper + local image download; summaries, backlinks, concepts |
| 2. IDE | Obsidian as viewing frontend | LLM writes/maintains all data; Marp for slides |
| 3. Q&A | Ask complex questions against the wiki | No RAG needed at ~100 articles / ~400K words; index files suffice |
| 4. Output | Render answers as files, file back into wiki | Markdown, Marp slides, matplotlib images; knowledge compounds |
| 5. Linting | Health checks for inconsistencies | Find stale data, impute missing data (web search), suggest new articles |
| 6. Extra tools | Custom CLIs for larger queries | Vibe-coded search engine used directly or handed to LLM via CLI |

^[raw/articles/karpathy-tweet-llm-wiki.md:7-22]

## Key Observations

- **Scale threshold**: At ~100 articles and ~400K words, the LLM can navigate the wiki without RAG by relying on auto-maintained index files and brief summaries. This suggests a practical scale where index-based navigation is sufficient without embedding infrastructure. ^[raw/articles/karpathy-tweet-llm-wiki.md:13]
- **Compounding knowledge**: Query outputs are filed back into the wiki rather than disappearing into chat history, so every exploration adds to the knowledge base. ^[raw/articles/karpathy-tweet-llm-wiki.md:16]
- **Future direction**: As the wiki grows, synthetic data generation + finetuning could allow the LLM to "know" the data in its weights instead of context windows. ^[raw/articles/karpathy-tweet-llm-wiki.md:25]

## Tools Used

| Tool | Purpose |
|------|---------|
| Obsidian Web Clipper | Convert web articles to markdown sources |
| Obsidian (IDE) | View wiki, raw data, visualizations |
| Marp (Obsidian plugin) | Generate slide decks from markdown |
| Custom search engine | Vibe-coded for larger queries via CLI |
| Unix CLI tools | Operate on file-based wiki data |

^[raw/articles/karpathy-tweet-llm-wiki.md:7-10,22]

## Key Quotes

> "I use an LLM to incrementally 'compile' a wiki, which is just a collection of .md files in a directory structure." ^[raw/articles/karpathy-tweet-llm-wiki.md:7]

> "The LLM writes and maintains all of the data of the wiki, I rarely touch it directly." ^[raw/articles/karpathy-tweet-llm-wiki.md:10]

> "I thought I had to reach for fancy RAG, but the LLM has been pretty good about auto-maintaining index files and brief summaries." ^[raw/articles/karpathy-tweet-llm-wiki.md:13]

> "My own explorations and queries always 'add up' in the knowledge base." ^[raw/articles/karpathy-tweet-llm-wiki.md:16]

> "I think there is room here for an incredible new product instead of a hacky collection of scripts." ^[raw/articles/karpathy-tweet-llm-wiki.md:27]

## Related

- [[concepts/llm_wiki]]
- [[concepts/rag]]
- [[concepts/memex]]
- [[entities/obsidian]]
- [[summaries/karpathy-github-llm-wiki]]
