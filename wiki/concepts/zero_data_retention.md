---
title: "Zero Data Retention"
summary: "An Anthropic policy for Claude for Enterprise that ensures prompts and model responses are not stored after delivery, with specific scope exclusions and disabled features"
type: concept
sources:
  - raw/document/claude code/claude-code-124-zero-data-retention-2026-04-29.md
  - raw/document/openrouter/openrouter-010-guides-overview-multimodal-video-generation-2026-04-29.md
  - raw/document/openrouter/openrouter-018-guides-routing-provider-selection-2026-04-29.md
  - raw/document/openrouter/openrouter-031-guides-features-response-caching-2026-04-29.md
  - raw/document/openrouter/openrouter-044-guides-features-zdr-2026-04-29.md
  - raw/document/openrouter/openrouter-046-guides-features-guardrails-2026-04-29.md
  - raw/document/openrouter/openrouter-068-guides-privacy-provider-logging-2026-04-29.md
tags:
  - claude-code
  - enterprise
  - data-retention
  - privacy
  - compliance
  - provider-routing
  - zdr
  - guardrails "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Zero Data Retention

Zero Data Retention (ZDR) is a data handling policy for Claude Code on Claude for Enterprise where prompts and model responses are processed in real time and not stored by Anthropic after the response is returned, except where needed to comply with law or combat misuse. ^[raw/document/claude code/claude-code-124-zero-data-retention-2026-04-29.md]

## Key Points

- ZDR is enabled on a per-organization basis by the Anthropic account team; each new organization under the same account requires separate enablement ^[raw/document/claude code/claude-code-124-zero-data-retention-2026-04-29.md]
- ZDR covers model inference calls made through Claude Code on Claude for Enterprise, regardless of the Claude model used ^[raw/document/claude code/claude-code-124-zero-data-retention-2026-04-29.md]
- ZDR applies only to Anthropic's direct platform; deployments on AWS Bedrock, Google Vertex AI, or Microsoft Foundry follow those platforms' data retention policies ^[raw/document/claude code/claude-code-124-zero-data-retention-2026-04-29.md]
- Even with ZDR enabled, Anthropic may retain data for up to 2 years when a session is flagged for a policy violation ^[raw/document/claude code/claude-code-124-zero-data-retention-2026-04-29.md]
- ZDR is distinct from "no training" policy — some providers do not train on user data but still retain it (e.g., for abuse scanning or legal reasons); OpenRouter gives controls over both policies ^[raw/document/openrouter/openrouter-044-guides-features-zdr-2026-04-29.md]
- OpenRouter tracks per-endpoint data policies, which may differ from a provider's general policy; in some cases OpenRouter creates special agreements with providers for more privacy-focused policies than their defaults ^[raw/document/openrouter/openrouter-044-guides-features-zdr-2026-04-29.md]
- If a provider or endpoint policy cannot be confirmed, OpenRouter takes a conservative stance and assumes the endpoint both retains and trains on data ^[raw/document/openrouter/openrouter-044-guides-features-zdr-2026-04-29.md]
- In-memory caching of prompts (kept temporarily in a provider's datacenter for repeated prompt processing) is not considered data retention under ZDR; endpoints with implicit caching are allowed under ZDR routing ^[raw/document/openrouter/openrouter-044-guides-features-zdr-2026-04-29.md]
- OpenRouter itself has a ZDR policy: prompts are not retained unless the user opts in to prompt logging ^[raw/document/openrouter/openrouter-044-guides-features-zdr-2026-04-29.md]
- A programmatic list of ZDR endpoints is available at `https://openrouter.ai/api/v1/endpoints/zdr`, automatically updated when provider data policies change ^[raw/document/openrouter/openrouter-044-guides-features-zdr-2026-04-29.md]
- OpenRouter does not enforce routing based on provider data retention policies; provider retention policies are surfaced for user information but users must manually filter non-compliant providers ^[raw/document/openrouter/openrouter-068-guides-privacy-provider-logging-2026-04-29.md]

## Details

ZDR on Claude for Enterprise also provides administrative capabilities alongside zero data retention: cost controls per user, an analytics dashboard, server-managed settings, and audit logs. ^[raw/document/claude code/claude-code-124-zero-data-retention-2026-04-29.md]

### What ZDR does not cover

The following are not covered by ZDR even for enabled organizations and follow standard data retention policies:

| Feature | Details |
|---------|---------|
| Chat on claude.ai | Conversations through the Claude for Enterprise web interface |
| Cowork | Cowork sessions |
| Claude Code Analytics | Stores productivity metadata (account emails, usage statistics) but not prompts or responses; contribution metrics are not available for ZDR organizations |
| User and seat management | Administrative data such as account emails and seat assignments |
| Third-party integrations | Data processed by MCP servers or other external integrations |

^[raw/document/claude code/claude-code-124-zero-data-retention-2026-04-29.md]

### OpenRouter ZDR enforcement

On OpenRouter, ZDR can be enforced on a per-request basis using the `zdr` parameter in the `provider` object. When set to `true`, requests are only routed to endpoints with a Zero Data Retention policy. When `false` or not provided, ZDR has no effect on routing. The per-request `zdr` parameter operates as an OR with the account-wide ZDR setting — if either is enabled, ZDR enforcement applies. The request-level parameter can only ensure ZDR is enabled, not override account-wide enforcement. ^[raw/document/openrouter/openrouter-018-guides-routing-provider-selection-2026-04-29.md]

An account-wide ZDR setting is available at `/settings/privacy`; when enabled, requests are only routed to endpoints that have a ZDR policy. ^[raw/document/openrouter/openrouter-044-guides-features-zdr-2026-04-29.md]

### OpenRouter video generation

On OpenRouter, video generation is not eligible for ZDR. Because the generation is asynchronous, the provider must temporarily retain the output so it can be retrieved after the job completes. If ZDR enforcement is enabled (via account settings or the per-request `zdr` parameter), video generation requests will not be routed. ^[raw/document/openrouter/openrouter-010-guides-overview-multimodal-video-generation-2026-04-29.md]

### OpenRouter response caching

On OpenRouter, response caching is disabled when account-level ZDR is enforced, since caching requires temporarily storing response data. Per-request `provider.zdr` does not affect cache eligibility — only account-level ZDR enforcement disables caching. ^[raw/document/openrouter/openrouter-031-guides-features-response-caching-2026-04-29.md]

### OpenRouter guardrails ZDR enforcement

Within OpenRouter guardrails, ZDR is one of the enforceable settings alongside budget limits, model allowlists, and provider allowlists. When multiple guardrails apply, ZDR uses OR logic: if any guardrail enforces ZDR, it is enforced for the request. This means a member-level guardrail requiring ZDR will enforce ZDR even if an API key's guardrail does not. ^[raw/document/openrouter/openrouter-046-guides-features-guardrails-2026-04-29.md]

### Features disabled under ZDR

Features that require storing prompts or completions are automatically disabled at the backend level:

| Feature | Reason |
|---------|--------|
| Claude Code on the Web | Requires server-side storage of conversation history |
| Remote sessions from the Desktop app | Requires persistent session data including prompts and completions |
| Feedback submission (`/feedback`) | Sends conversation data to Anthropic |

^[raw/document/claude code/claude-code-124-zero-data-retention-2026-04-29.md]

## Related

- [[entities/claude_code]]
- [[entities/claude_code_web]]
- [[concepts/analytics]]
- [[concepts/server_managed_settings]]
- [[entities/amazon_bedrock]]
- [[entities/google_vertex_ai]]
- [[entities/microsoft_foundry]]
- [[summaries/claude-code-zero-data-retention]]
- [[concepts/video_generation]]
- [[entities/openrouter]]
- [[concepts/data_collection_policy]]
- [[concepts/provider_routing]]
- [[concepts/response_caching]]
- [[summaries/openrouter-guides-features-zdr]]
- [[concepts/guardrails]]
- [[concepts/provider_logging]]
- [[summaries/openrouter-guides-privacy-provider-logging]]