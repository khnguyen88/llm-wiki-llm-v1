---
title: "Prompt Caching"
summary: "A mechanism in the Agent SDK that caches repeated prompt content to reduce input costs, with configurable TTL and separate token counters for cache creation and reads"
type: concept
sources:
  - raw/document/claude code/claude-code-004-agent-sdk-cost-tracking-2026-04-29.md
  - raw/document/claude code/claude-code-011-agent-sdk-modifying-system-prompts-2026-04-29.md
tags:
  - prompt-caching
  - agent-sdk
  - cost-optimization
  - token-usage
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Prompt Caching

A mechanism in the Agent SDK that automatically caches repeated prompt content to reduce input costs. The SDK enables prompt caching by default; no manual configuration is required. The usage object reports cache tokens separately from standard input tokens so callers can measure caching savings. ^[raw/document/claude code/claude-code-004-agent-sdk-cost-tracking-2026-04-29.md]

## Key Points

- The Agent SDK automatically uses prompt caching to reduce costs on repeated content; no configuration is needed ^[raw/document/claude code/claude-code-004-agent-sdk-cost-tracking-2026-04-29.md]
- `cache_creation_input_tokens` tracks tokens used to create new cache entries, charged at a higher rate than standard input tokens ^[raw/document/claude code/claude-code-004-agent-sdk-cost-tracking-2026-04-29.md]
- `cache_read_input_tokens` tracks tokens read from existing cache entries, charged at a reduced rate ^[raw/document/claude code/claude-code-004-agent-sdk-cost-tracking-2026-04-29.md]
- Default cache TTL is 5 minutes when authenticating with an API key or running on Amazon Bedrock, Google Cloud Vertex AI, or Microsoft Foundry ^[raw/document/claude code/claude-code-004-agent-sdk-cost-tracking-2026-04-29.md]
- Setting the `ENABLE_PROMPT_CACHING_1H` environment variable extends cache TTL to 1 hour, trading higher write cost for more cache reads ^[raw/document/claude code/claude-code-004-agent-sdk-cost-tracking-2026-04-29.md]
- Claude subscription users receive 1-hour TTL automatically and do not need to set `ENABLE_PROMPT_CACHING_1H` ^[raw/document/claude code/claude-code-004-agent-sdk-cost-tracking-2026-04-29.md]
- `excludeDynamicSections: true` on the `claude_code` preset moves per-session context (working directory, git status, date, auto-memory paths) from the system prompt into the first user message, enabling identical preset-plus-append configurations to share a cache entry across different directories and machines ^[raw/document/claude code/claude-code-011-agent-sdk-modifying-system-prompts-2026-04-29.md]
- Without `excludeDynamicSections`, two sessions with the same preset and append text still cannot share a cache entry if they run from different working directories, because the preset embeds per-session context ahead of the append text ^[raw/document/claude code/claude-code-011-agent-sdk-modifying-system-prompts-2026-04-29.md]

## Details

Prompt caching in the Agent SDK follows a write-once, read-many model. When the SDK first encounters a portion of the prompt, it creates a cache entry (`cache_creation_input_tokens`), which is billed at a higher rate than standard input tokens. Subsequent requests that include the same content can read from the cache (`cache_read_input_tokens`) at a reduced rate. The default TTL for cache entries is 5 minutes when using API key authentication or running on cloud providers (Bedrock, Vertex AI, Foundry). This means that if more than 5 minutes pass between requests with the same system prompt and context, the cache expires and the next request pays the full creation price again. ^[raw/document/claude code/claude-code-004-agent-sdk-cost-tracking-2026-04-29.md]

For workloads that run many short sessions against the same system prompt with gaps longer than 5 minutes between them, the `ENABLE_PROMPT_CACHING_1H` environment variable extends the cache TTL to 1 hour. This can be set in the shell environment or passed through `options.env` in the SDK. Cache writes with a 1-hour TTL are billed at a higher rate than 5-minute writes, so enabling this trades higher upfront cost for more cache hits on subsequent requests. Claude subscription users receive the 1-hour TTL automatically without needing to set this variable. ^[raw/document/claude code/claude-code-004-agent-sdk-cost-tracking-2026-04-29.md]

Cross-session cache reuse is also blocked by per-session context embedded in the system prompt. When using the `claude_code` preset, the working directory, platform, OS version, date, git status, and auto-memory paths are embedded ahead of any `append` text. Any difference in this context produces a different system prompt and a cache miss. The `excludeDynamicSections: true` option moves this dynamic content into the first user message instead, leaving only the static preset and `append` text in the system prompt. This enables fleets of agents running from different directories to reuse the same cached system prompt. The tradeoff is that instructions in the user message carry marginally less weight than the same text in the system prompt. `excludeDynamicSections` requires SDK v0.2.98+ (TypeScript) or v0.1.58+ (Python) and applies only to the preset object form. ^[raw/document/claude code/claude-code-011-agent-sdk-modifying-system-prompts-2026-04-29.md]

## Related

- [[entities/agent_sdk]]
- [[concepts/cost_tracking]]
- [[concepts/system_prompt]]