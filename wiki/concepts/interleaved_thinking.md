---
title: "Interleaved Thinking"
summary: "A technique allowing models to reason between tool calls, enabling multi-step decision-making with thinking steps interspersed across tool invocations"
type: concept
sources:
  - raw/document/openrouter/openrouter-032-guides-features-tool-calling-2026-04-29.md
tags:
  - interleaved-thinking
  - tool-calling
  - reasoning
  - agentic
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Interleaved Thinking

Interleaved thinking allows models to reason between tool calls, enabling more sophisticated decision-making after receiving tool results. The model can chain multiple tool calls with reasoning steps in between, make nuanced decisions based on intermediate results, and provide transparent reasoning for tool selection. ^[raw/document/openrouter/openrouter-032-guides-features-tool-calling-2026-04-29.md]

## Key Points

- Interleaved thinking allows models to reason about tool results before deciding the next action, rather than immediately proceeding to the next tool call ^[raw/document/openrouter/openrouter-032-guides-features-tool-calling-2026-04-29.md]
- Models can chain multiple tool calls with reasoning steps in between, making nuanced decisions based on intermediate results ^[raw/document/openrouter/openrouter-032-guides-features-tool-calling-2026-04-29.md]
- Increases token usage and response latency; should be enabled with consideration for budget and performance requirements ^[raw/document/openrouter/openrouter-032-guides-features-tool-calling-2026-04-29.md]
- Best practices include clear tool descriptions, structured parameter schemas, context preservation across interactions, and designing tools that return meaningful error messages to help the model adjust its approach ^[raw/document/openrouter/openrouter-032-guides-features-tool-calling-2026-04-29.md]

## Details

In a typical interleaved thinking workflow, the model reasons about what tool to call first, receives the result, then reasons about what to do next based on those results. For example, a model researching electric vehicles might call an academic search tool, reason about gaps in the results, call a statistics tool for current data, reason about remaining gaps, and call another search tool with a more specific query before synthesizing a final answer. ^[raw/document/openrouter/openrouter-032-guides-features-tool-calling-2026-04-29.md]

Implementation considerations include higher response latency due to reasoning steps, increased token usage from the reasoning process, and variation in reasoning quality across models. Some models are better suited for interleaved thinking than others. ^[raw/document/openrouter/openrouter-032-guides-features-tool-calling-2026-04-29.md]

## Related

- [[concepts/tool_calling]]
- [[concepts/extended_thinking]]
- [[concepts/agent_loop]]
- [[entities/openrouter]]