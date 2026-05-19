---
title: "LLM Gateway"
summary: "An intermediary service between Claude Code and a cloud provider that handles authentication, routing, and centralized usage tracking"
type: concept
sources:
  - raw/document/claude code/claude-code-108-third-party-integrations-2026-04-29.md
  - raw/document/openrouter/openrouter-001-quickstart-2026-04-29.md
tags:
  - enterprise
  - deployment
  - proxy
  - cloud-provider
  - authentication
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# LLM Gateway

A service that sits between Claude Code and the cloud provider to handle authentication and routing. Distinct from a corporate proxy, which only routes outbound traffic for security monitoring. ^[raw/document/claude code/claude-code-108-third-party-integrations-2026-04-29.md]

## Key Points

- Routes Claude Code API requests through an intermediary service instead of directly to the cloud provider ^[raw/document/claude code/claude-code-108-third-party-integrations-2026-04-29.md]
- Use cases include centralized usage tracking across teams, custom rate limiting or budgets, and centralized authentication management ^[raw/document/claude code/claude-code-108-third-party-integrations-2026-04-29.md]
- Configured via provider-specific base URL environment variables: `ANTHROPIC_BEDROCK_BASE_URL`, `ANTHROPIC_VERTEX_BASE_URL`, or `ANTHROPIC_FOUNDRY_BASE_URL` ^[raw/document/claude code/claude-code-108-third-party-integrations-2026-04-29.md]
- When the gateway handles cloud provider authentication, set the corresponding skip-auth flag (`CLAUDE_CODE_SKIP_BEDROCK_AUTH`, `CLAUDE_CODE_SKIP_VERTEX_AUTH`, `CLAUDE_CODE_SKIP_FOUNDRY_AUTH`) ^[raw/document/claude code/claude-code-108-third-party-integrations-2026-04-29.md]
- Can be used together with a corporate proxy (they serve different purposes and are not mutually exclusive) ^[raw/document/claude code/claude-code-108-third-party-integrations-2026-04-29.md]

## Details

An LLM gateway differs from a corporate proxy in purpose and configuration. A corporate proxy routes all outbound HTTP traffic through a server for security monitoring, compliance, or network policy enforcement, configured via `HTTPS_PROXY` or `HTTP_PROXY`. An LLM gateway specifically handles the API communication between Claude Code and the model provider, managing authentication, rate limiting, and usage tracking. Both can be configured simultaneously. ^[raw/document/claude code/claude-code-108-third-party-integrations-2026-04-29.md]

Each cloud provider has its own base URL environment variable for gateway routing. When the gateway handles authentication for the underlying cloud provider, the skip-auth flag tells Claude Code not to attempt direct cloud provider authentication, letting the gateway manage that responsibility instead. ^[raw/document/claude code/claude-code-108-third-party-integrations-2026-04-29.md]

## Related

- [[entities/amazon_bedrock]]
- [[entities/google_vertex_ai]]
- [[entities/microsoft_foundry]]
- [[concepts/proxy_pattern]]
- [[concepts/deployment_patterns]]
- [[concepts/authentication]]
- [[entities/openrouter]]