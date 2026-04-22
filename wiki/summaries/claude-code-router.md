---
title: Claude Code Router
type: summary
date: 2026-04-22
sources:
  - raw/repos/claude-code-router/README.md
  - raw/repos/claude-code-router/docs/docs/server/intro.md
  - raw/repos/claude-code-router/docs/docs/server/config/routing.md
  - raw/repos/claude-code-router/docs/docs/server/config/transformers.md
  - raw/repos/claude-code-router/docs/docs/server/config/basic.md
  - raw/repos/claude-code-router/docs/docs/server/advanced/custom-router.md
  - raw/repos/claude-code-router/docs/docs/cli/intro.md
  - raw/repos/claude-code-router/docs/docs/cli/quick-start.md
  - raw/repos/claude-code-router/docs/docs/presets/intro.md
  - raw/repos/claude-code-router/docs/docs/server/deployment.md
tags:
  - tool
  - claude-code
  - model-routing
  - llm-proxy
---

# Claude Code Router

An open-source proxy that routes Claude Code requests to different LLM providers and models. Published by musistudio on GitHub and npm as `@musistudio/claude-code-router`.

## What It Does

Claude Code Router (CCR) sits between the Claude Code client and LLM provider APIs, translating requests/responses so Claude Code can talk to any provider (OpenRouter, DeepSeek, Ollama, Gemini, Volcengine, SiliconFlow, and others). It provides scenario-based routing, model switching, request/response transformation, and preset management.

## Architecture

Client -> CCR Server -> LLM Providers. The server wraps `@musistudio/llms`, a standalone universal LLM API transformation library that provides `UnifiedChatRequest`/`UnifiedChatResponse`, the `Transformer` interface, and built-in transformers.

## Core Features

- **Model routing**: Route by scenario (default, background, think, longContext, webSearch, image) with fallback chains
- **Multi-provider support**: DeepSeek, Groq, Gemini, OpenRouter, Ollama, Volcengine, ModelScope, DashScope, AIHubMix
- **Transformers**: Plugins that convert between Anthropic API format and provider-specific formats (deepseek, gemini, openrouter, groq, etc.)
- **Custom routers**: JavaScript functions for advanced routing logic (time-based, cost-optimization, per-project)
- **Subagent routing**: `<CCR-SUBAGENT-MODEL>provider,model</CCR-SUBAGENT-MODEL>` tags in prompts
- **Dynamic model switching**: `/model` command or `ccr model` CLI within Claude Code
- **Presets**: Save, share, and install configuration bundles with schema-driven input
- **CLI management**: `ccr start/stop/restart/code/ui/model/activate/statusline`
- **Web UI**: Browser-based config editor at `/ui/`
- **Statusline**: Terminal status bar showing model, tokens, cost, speed, etc.
- **GitHub Actions integration**: Run Claude Code with routing in CI/CD pipelines
- **Docker deployment**: Official image on Docker Hub with compose support

## Configuration

Config at `~/.claude-code-router/config.json` with three main sections: Providers (name, api_base_url, api_key, models, transformer), Router (default, background, think, longContext, webSearch, image), and transformers. Supports environment variable interpolation (`$VAR` / `${VAR}`).

## Key CLI Commands

| Command | Purpose |
|---------|---------|
| `ccr start` | Start the router server |
| `ccr stop` | Stop the server |
| `ccr restart` | Restart after config changes |
| `ccr code` | Launch Claude Code through the router |
| `ccr ui` | Open web-based config editor |
| `ccr model` | Interactive model selector |
| `ccr activate` | Output shell env vars for SDK integration |
| `ccr statusline` | Terminal status bar |
| `ccr preset export/install/list/info/delete` | Preset management |

## Related

- [[model_routing]] — the routing concept
- [[request_transformers]] — the transformer system
- [[claude_code]] — the tool it extends
- [[headless_llm_execution]] — automated use of CCR without interactive input