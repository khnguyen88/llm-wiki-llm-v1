---
title: "Claude Code Agent Sdk Migration Guide"
summary: "Migration guide for the Claude Code SDK rename to Claude Agent SDK, covering package name changes, import updates, and three breaking changes in v0.1.0"
type: summary
sources:
  - raw/document/claude code/claude-code-010-agent-sdk-migration-guide-2026-04-29.md
tags:
  - agent-sdk
  - migration
  - breaking-changes
  - sdk
  - python
  - typescript
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Claude Code Agent Sdk Migration Guide

## Key Points

- The Claude Code SDK has been renamed to **Claude Agent SDK**; the TS/JS package changed from `@anthropic-ai/claude-code` to `@anthropic-ai/claude-agent-sdk` and the Python package from `claude-code-sdk` to `claude-agent-sdk` ^[001a-raw/document/claude code/claude-code-010-agent-sdk-migration-guide-2026-04-29.md]
- TypeScript migration requires only uninstalling the old package, installing the new one, and updating import paths; no other code changes are required ^[001a-raw/document/claude code/claude-code-010-agent-sdk-migration-guide-2026-04-29.md]
- Python migration additionally requires renaming `ClaudeCodeOptions` to `ClaudeAgentOptions` and changing imports from `claude_code_sdk` to `claude_agent_sdk` ^[001a-raw/document/claude code/claude-code-010-agent-sdk-migration-guide-2026-04-29.md]
- v0.1.0 introduced three breaking changes: `ClaudeCodeOptions` renamed to `ClaudeAgentOptions`, system prompt no longer defaults to Claude Code's CLI prompt, and filesystem settings are no longer loaded by default ^[001a-raw/document/claude code/claude-code-010-agent-sdk-migration-guide-2026-04-29.md]
- The settings source default has been **reverted** in current releases: omitting `settingSources` once again loads user, project, and local settings, matching the CLI behavior ^[001a-raw/document/claude code/claude-code-010-agent-sdk-migration-guide-2026-04-29.md]
- Python SDK 0.1.59 and earlier treated an empty `setting_sources` list the same as omitting the option; upgrade before relying on `setting_sources=[]` for isolation ^[001a-raw/document/claude code/claude-code-010-agent-sdk-migration-guide-2026-04-29.md]
- The rename reflects the SDK's evolution beyond coding tasks to building all types of AI agents (legal assistants, finance advisors, SRE bots, security reviewers) ^[001a-raw/document/claude code/claude-code-010-agent-sdk-migration-guide-2026-04-29.md]

## Notes

- The system prompt breaking change means SDK applications now get a minimal system prompt by default; to restore the old behavior, explicitly set `systemPrompt: { type: "preset", preset: "claude_code" }` ^[001a-raw/document/claude code/claude-code-010-agent-sdk-migration-guide-2026-04-29.md]
- The settings source breaking change was motivated by CI/CD consistency, deployed application isolation, test reproducibility, and multi-tenant leak prevention, but the default was later reverted ^[001a-raw/document/claude code/claude-code-010-agent-sdk-migration-guide-2026-04-29.md]
- Agent SDK documentation moved from Claude Code docs to the API Guide under a dedicated Agent SDK section; Claude Code docs now focus on the CLI tool and automation features ^[001a-raw/document/claude code/claude-code-010-agent-sdk-migration-guide-2026-04-29.md]

## Related

- [[004-wiki/entities/agent_sdk]]
- [[004-wiki/entities/claude_code]]
- [[004-wiki/concepts/setting_sources]]
- [[004-wiki/concepts/managed_settings]]