---
title: "Bare Mode"
summary: "Minimal startup mode that strips auto-discovery for faster scripted execution, available via --bare flag or CLAUDE_CODE_SIMPLE environment variable"
type: concept
sources:
  - raw/document/claude code/claude-code-045-cli-reference-2026-04-29.md
tags:
  - claude-code
  - cli
  - bare-mode
  - performance
  - scripting
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.95
provenance: extracted
---

# Bare Mode

A minimal startup mode for Claude Code that skips auto-discovery to reduce startup time for scripted and non-interactive workloads. Bare mode is enabled with the `--bare` flag and sets the `CLAUDE_CODE_SIMPLE` environment variable. ^[raw/document/claude code/claude-code-045-cli-reference-2026-04-29.md]

## Key Points

- Bare mode skips auto-discovery of hooks, skills, plugins, MCP servers, auto memory, and CLAUDE.md files ^[raw/document/claude code/claude-code-045-cli-reference-2026-04-29.md]
- Only Bash, Read, and Edit tools are available in bare mode; all other tools are excluded ^[raw/document/claude code/claude-code-045-cli-reference-2026-04-29.md]
- Bare mode sets the `CLAUDE_CODE_SIMPLE` environment variable, which can also be set directly for the same effect ^[raw/document/claude code/claude-code-045-cli-reference-2026-04-29.md]
- Designed for non-interactive use with `claude --bare -p "query"` where faster startup matters more than full feature discovery ^[raw/document/claude code/claude-code-045-cli-reference-2026-04-29.md]

## Details

Bare mode targets scripted and CI workflows where startup speed is critical and the full set of Claude Code features (hooks, skills, MCP servers, etc.) are unnecessary. By skipping the discovery and initialization of these subsystems, bare mode significantly reduces the time between invocation and the first model response. The tradeoff is that only three built-in tools (Bash, Read, Edit) are available, and no project-level configuration is loaded from CLAUDE.md files or settings.

The `CLAUDE_CODE_SIMPLE` environment variable provides an alternative entry point for enabling bare mode, useful in containerized or CI environments where command-line flags are harder to inject. ^[raw/document/claude code/claude-code-045-cli-reference-2026-04-29.md]

## Related

- [[entities/claude_code]]
- [[concepts/non_interactive_mode]]
- [[concepts/hooks]]
- [[concepts/skills]]
- [[concepts/plugins]]
- [[concepts/mcp]]