---
title: "Proxy Pattern"
summary: "Security pattern where a proxy outside the agent's security boundary injects credentials into outgoing requests, preventing the agent from ever seeing sensitive credentials"
type: concept
sources:
  - raw/document/claude code/claude-code-018-agent-sdk-secure-deployment-2026-04-29.md
  - raw/document/claude code/claude-code-108-third-party-integrations-2026-04-29.md
tags:
  - security
  - credential-management
  - proxy
  - agent-sdk
  - deployment
  - enterprise
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Proxy Pattern

A security pattern for credential management where a proxy runs outside the agent's security boundary, injecting credentials into outgoing requests. The agent sends requests without credentials, the proxy adds them, and forwards the request to its destination. This ensures the agent never sees the actual credentials. ^[raw/document/claude code/claude-code-018-agent-sdk-secure-deployment-2026-04-29.md]

## Key Points

- The agent never sees actual credentials; they are stored only at the proxy ^[raw/document/claude code/claude-code-018-agent-sdk-secure-deployment-2026-04-29.md]
- The proxy can enforce an allowlist of permitted endpoints, log all requests for auditing, and centralize credential storage ^[raw/document/claude code/claude-code-018-agent-sdk-secure-deployment-2026-04-29.md]
- `ANTHROPIC_BASE_URL` routes sampling API requests to a proxy in plaintext, allowing inspection and credential injection ^[raw/document/claude code/claude-code-018-agent-sdk-secure-deployment-2026-04-29.md]
- `HTTP_PROXY`/`HTTPS_PROXY` routes all HTTP traffic but creates opaque TLS tunnels for HTTPS without TLS termination; the proxy cannot see or modify HTTPS request contents ^[raw/document/claude code/claude-code-018-agent-sdk-secure-deployment-2026-04-29.md]
- For HTTPS services beyond the Claude API, TLS-terminating proxies (e.g., mitmproxy) can decrypt, inspect, re-encrypt traffic but require CA certificate installation in the agent's trust store ^[raw/document/claude code/claude-code-018-agent-sdk-secure-deployment-2026-04-29.md]

## Details

Two proxy configuration methods are available for Claude Code and the Agent SDK. `ANTHROPIC_BASE_URL` is simple but limited to sampling API requests; the proxy receives plaintext HTTP and can inspect and modify requests including injecting credentials before forwarding to the real API. `HTTP_PROXY`/`HTTPS_PROXY` provides system-wide routing for all HTTP traffic, but for HTTPS the proxy can only create an encrypted CONNECT tunnel without seeing request contents. ^[raw/document/claude code/claude-code-018-agent-sdk-secure-deployment-2026-04-29.md]

For non-Claude-API HTTPS services (GitHub, npm registries, internal APIs), two approaches exist: custom tools (MCP servers or tool handlers running outside the boundary that make authenticated requests directly) and TLS-terminating proxies that decrypt, modify, and re-encrypt traffic. Custom tools avoid TLS interception entirely since the external service makes authenticated requests directly, but require per-service implementation. TLS-terminating proxies handle any HTTP service without custom code but add certificate management complexity. Not all programs respect `HTTP_PROXY`/`HTTPS_PROXY`; for comprehensive coverage, `proxychains` intercepts network calls or iptables redirects outbound traffic to a transparent proxy. ^[raw/document/claude code/claude-code-018-agent-sdk-secure-deployment-2026-04-29.md]

Proxy implementations include Envoy (with `credential_injector` filter), mitmproxy (TLS-terminating), Squid (caching with ACLs), and LiteLLM (LLM gateway with credential injection and rate limiting). ^[raw/document/claude code/claude-code-018-agent-sdk-secure-deployment-2026-04-29.md]

### Corporate Proxy for Enterprise Deployment

Organizations requiring all outbound traffic to pass through a proxy server for security monitoring, compliance, or network policy enforcement can configure a corporate proxy via `HTTPS_PROXY` or `HTTP_PROXY` environment variables. This is distinct from an LLM gateway, which handles authentication and routing for the Claude API specifically. Both configurations can be used together. ^[raw/document/claude code/claude-code-108-third-party-integrations-2026-04-29.md]

Provider-specific corporate proxy configuration:
- **Bedrock**: `CLAUDE_CODE_USE_BEDROCK=1`, `AWS_REGION`, `HTTPS_PROXY` ^[raw/document/claude code/claude-code-108-third-party-integrations-2026-04-29.md]
- **Foundry**: `CLAUDE_CODE_USE_FOUNDRY=1`, `ANTHROPIC_FOUNDRY_RESOURCE`, `ANTHROPIC_FOUNDRY_API_KEY`, `HTTPS_PROXY` ^[raw/document/claude code/claude-code-108-third-party-integrations-2026-04-29.md]
- **Vertex AI**: `CLAUDE_CODE_USE_VERTEX=1`, `CLOUD_ML_REGION`, `ANTHROPIC_VERTEX_PROJECT_ID`, `HTTPS_PROXY` ^[raw/document/claude code/claude-code-108-third-party-integrations-2026-04-29.md]

## Related

- [[entities/agent_sdk]]
- [[concepts/sandbox_hosting]]
- [[concepts/secure_deployment]]
- [[concepts/deployment_patterns]]
- [[concepts/permissions]]
- [[concepts/llm_gateway]]