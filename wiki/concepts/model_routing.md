---
title: Model Routing
type: concept
date: 2026-04-22
sources:
  - raw/repos/claude-code-router/README.md
  - raw/repos/claude-code-router/docs/docs/server/config/routing.md
tags:
  - llm
  - routing
  - proxy
  - claude-code
---

# Model Routing

The practice of directing LLM requests to different models based on the task scenario, cost, or context requirements. Implemented by [[claude-code-router]] as its core feature.

## Scenario-Based Routing

CCR defines built-in scenarios with fallback chains:

| Scenario | Purpose | Example Model |
|----------|---------|---------------|
| default | General tasks | deepseek-chat |
| background | Background tasks (cheaper) | qwen2.5-coder |
| think | Reasoning-heavy tasks | deepseek-reasoner |
| longContext | Tasks exceeding token threshold | gemini-2.5-pro |
| webSearch | Web search tasks | gemini-2.5-flash |
| image | Image-related tasks | (model with image support) |

## Fallback System

Per-scenario ordered list of backup models tried sequentially on failure. Configured in the `"fallback"` key of config.json.

## Routing Priority

1. Custom router function (highest)
2. Project-level config (`~/.claude/projects/<project-id>/claude-code-router.json`)
3. Global config
4. Built-in rules (lowest)

## Subagent Routing

The `<CCR-SUBAGENT-MODEL>provider,model</CCR-SUBAGENT-MODEL>` tag at the beginning of a subagent prompt directs that specific subagent to a designated model, bypassing normal routing.

## Related

- [[claude-code-router]] — the tool implementing this
- [[request_transformers]] — format conversion layer
- [[headless_llm_execution]] — automation use case that relies on model routing