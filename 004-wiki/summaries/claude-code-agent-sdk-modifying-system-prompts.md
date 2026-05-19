---
title: "Claude Code Agent SDK Modifying System Prompts"
summary: "Four methods for customizing Claude's behavior via system prompts: CLAUDE.md files, output styles, systemPrompt with append, and custom systemPrompt"
type: summary
sources:
  - raw/document/claude code/claude-code-011-agent-sdk-modifying-system-prompts-2026-04-29.md
tags:
  - agent-sdk
  - system-prompt
  - output-styles
  - claude-md
  - prompt-caching
  - configuration
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Claude Code Agent SDK Modifying System Prompts

## Key Points

- The Agent SDK uses a minimal system prompt by default containing only essential tool instructions; the full Claude Code system prompt (with coding guidelines, response style, security instructions) is opt-in via `systemPrompt: { type: "preset", preset: "claude_code" }` ^[raw/document/claude code/claude-code-011-agent-sdk-modifying-system-prompts-2026-04-29.md]
- Four methods exist for modifying system prompts: CLAUDE.md files (project-level, persistent), output styles (file-based, reusable across projects), `systemPrompt` with `append` (session-scoped additions to the preset), and custom `systemPrompt` strings (complete replacement) ^[raw/document/claude code/claude-code-011-agent-sdk-modifying-system-prompts-2026-04-29.md]
- CLAUDE.md loading is controlled by `settingSources` (`setting_sources` in Python), not by the `claude_code` preset; project-level CLAUDE.md loads when `"project"` is enabled and user-level when `"user"` is enabled ^[raw/document/claude code/claude-code-011-agent-sdk-modifying-system-prompts-2026-04-29.md]
- Output styles are markdown files stored at `~/.claude/output-styles` (user-level) or `.claude/output-styles` (project-level) with frontmatter containing `name` and `description`; they load when `settingSources` includes `"user"` or `"project"` ^[raw/document/claude code/claude-code-011-agent-sdk-modifying-system-prompts-2026-04-29.md]
- `excludeDynamicSections: true` moves per-session context (working directory, git status, date, auto-memory paths) from the system prompt into the first user message, enabling cross-session prompt cache reuse across different directories and machines ^[raw/document/claude code/claude-code-011-agent-sdk-modifying-system-prompts-2026-04-29.md]
- Custom `systemPrompt` strings replace the default prompt entirely, losing built-in tool instructions, safety instructions, and environment context unless manually included ^[raw/document/claude code/claude-code-011-agent-sdk-modifying-system-prompts-2026-04-29.md]
- The four approaches can be combined; for example, an output style can be active while `systemPrompt` with `append` adds session-specific instructions ^[raw/document/claude code/claude-code-011-agent-sdk-modifying-system-prompts-2026-04-29.md]

## Quotes

- "The Agent SDK uses a minimal system prompt by default. It contains only essential tool instructions but omits Claude Code's coding guidelines, response style, and project context." ^[raw/document/claude code/claude-code-011-agent-sdk-modifying-system-prompts-2026-04-29.md]
- "Instructions in the user message carry marginally less weight than the same text in the system prompt, so Claude may rely on them less strongly when reasoning about the current directory or auto-memory paths." ^[raw/document/claude code/claude-code-011-agent-sdk-modifying-system-prompts-2026-04-29.md]

## Notes

- `excludeDynamicSections` requires `@anthropic-ai/claude-agent-sdk` v0.2.98+ (TypeScript) or `claude-agent-sdk` v0.1.58+ (Python) and applies only to the preset object form
- The CLI equivalent of `excludeDynamicSections` is the `--exclude-dynamic-system-prompt-sections` flag

## Related

- [[entities/agent_sdk]]
- [[entities/claude_code]]
- [[concepts/system_prompt]]
- [[concepts/output_styles]]
- [[concepts/setting_sources]]
- [[concepts/prompt_caching]]