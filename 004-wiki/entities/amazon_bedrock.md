---
title: "Amazon Bedrock"
summary: "AWS cloud service that provides Claude model access and serves as a cloud provider authentication option for Claude Code"
type: entity
sources:
  - raw/document/claude code/claude-code-034-authentication-2026-04-29.md
  - raw/document/claude code/claude-code-047-commands-2026-04-29.md
  - raw/document/claude code/claude-code-108-third-party-integrations-2026-04-29.md
  - raw/document/claude code/claude-code-120-whats-new-2026-w15-2026-04-29.md
  - raw/document/openrouter/openrouter-014-guides-overview-auth-byok-2026-04-29.md
  - raw/document/openrouter/openrouter-070-guides-best-practices-prompt-caching-2026-04-29.md
tags:
  - aws
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

# Amazon Bedrock

AWS cloud service that provides access to Claude models and serves as a cloud provider authentication option for Claude Code. When `CLAUDE_CODE_USE_BEDROCK` is set, Bedrock credentials take highest precedence in the authentication order. ^[raw/document/claude code/claude-code-034-authentication-2026-04-29.md]

## Key Facts

- Activated by setting the `CLAUDE_CODE_USE_BEDROCK` environment variable; when set, Bedrock credentials take highest authentication precedence ^[raw/document/claude code/claude-code-034-authentication-2026-04-29.md]
- Does not require browser login; authentication is handled entirely through environment variables and cloud credentials ^[raw/document/claude code/claude-code-034-authentication-2026-04-29.md]
- Administrators distribute environment variables and instructions for generating cloud credentials to users ^[raw/document/claude code/claude-code-034-authentication-2026-04-29.md]
- Bedrock Auth is one of the supported authentication types stored in Claude Code's credential management system ^[raw/document/claude code/claude-code-034-authentication-2026-04-29.md]
- `/setup-bedrock` provides an interactive wizard for configuring Bedrock authentication, region, and model pins; only visible when CLAUDE_CODE_USE_BEDROCK=1 is set ^[raw/document/claude code/claude-code-047-commands-2026-04-29.md]
- Best for AWS-native deployments; billed via AWS with PAYG pricing and cost tracking through AWS Cost Explorer ^[raw/document/claude code/claude-code-108-third-party-integrations-2026-04-29.md]
- Supports multiple AWS regions ^[raw/document/claude code/claude-code-108-third-party-integrations-2026-04-29.md]
- Enterprise features include IAM policies and CloudTrail ^[raw/document/claude code/claude-code-108-third-party-integrations-2026-04-29.md]
- Corporate proxy: set `CLAUDE_CODE_USE_BEDROCK=1`, `AWS_REGION`, and `HTTPS_PROXY` to route traffic through an organizational proxy ^[raw/document/claude code/claude-code-108-third-party-integrations-2026-04-29.md]
- LLM gateway: set `CLAUDE_CODE_USE_BEDROCK=1`, `ANTHROPIC_BEDROCK_BASE_URL` to the gateway URL, and `CLAUDE_CODE_SKIP_BEDROCK_AUTH=1` if the gateway handles AWS authentication ^[raw/document/claude code/claude-code-108-third-party-integrations-2026-04-29.md]
- A guided setup wizard on the login screen (pick "3rd-party platform") provides step-by-step Bedrock auth, region, credential, and model pinning (Week 15, v2.1.92-101) ^[raw/document/claude code/claude-code-120-whats-new-2026-w15-2026-04-29.md]
- `CLAUDE_CODE_USE_MANTLE=1` enables Amazon Bedrock powered by Mantle ^[raw/document/claude code/claude-code-120-whats-new-2026-w15-2026-04-29.md]
- Supported as a BYOK provider on OpenRouter with two credential options: Bedrock API keys (simpler, recommended, but tied to a specific AWS region) or AWS credentials in JSON format (accessKeyId, secretAccessKey, region) ^[raw/document/openrouter/openrouter-014-guides-overview-auth-byok-2026-04-29.md]
- Minimum required IAM permissions for OpenRouter BYOK: `bedrock:InvokeModel` and `bedrock:InvokeModelWithResponseStream` (for streaming responses) ^[raw/document/openrouter/openrouter-014-guides-overview-auth-byok-2026-04-29.md]
- OpenRouter recommends creating dedicated IAM users with limited permissions specifically for use with OpenRouter BYOK ^[raw/document/openrouter/openrouter-014-guides-overview-auth-byok-2026-04-29.md]
- Does not support Anthropic's top-level automatic caching (`cache_control` at the request level); when top-level `cache_control` is present, OpenRouter routes only to the Anthropic provider directly and excludes Bedrock endpoints ^[raw/document/openrouter/openrouter-070-guides-best-practices-prompt-caching-2026-04-29.md]
- Supports Anthropic explicit per-block `cache_control` breakpoints for prompt caching, including the 1-hour TTL option ^[raw/document/openrouter/openrouter-070-guides-best-practices-prompt-caching-2026-04-29.md]

## Related

- [[entities/claude_code]]
- [[entities/google_vertex_ai]]
- [[entities/microsoft_foundry]]
- [[concepts/authentication]]
- [[concepts/deployment_patterns]]
- [[concepts/commands]]
- [[concepts/llm_gateway]]
- [[concepts/proxy_pattern]]
- [[concepts/byok]]
- [[concepts/prompt_caching]]
- [[entities/openrouter]]
- [[entities/anthropic]]