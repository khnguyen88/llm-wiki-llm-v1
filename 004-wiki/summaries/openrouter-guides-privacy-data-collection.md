---
title: "Openrouter Guides Privacy Data Collection"
summary: "OpenRouter stores no prompts or completions by default; two opt-in settings control logging and product-improvement use, while metadata is always collected and anonymous prompt categorization occurs without account linkage"
type: summary
sources:
  - raw/document/openrouter/openrouter-067-guides-privacy-data-collection-2026-04-29.md
tags:
  - openrouter
  - privacy
  - data-collection
  - logging
  - metadata
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Openrouter Guides Privacy Data Collection

## Key Points

- OpenRouter does not store prompts or responses unless the user opts in to one or both data-sharing settings ^[raw/document/openrouter/openrouter-067-guides-privacy-data-collection-2026-04-29.md]
- **Private Input & Output Logging** (off by default) makes prompts and completions visible in logs for debugging and prompt optimization; OpenRouter does not access or use this data; for organizations, only admins can view logged data; enabled via Observability settings ^[raw/document/openrouter/openrouter-067-guides-privacy-data-collection-2026-04-29.md]
- **OpenRouter Use of Inputs/Outputs** (off by default) allows OpenRouter to use prompt and completion data to improve the product, in exchange for a 1% discount on all model usage; enabled via Privacy settings ^[raw/document/openrouter/openrouter-067-guides-privacy-data-collection-2026-04-29.md]
- OpenRouter samples a small number of prompts for anonymous categorization to power reporting and model ranking; if not opted in to OpenRouter use of inputs/outputs, categorization is stored completely anonymously and never associated with the user's account or user ID ^[raw/document/openrouter/openrouter-067-guides-privacy-data-collection-2026-04-29.md]
- Categorization is performed by a model with a zero-data-retention policy ^[raw/document/openrouter/openrouter-067-guides-privacy-data-collection-2026-04-29.md]
- Metadata (prompt/completion token counts, latency, etc.) is stored for every request regardless of opt-in status; metadata does not include prompt or response content ^[raw/document/openrouter/openrouter-067-guides-privacy-data-collection-2026-04-29.md]
- Metadata powers reporting, model ranking, and the logs metadata page ^[raw/document/openrouter/openrouter-067-guides-privacy-data-collection-2026-04-29.md]

## Quotes

- "OpenRouter does not store your prompts or responses, *unless* you opt in to one or both of the following" ^[raw/document/openrouter/openrouter-067-guides-privacy-data-collection-2026-04-29.md:15]
- "if you are not opted in to OpenRouter use of inputs/outputs, any categorization of your prompts is stored completely anonymously and never associated with your account or user ID" ^[raw/document/openrouter/openrouter-067-guides-privacy-data-collection-2026-04-29.md:23]
- "This metadata does not include the content of your prompts or responses, only information about the request itself." ^[raw/document/openrouter/openrouter-067-guides-privacy-data-collection-2026-04-29.md:27]

## Notes

- This page clarifies the distinction between two separate opt-in settings (Observability vs Privacy) and the always-on metadata collection, which is a more structured presentation than the FAQ and individual feature pages.

## Related

- [[entities/openrouter]]
- [[concepts/data_privacy]]
- [[concepts/data_collection_policy]]
- [[concepts/input_output_logging]]
- [[concepts/observability]]
- [[concepts/zero_data_retention]]