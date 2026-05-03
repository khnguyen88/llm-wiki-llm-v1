---
title: "Input & Output Logging"
summary: "An OpenRouter feature (off by default) that privately stores full request and response content for user review, debugging, and prompt optimization"
type: concept
sources:
  - raw/document/openrouter/openrouter-048-guides-features-input-output-logging-2026-04-29.md
  - raw/document/openrouter/openrouter-067-guides-privacy-data-collection-2026-04-29.md
tags:
  - openrouter
  - logging
  - observability
  - privacy
  - debugging
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: merged
---

# Input & Output Logging

An OpenRouter feature (currently in Beta) that lets users privately save and review the full content of their LLM requests and responses. Off by default — prompts and completions are not stored unless this setting is explicitly enabled. Once enabled, prompts and completions are accessible from the OpenRouter Logs page. ^[raw/document/openrouter/openrouter-048-guides-features-input-output-logging-2026-04-29.md] ^[raw/document/openrouter/openrouter-067-guides-privacy-data-collection-2026-04-29.md]

## Key Points

- Enabled via the Observability settings toggle at `openrouter.ai/workspaces/default/observability`; for organizations, only admins can view and toggle this setting ^[raw/document/openrouter/openrouter-048-guides-features-input-output-logging-2026-04-29.md]
- Stored prompts and completions are viewable from the Logs page by clicking a generation, then switching between Prompt and Completion tabs; generation detail view also shows model, provider, token counts, and cost ^[raw/document/openrouter/openrouter-048-guides-features-input-output-logging-2026-04-29.md]
- Only generations made after enabling the feature have stored content; prior generations are not retroactively logged ^[raw/document/openrouter/openrouter-048-guides-features-input-output-logging-2026-04-29.md]
- Does not apply to requests routed through `eu.openrouter.ai`; EU-routed requests work normally but I/O logging is skipped ^[raw/document/openrouter/openrouter-048-guides-features-input-output-logging-2026-04-29.md]
- Distinct from [[concepts/broadcast|Broadcast]] (which sends data to external platforms) and from Data Discount Logging (a separate Privacy setting that grants 1% discount in exchange for allowing OpenRouter to use data) ^[raw/document/openrouter/openrouter-048-guides-features-input-output-logging-2026-04-29.md]

## Details

### Storage, Privacy, and Access

Prompt and response data is stored in an isolated Google Cloud Storage project with separate access controls. All data is encrypted at rest using Google Cloud's default encryption (AES-256). Data is retained for a minimum of 3 months and may be retained beyond that at OpenRouter's discretion unless the account owner requests deletion by contacting support@openrouter.ai. ^[raw/document/openrouter/openrouter-048-guides-features-input-output-logging-2026-04-29.md]

OpenRouter does not access or use logged prompt and response data for model training, analytics, or any other purpose. The data is stored solely for the user's own review. For organization accounts, only organization admins can view stored prompt and response content; non-admin members cannot access it. ^[raw/document/openrouter/openrouter-048-guides-features-input-output-logging-2026-04-29.md]

### Comparison with Broadcast

Both Input & Output Logging and [[concepts/broadcast|Broadcast]] are configured in workspace Observability settings and can be used together. Input & Output Logging stores data on OpenRouter for quick debugging and prompt optimization; Broadcast sends data to external observability platforms for production monitoring and analytics. ^[raw/document/openrouter/openrouter-048-guides-features-input-output-logging-2026-04-29.md]

### Comparison with Data Discount Logging

Input & Output Logging keeps data strictly private and is enabled in Observability settings. Data Discount Logging is an independent setting enabled in Privacy settings that allows OpenRouter to use data to improve the product in exchange for a 1% discount on all model usage. Users can enable one, the other, or both independently. ^[raw/document/openrouter/openrouter-048-guides-features-input-output-logging-2026-04-29.md]

## Related

- [[entities/openrouter]]
- [[concepts/observability]]
- [[concepts/data_privacy]]
- [[concepts/broadcast]]
- [[concepts/zero_data_retention]]