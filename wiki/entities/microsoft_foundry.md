---
title: "Microsoft Foundry"
summary: "Microsoft Azure service that provides Claude model access and serves as a cloud provider authentication option for Claude Code"
type: entity
sources:
  - raw/document/claude code/claude-code-034-authentication-2026-04-29.md
  - raw/document/claude code/claude-code-108-third-party-integrations-2026-04-29.md
tags:
  - azure
  - cloud-provider
  - enterprise
  - authentication
  - deployment
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Microsoft Foundry

Microsoft Azure service that provides access to Claude models and serves as a cloud provider authentication option for Claude Code. When `CLAUDE_CODE_USE_FOUNDRY` is set, Foundry credentials take highest precedence in the authentication order. ^[raw/document/claude code/claude-code-034-authentication-2026-04-29.md]

## Key Facts

- Activated by setting the `CLAUDE_CODE_USE_FOUNDRY` environment variable; when set, Foundry credentials take highest authentication precedence ^[raw/document/claude code/claude-code-034-authentication-2026-04-29.md]
- Does not require browser login; authentication is handled entirely through environment variables and cloud credentials ^[raw/document/claude code/claude-code-034-authentication-2026-04-29.md]
- Administrators distribute environment variables and instructions for generating cloud credentials to users ^[raw/document/claude code/claude-code-034-authentication-2026-04-29.md]
- Azure Auth is one of the supported authentication types stored in Claude Code's credential management system ^[raw/document/claude code/claude-code-034-authentication-2026-04-29.md]
- Best for Azure-native deployments; billed via Azure with PAYG pricing and cost tracking through Azure Cost Management ^[raw/document/claude code/claude-code-108-third-party-integrations-2026-04-29.md]
- Supports multiple Azure regions ^[raw/document/claude code/claude-code-108-third-party-integrations-2026-04-29.md]
- Enterprise features include RBAC policies and Azure Monitor ^[raw/document/claude code/claude-code-108-third-party-integrations-2026-04-29.md]
- Authentication via API key or Microsoft Entra ID ^[raw/document/claude code/claude-code-108-third-party-integrations-2026-04-29.md]
- Corporate proxy: set `CLAUDE_CODE_USE_FOUNDRY=1`, `ANTHROPIC_FOUNDRY_RESOURCE`, `ANTHROPIC_FOUNDRY_API_KEY` (or omit for Entra ID auth), and `HTTPS_PROXY` to route traffic through an organizational proxy ^[raw/document/claude code/claude-code-108-third-party-integrations-2026-04-29.md]
- LLM gateway: set `CLAUDE_CODE_USE_FOUNDRY=1`, `ANTHROPIC_FOUNDRY_BASE_URL` to the gateway URL, and `CLAUDE_CODE_SKIP_FOUNDRY_AUTH=1` if the gateway handles Azure authentication ^[raw/document/claude code/claude-code-108-third-party-integrations-2026-04-29.md]

## Related

- [[entities/claude_code]]
- [[entities/amazon_bedrock]]
- [[entities/google_vertex_ai]]
- [[concepts/authentication]]
- [[concepts/deployment_patterns]]
- [[concepts/llm_gateway]]
- [[concepts/proxy_pattern]]