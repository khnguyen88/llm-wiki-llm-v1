---
title: "Native Binaries"
summary: "Architecture change where the Claude CLI spawns a native per-platform binary instead of bundled JavaScript, improving startup time and removing the Node.js runtime dependency"
type: concept
sources:
  - raw/document/claude code/claude-code-121-whats-new-2026-w16-2026-04-29.md
  - raw/document/claude code/claude-code-122-whats-new-2026-w17-2026-04-29.md
tags:
  - claude-code
  - cli
  - installation
  - native
  - binaries
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Native Binaries

Starting with v2.1.113, the `claude` CLI spawns a native per-platform binary instead of running bundled JavaScript through Node.js. The npm package pulls the correct platform binary via an optional dependency such as `@anthropic-ai/claude-code-darwin-arm64`, so the install command does not change. The standalone installer already shipped a native binary; npm now matches it. ^[raw/document/claude code/claude-code-121-whats-new-2026-w16-2026-04-29.md]

## Key Points

- The installed `claude` command no longer invokes Node.js directly; it launches a platform-specific native binary ^[raw/document/claude code/claude-code-121-whats-new-2026-w16-2026-04-29.md]
- Platform binaries are distributed as npm optional dependencies (e.g., `@anthropic-ai/claude-code-darwin-arm64`) and automatically selected during install ^[raw/document/claude code/claude-code-121-whats-new-2026-w16-2026-04-29.md]
- The `npm install` command remains unchanged; the correct binary is selected transparently ^[raw/document/claude code/claude-code-121-whats-new-2026-w16-2026-04-29.md]
- The standalone installer had already shipped a native binary; this change brings npm parity ^[raw/document/claude code/claude-code-121-whats-new-2026-w16-2026-04-29.md]
- Users can verify the change by running `claude update` followed by `claude --version` ^[raw/document/claude code/claude-code-121-whats-new-2026-w16-2026-04-29.md]
- Native macOS and Linux builds replace the `Glob` and `Grep` tools with embedded `bfs` and `ugrep` available through Bash, enabling faster searches without a separate tool round-trip ^[raw/document/claude code/claude-code-122-whats-new-2026-w17-2026-04-29.md]

## Details

The shift to native binaries eliminates the Node.js runtime dependency from the `claude` command path. Previously, the npm-installed CLI ran as a Node.js application that bundled its own runtime. The new architecture uses the npm package's optional dependency mechanism to select the correct platform-specific binary at install time. Each platform combination (darwin-arm64, darwin-x64, linux-arm64, linux-x64, win32-x64, etc.) has its own npm package, and npm resolves the appropriate one based on the host platform. This approach preserves the familiar `npm install -g @anthropic-ai/claude-code` workflow while delivering the performance and compatibility benefits of a native binary. ^[raw/document/claude code/claude-code-121-whats-new-2026-w16-2026-04-29.md]

## Related

- [[entities/claude_code]]
- [[concepts/release_channels]]
- [[concepts/binary_verification]]
- [[concepts/troubleshoot_install]]
- [[summaries/claude-code-whats-new-2026-w17]]