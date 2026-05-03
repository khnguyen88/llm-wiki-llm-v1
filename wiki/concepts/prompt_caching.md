---
title: "Prompt Caching"
summary: "A mechanism that caches repeated prompt content to reduce input costs, with provider-specific implementations including automatic caching, explicit cache breakpoints, and provider sticky routing on OpenRouter"
type: concept
sources:
  - raw/document/claude code/claude-code-004-agent-sdk-cost-tracking-2026-04-29.md
  - raw/document/claude code/claude-code-011-agent-sdk-modifying-system-prompts-2026-04-29.md
  - raw/document/claude code/claude-code-121-whats-new-2026-w16-2026-04-29.md
  - raw/document/openrouter/openrouter-031-guides-features-response-caching-2026-04-29.md
  - raw/document/openrouter/openrouter-044-guides-features-zdr-2026-04-29.md
  - raw/document/openrouter/openrouter-070-guides-best-practices-prompt-caching-2026-04-29.md
tags:
  - prompt-caching
  - agent-sdk
  - cost-optimization
  - token-usage
  - provider-sticky-routing
  - openrouter
created: "2026-05-01T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: merged
---

# Prompt Caching

A mechanism that caches repeated prompt content to reduce input costs. In the Agent SDK, prompt caching is enabled by default with no configuration required. On OpenRouter, prompt caching varies by provider: some enable it automatically (OpenAI, DeepSeek, Grok, Moonshot AI, Groq), while others require explicit configuration (Anthropic, Google Gemini). OpenRouter uses [[concepts/provider_sticky_routing|provider sticky routing]] to maximize cache hit rates. ^[raw/document/claude code/claude-code-004-agent-sdk-cost-tracking-2026-04-29.md] ^[raw/document/openrouter/openrouter-070-guides-best-practices-prompt-caching-2026-04-29.md]

## Key Points

- The Agent SDK automatically uses prompt caching to reduce costs on repeated content; no configuration is needed ^[raw/document/claude code/claude-code-004-agent-sdk-cost-tracking-2026-04-29.md]
- `cache_creation_input_tokens` tracks tokens used to create new cache entries, charged at a higher rate than standard input tokens ^[raw/document/claude code/claude-code-004-agent-sdk-cost-tracking-2026-04-29.md]
- `cache_read_input_tokens` tracks tokens read from existing cache entries, charged at a reduced rate ^[raw/document/claude code/claude-code-004-agent-sdk-cost-tracking-2026-04-29.md]
- Default cache TTL is 5 minutes when authenticating with an API key or running on Amazon Bedrock, Google Cloud Vertex AI, or Microsoft Foundry ^[raw/document/claude code/claude-code-004-agent-sdk-cost-tracking-2026-04-29.md]
- Setting the `ENABLE_PROMPT_CACHING_1H` environment variable extends cache TTL to 1 hour, trading higher write cost for more cache reads; applies to API key, Amazon Bedrock, Google Vertex AI, and Microsoft Foundry users ^[raw/document/claude code/claude-code-004-agent-sdk-cost-tracking-2026-04-29.md] ^[raw/document/claude code/claude-code-121-whats-new-2026-w16-2026-04-29.md]
- Claude subscription users receive 1-hour TTL automatically and do not need to set `ENABLE_PROMPT_CACHING_1H` ^[raw/document/claude code/claude-code-004-agent-sdk-cost-tracking-2026-04-29.md]
- `excludeDynamicSections: true` on the `claude_code` preset moves per-session context (working directory, git status, date, auto-memory paths) from the system prompt into the first user message, enabling identical preset-plus-append configurations to share a cache entry across different directories and machines ^[raw/document/claude code/claude-code-011-agent-sdk-modifying-system-prompts-2026-04-29.md]
- Without `excludeDynamicSections`, two sessions with the same preset and append text still cannot share a cache entry if they run from different working directories, because the preset embeds per-session context ahead of the append text ^[raw/document/claude code/claude-code-011-agent-sdk-modifying-system-prompts-2026-04-29.md]
- On OpenRouter, in-memory prompt caching (temporary storage in a provider's datacenter for repeated prompt processing) is not considered "retaining" data; endpoints with implicit caching are allowed under ZDR routing policies ^[raw/document/openrouter/openrouter-044-guides-features-zdr-2026-04-29.md]
- On OpenRouter, most providers (OpenAI, Grok, Moonshot AI, Groq, DeepSeek) enable prompt caching automatically with no configuration required ^[raw/document/openrouter/openrouter-070-guides-best-practices-prompt-caching-2026-04-29.md]
- Anthropic requires explicit `cache_control` configuration; supports two modes: automatic caching (top-level field, Anthropic-only) and explicit cache breakpoints (per-block, works across all Anthropic-compatible providers) ^[raw/document/openrouter/openrouter-070-guides-best-practices-prompt-caching-2026-04-29.md]
- OpenAI cache writes are free; cache reads are charged at 0.25x or 0.50x original input pricing depending on the model; minimum prompt size of 1024 tokens ^[raw/document/openrouter/openrouter-070-guides-best-practices-prompt-caching-2026-04-29.md]
- Anthropic cache writes cost 1.25x base input price (5-min TTL) or 2x base input price (1-hr TTL); cache reads at a reduced rate; maximum four explicit breakpoints per request ^[raw/document/openrouter/openrouter-070-guides-best-practices-prompt-caching-2026-04-29.md]
- DeepSeek cache writes cost the same as regular input tokens (unlike providers offering free writes); cache reads at a reduced rate ^[raw/document/openrouter/openrouter-070-guides-best-practices-prompt-caching-2026-04-29.md]
- Google Gemini 2.5 Pro and 2.5 Flash support implicit caching with no write or storage costs and reduced read pricing; explicit `cache_control` breakpoints are also supported via OpenRouter ^[raw/document/openrouter/openrouter-070-guides-best-practices-prompt-caching-2026-04-29.md]
- Cache usage on OpenRouter is inspectable via the Activity page, the `/api/v1/generation` API, or the `prompt_tokens_details` object in API responses (containing `cached_tokens` and `cache_write_tokens` fields) ^[raw/document/openrouter/openrouter-070-guides-best-practices-prompt-caching-2026-04-29.md]

## Details

Prompt caching in the Agent SDK follows a write-once, read-many model. When the SDK first encounters a portion of the prompt, it creates a cache entry (`cache_creation_input_tokens`), which is billed at a higher rate than standard input tokens. Subsequent requests that include the same content can read from the cache (`cache_read_input_tokens`) at a reduced rate. The default TTL for cache entries is 5 minutes when using API key authentication or running on cloud providers (Bedrock, Vertex AI, Foundry). This means that if more than 5 minutes pass between requests with the same system prompt and context, the cache expires and the next request pays the full creation price again. ^[raw/document/claude code/claude-code-004-agent-sdk-cost-tracking-2026-04-29.md]

For workloads that run many short sessions against the same system prompt with gaps longer than 5 minutes between them, the `ENABLE_PROMPT_CACHING_1H` environment variable extends the cache TTL to 1 hour. This can be set in the shell environment or passed through `options.env` in the SDK. Cache writes with a 1-hour TTL are billed at a higher rate than 5-minute writes, so enabling this trades higher upfront cost for more cache hits on subsequent requests. Claude subscription users receive the 1-hour TTL automatically without needing to set this variable. ^[raw/document/claude code/claude-code-004-agent-sdk-cost-tracking-2026-04-29.md]

Cross-session cache reuse is also blocked by per-session context embedded in the system prompt. When using the `claude_code` preset, the working directory, platform, OS version, date, git status, and auto-memory paths are embedded ahead of any `append` text. Any difference in this context produces a different system prompt and a cache miss. The `excludeDynamicSections: true` option moves this dynamic content into the first user message instead, leaving only the static preset and `append` text in the system prompt. This enables fleets of agents running from different directories to reuse the same cached system prompt. The tradeoff is that instructions in the user message carry marginally less weight than the same text in the system prompt. `excludeDynamicSections` requires SDK v0.2.98+ (TypeScript) or v0.1.58+ (Python) and applies only to the preset object form. ^[raw/document/claude code/claude-code-011-agent-sdk-modifying-system-prompts-2026-04-29.md]

### Distinction from OpenRouter response caching

Provider-level prompt caching (e.g., Anthropic prompt caching, OpenAI cached context) operates within the provider's infrastructure and caches repeated prompt prefixes at a reduced token rate. OpenRouter response caching is a separate mechanism that operates at the request level before the call reaches the provider, storing and returning complete responses for identical requests at zero cost. The two mechanisms are independent and can be used together. ^[raw/document/openrouter/openrouter-031-guides-features-response-caching-2026-04-29.md]

### Provider-Specific Caching on OpenRouter

Each provider implements prompt caching differently on OpenRouter:

| Provider | Mode | Cache Write Cost | Cache Read Cost | Min Tokens | Notes |
|---|---|---|---|---|---|
| OpenAI | Automatic | Free | 0.25x–0.50x input | 1024 | No configuration needed |
| Grok | Automatic | Free | Reduced multiplier | — | No configuration needed |
| Moonshot AI | Automatic | Free | Reduced multiplier | — | No configuration needed |
| Groq | Automatic | Free | Reduced multiplier | — | Kimi K2 models only |
| DeepSeek | Automatic | Same as input | Reduced multiplier | — | No configuration needed |
| Anthropic | Automatic or Explicit | 1.25x (5-min) / 2x (1-hr) | Reduced | 1024–4096 | Max 4 explicit breakpoints; automatic mode excludes Bedrock/Vertex |
| Gemini 2.5 | Implicit or Explicit | Free (implicit) / Input + storage (explicit) | Reduced multiplier | Model-specific | Explicit uses `cache_control` breakpoints; only last breakpoint used for Gemini |

^[raw/document/openrouter/openrouter-070-guides-best-practices-prompt-caching-2026-04-29.md]

Anthropic's automatic caching (top-level `cache_control`) is only supported when routed directly to the Anthropic provider; Amazon Bedrock and Google Vertex AI endpoints do not support it. Explicit per-block `cache_control` breakpoints work across all Anthropic-compatible providers. The 1-hour TTL for explicit cache breakpoints is supported across all Claude model providers (Anthropic, Amazon Bedrock, and Google Vertex AI). ^[raw/document/openrouter/openrouter-070-guides-best-practices-prompt-caching-2026-04-29.md]

For Google Gemini, OpenRouter simplifies cache management — no manual creation, updating, or deletion of caches is needed. Only the last `cache_control` breakpoint is used for Gemini caching, but multiple breakpoints are safe and help maintain compatibility with Anthropic. Gemini's `systemInstruction` field is treated as immutable when cached; dynamic content should be placed in a later `user` message rather than after a cached block in the first system message. ^[raw/document/openrouter/openrouter-070-guides-best-practices-prompt-caching-2026-04-29.md]

## Related

- [[entities/agent_sdk]]
- [[entities/openrouter]]
- [[entities/anthropic]]
- [[entities/openai]]
- [[entities/deepseek]]
- [[entities/google_gemini]]
- [[entities/grok]]
- [[entities/moonshot_ai]]
- [[entities/groq]]
- [[concepts/cost_tracking]]
- [[concepts/system_prompt]]
- [[concepts/response_caching]]
- [[concepts/zero_data_retention]]
- [[concepts/provider_sticky_routing]]
- [[summaries/openrouter-guides-best-practices-prompt-caching]]