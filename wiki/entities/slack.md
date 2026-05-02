---
title: "Slack"
summary: "Messaging platform integrated with Claude Code, enabling coding task delegation via @Claude mentions that create cloud sessions on claude.ai/code"
type: entity
sources:
  - raw/document/claude code/claude-code-104-slack-2026-04-29.md
tags:
  - slack
  - integration
  - messaging
  - collaboration
  - claude-code
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Slack

Slack is a messaging platform that integrates with Claude Code through the Claude for Slack app, enabling users to delegate coding tasks via @Claude mentions directly from team conversations.

## Key Facts

- The Claude app is installed from the Slack App Marketplace by a workspace administrator ^[raw/document/claude code/claude-code-104-slack-2026-04-29.md]
- Individual users authenticate by opening the Claude app in Slack, navigating to App Home, and clicking "Connect" to link their Slack account with their Claude account ^[raw/document/claude code/claude-code-104-slack-2026-04-29.md]
- Claude Code in Slack only works in channels (public or private), not in direct messages (DMs) ^[raw/document/claude code/claude-code-104-slack-2026-04-29.md]
- Users must explicitly invite Claude to channels with `/invite @Claude`; it is not added to any channels automatically after installation ^[raw/document/claude code/claude-code-104-slack-2026-04-29.md]
- Routing modes are configured in the Claude App Home: Code only routes all @mentions to coding sessions, Code + Chat intelligently routes between Claude Code and Claude Chat ^[raw/document/claude code/claude-code-104-slack-2026-04-29.md]
- Each user's sessions run under their own Claude account with their own plan limits; repository access is limited to repos the user has personally connected ^[raw/document/claude code/claude-code-104-slack-2026-04-29.md]
- Workspace administrators control app installation and can remove the app to immediately revoke access for all users ^[raw/document/claude code/claude-code-104-slack-2026-04-29.md]
- Enterprise Grid organizations can control which workspaces have access to the Claude app ^[raw/document/claude code/claude-code-104-slack-2026-04-29.md]

## Details

### Access and Permissions

Access is controlled at three levels:

- **User-level**: Each user authenticates their own Claude account and works within their own plan limits and connected repositories.
- **Workspace-level**: Workspace administrators decide whether to install the app. Removing the app immediately revokes access for all users.
- **Channel-level**: Claude must be explicitly invited to channels. This allows admins to restrict usage to specific channels, providing an additional layer of access control beyond workspace permissions.

### User Interface

When Claude completes a task in Slack, it @mentions the user with a summary and action buttons:

- **View Session**: Opens the full Claude Code session transcript on claude.ai/code
- **Create PR**: Creates a pull request from the session's changes
- **Retry as Code**: Re-routes a chat response as a coding session
- **Change Repo**: Selects a different repository if Claude chose incorrectly

### Context and Security

When @Claude is invoked in a thread, it gathers context from all messages in that thread. When mentioned directly in a channel, it uses recent channel messages. Claude may follow directions from other messages in the context, so users should only use Claude in trusted conversations.

## Related

- [[entities/claude_code]]
- [[entities/claude_code_web]]
- [[entities/github]]
- [[concepts/routing_mode]]
- [[concepts/sessions]]
- [[concepts/channels]]
- [[summaries/claude-code-slack]]