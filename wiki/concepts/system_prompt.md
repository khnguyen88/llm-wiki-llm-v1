---
title: "System Prompt"
summary: "The initial instruction set in the Agent SDK that shapes Claude's behavior, tools, and response style, customizable via four methods with varying persistence and control levels"
type: concept
sources:
  - raw/document/claude code/claude-code-011-agent-sdk-modifying-system-prompts-2026-04-29.md
  - raw/document/claude code/claude-code-045-cli-reference-2026-04-29.md
tags:
  - agent-sdk
  - system-prompt
  - configuration
  - customization
  - cli
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: merged
---

# System Prompt

The initial instruction set that shapes how Claude behaves throughout a conversation. In the Agent SDK, the default system prompt is minimal — it contains only essential tool instructions and omits Claude Code's coding guidelines, response style, and project context. The full Claude Code system prompt is available as an opt-in preset. ^[raw/document/claude code/claude-code-011-agent-sdk-modifying-system-prompts-2026-04-29.md]

## Key Points

- The default Agent SDK system prompt is minimal (essential tool instructions only); the full Claude Code system prompt must be explicitly requested via `systemPrompt: { type: "preset", preset: "claude_code" }` ^[raw/document/claude code/claude-code-011-agent-sdk-modifying-system-prompts-2026-04-29.md]
- The full Claude Code system prompt includes tool usage instructions, code style guidelines, response tone settings, security instructions, and environment context ^[raw/document/claude code/claude-code-011-agent-sdk-modifying-system-prompts-2026-04-29.md]
- Four modification methods exist, ranked by control level: CLAUDE.md (additions only), output styles (replace default style), systemPrompt with append (additions to preset), and custom systemPrompt (complete replacement) ^[raw/document/claude code/claude-code-011-agent-sdk-modifying-system-prompts-2026-04-29.md]
- Custom systemPrompt strings lose built-in tool instructions, safety instructions, and environment context unless manually included ^[raw/document/claude code/claude-code-011-agent-sdk-modifying-system-prompts-2026-04-29.md]
- `excludeDynamicSections: true` moves per-session context (working directory, git status, date, auto-memory paths) from the system prompt to the first user message, enabling cross-session cache reuse at the cost of marginally weaker environment context ^[raw/document/claude code/claude-code-011-agent-sdk-modifying-system-prompts-2026-04-29.md]
- Four CLI flags control the system prompt: `--system-prompt` replaces the entire default prompt with custom text, `--system-prompt-file` replaces it with file contents, `--append-system-prompt` appends custom text to the default prompt, and `--append-system-prompt-file` appends file contents to the default prompt ^[raw/document/claude code/claude-code-045-cli-reference-2026-04-29.md]
- `--system-prompt` and `--system-prompt-file` are mutually exclusive; the append flags can be combined with either replacement flag ^[raw/document/claude code/claude-code-045-cli-reference-2026-04-29.md]
- `--exclude-dynamic-system-prompt-sections` (CLI) moves per-machine sections (working directory, environment info, memory paths, git status) from the system prompt into the first user message, improving prompt-cache reuse across different users and machines running the same task; only applies with the default system prompt and is ignored when `--system-prompt` or `--system-prompt-file` is set ^[raw/document/claude code/claude-code-045-cli-reference-2026-04-29.md]
- For most use cases, append flags are preferred because they preserve Claude Code's built-in capabilities; replacement flags should only be used when complete control over the system prompt is needed ^[raw/document/claude code/claude-code-045-cli-reference-2026-04-29.md]

## Details

The system prompt in the Agent SDK is structured as a layered composition. The base layer is the minimal default, which includes only the essential tool instructions needed for Claude to function. The `claude_code` preset layer adds coding guidelines, response style, security instructions, and environment context on top of this base. Additional layers can be contributed by CLAUDE.md files (loaded via setting sources), output styles (file-based configurations), and the `append` field on the preset object.

The `append` approach preserves all built-in functionality while adding custom instructions. It is the recommended middle ground when the default behavior is mostly correct but needs domain-specific additions. In contrast, a custom `systemPrompt` string replaces everything, giving complete control but requiring the author to manually include any tool instructions, safety guidelines, or environment context that the agent needs.

The `excludeDynamicSections` flag addresses a specific caching problem: the `claude_code` preset embeds per-session context (working directory, platform, date, git status, auto-memory paths) in the system prompt before the `append` text. Any difference in this context produces a different system prompt and a cache miss. By moving this dynamic content to the first user message, identical preset-plus-append configurations can share a cache entry across users, machines, and directories. The tradeoff is that instructions in the user message carry marginally less weight than the same text in the system prompt. ^[raw/document/claude code/claude-code-011-agent-sdk-modifying-system-prompts-2026-04-29.md]

## Related

- [[entities/agent_sdk]]
- [[concepts/output_styles]]
- [[concepts/setting_sources]]
- [[concepts/prompt_caching]]
- [[summaries/claude-code-cli-reference]]