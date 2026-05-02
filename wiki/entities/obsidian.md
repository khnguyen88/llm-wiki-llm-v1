---
title: "Obsidian"
summary: "A markdown-based note-taking application used as the viewing IDE for LLM Wikis, with graph view, plugins, and Web Clipper for source collection"
type: entity
sources:
  - raw/articles/karpathy-github-llm-wiki.md
  - raw/articles/karpathy-tweet-llm-wiki.md
tags:
  - llm-wiki
  - knowledge-management
  - tools
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T16:30:00Z"
confidence: 0.9
provenance: extracted
---

# Obsidian

A markdown-based note-taking application that serves as the viewing and browsing interface for an LLM Wiki. Karpathy describes the relationship: "Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase." ^[raw/articles/karpathy-github-llm-wiki.md:17]

## Key Facts

- Used as the real-time browser for wiki content — the LLM agent makes edits while the user follows links, checks graph view, and reads updated pages ^[raw/articles/karpathy-github-llm-wiki.md:17]
- Web Clipper is a browser extension that converts web articles to markdown for adding sources to the raw collection ^[raw/articles/karpathy-github-llm-wiki.md:59]
- Supports downloading images locally by setting an attachment folder path and binding a hotkey, allowing the LLM to view and reference images directly ^[raw/articles/karpathy-github-llm-wiki.md:60]
- Graph view shows the shape of the wiki — what's connected to what, which pages are hubs, which are orphans ^[raw/articles/karpathy-github-llm-wiki.md:61]
- Marp plugin enables generating slide deck presentations directly from wiki content ^[raw/articles/karpathy-github-llm-wiki.md:62]
- Dataview plugin runs queries over page frontmatter (tags, dates, source counts) to generate dynamic tables and lists ^[raw/articles/karpathy-github-llm-wiki.md:63]
- Serves as the "IDE frontend" where users view raw data, compiled wiki, and derived visualizations; the LLM writes and maintains all wiki data directly ^[raw/articles/karpathy-tweet-llm-wiki.md:10]

## Related

- [[concepts/llm_wiki]]