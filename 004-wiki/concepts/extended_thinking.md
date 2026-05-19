---
title: "Extended Thinking"
summary: "A default-on feature giving Claude space to reason through complex problems step-by-step before responding, with adaptive reasoning on supported models that dynamically allocates thinking tokens based on effort level"
type: concept
sources:
  - raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md
  - raw/document/claude code/claude-code-052-costs-2026-04-29.md
tags:
  - claude-code
  - thinking
  - reasoning
  - effort
  - configuration
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Extended Thinking

Extended thinking is enabled by default, giving Claude space to reason through complex problems step-by-step before responding. The internal reasoning is visible in verbose mode (toggled with Ctrl+O), appearing as gray italic text. On models that support effort levels, thinking uses adaptive reasoning: the model dynamically allocates thinking tokens based on the effort level setting and task complexity rather than a fixed token budget. ^[raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]

## Key Points

- Extended thinking is enabled by default; toggle per-session with Option+T (macOS) or Alt+T (Windows/Linux) ^[raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]
- On supported models, adaptive reasoning dynamically decides whether and how much to think based on effort level and task complexity; phrases like "think" or "think hard" are interpreted as regular prompts and do not allocate thinking tokens ^[raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]
- Configure effort level via `/effort`, the `/model` menu, or `CLAUDE_CODE_EFFORT_LEVEL` environment variable; levels include `low`, `medium`, `high`, `xhigh`, and `max` ^[raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]
- The `ultrathink` keyword in a prompt adds an in-context instruction for deeper reasoning on that turn without changing the effort level itself ^[raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]
- Set `MAX_THINKING_TOKENS` environment variable to limit the thinking token budget; on adaptive reasoning models, only `0` applies (disabling thinking) unless `CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING=1` reverts to fixed budgets ^[raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]
- Toggle thinking globally via `/config`, which sets `alwaysThinkingEnabled` in `~/.claude/settings.json` ^[raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]
- All thinking tokens are charged even when thinking summaries are redacted; set `showThinkingSummaries: true` in `settings.json` to display full summaries ^[raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]
- During extended thinking, the spinner shows inline progress hints like "still thinking" and "almost done thinking" ^[raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]
- Extended thinking is most valuable for complex architectural decisions, challenging bugs, multi-step implementation planning, and evaluating tradeoffs between approaches ^[raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]
- Thinking tokens are billed as output tokens; the default budget can be tens of thousands of tokens per request depending on the model, making it a significant cost factor ^[raw/document/claude code/claude-code-052-costs-2026-04-29.md]
- For simpler tasks, reduce thinking costs by lowering the effort level with `/effort` or `/model`, disabling thinking in `/config`, or capping the budget with `MAX_THINKING_TOKENS=8000` ^[raw/document/claude code/claude-code-052-costs-2026-04-29.md]

## Details

Extended thinking controls how much internal reasoning Claude performs before responding. More thinking provides space to explore solutions, analyze edge cases, and self-correct mistakes. The adaptive reasoning system on supported models (Opus 4.6 and Sonnet 4.6) dynamically adjusts thinking depth: routine prompts receive less thinking, while complex steps benefit from deeper reasoning. This is the recommended way to tune the tradeoff between speed and reasoning depth.

On older models without adaptive reasoning, thinking uses a fixed token budget drawn from the output allocation. The budget varies by model, with `MAX_THINKING_TOKENS` as an override ceiling. Opus 4.7 always uses adaptive reasoning and does not support a fixed thinking budget. `CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING` applies only to Opus 4.6 and Sonnet 4.6, reverting them to the fixed budget model. ^[raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]

## Related

- [[concepts/context_window]]
- [[concepts/permissions]]
- [[entities/claude_code]]
- [[summaries/claude-code-common-workflows]]
- [[concepts/token_optimization]]
- [[summaries/claude-code-costs]]