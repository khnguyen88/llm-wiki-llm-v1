---
title: "Claude Code Best Practices"
summary: "Guidance for effective Claude Code usage covering verification, workflow, context management, scaling, and common failure patterns"
type: summary
sources:
  - raw/document/claude code/claude-code-036-best-practices-2026-04-29.md
tags:
  - claude-code
  - best-practices
  - context-management
  - verification
  - workflow
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Claude Code Best Practices

Guidance from Anthropic on effective Claude Code usage, organized around the fundamental constraint that context window capacity degrades performance as it fills. ^[001a-raw/document/claude code/claude-code-036-best-practices-2026-04-29.md]

## Key Points

- Verification is the single highest-leverage practice: provide tests, screenshots, or expected outputs so Claude can check its own work ^[001a-raw/document/claude code/claude-code-036-best-practices-2026-04-29.md]
- Separate exploration from implementation using Plan Mode; planning is most useful when the approach is uncertain, the change touches multiple files, or you are unfamiliar with the code ^[001a-raw/document/claude code/claude-code-036-best-practices-2026-04-29.md]
- Context window management is critical: use `/clear` between unrelated tasks, `/compact` with instructions to preserve specific context, and `/btw` for quick questions that don't need to persist ^[001a-raw/document/claude code/claude-code-036-best-practices-2026-04-29.md]
- Subagents preserve context by running investigation in a separate context window, returning only summaries to the main conversation ^[001a-raw/document/claude code/claude-code-036-best-practices-2026-04-29.md]
- Three ways to reduce permission interruptions: auto mode (classifier handles approvals), permission allowlists (permit specific safe commands), and sandboxing (OS-level isolation) ^[001a-raw/document/claude code/claude-code-036-best-practices-2026-04-29.md]
- Common failure patterns include kitchen-sink sessions, repeated corrections, over-specified CLAUDE.md, trust-without-verification, and infinite exploration ^[001a-raw/document/claude code/claude-code-036-best-practices-2026-04-29.md]
- Scale work with non-interactive mode (`claude -p`), parallel sessions, and fan-out patterns across files ^[001a-raw/document/claude code/claude-code-036-best-practices-2026-04-29.md]

## Quotes

> "Claude performs dramatically better when it can verify its own work, like run tests, compare screenshots, and validate outputs. Without clear success criteria, it might produce something that looks right but actually doesn't work." ^[001a-raw/document/claude code/claude-code-036-best-practices-2026-04-29.md]

> "Most best practices are based on one constraint: Claude's context window fills up fast, and performance degrades as it fills." ^[001a-raw/document/claude code/claude-code-036-best-practices-2026-04-29.md]

> "After two failed corrections, /clear and write a better initial prompt incorporating what you learned. A clean session with a better prompt almost always outperforms a long session with accumulated corrections." ^[001a-raw/document/claude code/claude-code-036-best-practices-2026-04-29.md]

## Notes

- The document emphasizes that context management is the fundamental constraint; most best practices derive from keeping context clean and relevant
- CLAUDE.md should be ruthlessly pruned: if Claude already does something correctly without the instruction, delete it or convert it to a hook
- Skills are preferred over CLAUDE.md for domain-specific knowledge because they load on demand rather than consuming context every session
- Hooks are deterministic and guarantee actions, unlike CLAUDE.md instructions which are advisory

## Related

- [[004-wiki/entities/claude-code]]
- [[004-wiki/concepts/verification]]
- [[004-wiki/concepts/explore-plan-code]]
- [[004-wiki/concepts/context-window]]
- [[004-wiki/concepts/auto-mode]]
- [[004-wiki/concepts/permissions]]
- [[004-wiki/concepts/hooks]]
- [[004-wiki/concepts/skills]]
- [[004-wiki/concepts/subagents]]
- [[004-wiki/concepts/sessions]]
- [[004-wiki/concepts/file-checkpointing]]
- [[004-wiki/concepts/non-interactive-mode]]
- [[004-wiki/concepts/parallel-sessions]]
- [[004-wiki/concepts/fan-out]]
- [[004-wiki/concepts/failure-patterns]]
- [[004-wiki/concepts/mcp]]
- [[004-wiki/concepts/plugins]]