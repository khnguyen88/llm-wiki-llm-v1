---
title: "Cost Tracking"
summary: "The mechanism by which the Agent SDK reports token usage and estimated costs at per-step, per-model, and per-query granularity"
type: concept
sources:
  - raw/document/claude code/claude-code-004-agent-sdk-cost-tracking-2026-04-29.md
  - raw/document/claude code/claude-code-052-costs-2026-04-29.md
tags:
  - cost-tracking
  - agent-sdk
  - token-usage
  - observability
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Cost Tracking

The mechanism by which the Agent SDK reports token usage and estimated costs across query calls, individual steps, and models. Cost tracking operates at three scopes: the `query()` call (one invocation, possibly many steps), the step (one request/response cycle within a call), and the session (multiple `query()` calls linked by a session ID). ^[raw/document/claude code/claude-code-004-agent-sdk-cost-tracking-2026-04-29.md]

## Key Points

- `total_cost_usd` and `costUSD` are client-side estimates computed from a bundled price table, not authoritative billing data; they can drift from actual invoices when pricing changes, the SDK doesn't recognize a model, or billing rules differ ^[raw/document/claude code/claude-code-004-agent-sdk-cost-tracking-2026-04-29.md]
- Each `query()` call emits a result message containing the cumulative `total_cost_usd` and `usage` for that call alone; sessions do not aggregate across calls ^[raw/document/claude code/claude-code-004-agent-sdk-cost-tracking-2026-04-29.md]
- Per-step usage is available on each assistant message: TypeScript exposes it via `message.message.id` and `message.message.usage`; Python exposes it via `message.message_id` and `message.usage` ^[raw/document/claude code/claude-code-004-agent-sdk-cost-tracking-2026-04-29.md]
- Parallel tool calls produce multiple assistant messages sharing the same message ID with identical usage data; deduplicating by ID prevents double-counting ^[raw/document/claude code/claude-code-004-agent-sdk-cost-tracking-2026-04-29.md]
- Per-model breakdowns are available via `modelUsage` (TypeScript) / `model_usage` (Python) on the result message, mapping model names to token counts and cost ^[raw/document/claude code/claude-code-004-agent-sdk-cost-tracking-2026-04-29.md]
- Both success and error result messages include `usage` and `total_cost_usd`; tokens consumed before a failure are still tracked ^[raw/document/claude code/claude-code-004-agent-sdk-cost-tracking-2026-04-29.md]
- In Claude Code CLI, the `/usage` command provides detailed token usage statistics for the current session; the dollar figure is a local estimate that may differ from actual billing ^[raw/document/claude code/claude-code-052-costs-2026-04-29.md]
- Workspace spend limits can be set on the total Claude Code workspace spend via the [[entities/claude_console|Claude Console]]; admins can view cost and usage reporting in the Console ^[raw/document/claude code/claude-code-052-costs-2026-04-29.md]
- On Bedrock, Vertex, and Foundry deployments, Claude Code does not send metrics from the cloud; [[entities/litellm|LiteLLM]] is an open-source alternative for tracking spend by key on those platforms ^[raw/document/claude code/claude-code-052-costs-2026-04-29.md]
- Background token usage (conversation summarization for `--resume`, command processing) typically costs under $0.04 per session ^[raw/document/claude code/claude-code-052-costs-2026-04-29.md]

## Details

The SDK scopes cost data at three levels. A **query call** is one invocation of `query()`, which may span multiple steps as the agent calls tools and receives results. Each query call produces a single result message with the cumulative `total_cost_usd`. A **step** is one request/response cycle within a query call; per-step usage is attached to each assistant message. A **session** is a series of `query()` calls linked by a session ID via the `resume` option, but each call within a session reports its cost independently. ^[raw/document/claude code/claude-code-004-agent-sdk-cost-tracking-2026-04-29.md]

When tracking per-step usage, the critical detail is deduplication: parallel tool calls within a single turn produce multiple assistant messages whose nested `BetaMessage` objects share the same `id` and identical `usage`. Counting each message without deduplication inflates token totals. The recommended approach is to maintain a `Set` of seen IDs and skip any message whose ID has already been counted. ^[raw/document/claude code/claude-code-004-agent-sdk-cost-tracking-2026-04-29.md]

In rare cases, messages with the same ID may report different `output_tokens` values. The source advises using the highest value, preferring the result message's `total_cost_usd` over manually summing per-step values, and reporting inconsistencies. For authoritative billing, the source directs users to the Usage and Cost API or the Claude Console. ^[raw/document/claude code/claude-code-004-agent-sdk-cost-tracking-2026-04-29.md]

## Related

- [[entities/agent_sdk]]
- [[concepts/prompt_caching]]
- [[concepts/agent_loop]]
- [[concepts/observability]]
- [[concepts/rate_limiting]]
- [[concepts/token_optimization]]
- [[summaries/claude-code-costs]]