---
title: "Openrouter Guides Overview Report Feedback"
summary: "OpenRouter's Report Feedback feature lets users flag problematic AI generations by category from the Chatroom or Activity page, helping improve model routing and platform reliability"
type: summary
sources:
  - raw/document/openrouter/openrouter-016-guides-overview-report-feedback-2026-04-29.md
tags:
  - openrouter
  - feedback
  - user-reporting
  - quality
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Openrouter Guides Overview Report Feedback

## Key Points

- Report Feedback allows users to flag problematic AI generations with a category and description, helping OpenRouter improve model responses, latency, billing, and overall reliability ^[raw/document/openrouter/openrouter-016-guides-overview-report-feedback-2026-04-29.md]
- Six feedback categories: Latency, Incoherence, Incorrect Response, Formatting, Billing, and API Error, plus an Other catch-all ^[raw/document/openrouter/openrouter-016-guides-overview-report-feedback-2026-04-29.md]
- From the Chatroom, hover over an assistant message and click the bug icon; the generation ID is automatically captured ^[raw/document/openrouter/openrouter-016-guides-overview-report-feedback-2026-04-29.md]
- From the Activity page, report per-generation via the row-level bug icon, or use the header "Report Feedback" button with a manually entered generation ID ^[raw/document/openrouter/openrouter-016-guides-overview-report-feedback-2026-04-29.md]
- The generation ID is returned in the API response under the `id` field and is also visible in Activity page row details ^[raw/document/openrouter/openrouter-016-guides-overview-report-feedback-2026-04-29.md]
- Submitted feedback is reviewed by the OpenRouter team to improve model routing, provider selection, error handling, billing accuracy, and platform reliability ^[raw/document/openrouter/openrouter-016-guides-overview-report-feedback-2026-04-29.md]

## Notes

- This is a user-facing quality improvement mechanism, not a real-time support channel.

## Related

- [[entities/openrouter]]
- [[concepts/report_feedback]]
- [[concepts/provider_fallback]]
- [[concepts/llm_gateway]]