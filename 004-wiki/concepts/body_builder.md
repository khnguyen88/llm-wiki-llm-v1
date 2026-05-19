---
title: "Body Builder"
summary: "An OpenRouter router that transforms natural language prompts into structured API request bodies for running the same task across multiple models in parallel"
type: concept
sources:
  - raw/document/openrouter/openrouter-027-guides-routing-routers-body-builder-2026-04-29.md
tags:
  - openrouter
  - body-builder
  - routing
  - parallel-execution
  - multi-model
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Body Builder

An [[entities/openrouter|OpenRouter]] router that uses AI to transform natural language prompts into structured API request bodies. Invoked by setting `model` to `openrouter/bodybuilder`, it generates ready-to-execute JSON requests that enable running the same task across multiple models in parallel. ^[raw/document/openrouter/openrouter-027-guides-routing-routers-body-builder-2026-04-29.md]

## Key Points

- Activated by sending a `messages`-format request with `model: "openrouter/bodybuilder"`; the response contains generated request bodies in `choices[0].message.content` as JSON ^[raw/document/openrouter/openrouter-027-guides-routing-routers-body-builder-2026-04-29.md]
- Returns a JSON object with a `requests` array, where each entry is a full OpenRouter-compatible request body containing `model` and `messages` fields ^[raw/document/openrouter/openrouter-027-guides-routing-routers-body-builder-2026-04-29.md]
- Free to use for generating request bodies; standard model pricing applies only when executing the generated requests ^[raw/document/openrouter/openrouter-027-guides-routing-routers-body-builder-2026-04-29.md]
- Understands model aliases and common names (e.g., "Claude Sonnet" → `anthropic/claude-sonnet-4.5`, "GPT-5" → `openai/gpt-5.1`, "Gemini" → `google/gemini-3.1-pro-preview`, "DeepSeek" → `deepseek/deepseek-v3.2`) and selects latest versions by default ^[raw/document/openrouter/openrouter-027-guides-routing-routers-body-builder-2026-04-29.md]
- Generated requests use minimal required fields; system messages from the input are preserved and forwarded to each generated request ^[raw/document/openrouter/openrouter-027-guides-routing-routers-body-builder-2026-04-29.md]

## Details

Body Builder addresses the model *selection* problem differently from the [[concepts/auto_router]]: instead of choosing a single optimal model, it generates request bodies for *all* requested models so they can be executed in parallel. This makes it suited for benchmarking, multi-provider verification, and A/B testing workflows.

The typical workflow is two-phase: (1) send a natural language prompt to `openrouter/bodybuilder` and parse the returned JSON to extract the `requests` array, then (2) execute each request in parallel using `Promise.all` (TypeScript) or `asyncio.gather` (Python). Standard model pricing applies to the execution phase only. ^[raw/document/openrouter/openrouter-027-guides-routing-routers-body-builder-2026-04-29.md]

## Related

- [[entities/openrouter]]
- [[concepts/auto_router]]
- [[concepts/model_fallback]]
- [[concepts/structured_output]]
- [[summaries/openrouter-guides-routing-routers-body-builder]]