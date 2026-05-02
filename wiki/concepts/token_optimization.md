---
title: "Token Optimization"
summary: "Strategies for reducing Claude Code token consumption through context management, model selection, preprocessing, and delegation patterns"
type: concept
sources:
  - raw/document/claude code/claude-code-052-costs-2026-04-29.md
tags:
  - token-optimization
  - claude-code
  - cost-management
  - context-window
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Token Optimization

Strategies for reducing Claude Code token consumption. Token costs scale with context size: the more context Claude processes, the more tokens are used. Claude Code automatically optimizes costs through [[concepts/prompt_caching|prompt caching]] (reducing costs for repeated content like system prompts) and auto-compaction (summarizing conversation history when approaching context limits). The following strategies help keep context small and reduce per-message costs. ^[raw/document/claude code/claude-code-052-costs-2026-04-29.md]

## Key Points

- Use `/clear` between unrelated tasks; stale context wastes tokens on every subsequent message, and `/rename` before clearing preserves session discoverability ^[raw/document/claude code/claude-code-052-costs-2026-04-29.md]
- Add custom compaction instructions via `/compact` (e.g., `/compact Focus on code samples and API usage`) or in CLAUDE.md to control what compaction preserves ^[raw/document/claude code/claude-code-052-costs-2026-04-29.md]
- Sonnet handles most coding tasks well and costs less than Opus; reserve Opus for complex architectural decisions or multi-step reasoning, and use Haiku for simple subagent tasks ^[raw/document/claude code/claude-code-052-costs-2026-04-29.md]
- MCP tool definitions are deferred by default (tool search), so only tool names enter context until a specific tool is used; prefer CLI tools like `gh`, `aws`, and `gcloud` over MCP servers when available, as CLI commands add no per-tool listing ^[raw/document/claude code/claude-code-052-costs-2026-04-29.md]
- Custom [[concepts/hooks|hooks]] can preprocess data before Claude sees it (e.g., grepping a 10,000-line log for errors reduces context from tens of thousands of tokens to hundreds) ^[raw/document/claude code/claude-code-052-costs-2026-04-29.md]
- [[concepts/skills|Skills]] load on-demand rather than at session start, so moving specialized instructions from CLAUDE.md to skills keeps base context smaller; aim to keep CLAUDE.md under 200 lines ^[raw/document/claude code/claude-code-052-costs-2026-04-29.md]
- [[concepts/extended_thinking|Extended thinking]] tokens are billed as output tokens; reduce costs by lowering the effort level with `/effort`, disabling thinking in `/config`, or lowering the budget with `MAX_THINKING_TOKENS=8000` ^[raw/document/claude code/claude-code-052-costs-2026-04-29.md]

## Details

### Context Management

Proactive context management is the most impactful lever for token reduction. Using `/clear` to start fresh when switching tasks prevents stale context from consuming tokens on every subsequent message. Using `/rename` before clearing preserves session discoverability so sessions can be found later with `/resume`. Custom compaction instructions, either via the `/compact` command or in CLAUDE.md, control what information is preserved during automatic summarization. A status line configuration can display context window usage continuously for monitoring. ^[raw/document/claude code/claude-code-052-costs-2026-04-29.md]

### Delegation Patterns

Delegating verbose operations to [[concepts/subagents|subagents]] keeps large outputs (test results, documentation, log files) in the subagent's context while only a summary returns to the main conversation. [[concepts/agent_teams|Agent teams]] use approximately 7x more tokens than standard sessions when teammates run in plan mode, because each teammate maintains its own context window. To manage team costs: use Sonnet for teammates, keep teams small, keep spawn prompts focused, and clean up teams when work is done (active teammates continue consuming tokens even if idle). ^[raw/document/claude code/claude-code-052-costs-2026-04-29.md]

### Prompt Specificity

Vague requests like "improve this codebase" trigger broad scanning. Specific requests like "add input validation to the login function in auth.ts" let Claude work efficiently with minimal file reads. For complex tasks, use [[concepts/plan_mode|plan mode]] (Shift+Tab) to explore and propose an approach before implementation, press Escape to course-correct early, include verification targets in prompts, and test incrementally (write one file, test it, then continue). ^[raw/document/claude code/claude-code-052-costs-2026-04-29.md]

## Related

- [[concepts/context_window]]
- [[concepts/prompt_caching]]
- [[concepts/extended_thinking]]
- [[concepts/subagents]]
- [[concepts/agent_teams]]
- [[concepts/hooks]]
- [[concepts/skills]]
- [[concepts/mcp]]
- [[concepts/cost_tracking]]
- [[summaries/claude-code-costs]]