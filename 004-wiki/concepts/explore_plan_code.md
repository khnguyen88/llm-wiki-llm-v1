---
title: "Explore-Plan-Code"
summary: "A four-phase workflow for Claude Code that separates research and planning from implementation to avoid solving the wrong problem"
type: concept
sources:
  - raw/document/claude code/claude-code-036-best-practices-2026-04-29.md
tags:
  - claude-code
  - workflow
  - planning
  - best-practices
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Explore-Plan-Code

A four-phase workflow that separates research and planning from implementation to avoid solving the wrong problem. Letting Claude jump straight to coding can produce code that solves the wrong problem. ^[raw/document/claude code/claude-code-036-best-practices-2026-04-29.md]

## Key Points

- The four phases are: Explore (read files, ask questions in Plan Mode), Plan (create a detailed implementation plan), Implement (code in Normal Mode against the plan), and Commit (commit and create PR) ^[raw/document/claude code/claude-code-036-best-practices-2026-04-29.md]
- Planning is most useful when the approach is uncertain, the change touches multiple files, or you are unfamiliar with the code; skip planning for small, clear-scope tasks ^[raw/document/claude code/claude-code-036-best-practices-2026-04-29.md]
- If you could describe the diff in one sentence, skip the plan ^[raw/document/claude code/claude-code-036-best-practices-2026-04-29.md]
- Press Ctrl+G to open the plan in a text editor for direct editing before Claude proceeds ^[raw/document/claude code/claude-code-036-best-practices-2026-04-29.md]
- Vague prompts can be useful for exploration when you can afford to course-correct; a prompt like "what would you improve in this file?" can surface insights you wouldn't have thought to ask about ^[raw/document/claude code/claude-code-036-best-practices-2026-04-29.md]

## Details

The workflow is structured around the insight that implementation without understanding produces wrong solutions. In the Explore phase, Claude reads relevant files and answers questions without making changes. In the Plan phase, Claude creates a detailed implementation plan that identifies which files need to change and what the session flow looks like. In the Implement phase, Claude switches to Normal Mode and codes against the plan, verifying its work against the expected outcomes. Finally, in the Commit phase, Claude commits with a descriptive message and optionally creates a PR. ^[raw/document/claude code/claude-code-036-best-practices-2026-04-29.md]

Planning adds overhead, so it should be used selectively. For tasks where the scope is clear and the fix is small — like fixing a typo, adding a log line, or renaming a variable — asking Claude to do it directly is more efficient. The key judgment call is whether the cost of planning is justified by the risk of solving the wrong problem. ^[raw/document/claude code/claude-code-036-best-practices-2026-04-29.md]

## Related

- [[entities/claude_code]]
- [[concepts/verification]]
- [[concepts/context_window]]
- [[concepts/failure_patterns]]