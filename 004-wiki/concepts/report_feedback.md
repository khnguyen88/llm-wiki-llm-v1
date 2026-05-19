---
title: "Report Feedback"
summary: "OpenRouter feature for flagging problematic AI generations by category to improve model routing and platform quality"
type: concept
sources:
  - raw/document/openrouter/openrouter-016-guides-overview-report-feedback-2026-04-29.md
tags:
  - openrouter
  - feedback
  - quality
  - user-reporting
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Report Feedback

A feature on [[entities/openrouter|OpenRouter]] that allows users to flag problematic AI generations with a category and description, helping the team identify and address issues with model responses, latency, billing, and more. ^[raw/document/openrouter/openrouter-016-guides-overview-report-feedback-2026-04-29.md]

## Key Points

- Six structured feedback categories: Latency, Incoherence, Incorrect Response, Formatting, Billing, and API Error, plus an Other catch-all ^[raw/document/openrouter/openrouter-016-guides-overview-report-feedback-2026-04-29.md]
- Chatroom reporting: hover over an assistant message, click the bug icon, select a category, add a comment, and submit — the generation ID is captured automatically ^[raw/document/openrouter/openrouter-016-guides-overview-report-feedback-2026-04-29.md]
- Activity page reporting: per-generation via the row-level bug icon, or general via the header "Report Feedback" button with a manually entered generation ID ^[raw/document/openrouter/openrouter-016-guides-overview-report-feedback-2026-04-29.md]
- Generation IDs come from the API response `id` field or from Activity page row details ^[raw/document/openrouter/openrouter-016-guides-overview-report-feedback-2026-04-29.md]
- Submitted feedback is reviewed by the OpenRouter team to improve model routing, provider selection, error handling, billing accuracy, and platform reliability ^[raw/document/openrouter/openrouter-016-guides-overview-report-feedback-2026-04-29.md]

## Details

The feature provides two entry points: the Chatroom (for immediate, in-context reporting on a specific message) and the Activity page (for batch or retrospective reporting using generation IDs). The Chatroom path automatically associates the feedback with the correct generation, while the Activity page supports both per-row and manual generation ID submission.

Feedback categories cover the full range of generation issues: Latency (slow responses), Incoherence (off-topic or nonsensical output), Incorrect Response (factual errors), Formatting (markdown or code block issues), Billing (unexpected charges or token counts), and API Error (technical failures).

## Related

- [[entities/openrouter]]
- [[concepts/provider_fallback]]
- [[concepts/llm_gateway]]
- [[concepts/rate_limiting]]