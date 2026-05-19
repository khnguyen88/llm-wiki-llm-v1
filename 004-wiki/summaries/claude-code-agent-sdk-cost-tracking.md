---
title: "Claude Code Agent Sdk Cost Tracking"
summary: "How the Agent SDK exposes token usage, cost estimates, and prompt caching configuration for tracking spending across multi-step agent sessions"
type: summary
sources:
  - raw/document/claude code/claude-code-004-agent-sdk-cost-tracking-2026-04-29.md
tags:
  - cost-tracking
  - agent-sdk
  - claude-code
  - token-usage
  - prompt-caching
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Claude Code Agent Sdk Cost Tracking

## Key Points

- `total_cost_usd` and `costUSD` are client-side estimates computed from a price table bundled at build time; they can drift from actual billing when pricing changes, the SDK doesn't recognize a model, or billing rules apply that the client cannot model ^[raw/document/claude code/claude-code-004-agent-sdk-cost-tracking-2026-04-29.md]
- Each `query()` call produces one result message with a cumulative `total_cost_usd`; per-step usage is available on each assistant message via a nested `BetaMessage` with `id` and `usage` fields ^[raw/document/claude code/claude-code-004-agent-sdk-cost-tracking-2026-04-29.md]
- When Claude uses tools in parallel, multiple assistant messages share the same message ID with identical usage data; deduplicating by ID avoids inflated totals ^[raw/document/claude code/claude-code-004-agent-sdk-cost-tracking-2026-04-29.md]
- The result message includes `modelUsage` (TypeScript) / `model_usage` (Python), a map of model name to per-model token counts and cost, useful for multi-model configurations ^[raw/document/claude code/claude-code-004-agent-sdk-cost-tracking-2026-04-29.md]
- Each `query()` call returns its own `total_cost_usd` independently; the SDK does not provide a session-level total, so callers must accumulate across calls themselves ^[raw/document/claude code/claude-code-004-agent-sdk-cost-tracking-2026-04-29.md]
- Both success and error result messages include `usage` and `total_cost_usd`; tokens consumed before a failure are still reported ^[raw/document/claude code/claude-code-004-agent-sdk-cost-tracking-2026-04-29.md]
- The SDK automatically uses prompt caching; usage fields include `cache_creation_input_tokens` (higher rate) and `cache_read_input_tokens` (reduced rate) ^[raw/document/claude code/claude-code-004-agent-sdk-cost-tracking-2026-04-29.md]

## Quotes

- "The `total_cost_usd` and `costUSD` fields are client-side estimates, not authoritative billing data. The SDK computes them locally from a price table bundled at build time." ^[raw/document/claude code/claude-code-004-agent-sdk-cost-tracking-2026-04-29.md:21]
- "Do not bill end users or trigger financial decisions from these fields." ^[raw/document/claude code/claude-code-004-agent-sdk-cost-tracking-2026-04-29.md:24]

## Notes

- The source provides both TypeScript and Python code examples for tracking costs at the query level, per-step level, per-model level, and across multiple calls.
- For authoritative billing, the source directs users to the Usage and Cost API or the Usage page in the Claude Console.

## Related

- [[entities/agent_sdk]]
- [[concepts/cost_tracking]]
- [[concepts/prompt_caching]]
- [[concepts/agent_loop]]