---
title: "Claude Code Agent Sdk Quickstart"
summary: "Step-by-step guide for setting up and running a Python or TypeScript agent that autonomously finds and fixes code bugs using the Agent SDK"
type: summary
sources:
  - raw/document/claude code/claude-code-017-agent-sdk-quickstart-2026-04-29.md
tags:
  - agent-sdk
  - quickstart
  - python
  - typescript
  - setup
  - permissions
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Claude Code Agent Sdk Quickstart

A tutorial walking through project setup, SDK installation, API key configuration, and building a minimal agent that reads code, identifies bugs, and applies fixes autonomously. ^[raw/document/claude code/claude-code-017-agent-sdk-quickstart-2026-04-29.md]

## Key Points

- Requires Node.js 18+ or Python 3.10+ and an Anthropic account ^[raw/document/claude code/claude-code-017-agent-sdk-quickstart-2026-04-29.md]
- Install via `npm install @anthropic-ai/claude-agent-sdk` (TypeScript), `uv init && uv add claude-agent-sdk` (Python with uv), or `pip3 install claude-agent-sdk` (Python with venv) ^[raw/document/claude code/claude-code-017-agent-sdk-quickstart-2026-04-29.md]
- The TypeScript SDK bundles a native Claude Code binary as an optional dependency, so no separate Claude Code install is needed ^[raw/document/claude code/claude-code-017-agent-sdk-quickstart-2026-04-29.md]
- API key is set via `.env` file with `ANTHROPIC_API_KEY`; third-party providers (Bedrock, Vertex AI, Azure) use environment variable flags ^[raw/document/claude code/claude-code-017-agent-sdk-quickstart-2026-04-29.md]
- The `query()` function is the main entry point, returning an async iterator that streams messages as Claude works through the agent loop ^[raw/document/claude code/claude-code-017-agent-sdk-quickstart-2026-04-29.md]
- `ClaudeAgentOptions` configures tools (`allowed_tools`), permission mode (`permission_mode`), and custom system prompts (`system_prompt`) ^[raw/document/claude code/claude-code-017-agent-sdk-quickstart-2026-04-29.md]
- Tool set determines agent capability: read-only (`Read`, `Glob`, `Grep`), code modification (`Read`, `Edit`, `Glob`), or full automation (`Read`, `Edit`, `Bash`, `Glob`, `Grep`) ^[raw/document/claude code/claude-code-017-agent-sdk-quickstart-2026-04-29.md]

## Quotes

- "This is what makes the Agent SDK different: Claude executes tools directly instead of asking you to implement them." ^[raw/document/claude code/claude-code-017-agent-sdk-quickstart-2026-04-29.md]
- "Unless previously approved, Anthropic does not allow third party developers to offer claude.ai login or rate limits for their products, including agents built on the Claude Agent SDK." ^[raw/document/claude code/claude-code-017-agent-sdk-quickstart-2026-04-29.md]

## Notes

- The quickstart demonstrates `acceptEdits` permission mode, which auto-approves file edits so the agent can run without interactive prompts ^[raw/document/claude code/claude-code-017-agent-sdk-quickstart-2026-04-29.md]
- Agent SDK v0.2.111+ is required for Opus 4.7; older versions fail with a `thinking.type.enabled` API error ^[raw/document/claude code/claude-code-017-agent-sdk-quickstart-2026-04-29.md]

## Related

- [[entities/agent_sdk]]
- [[concepts/agent_loop]]
- [[concepts/permissions]]
- [[concepts/custom_tools]]
- [[concepts/system_prompt]]