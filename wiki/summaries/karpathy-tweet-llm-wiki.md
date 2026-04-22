---
title: Karpathy Tweet on LLM Knowledge Bases
type: summary
date: 2026-04-22
sources:
  - raw/articles/karpathy-tweet-llm-wiki.md
tags:
  - knowledge-management
  - llm
  - karpathy
  - twitter
---

# Karpathy Tweet on LLM Knowledge Bases

## Key Points

- Karpathy finds LLM knowledge bases "very useful recently" — a large fraction of his token throughput goes into manipulating knowledge (stored as markdown and images), not just code
- Data ingest: index sources into `raw/`, then use an LLM to incrementally "compile" a wiki with summaries, backlinks, concept articles, and cross-links
- Uses Obsidian Web Clipper to convert web articles, plus a hotkey to download images locally for LLM reference
- IDE: Obsidian as the "frontend" — views raw data, compiled wiki, and derived visualizations. The LLM writes and maintains all wiki data; Karpathy rarely edits it directly
- Q&A: once the wiki is big enough (~100 articles, ~400K words), complex questions work well without RAG — the LLM auto-maintains index files and reads relevant data
- Output: markdown files, Marp slide decks, matplotlib images — all viewable in Obsidian. Answers can be "filed back" into the wiki
- Linting: LLM health checks for inconsistent data, missing data (with web search), interesting connections for new articles
- Extra tools: developing CLI tools for the LLM to use, like a small search engine accessible via web UI or CLI
- Future: synthetic data generation + finetuning so the LLM "knows" the data in weights, not just context windows

## Quote

> "TLDR: raw data from a given number of sources is collected, then compiled by an LLM into a .md wiki, then operated on by various CLIs by the LLM to do Q&A and to incrementally enhance the wiki, and all of it viewable in Obsidian. You rarely ever write or edit the wiki manually, it's the domain of the LLM."

## Notes

This tweet is a shorter, more practical summary of the same ideas as the LLM Wiki gist. The gist provides more architectural depth; the tweet provides the hands-on workflow and scale observations.