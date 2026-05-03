---
title: "Google Vertex AI"
summary: "Google Cloud service that provides Claude model access and serves as a cloud provider authentication option for Claude Code"
type: entity
sources:
  - raw/document/claude code/claude-code-034-authentication-2026-04-29.md
  - raw/document/claude code/claude-code-047-commands-2026-04-29.md
  - raw/document/claude code/claude-code-108-third-party-integrations-2026-04-29.md
  - raw/document/claude code/claude-code-120-whats-new-2026-w15-2026-04-29.md
  - raw/document/openrouter/openrouter-009-guides-overview-multimodal-videos-2026-04-29.md
  - raw/document/openrouter/openrouter-014-guides-overview-auth-byok-2026-04-29.md
  - raw/document/openrouter/openrouter-070-guides-best-practices-prompt-caching-2026-04-29.md
tags:
  - google-cloud
  - cloud-provider
  - enterprise
  - authentication
  - commands
  - deployment
  - prompt-caching
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: merged
---

# Google Vertex AI

Google Cloud service that provides access to Claude models and serves as a cloud provider authentication option for Claude Code. When `CLAUDE_CODE_USE_VERTEX` is set, Vertex AI credentials take highest precedence in the authentication order. ^[raw/document/claude code/claude-code-034-authentication-2026-04-29.md]

## Key Facts

- Activated by setting the `CLAUDE_CODE_USE_VERTEX` environment variable; when set, Vertex AI credentials take highest authentication precedence ^[raw/document/claude code/claude-code-034-authentication-2026-04-29.md]
- Does not require browser login; authentication is handled entirely through environment variables and cloud credentials ^[raw/document/claude code/claude-code-034-authentication-2026-04-29.md]
- Administrators distribute environment variables and instructions for generating cloud credentials to users ^[raw/document/claude code/claude-code-034-authentication-2026-04-29.md]
- Vertex Auth is one of the supported authentication types stored in Claude Code's credential management system ^[raw/document/claude code/claude-code-034-authentication-2026-04-29.md]
- `/setup-vertex` provides an interactive wizard for configuring Vertex AI authentication, project, region, and model pins; only visible when CLAUDE_CODE_USE_VERTEX=1 is set ^[raw/document/claude code/claude-code-047-commands-2026-04-29.md]
- Best for GCP-native deployments; billed via GCP with PAYG pricing and cost tracking through GCP Billing ^[raw/document/claude code/claude-code-108-third-party-integrations-2026-04-29.md]
- Supports multiple GCP regions ^[raw/document/claude code/claude-code-108-third-party-integrations-2026-04-29.md]
- Enterprise features include IAM roles and Cloud Audit Logs ^[raw/document/claude code/claude-code-108-third-party-integrations-2026-04-29.md]
- Corporate proxy: set `CLAUDE_CODE_USE_VERTEX=1`, `CLOUD_ML_REGION`, `ANTHROPIC_VERTEX_PROJECT_ID`, and `HTTPS_PROXY` to route traffic through an organizational proxy ^[raw/document/claude code/claude-code-108-third-party-integrations-2026-04-29.md]
- LLM gateway: set `CLAUDE_CODE_USE_VERTEX=1`, `ANTHROPIC_VERTEX_BASE_URL` to the gateway URL, and `CLAUDE_CODE_SKIP_VERTEX_AUTH=1` if the gateway handles GCP authentication ^[raw/document/claude code/claude-code-108-third-party-integrations-2026-04-29.md]
- A guided setup wizard on the login screen (pick "3rd-party platform") provides step-by-step Vertex AI auth, project, region, and model pinning (Week 15, v2.1.92-101) ^[raw/document/claude code/claude-code-120-whats-new-2026-w15-2026-04-29.md]
- When used with OpenRouter for video input, Google Gemini on Vertex AI does not support video URLs — base64-encoded data URLs must be used instead ^[raw/document/openrouter/openrouter-009-guides-overview-multimodal-videos-2026-04-29.md]
- Supported as a BYOK provider on OpenRouter using Google Cloud service account keys in JSON format, which must include all standard service account fields plus an optional `region` field for specifying deployment region ^[raw/document/openrouter/openrouter-014-guides-overview-auth-byok-2026-04-29.md]
- OpenRouter BYOK for Vertex AI requires the service account to have `aiplatform.endpoints.predict` permissions ^[raw/document/openrouter/openrouter-014-guides-overview-auth-byok-2026-04-29.md]
- The `region` field in the service account key for OpenRouter BYOK supports `"global"` (any available region) or specific regions like `"us-central1"` or `"europe-west1"` ^[raw/document/openrouter/openrouter-014-guides-overview-auth-byok-2026-04-29.md]
- Does not support Anthropic's top-level automatic caching (`cache_control` at the request level); when top-level `cache_control` is present, OpenRouter routes only to the Anthropic provider directly and excludes Vertex AI endpoints ^[raw/document/openrouter/openrouter-070-guides-best-practices-prompt-caching-2026-04-29.md]
- Supports Anthropic explicit per-block `cache_control` breakpoints for prompt caching, including the 1-hour TTL option ^[raw/document/openrouter/openrouter-070-guides-best-practices-prompt-caching-2026-04-29.md]

## Related

- [[entities/claude_code]]
- [[entities/amazon_bedrock]]
- [[entities/microsoft_foundry]]
- [[concepts/authentication]]
- [[concepts/deployment_patterns]]
- [[concepts/commands]]
- [[concepts/llm_gateway]]
- [[concepts/proxy_pattern]]
- [[concepts/video_input]]
- [[concepts/byok]]
- [[concepts/prompt_caching]]
- [[entities/openrouter]]
- [[entities/anthropic]]
- [[entities/google_gemini]]