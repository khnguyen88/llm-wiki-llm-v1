---
title: "Output Styles"
summary: "File-based, reusable system prompt configurations in the Agent SDK stored as markdown files with frontmatter, activatable via CLI or settings"
type: concept
sources:
  - raw/document/claude code/claude-code-011-agent-sdk-modifying-system-prompts-2026-04-29.md
tags:
  - agent-sdk
  - output-styles
  - configuration
  - system-prompt
  - customization
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Output Styles

Saved configurations that modify Claude's system prompt, stored as markdown files and reusable across sessions and projects. They allow persistent behavior changes without modifying code. ^[raw/document/claude code/claude-code-011-agent-sdk-modifying-system-prompts-2026-04-29.md]

## Key Points

- Output styles are markdown files with YAML frontmatter containing `name` and `description` fields, plus prompt content in the body ^[raw/document/claude code/claude-code-011-agent-sdk-modifying-system-prompts-2026-04-29.md]
- User-level styles live at `~/.claude/output-styles/`; project-level styles at `.claude/output-styles/` ^[raw/document/claude code/claude-code-011-agent-sdk-modifying-system-prompts-2026-04-29.md]
- Activated via CLI (`/output-style [style-name]`), settings (`.claude/settings.local.json`), or by creating new ones (`/output-style:new [description]`) ^[raw/document/claude code/claude-code-011-agent-sdk-modifying-system-prompts-2026-04-29.md]
- SDK users access output styles by including `settingSources: ['user']` or `settingSources: ['project']` in options ^[raw/document/claude code/claude-code-011-agent-sdk-modifying-system-prompts-2026-04-29.md]
- Best suited for persistent behavior changes across sessions, team-shared configurations, and specialized assistants (code reviewer, data scientist, DevOps) ^[raw/document/claude code/claude-code-011-agent-sdk-modifying-system-prompts-2026-04-29.md]

## Details

Output styles fill a niche between CLAUDE.md (project-scoped, additions only) and programmatic `systemPrompt` modification (session-scoped, code-defined). They are file-based like CLAUDE.md but can apply across projects, and they replace the default response style rather than merely appending to it. This makes them suitable for creating specialized assistant personas that persist across sessions without duplicating code.

The filename convention is the style name lowercased with spaces replaced by hyphens (e.g., "Code Reviewer" becomes `code-reviewer.md`). Because they load through setting sources, output styles are not available when `settingSources` is set to an empty array or when the relevant source type is omitted. ^[raw/document/claude code/claude-code-011-agent-sdk-modifying-system-prompts-2026-04-29.md]

## Related

- [[entities/agent_sdk]]
- [[concepts/system_prompt]]
- [[concepts/setting_sources]]