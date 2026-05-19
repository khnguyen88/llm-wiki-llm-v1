---
title: "Transcript Search"
summary: "Feature that lets users search conversation transcripts in transcript mode by pressing /, stepping through matches with n and N"
type: concept
sources:
  - raw/document/claude code/claude-code-118-whats-new-2026-w13-2026-04-29.md
tags:
  - claude-code
  - transcripts
  - search
  - sessions
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Transcript Search

A feature introduced in v2.1.83 that enables searching within conversation transcripts. Press `/` in transcript mode to initiate a search, then use `n` to step to the next match and `N` to step to the previous match. ^[raw/document/claude code/claude-code-118-whats-new-2026-w13-2026-04-29.md]

## Key Points

- Press `/` in transcript mode to search the conversation ^[raw/document/claude code/claude-code-118-whats-new-2026-w13-2026-04-29.md]
- `n` steps forward through matches; `N` steps backward ^[raw/document/claude code/claude-code-118-whats-new-2026-w13-2026-04-29.md]
- Open transcript mode with `Ctrl+O`, then search (e.g., `/migrate` to find the word "migrate") ^[raw/document/claude code/claude-code-118-whats-new-2026-w13-2026-04-29.md]
- Useful for locating specific commands or outputs deep in long conversations ^[raw/document/claude code/claude-code-118-whats-new-2026-w13-2026-04-29.md]

## Details

Transcript search addresses the difficulty of finding specific content in long sessions. Before this feature, locating a particular Bash command or output in a conversation hundreds of messages deep required scrolling through the entire transcript. The search interface follows Vim conventions (`/` to search, `n`/`N` to navigate), making it familiar to terminal users. ^[raw/document/claude code/claude-code-118-whats-new-2026-w13-2026-04-29.md]

## Related

- [[concepts/sessions]]
- [[entities/claude_code]]
- [[summaries/claude-code-whats-new-2026-w13]]