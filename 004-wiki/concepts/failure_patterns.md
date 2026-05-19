---
title: "Failure Patterns"
summary: "Common anti-patterns when using Claude Code and their fixes, including kitchen-sink sessions, repeated corrections, over-specified CLAUDE.md, trust-without-verification, and infinite exploration"
type: concept
sources:
  - raw/document/claude code/claude-code-036-best-practices-2026-04-29.md
tags:
  - claude-code
  - anti-patterns
  - debugging
  - best-practices
  - context-management
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Failure Patterns

Common mistakes when using Claude Code that waste time and degrade output quality. Recognizing these patterns early allows course correction before they compound. ^[raw/document/claude code/claude-code-036-best-practices-2026-04-29.md]

## Key Points

- **Kitchen sink session**: Starting with one task, then asking unrelated questions, then returning to the original task; context fills with irrelevant information. Fix: `/clear` between unrelated tasks. ^[raw/document/claude code/claude-code-036-best-practices-2026-04-29.md]
- **Repeated corrections**: Correcting Claude multiple times on the same issue pollutes context with failed approaches. Fix: After two failed corrections, `/clear` and write a better initial prompt incorporating what you learned. ^[raw/document/claude code/claude-code-036-best-practices-2026-04-29.md]
- **Over-specified CLAUDE.md**: Important rules get lost in the noise when CLAUDE.md is too long, causing Claude to ignore actual instructions. Fix: Ruthlessly prune; if Claude does something correctly without the instruction, delete it or convert it to a hook. ^[raw/document/claude code/claude-code-036-best-practices-2026-04-29.md]
- **Trust-without-verification**: Claude produces plausible-looking implementations that don't handle edge cases. Fix: Always provide verification — tests, scripts, screenshots. If you can't verify it, don't ship it. ^[raw/document/claude code/claude-code-036-best-practices-2026-04-29.md]
- **Infinite exploration**: Asking Claude to "investigate" without scoping it, causing Claude to read hundreds of files and fill context. Fix: Scope investigations narrowly or use subagents. ^[raw/document/claude code/claude-code-036-best-practices-2026-04-29.md]

## Details

These five patterns all relate to the fundamental constraint of context window capacity. Kitchen sink sessions and infinite exploration waste context on irrelevant information. Repeated corrections fill context with failed approaches that bias future responses. Over-specified CLAUDE.md files dilute important instructions. Trust-without-verification produces plausible but incorrect output that requires human intervention to catch. ^[raw/document/claude code/claude-code-036-best-practices-2026-04-29.md]

The `/clear` command is the primary recovery mechanism for most of these patterns. Starting a fresh session with a better prompt that incorporates lessons from the failed session is more effective than continuing in a polluted context. For the trust-without-verification pattern, the fix is structural: always pair implementation with verification criteria that give Claude an objective pass/fail signal. ^[raw/document/claude code/claude-code-036-best-practices-2026-04-29.md]

## Related

- [[entities/claude_code]]
- [[concepts/context_window]]
- [[concepts/verification]]
- [[concepts/subagents]]
- [[concepts/explore_plan_code]]