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
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Karpathy Tweet Llm Wiki

## Key Points

- Karpathy uses LLMs to build personal knowledge bases, shifting token throughput from code manipulation to knowledge manipulation (markdown and images) ^[raw/articles/karpathy-tweet-llm-wiki.md:4]
- Source documents are indexed into a raw/ directory, then incrementally compiled into a wiki of .md files with summaries, backlinks, concept categorization, and cross-links ^[raw/articles/karpathy-tweet-llm-wiki.md:7]
- At ~100 articles and ~400K words, RAG is unnecessary — the LLM auto-maintains index files and brief summaries to navigate the wiki ^[raw/articles/karpathy-tweet-llm-wiki.md:13]
- Query outputs (markdown files, Marp slides, matplotlib images) are filed back into the wiki so that explorations always "add up" in the knowledge base ^[raw/articles/karpathy-tweet-llm-wiki.md:16]
- LLM "health checks" (linting) find inconsistencies, impute missing data, discover connections for new articles, and improve data integrity ^[raw/articles/karpathy-tweet-llm-wiki.md:19]
- Custom tools like a vibe-coded search engine can be handed off to the LLM via CLI for larger queries ^[raw/articles/karpathy-tweet-llm-wiki.md:22]
- As the wiki grows, synthetic data generation and finetuning could let the LLM "know" the data in its weights rather than context windows ^[raw/articles/karpathy-tweet-llm-wiki.md:25]

## Quotes

- "I use an LLM to incrementally 'compile' a wiki, which is just a collection of .md files in a directory structure" ^[raw/articles/karpathy-tweet-llm-wiki.md:7]
- "The LLM writes and maintains all of the data of the wiki, I rarely touch it directly" ^[raw/articles/karpathy-tweet-llm-wiki.md:10]
- "I thought I had to reach for fancy RAG, but the LLM has been pretty good about auto-maintaining index files and brief summaries" ^[raw/articles/karpathy-tweet-llm-wiki.md:13]
- "My own explorations and queries always 'add up' in the knowledge base" ^[raw/articles/karpathy-tweet-llm-wiki.md:16]
- "I think there is room here for an incredible new product instead of a hacky collection of scripts" ^[raw/articles/karpathy-tweet-llm-wiki.md:27]

## Notes

- This tweet is a more condensed, practical companion to the longer karpathy-github-llm-wiki source — it focuses on workflow steps rather than architecture
- The Obsidian Web Clipper and local image download are the primary data ingestion tools mentioned
- No new entities or concepts beyond those already captured in the wiki

## Related

- [[concepts/llm_wiki]]
- [[concepts/rag]]
- [[concepts/memex]]
- [[entities/obsidian]]