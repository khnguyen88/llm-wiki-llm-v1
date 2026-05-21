---
title: "Session Recap"
summary: "Claude Code feature that summarizes what happened in a session while the terminal was unfocused, so users can quickly catch up after switching away"
type: concept
sources:
  - raw/document/claude code/claude-code-117-whats-new-2026-04-29.md
  - raw/document/claude code/claude-code-121-whats-new-2026-w16-2026-04-29.md
  - raw/document/claude code/claude-code-122-whats-new-2026-w17-2026-04-29.md
tags:
  - claude-code
  - sessions
  - ux
  - productivity
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.8
provenance: merged
---

# Session Recap

Session recap shows users what happened in a Claude Code session while the terminal was unfocused, enabling them to quickly catch up on progress without scrolling through the full transcript. It was introduced as part of the Week 17 release (v2.1.114-119). ^[001a-raw/document/claude code/claude-code-117-whats-new-2026-04-29.md]

## Key Points

- Displays a summary of activity that occurred while the terminal window was not in focus ^[001a-raw/document/claude code/claude-code-117-whats-new-2026-04-29.md]
- Introduced in the Week 17 release (v2.1.114-119, April 20-24, 2026) ^[001a-raw/document/claude code/claude-code-117-whats-new-2026-04-29.md]
- `/recap` triggers an on-demand session recap; recap display can be toggled via `/config` ^[001a-raw/document/claude code/claude-code-121-whats-new-2026-w16-2026-04-29.md]
- Automatic session recap triggers when the user returns to a terminal after switching focus away, providing a one-line summary of what happened while away ^[001a-raw/document/claude code/claude-code-122-whats-new-2026-w17-2026-04-29.md]
- The automatic recap can be turned off from `/config` ^[001a-raw/document/claude code/claude-code-122-whats-new-2026-w17-2026-04-29.md]

## Details

Session recap addresses the common scenario where a user switches away from the Claude Code terminal to another window or application and later returns to find that Claude has continued working. Rather than requiring the user to scroll through the full conversation history, session recap presents a condensed summary of the actions and results that occurred during the unfocused period. ^[001a-raw/document/claude code/claude-code-117-whats-new-2026-04-29.md]

The `/recap` command provides on-demand access to the session summary, and the feature can be disabled through `/config` settings. ^[001a-raw/document/claude code/claude-code-121-whats-new-2026-w16-2026-04-29.md]

## Related

- [[004-wiki/concepts/sessions]]
- [[004-wiki/entities/claude-code]]
- [[004-wiki/summaries/claude-code-whats-new]]
- [[004-wiki/summaries/claude-code-whats-new-2026-w17]]