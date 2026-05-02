---
title: "Ultrareview"
summary: "Deep multi-agent code review that runs in a remote cloud sandbox, independently verifying each finding for higher signal and broader coverage than a single-pass local review"
type: concept
sources:
  - raw/document/claude code/claude-code-113-ultrareview-2026-04-29.md
  - raw/document/claude code/claude-code-117-whats-new-2026-04-29.md
tags:
  - claude-code
  - code-review
  - multi-agent
  - cloud
  - verification
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Ultrareview

Ultrareview is a deep code review feature that launches a fleet of reviewer agents in a [[entities/claude_code_web|cloud sandbox]] to find bugs in a branch or pull request. Unlike the local `/review` command, ultrareview independently reproduces and verifies every finding so results focus on real bugs rather than style suggestions. The feature is a public research preview available in Claude Code v2.1.86 and later. ^[raw/document/claude code/claude-code-113-ultrareview-2026-04-29.md] ^[raw/document/claude code/claude-code-117-whats-new-2026-04-29.md]

## Key Points

- Runs remotely on Claude Code on the web infrastructure: the terminal stays free for other work while the review executes ^[raw/document/claude code/claude-code-113-ultrareview-2026-04-29.md]
- Requires Claude.ai account authentication; not available with Amazon Bedrock, Google Vertex AI, Microsoft Foundry, or Zero Data Retention organizations ^[raw/document/claude code/claude-code-113-ultrareview-2026-04-29.md]
- Without arguments, reviews the diff between the current branch and the default branch including uncommitted and staged changes; `/ultrareview 1234` reviews a specific GitHub PR by cloning it in the remote sandbox ^[raw/document/claude code/claude-code-113-ultrareview-2026-04-29.md]
- A `claude ultrareview` subcommand supports non-interactive use for CI and scripts, blocking until completion and printing findings to stdout; supports `--json` for raw payload output and `--timeout <minutes>` to override the 30-minute default ^[raw/document/claude code/claude-code-113-ultrareview-2026-04-29.md]

## Details

### Pricing and Free Runs

Pro and Max subscribers receive three free ultrareview runs as a one-time allotment that does not refresh and expires on May 5, 2026. After the free runs are exhausted or expired, each review costs $5-$20 depending on the change size and is billed as extra usage. Team and Enterprise plans have no free runs and pay per review. Extra usage must be enabled on the account before launching a paid review; `/extra-usage` checks or changes the setting. A review that is stopped early or fails to complete still consumes a free run; paid reviews are billed only for the portion that ran. ^[raw/document/claude code/claude-code-113-ultrareview-2026-04-29.md]

### Tracking and Non-Interactive Mode

Reviews typically take 5-10 minutes and run as background tasks, allowing continued use of the session or even closing the terminal. `/tasks` lists running and completed reviews. When a review finishes, verified findings appear as a notification with file locations and explanations so the user can ask Claude to fix issues directly. ^[raw/document/claude code/claude-code-113-ultrareview-2026-04-29.md]

The `claude ultrareview` subcommand runs non-interactively for CI integration. It blocks until the review completes, prints findings to stdout, and exits with code 0 on success, 1 on failure or timeout, and 130 on Ctrl-C interrupt. The remote review continues running even if the subcommand is interrupted; follow the session URL printed to stderr to monitor it in the browser. Progress messages and the live session URL go to stderr so stdout remains parseable. ^[raw/document/claude code/claude-code-113-ultrareview-2026-04-29.md]

### Comparison with /review

Both `/review` and `/ultrareview` review code but target different stages. `/review` runs locally in the session as a single-pass review in seconds, counted toward normal usage. `/ultrareview` runs remotely with a multi-agent fleet and independent verification in 5-10 minutes, billed as extra usage after free runs. Use `/review` for quick feedback while iterating; use `/ultrareview` before merging a substantial change. ^[raw/document/claude code/claude-code-113-ultrareview-2026-04-29.md]

## Related

- [[entities/claude_code]]
- [[entities/claude_code_web]]
- [[concepts/code_review]]
- [[concepts/non_interactive_mode]]
- [[concepts/ultraplan]]
- [[summaries/claude-code-ultrareview]]