---
title: "Guard Models"
summary: "Safety-filtering LLMs that classify user input or model output as safe or unsafe, used as input/output filters in chat workflows"
type: concept
sources:
  - raw/articles/How to navigate LLM model names.md
tags:
  - llm
  - safety
  - guard
  - filtering
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.85
provenance: extracted
---

# Guard Models

Guard (or guardian) models are LLMs designed to identify unsafe content or questions. They are named with a "guard" or "guardian" suffix and used as safety filters in chat-based workflows. ^[raw/articles/How to navigate LLM model names.md]

## Key Points

- Guard models are used in a two-stage workflow: user input is first sent to the guard model for safety classification, then forwarded to the instruct model only if safe; guard models can also filter model output before it reaches the user ^[raw/articles/How to navigate LLM model names.md]
- When a guard model detects unacceptable content, it typically responds with a pre-determined refusal message ^[raw/articles/How to navigate LLM model names.md]

## Related

- [[concepts/model_naming]]
- [[concepts/instruction_tuning]]