---
title: "Routing Mode"
summary: "Configuration in Claude Code for Slack that determines how @Claude mentions are processed: either all as coding tasks (Code only) or intelligently between coding and chat (Code + Chat)"
type: concept
sources:
  - raw/document/claude code/claude-code-104-slack-2026-04-29.md
tags:
  - slack
  - routing
  - claude-code
  - configuration
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Routing Mode

Routing mode controls how Claude Code for Slack handles @Claude mentions, determining whether messages are sent to a Claude Code coding session on the web or to a standard Claude Chat response.

## Key Points

- Two modes available: Code only and Code + Chat, configured in the Claude App Home in Slack ^[raw/document/claude code/claude-code-104-slack-2026-04-29.md]
- Code only routes all @mentions to Claude Code sessions, best for teams using Claude in Slack exclusively for development tasks ^[raw/document/claude code/claude-code-104-slack-2026-04-29.md]
- Code + Chat analyzes each message and routes between Claude Code (for coding tasks) and Claude Chat (for writing, analysis, and general questions) ^[raw/document/claude code/claude-code-104-slack-2026-04-29.md]
- In Code + Chat mode, users can click "Retry as Code" to re-route a chat response as a coding session, or choose to send a coding session result to Chat ^[raw/document/claude code/claude-code-104-slack-2026-04-29.md]

## Details

The routing decision happens automatically when a user @mentions Claude in a Slack channel or thread. In Code + Chat mode, Claude analyzes the message content to determine intent. If it detects coding intent, the request is routed to a Claude Code session on the web. Otherwise, it responds as a chat assistant. The "Retry as Code" button lets users override the automatic routing when Claude misclassifies a request.

In Code only mode, no intent analysis occurs — all @mentions are treated as coding tasks. This is appropriate for teams that use Claude in Slack exclusively for software development work.

## Related

- [[entities/slack]]
- [[entities/claude_code]]
- [[entities/claude_code_web]]
- [[concepts/sessions]]
- [[summaries/claude-code-slack]]