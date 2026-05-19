---
title: "Verification"
summary: "Providing Claude with tests, screenshots, or expected outputs so it can validate its own work — identified as the single highest-leverage practice for effective Claude Code usage"
type: concept
sources:
  - raw/document/claude code/claude-code-036-best-practices-2026-04-29.md
tags:
  - claude-code
  - verification
  - testing
  - best-practices
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Verification

Providing Claude with ways to check its own work is the single highest-leverage practice for effective Claude Code usage. Without verification criteria, Claude may produce output that appears correct but contains subtle bugs or misses edge cases. ^[raw/document/claude code/claude-code-036-best-practices-2026-04-29.md]

## Key Points

- Verification is the single highest-leverage practice: include tests, screenshots, or expected outputs so Claude can check itself ^[raw/document/claude code/claude-code-036-best-practices-2026-04-29.md]
- Provide specific test cases with inputs and expected outputs rather than vague instructions like "add tests" ^[raw/document/claude code/claude-code-036-best-practices-2026-04-29.md]
- For UI changes, provide a reference screenshot and ask Claude to take a screenshot of its result, compare the two, and list differences ^[raw/document/claude code/claude-code-036-best-practices-2026-04-29.md]
- Address root causes rather than symptoms: provide the actual error message and ask Claude to fix the underlying issue, not suppress it ^[raw/document/claude code/claude-code-036-best-practices-2026-04-29.md]
- Verification can be a test suite, a linter, or a Bash command that checks output — anything that gives Claude an objective pass/fail signal ^[raw/document/claude code/claude-code-036-best-practices-2026-04-29.md]

## Details

The verification pattern transforms Claude from a system that produces code and waits for human review into one that can iteratively improve its output. When Claude can run tests and see failures, it can fix them. When it can take screenshots and compare them to a reference, it can adjust styling. When it can run a linter and see errors, it can correct them. Without this feedback loop, the human becomes the only verification mechanism, and every mistake requires human attention. ^[raw/document/claude code/claude-code-036-best-practices-2026-04-29.md]

The Claude in Chrome extension enables visual verification for UI changes by opening new tabs, testing the UI, and iterating until the implementation matches the reference design. Verification can also be a command-line tool, a build script, or any automated check that produces a clear pass/fail result. ^[raw/document/claude code/claude-code-036-best-practices-2026-04-29.md]

## Related

- [[entities/claude_code]]
- [[concepts/explore_plan_code]]
- [[concepts/failure_patterns]]