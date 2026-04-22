---
title: Claude Code
type: concept
date: 2026-04-22
sources:
  - raw/repos/claude-code-router/README.md
  - raw/repos/claude-code-router/docs/docs/cli/intro.md
tags:
  - anthropic
  - cli
  - coding
  - llm
---

# Claude Code

Anthropic's official CLI tool for AI-assisted coding. Runs in the terminal and provides an agentic coding experience with access to the file system, shell, and other tools.

## Relevance to This Wiki

Claude Code is the tool that [[claude-code-router]] extends by proxying its API requests to alternative LLM providers. The router replaces the direct Anthropic API connection, enabling model switching, cost optimization, and multi-provider usage within the Claude Code workflow.

## Integration Points

- `ccr code` — launches Claude Code through the router
- `ccr activate` — sets environment variables (`ANTHROPIC_BASE_URL`, `ANTHROPIC_AUTH_TOKEN`) so `claude` command routes through CCR
- Agent SDK applications automatically use configured router when activated

## Related

- [[claude-code-router]] — the proxy extending Claude Code
- [[model_routing]] — how requests get directed to different models