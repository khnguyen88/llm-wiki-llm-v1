---
title: "Amazon Bedrock"
summary: "AWS cloud service that provides Claude model access and serves as a cloud provider authentication option for Claude Code"
type: entity
sources:
  - raw/document/claude code/claude-code-034-authentication-2026-04-29.md
  - raw/document/claude code/claude-code-047-commands-2026-04-29.md
tags:
  - aws
  - cloud-provider
  - enterprise
  - authentication
  - commands
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Amazon Bedrock

AWS cloud service that provides access to Claude models and serves as a cloud provider authentication option for Claude Code. When `CLAUDE_CODE_USE_BEDROCK` is set, Bedrock credentials take highest precedence in the authentication order. ^[raw/document/claude code/claude-code-034-authentication-2026-04-29.md]

## Key Facts

- Activated by setting the `CLAUDE_CODE_USE_BEDROCK` environment variable; when set, Bedrock credentials take highest authentication precedence ^[raw/document/claude code/claude-code-034-authentication-2026-04-29.md]
- Does not require browser login; authentication is handled entirely through environment variables and cloud credentials ^[raw/document/claude code/claude-code-034-authentication-2026-04-29.md]
- Administrators distribute environment variables and instructions for generating cloud credentials to users ^[raw/document/claude code/claude-code-034-authentication-2026-04-29.md]
- Bedrock Auth is one of the supported authentication types stored in Claude Code's credential management system ^[raw/document/claude code/claude-code-034-authentication-2026-04-29.md]
- `/setup-bedrock` provides an interactive wizard for configuring Bedrock authentication, region, and model pins; only visible when CLAUDE_CODE_USE_BEDROCK=1 is set ^[raw/document/claude code/claude-code-047-commands-2026-04-29.md]

## Related

- [[entities/claude_code]]
- [[entities/google_vertex_ai]]
- [[entities/microsoft_foundry]]
- [[concepts/authentication]]
- [[concepts/deployment_patterns]]
- [[concepts/commands]]