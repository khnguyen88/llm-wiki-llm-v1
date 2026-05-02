---
title: "Monitor Tool"
summary: "Background monitoring tool in Claude Code that runs scripts and feeds each output line back to the conversation, enabling real-time reaction to logs, file changes, and polled status"
type: concept
sources:
  - raw/document/claude code/claude-code-109-tools-reference-2026-04-29.md
tags:
  - claude-code
  - monitoring
  - background
  - tools
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Monitor Tool

A background monitoring tool (requires Claude Code v2.1.98+) that runs a script and streams each output line back to Claude mid-conversation, enabling real-time reaction to log entries, file changes, or polled status without pausing the session. ^[raw/document/claude code/claude-code-109-tools-reference-2026-04-29.md]

## Key Points

- The Monitor tool requires explicit permission (same rules as Bash) and is not available on Amazon Bedrock, Google Vertex AI, or Microsoft Foundry ^[raw/document/claude code/claude-code-109-tools-reference-2026-04-29.md]

- The tool is unavailable when `DISABLE_TELEMETRY` or `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` is set ^[raw/document/claude code/claude-code-109-tools-reference-2026-04-29.md]

- Use cases include: tailing log files and flagging errors, polling a PR or CI job for status changes, watching a directory for file changes, and tracking output from long-running scripts ^[raw/document/claude code/claude-code-109-tools-reference-2026-04-29.md]

- Plugins can declare monitors that start automatically when the plugin is active, instead of requiring Claude to start them manually ^[raw/document/claude code/claude-code-109-tools-reference-2026-04-29.md]

- The tool uses the same permission rules as Bash; `allow` and `deny` patterns configured for Bash apply to Monitor as well ^[raw/document/claude code/claude-code-109-tools-reference-2026-04-29.md]

## Details

The Monitor tool enables a streaming interaction pattern where Claude can observe system events in real time. Claude writes a small script for the watch operation, runs it in the background, and receives each output line as it arrives. The user keeps working in the same session while Claude interjects when a relevant event lands. Monitoring continues until Claude is asked to cancel it or the session ends. ^[raw/document/claude code/claude-code-109-tools-reference-2026-04-29.md]

Plugin-defined monitors extend this capability by declaring monitors that activate automatically when the plugin is loaded, removing the need for manual setup. This allows plugins to provide domain-specific observability (e.g., a deployment plugin could auto-monitor CI status) without requiring the user to ask Claude to start watching. ^[raw/document/claude code/claude-code-109-tools-reference-2026-04-29.md]

## Related

- [[entities/claude_code]]
- [[concepts/permissions]]
- [[concepts/plugins]]
- [[entities/amazon_bedrock]]
- [[entities/google_vertex_ai]]
- [[entities/microsoft_foundry]]
- [[summaries/claude-code-tools-reference]]