---
title: "Claude Code Ultrareview"
summary: "Deep multi-agent code review running in a cloud sandbox via /ultrareview, offering independently verified findings, broader coverage, and no local resource use"
type: summary
sources:
  - raw/document/claude code/claude-code-113-ultrareview-2026-04-29.md
tags:
  - claude-code
  - code-review
  - cloud
  - multi-agent
  - verification
  - ultrareview
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Claude Code Ultrareview

## Key Points

- Ultrareview runs a fleet of reviewer agents in a remote sandbox to find and verify bugs before merging; every finding is independently reproduced and verified so results focus on real bugs rather than style suggestions ^[raw/document/claude code/claude-code-113-ultrareview-2026-04-29.md]
- Requires Claude Code v2.1.86+ and authentication with a Claude.ai account; not available with Amazon Bedrock, Google Vertex AI, or Microsoft Foundry authentication, nor for organizations with Zero Data Retention ^[raw/document/claude code/claude-code-113-ultrareview-2026-04-29.md]
- Three Pro/Max free runs through May 5, 2026 (one-time, non-refreshing); after free runs or for Team/Enterprise, each review costs $5-$20 billed as extra usage ^[raw/document/claude code/claude-code-113-ultrareview-2026-04-29.md]
- Without arguments reviews the current branch diff plus uncommitted/staged changes; `/ultrareview 1234` reviews a GitHub PR directly from the remote repository ^[raw/document/claude code/claude-code-113-ultrareview-2026-04-29.md]
- Non-interactive `claude ultrareview` subcommand available for CI/scripts, blocking until completion and exiting 0 on success or 1 on failure; supports `--json` and `--timeout <minutes>` flags ^[raw/document/claude code/claude-code-113-ultrareview-2026-04-29.md]
- Reviews take 5-10 minutes, run as background tasks, and findings appear as notifications with file locations and explanations ^[raw/document/claude code/claude-code-113-ultrareview-2026-04-29.md]
- Compared to `/review`: ultrareview runs remotely with multi-agent verification in 5-10 minutes for pre-merge confidence, while `/review` runs locally as a single-pass review in seconds for quick iteration feedback ^[raw/document/claude code/claude-code-113-ultrareview-2026-04-29.md]

## Quotes

- "every reported finding is independently reproduced and verified, so the results focus on real bugs rather than style suggestions" ^[raw/document/claude code/claude-code-113-ultrareview-2026-04-29.md]

## Notes

- The ultrareview confirmation dialog shows review scope, remaining free runs, and estimated cost before launch ^[raw/document/claude code/claude-code-113-ultrareview-2026-04-29.md]
- If the repository is too large to bundle, Claude Code prompts the user to use PR mode instead ^[raw/document/claude code/claude-code-113-ultrareview-2026-04-29.md]
- A stopped review archives the cloud session and partial findings are not returned ^[raw/document/claude code/claude-code-113-ultrareview-2026-04-29.md]
- For automatic PR reviews without a CLI step, [[concepts/code_review|Code Review]] integrates directly with repositories and posts findings as inline PR comments ^[raw/document/claude code/claude-code-113-ultrareview-2026-04-29.md]

## Related

- [[concepts/ultrareview]]
- [[entities/claude_code]]
- [[entities/claude_code_web]]
- [[concepts/code_review]]
- [[concepts/non_interactive_mode]]
- [[concepts/ultraplan]]