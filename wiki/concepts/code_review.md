---
title: "Code Review"
summary: "Automated PR review feature in Claude Code that uses multi-agent analysis to detect logic errors, security vulnerabilities, and regressions, posting findings as inline GitHub comments with severity levels"
type: concept
sources:
  - raw/document/claude code/claude-code-046-code-review-2026-04-29.md
  - raw/document/claude code/claude-code-113-ultrareview-2026-04-29.md
tags:
  - claude-code
  - code-review
  - github
  - ci-cd
  - automation
  - severity
created: "2026-05-01T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Code Review

Automated PR review feature in Claude Code that uses a fleet of specialized agents to analyze diffs and surrounding code in parallel, detect issues, and post findings as inline GitHub comments. The feature is in research preview and available for Team and Enterprise subscriptions. ^[raw/document/claude code/claude-code-046-code-review-2026-04-29.md]

## Key Points

- Multiple agents analyze the diff and surrounding code in parallel on Anthropic infrastructure; a verification step checks candidates against actual code behavior to filter false positives before findings are posted ^[raw/document/claude code/claude-code-046-code-review-2026-04-29.md]
- Three severity levels: Important (bugs that should be fixed before merging), Nit (minor issues worth fixing but not blocking), and Pre-existing (bugs that exist in the codebase but were not introduced by the PR) ^[raw/document/claude code/claude-code-046-code-review-2026-04-29.md]
- Review triggers are configurable per repository: once after PR creation, after every push, or manual only; manual triggers use `@claude review` (subscribes to future pushes) or `@claude review once` (one-shot) as top-level PR comments ^[raw/document/claude code/claude-code-046-code-review-2026-04-29.md]
- REVIEW.md at the repository root overrides review behavior as highest-priority instruction injected into every review agent; CLAUDE.md rules are treated as project context with violations flagged as nits ^[raw/document/claude code/claude-code-046-code-review-2026-04-29.md]
- The check run always completes with a neutral conclusion so it never blocks merging through branch protection rules; a machine-readable severity breakdown is available for custom CI gating via `gh api` ^[raw/document/claude code/claude-code-046-code-review-2026-04-29.md]
- Reviews average $15-25 in cost and about 20 minutes to complete, scaling with PR size, codebase complexity, and issue verification depth ^[raw/document/claude code/claude-code-046-code-review-2026-04-29.md]
- Code Review posts findings as inline GitHub comments on the PR itself, unlike [[concepts/ultrareview|ultrareview]] which returns findings in the CLI session ^[raw/document/claude code/claude-code-113-ultrareview-2026-04-29.md]

## Details

### How Reviews Work

When a review runs, multiple agents analyze the diff and surrounding code in parallel on Anthropic infrastructure. Each agent looks for a different class of issue, then a verification step checks candidates against actual code behavior to filter false positives. Results are deduplicated, ranked by severity, and posted as inline comments on the specific lines where issues were found, with a summary in the review body. If no issues are found, Claude posts a short confirmation comment. ^[raw/document/claude code/claude-code-046-code-review-2026-04-29.md]

### Severity Levels and Check Run Output

Each finding is tagged with a severity marker: Important, Nit, or Pre-existing. Beyond inline comments, each review populates the **Claude Code Review** check run that appears alongside CI checks. The check run Details link shows a severity table listing every finding with file, line, and summary. Findings also appear as annotations in the Files changed tab. The machine-readable severity line at the end of the Details text can be parsed with `gh api` and `jq` to extract a JSON object with counts per severity level. ^[raw/document/claude code/claude-code-046-code-review-2026-04-29.md]

### Customization with REVIEW.md

REVIEW.md is freeform markdown injected verbatim into every review agent's system prompt as the highest-priority instruction block. The `@` import syntax is not expanded in REVIEW.md. Key tuning areas include: redefining severity (what counts as Important vs. Nit), capping nit volume, defining skip rules for paths and finding categories, adding repo-specific checks, setting verification bars for evidence requirements, controlling re-review convergence behavior, and shaping the summary format. ^[raw/document/claude code/claude-code-046-code-review-2026-04-29.md]

### Manual Triggers

Two comment commands trigger reviews on demand regardless of configured trigger mode: `@claude review` starts a review and subscribes the PR to push-triggered reviews going forward; `@claude review once` starts a single review without subscribing. Both require owner, member, or collaborator access and must be posted as top-level PR comments. Unlike automatic triggers, manual triggers run on draft PRs. If a review is already running, the request is queued. ^[raw/document/claude code/claude-code-046-code-review-2026-04-29.md]

### Pricing and Troubleshooting

Code Review is billed based on token usage, averaging $15-25 per review, billed separately through extra usage. A monthly spend cap can be configured at `claude.ai/admin-settings/usage`. Failed or timed-out reviews never block PRs and can be retriggered with `@claude review once` or a new push; GitHub's Re-run button does not retrigger Code Review. When the spend cap is reached, a single comment is posted explaining the review was skipped; reviews resume at the next billing period or when the cap is raised. ^[raw/document/claude code/claude-code-046-code-review-2026-04-29.md]

## Related

- [[entities/claude_code]]
- [[entities/github]]
- [[concepts/claude_directory]]
- [[concepts/verification]]
- [[concepts/auto_fix]]
- [[concepts/ultrareview]]