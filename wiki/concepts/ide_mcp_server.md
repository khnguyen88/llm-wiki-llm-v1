---
title: "IDE MCP Server"
summary: "Built-in MCP server that the VS Code extension runs to provide language-server diagnostics and Jupyter cell execution to Claude Code via the CLI"
type: concept
sources:
  - raw/document/claude code/claude-code-115-vs-code-2026-04-29.md
tags:
  - claude-code
  - vs-code
  - mcp
  - ide
  - diagnostics
  - jupyter
  - security
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# IDE MCP Server

A local MCP server that the VS Code extension runs automatically when active. The CLI connects to it to provide IDE-specific capabilities such as reading language-server diagnostics and executing Jupyter notebook cells. The server is named `ide` and is hidden from `/mcp` because there is nothing for users to configure. ^[raw/document/claude code/claude-code-115-vs-code-2026-04-29.md]

## Key Points

- The IDE MCP server binds to `127.0.0.1` on a random high port and is not reachable from other machines ^[raw/document/claude code/claude-code-115-vs-code-2026-04-29.md]
- Each extension activation generates a fresh random auth token written to a lock file at `~/.claude/ide/` with `0600` permissions in a `0700` directory ^[raw/document/claude code/claude-code-115-vs-code-2026-04-29.md]
- Only two tools are visible to the model; the remaining dozen are internal RPC used by the CLI for UI operations (opening diffs, reading selections, saving files) ^[raw/document/claude code/claude-code-115-vs-code-2026-04-29.md]
- `mcp__ide__getDiagnostics` returns language-server diagnostics (errors and warnings from VS Code's Problems panel), optionally scoped to a single file; it does not write ^[raw/document/claude code/claude-code-115-vs-code-2026-04-29.md]
- `mcp__ide__executeCode` runs Python code in the active Jupyter notebook's kernel; it is a write-capable tool that always requires user confirmation ^[raw/document/claude code/claude-code-115-vs-code-2026-04-29.md]
- Jupyter execution always asks first: code is inserted as a new cell, VS Code scrolls it into view, and a native Quick Pick asks the user to Execute or Cancel; dismissing with Esc returns an error to Claude and nothing runs ^[raw/document/claude code/claude-code-115-vs-code-2026-04-29.md]
- `mcp__ide__executeCode` refuses outright when there is no active notebook, when the Jupyter extension (`ms-toolsai.jupyter`) is not installed, or when the kernel is not Python ^[raw/document/claude code/claude-code-115-vs-code-2026-04-29.md]
- The Quick Pick confirmation is separate from `PreToolUse` hooks: an allowlist entry for `mcp__ide__executeCode` lets Claude propose running a cell, but the Quick Pick inside VS Code controls whether it actually runs ^[raw/document/claude code/claude-code-115-vs-code-2026-04-29.md]
- Organizations using `PreToolUse` hooks to allowlist MCP tools need to account for the `ide` server and its `mcp__ide__getDiagnostics` and `mcp__ide__executeCode` tools ^[raw/document/claude code/claude-code-115-vs-code-2026-04-29.md]

## Details

The IDE MCP server bridges VS Code's language intelligence to the CLI. When the extension is active, the CLI automatically discovers and connects to the server using the auth token from the lock file. This is how the CLI opens diffs in VS Code's native diff viewer, reads the user's current selection for @-mentions, and — when working in a Jupyter notebook — asks VS Code to execute cells.

The server hosts about a dozen tools, but only two are exposed to the model's tool list. The rest are internal RPC calls that the CLI uses for its own UI operations. This design means that users do not need to configure anything for the IDE server; it starts and authenticates automatically.

For Jupyter execution, the security model requires explicit user confirmation every time. The code is visible in a new cell before execution, and the user must actively choose to execute it. This prevents silent code execution in notebooks. ^[raw/document/claude code/claude-code-115-vs-code-2026-04-29.md]

## Related

- [[entities/vs_code_extension]]
- [[entities/claude_code]]
- [[concepts/mcp]]
- [[concepts/permissions]]
- [[concepts/hooks]]