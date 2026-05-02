---
title: "Context Window"
summary: "The total information available to an LLM during a session, including system prompts, tool definitions, conversation history, and tool outputs, with automatic compaction when capacity is exceeded"
type: concept
sources:
  - raw/document/claude code/claude-code-002-agent-sdk-agent-loop-2026-04-29.md
  - raw/document/claude code/claude-code-036-best-practices-2026-04-29.md
  - raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md
  - raw/document/claude code/claude-code-051-context-window-2026-04-29.md
  - raw/document/claude code/claude-code-105-statusline-2026-04-29.md
tags:
  - context-window
  - claude-code
  - agent-sdk
  - compaction
  - token-management
  - path-scoped-rules
  - statusline
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: merged
---

# Context Window

The total amount of information available to a model during a session. The context window does not reset between turns — everything accumulates: system prompt, tool definitions, conversation history, tool inputs, and tool outputs. ^[raw/document/claude code/claude-code-002-agent-sdk-agent-loop-2026-04-29.md]

## Key Points

- Context accumulates across turns within a session; it does not reset between tool calls ^[raw/document/claude code/claude-code-002-agent-sdk-agent-loop-2026-04-29.md]
- Content that stays the same across turns (system prompt, tool definitions, CLAUDE.md) is automatically prompt cached, reducing cost and latency for repeated prefixes ^[raw/document/claude code/claude-code-002-agent-sdk-agent-loop-2026-04-29.md]
- Major context consumers: system prompt (small fixed cost), CLAUDE.md files (full content every request but cached), tool definitions (each tool adds its schema), conversation history (grows with each turn), and skill descriptions (short summaries, full content loads on invocation) ^[raw/document/claude code/claude-code-002-agent-sdk-agent-loop-2026-04-29.md]
- When the context window approaches its limit, the SDK automatically compacts older conversation history into summaries, preserving recent exchanges and key decisions ^[raw/document/claude code/claude-code-002-agent-sdk-agent-loop-2026-04-29.md]
- Compaction can be customized via summarization instructions in CLAUDE.md, PreCompact hooks, or manual `/compact` commands ^[raw/document/claude code/claude-code-002-agent-sdk-agent-loop-2026-04-29.md]
- Use `/clear` frequently between unrelated tasks to reset the context window entirely; long sessions with irrelevant context reduce performance ^[raw/document/claude code/claude-code-036-best-practices-2026-04-29.md]
- Run `/compact <instructions>` to customize what compaction preserves, e.g., `/compact Focus on the API changes` ^[raw/document/claude code/claude-code-036-best-practices-2026-04-29.md]
- Use `/btw` for quick questions that don't need to stay in context; the answer appears in a dismissible overlay and never enters conversation history ^[raw/document/claude code/claude-code-036-best-practices-2026-04-29.md]
- Track context usage continuously with a custom status line ^[raw/document/claude code/claude-code-036-best-practices-2026-04-29.md]
- Extended thinking uses context tokens for internal reasoning; on supported models, adaptive reasoning dynamically allocates thinking tokens based on effort level; thinking tokens are charged even when summaries are redacted ^[raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]
- Before any user input, the context window pre-fills with CLAUDE.md, auto memory, MCP tool names, skill descriptions, output style, and `--append-system-prompt` text — all entering the system prompt the same way ^[raw/document/claude code/claude-code-051-context-window-2026-04-29.md]
- As work proceeds, each file read adds tokens; path-scoped rules load automatically alongside matching files, and PostToolUse hooks fire after each edit ^[raw/document/claude code/claude-code-051-context-window-2026-04-29.md]
- Subagents handle research in separate context windows; only the summary and a small metadata trailer return to the parent, keeping large file reads out of the main session ^[raw/document/claude code/claude-code-051-context-window-2026-04-29.md]
- After compaction, system prompt and output style are unchanged (not part of message history), project-root CLAUDE.md and unscoped rules are re-injected from disk, auto memory is re-injected from disk, but path-scoped rules and nested CLAUDE.md files are lost until their trigger files are read again ^[raw/document/claude code/claude-code-051-context-window-2026-04-29.md]
- Invoked skill bodies are re-injected after compaction, capped at 5,000 tokens per skill and 25,000 tokens total; oldest invoked skills are dropped first when the total budget is exceeded ^[raw/document/claude code/claude-code-051-context-window-2026-04-29.md]
- Hooks are unaffected by compaction because they execute as code outside the context window, not as context content ^[raw/document/claude code/claude-code-051-context-window-2026-04-29.md]
- Run `/context` for a live breakdown of context usage by category with optimization suggestions ^[raw/document/claude code/claude-code-051-context-window-2026-04-29.md]
- Run `/memory` to check which CLAUDE.md and auto memory files loaded at startup ^[raw/document/claude code/claude-code-051-context-window-2026-04-29.md]
- The statusline provides `context_window.used_percentage` (calculated from input tokens only: `input_tokens + cache_creation_input_tokens + cache_read_input_tokens`, excluding output tokens) and `context_window.remaining_percentage` for at-a-glance monitoring ^[raw/document/claude code/claude-code-105-statusline-2026-04-29.md]
- `context_window.current_usage` contains per-call token breakdowns (`input_tokens`, `output_tokens`, `cache_creation_input_tokens`, `cache_read_input_tokens`); it is `null` before the first API call ^[raw/document/claude code/claude-code-105-statusline-2026-04-29.md]
- `exceeds_200k_tokens` indicates whether total tokens from the most recent API response exceed 200k, regardless of actual context window size ^[raw/document/claude code/claude-code-105-statusline-2026-04-29.md]

## Details

Each component in the agent session has a distinct context impact. The system prompt is a small fixed cost present in every request. CLAUDE.md files load in full at session start but benefit from prompt caching. Tool definitions add their schemas to every request, making it important to scope subagents to minimum tool sets and use MCP tool search for on-demand loading rather than preloading all tools. Large tool outputs — reading a big file or running a command with verbose output — can consume thousands of tokens in a single turn. ^[raw/document/claude code/claude-code-002-agent-sdk-agent-loop-2026-04-29.md]

Automatic compaction replaces older messages with a summary, which means specific instructions from early in the conversation may not be preserved. Persistent rules should be placed in CLAUDE.md (loaded via `settingSources`) rather than in the initial prompt, because CLAUDE.md content is re-injected on every request. The SDK emits a system message with `subtype: "compact_boundary"` when compaction occurs; in TypeScript this is a separate `SDKCompactBoundaryMessage` type. ^[raw/document/claude code/claude-code-002-agent-sdk-agent-loop-2026-04-29.md]

Strategies for keeping context efficient include: using subagents for subtasks (each subagent starts with a fresh conversation, and only the final response returns to the parent), being selective with tools, watching MCP server costs (each server adds all its tool schemas to every request), and using lower effort levels for routine tasks. ^[raw/document/claude code/claude-code-002-agent-sdk-agent-loop-2026-04-29.md]

### Compaction Survival

When a long session compacts, conversation history is summarized to fit the context window. What survives depends on how each mechanism was loaded:

| Mechanism | After Compaction |
|---|---|
| System prompt and output style | Unchanged; not part of message history |
| Project-root CLAUDE.md and unscoped rules | Re-injected from disk |
| Auto memory | Re-injected from disk |
| Path-scoped rules (`paths:` frontmatter) | Lost until a matching file is read again |
| Nested CLAUDE.md in subdirectories | Lost until a file in that subdirectory is read again |
| Invoked skill bodies | Re-injected, capped at 5,000 tokens per skill and 25,000 tokens total; oldest dropped first |
| Hooks | Not applicable; run as code, not context |

^[raw/document/claude code/claude-code-051-context-window-2026-04-29.md]

Path-scoped rules and nested CLAUDE.md files load into message history when their trigger file is read, so compaction summarizes them away with everything else. They reload the next time Claude reads a matching file. If a rule must persist across compaction, drop the `paths:` frontmatter or move it to the project-root CLAUDE.md. Skill bodies are re-injected after compaction, but large skills are truncated to fit the per-skill cap; truncation keeps the start of the file, so important instructions should be placed near the top of `SKILL.md`. ^[raw/document/claude code/claude-code-051-context-window-2026-04-29.md]

## Related

- [[entities/agent_sdk]]
- [[entities/claude_code]]
- [[concepts/agent_loop]]
- [[concepts/hooks]]
- [[concepts/failure_patterns]]
- [[concepts/extended_thinking]]
- [[concepts/skills]]
- [[concepts/output_styles]]
- [[summaries/claude-code-best-practices]]
- [[summaries/claude-code-common-workflows]]
- [[summaries/claude-code-context-window]]
- [[concepts/statusline]]