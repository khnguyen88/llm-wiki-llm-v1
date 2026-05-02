---
title: "LSP Tool"
summary: "Code intelligence tool in Claude Code that connects to language servers for navigation, type checking, and code analysis, activated by installing a code intelligence plugin"
type: concept
sources:
  - raw/document/claude code/claude-code-109-tools-reference-2026-04-29.md
tags:
  - claude-code
  - lsp
  - code-intelligence
  - tools
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# LSP Tool

Code intelligence tool in Claude Code that leverages running language servers to provide real-time code analysis, navigation, and type checking. The tool is inactive until a code intelligence plugin is installed for the target language. ^[raw/document/claude code/claude-code-109-tools-reference-2026-04-29.md]

## Key Points

- After each file edit, the LSP tool automatically reports type errors and warnings so Claude can fix issues without a separate build step ^[raw/document/claude code/claude-code-109-tools-reference-2026-04-29.md]

- Capabilities include: jump to a symbol's definition, find all references, get type information at a position, list symbols in a file or workspace, find implementations of an interface, and trace call hierarchies ^[raw/document/claude code/claude-code-109-tools-reference-2026-04-29.md]

- The tool requires a code intelligence plugin for the target language; the plugin bundles the language server configuration, and the server binary must be installed separately ^[raw/document/claude code/claude-code-109-tools-reference-2026-04-29.md]

- The LSP tool does not require explicit permission to use (no permission prompt) ^[raw/document/claude code/claude-code-109-tools-reference-2026-04-29.md]

## Details

The LSP tool bridges Claude Code's editing capabilities with Language Server Protocol implementations, enabling Claude to understand code semantics beyond simple text matching. After each file edit, the tool automatically surfaces diagnostics (type errors, warnings) from the language server, creating a tight feedback loop where Claude can identify and fix issues without requiring a manual build cycle. Direct invocations support code navigation workflows: jumping to definitions, finding references, listing workspace symbols, and tracing call hierarchies.

The tool relies on a code intelligence plugin ecosystem. Each plugin provides the configuration needed to connect Claude Code to a specific language server, while the language server binary itself (e.g., `pylsp` for Python, `gopls` for Go) must be installed on the system separately. Without a matching plugin for the language in use, the LSP tool remains inactive and provides no functionality. ^[raw/document/claude code/claude-code-109-tools-reference-2026-04-29.md]

## Related

- [[entities/claude_code]]
- [[concepts/permissions]]
- [[concepts/plugins]]
- [[summaries/claude-code-tools-reference]]