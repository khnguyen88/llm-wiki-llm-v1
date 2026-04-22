---
title: Headless LLM Execution
type: concept
date: 2026-04-22
sources:
  - raw/document/working_ps_script_to_run_headless_claude_code.txt
tags:
  - automation
  - headless
  - llm
  - ci-cd
---

# Headless LLM Execution

Running LLM-powered coding tools without interactive input — fully automated, no human approval prompts, no terminal UI. Enables LLM tasks in CI/CD pipelines, scheduled jobs, and batch workflows.

## Key Mechanisms

- `--print` flag: non-interactive output mode (Claude Code)
- `--dangerously-skip-permissions`: bypasses all tool approval prompts for full automation
- Prompt termination: `/exit` command ensures the session ends after task completion
- Proxy lifecycle: start/check/stop the routing proxy as part of the script

## Trade-offs

- **Speed**: No human-in-the-loop means tasks run end-to-end without blocking
- **Risk**: Skipping permissions removes safety rails — only suitable for trusted, well-defined tasks
- **Reliability**: Requires CCR/router to be running and the target model to be available

## Related

- [[claude-code-router]] — the proxy enabling non-Anthropic models in this flow
- [[model_routing]] — routing decisions behind headless execution
- [[summaries/headless-claude-code-ps]] — concrete PowerShell implementation