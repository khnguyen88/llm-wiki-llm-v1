---
title: "Claude Code Third Party Integrations"
summary: "Enterprise deployment overview comparing Claude for Teams/Enterprise, Anthropic Console, Amazon Bedrock, Google Vertex AI, and Microsoft Foundry, with proxy and LLM gateway configuration"
type: summary
sources:
  - raw/document/claude code/claude-code-108-third-party-integrations-2026-04-29.md
tags:
  - enterprise
  - deployment
  - cloud-provider
  - proxy
  - llm-gateway
  - bedrock
  - vertex
  - foundry
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Claude Code Third Party Integrations

## Key Points

- Claude for Teams and Enterprise provide the recommended deployment path, including both Claude Code and Claude on the web with a single subscription and centralized billing ^[raw/document/claude code/claude-code-108-third-party-integrations-2026-04-29.md]
- Five deployment options exist: Claude for Teams/Enterprise (recommended), Anthropic Console (individual developers), Amazon Bedrock (AWS-native), Google Vertex AI (GCP-native), and Microsoft Foundry (Azure-native) ^[raw/document/claude code/claude-code-108-third-party-integrations-2026-04-29.md]
- Two network configurations can be used together: corporate proxy (routes all outbound traffic through `HTTPS_PROXY`/`HTTP_PROXY` for security monitoring) and LLM gateway (sits between Claude Code and the cloud provider for centralized auth, routing, and usage tracking via `ANTHROPIC_*_BASE_URL` environment variables) ^[raw/document/claude code/claude-code-108-third-party-integrations-2026-04-29.md]
- Each cloud provider uses a skip-auth flag (`CLAUDE_CODE_SKIP_BEDROCK_AUTH`, `CLAUDE_CODE_SKIP_FOUNDRY_AUTH`, `CLAUDE_CODE_SKIP_VERTEX_AUTH`) when an LLM gateway handles authentication instead ^[raw/document/claude code/claude-code-108-third-party-integrations-2026-04-29.md]
- Cloud providers should pin specific model versions using `ANTHROPIC_DEFAULT_OPUS_MODEL`, `ANTHROPIC_DEFAULT_SONNET_MODEL`, and `ANTHROPIC_DEFAULT_HAIKU_MODEL` to control when users move to new model releases ^[raw/document/claude code/claude-code-108-third-party-integrations-2026-04-29.md]
- `/status` verifies that proxy and gateway configurations are applied correctly ^[raw/document/claude code/claude-code-108-third-party-integrations-2026-04-29.md]
- Organizations should invest in CLAUDE.md documentation at both organization-wide (system directories) and repository levels, simplify deployment with one-click installs, start with guided usage (codebase Q&A, small bug fixes), and leverage MCP for integrations ^[raw/document/claude code/claude-code-108-third-party-integrations-2026-04-29.md]

## Quotes

- "Organizations can deploy Claude Code through Anthropic directly or through a cloud provider." ^[raw/document/claude code/claude-code-108-third-party-integrations-2026-04-29.md]
- "Without pinning, model aliases resolve to the latest version, which may not yet be enabled in your account when Anthropic releases an update." ^[raw/document/claude code/claude-code-108-third-party-integrations-2026-04-29.md]

## Notes

- Only Claude for Teams/Enterprise includes Claude on the web; all other deployment options provide only Claude Code access ^[raw/document/claude code/claude-code-108-third-party-integrations-2026-04-29.md]
- Prompt caching is enabled by default across all deployment options ^[raw/document/claude code/claude-code-108-third-party-integrations-2026-04-29.md]

## Related

- [[entities/amazon_bedrock]]
- [[entities/google_vertex_ai]]
- [[entities/microsoft_foundry]]
- [[entities/claude_code]]
- [[concepts/deployment_patterns]]
- [[concepts/proxy_pattern]]
- [[concepts/llm_gateway]]
- [[concepts/managed_settings]]
- [[concepts/model_naming]]
- [[concepts/mcp]]