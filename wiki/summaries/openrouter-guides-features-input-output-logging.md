---
title: "Openrouter Guides Features Input Output Logging"
summary: "OpenRouter's Input & Output Logging feature lets users privately save and review full request/response content for debugging and prompt optimization, with data encrypted in isolated Google Cloud Storage"
type: summary
sources:
  - raw/document/openrouter/openrouter-048-guides-features-input-output-logging-2026-04-29.md
tags:
  - openrouter
  - logging
  - observability
  - privacy
  - debugging
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Openrouter Guides Features Input Output Logging

## Key Points

- Input & Output Logging privately saves full request and response content for debugging, response comparison, and prompt optimization ^[raw/document/openrouter/openrouter-048-guides-features-input-output-logging-2026-04-29.md]
- Currently in Beta ^[raw/document/openrouter/openrouter-048-guides-features-input-output-logging-2026-04-29.md]
- Enabled via Observability settings toggle; only organization admins can toggle it for org accounts ^[raw/document/openrouter/openrouter-048-guides-features-input-output-logging-2026-04-29.md]
- Stored content viewable from the Logs page with Prompt and Completion tabs; generation detail view also shows model, provider, token counts, and cost ^[raw/document/openrouter/openrouter-048-guides-features-input-output-logging-2026-04-29.md]
- Only generations made after enabling the feature have stored content ^[raw/document/openrouter/openrouter-048-guides-features-input-output-logging-2026-04-29.md]
- Data stored in isolated Google Cloud Storage with AES-256 encryption at rest; minimum 3-month retention ^[raw/document/openrouter/openrouter-048-guides-features-input-output-logging-2026-04-29.md]
- OpenRouter does not access or use logged data for model training, analytics, or any other purpose ^[raw/document/openrouter/openrouter-048-guides-features-input-output-logging-2026-04-29.md]
- Does not apply to requests routed through `eu.openrouter.ai` ^[raw/document/openrouter/openrouter-048-guides-features-input-output-logging-2026-04-29.md]
- Distinct from Broadcast (sends data to external platforms) and Data Discount Logging (1% discount in exchange for data sharing) ^[raw/document/openrouter/openrouter-048-guides-features-input-output-logging-2026-04-29.md]

## Notes

- The feature and Broadcast can be used together for comprehensive observability, both configured in workspace Observability settings ^[raw/document/openrouter/openrouter-048-guides-features-input-output-logging-2026-04-29.md]

## Related

- [[entities/openrouter]]
- [[concepts/input_output_logging]]
- [[concepts/observability]]
- [[concepts/data_privacy]]
- [[concepts/broadcast]]