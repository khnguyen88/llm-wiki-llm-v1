---
title: Headless Claude Code via PowerShell
type: summary
date: 2026-04-22
sources:
  - raw/document/working_ps_script_to_run_headless_claude_code.txt
tags:
  - automation
  - powershell
  - claude-code
  - headless
  - ccr
---

# Headless Claude Code via PowerShell

A working PowerShell script by Khiem Nguyen that runs Claude Code headlessly through [[claude-code-router]] to execute a task against a project using a non-Anthropic LLM.

## Script Flow

1. **Check CCR status** — parses `ccr status` output to detect if the router is running
2. **Start/restart if needed** — stops then restarts CCR if not running; skips restart if already active
3. **Set project directory** — `Set-Location` to the target project
4. **Execute headless task** — `ccr code --print --dangerously-skip-permissions "$PROMPT"`
5. **Cleanup** — stops CCR if it wasn't running before the script

## Key Patterns

- Prompt constructed by concatenating parts: instructions, content spec, exit command (`/exit`)
- `--print` flag for non-interactive output
- `--dangerously-skip-permissions` for full automation (no approval prompts)
- Graceful CCR lifecycle management: only stop if the script started it
- `try/catch` error handling around the entire flow

## Relevance

Demonstrates the practical automation layer of [[model_routing]] — using CCR to run Claude Code tasks unattended with alternative LLMs. Connects to [[claude_code]] as a headless execution mode and to [[claude-code-router]] as the proxy enabling multi-provider access.

## Source

`raw/document/working_ps_script_to_run_headless_claude_code.txt`