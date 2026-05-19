---
title: "Claude Code Slack"
summary: "Integration that brings Claude Code into Slack workspaces, routing @Claude mentions to coding sessions on claude.ai/code with automatic intent detection and channel-based access control"
type: summary
sources:
  - raw/document/claude code/claude-code-104-slack-2026-04-29.md
tags:
  - slack
  - integration
  - claude-code
  - routing
  - channels
  - collaboration
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Claude Code Slack

## Key Points

- Claude Code in Slack routes @Claude mentions to Claude Code on the web when coding intent is detected, creating cloud sessions at claude.ai/code without leaving Slack ^[raw/document/claude code/claude-code-104-slack-2026-04-29.md]
- Two routing modes: Code only (all @mentions go to Claude Code) and Code + Chat (intelligent routing between Code and Chat based on message content); Code + Chat users can retry with the other mode via action buttons ^[raw/document/claude code/claude-code-104-slack-2026-04-29.md]
- Context is gathered from the full thread (when mentioned in a thread) or recent channel messages (when mentioned directly), helping Claude select the appropriate repository and approach ^[raw/document/claude code/claude-code-104-slack-2026-04-29.md]
- Access is channel-based: Claude must be explicitly invited to channels with `/invite @Claude`; it only responds to @mentions in channels where it has been added, not in DMs ^[raw/document/claude code/claude-code-104-slack-2026-04-29.md]
- Each user runs sessions under their own Claude account with their own plan limits; repository access is limited to repos the user has personally connected ^[raw/document/claude code/claude-code-104-slack-2026-04-29.md]
- Prerequisites: Pro, Max, Team, or Enterprise plan with Claude Code access; Claude Code on the web enabled; GitHub account connected with at least one authenticated repository; Slack account linked to Claude via the app ^[raw/document/claude code/claude-code-104-slack-2026-04-29.md]
- Current limitations: GitHub only (no GitLab/Bitbucket), one PR per session, individual rate limits apply, web access required (users without it only get standard Claude chat) ^[raw/document/claude code/claude-code-104-slack-2026-04-29.md]

## Notes

- The integration is built on the existing Claude for Slack app, adding intelligent routing to Claude Code on the web for coding-related requests
- Sessions created from Slack are accessible in Claude Code history on the web; for Enterprise and Team accounts, sessions are automatically visible to the organization
- When @Claude is invoked, Claude receives access to conversation context, so users should only use Claude in trusted Slack conversations

## Related

- [[entities/slack]]
- [[entities/claude_code]]
- [[entities/claude_code_web]]
- [[concepts/routing_mode]]
- [[concepts/sessions]]
- [[concepts/channels]]