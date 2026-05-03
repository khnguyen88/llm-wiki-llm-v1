---
title: "Data Privacy"
summary: "OpenRouter's data handling policies: zero prompt/completion logging by default, with two opt-in settings for logging and product-improvement use, anonymous categorization, and always-on metadata collection"
type: concept
sources:
  - raw/document/openrouter/openrouter-015-faq-2026-04-29.md
  - raw/document/openrouter/openrouter-044-guides-features-zdr-2026-04-29.md
  - raw/document/openrouter/openrouter-048-guides-features-input-output-logging-2026-04-29.md
  - raw/document/openrouter/openrouter-052-guides-features-broadcast-clickhouse-2026-04-29.md
  - raw/document/openrouter/openrouter-067-guides-privacy-data-collection-2026-04-29.md
  - raw/document/openrouter/openrouter-068-guides-privacy-provider-logging-2026-04-29.md
tags:
  - openrouter
  - privacy
  - data-logging
  - data-collection
  - provider-routing
  - zdr
  - provider-policies
  - provider-logging
  - data-retention
  - eu-routing
  - input-output-logging
  - broadcast
  - metadata
  - anonymous-categorization
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: merged
---

# Data Privacy

OpenRouter's approach to data collection and privacy: prompts and completions are not logged by default, with an opt-in setting that provides a 1% usage discount in exchange for logging. Provider routing can be restricted based on privacy preferences. ^[raw/document/openrouter/openrouter-015-faq-2026-04-29.md]

## Key Points

- Only basic request metadata is logged by default (timestamps, model used, token counts) — prompts and completions are never logged unless the user opts in ^[raw/document/openrouter/openrouter-015-faq-2026-04-29.md]
- Zero logging applies even when errors occur; logging is strictly opt-in ^[raw/document/openrouter/openrouter-015-faq-2026-04-29.md]
- An opt-in setting at openrouter.ai/settings/preferences grants a 1% discount on usage costs in exchange for logging prompts and completions ^[raw/document/openrouter/openrouter-015-faq-2026-04-29.md]
- OpenRouter works with providers to ensure prompts and completions are not logged or used for training when possible ^[raw/document/openrouter/openrouter-015-faq-2026-04-29.md]
- Providers that log data, or where logging policy cannot be confirmed, will not be routed to unless the user enables the model training toggle in privacy settings ^[raw/document/openrouter/openrouter-015-faq-2026-04-29.md]
- If provider routing is specified in a request but none of the providers match the user's privacy level, the request returns an error rather than routing to a non-compliant provider ^[raw/document/openrouter/openrouter-015-faq-2026-04-29.md]
- ZDR is distinct from "no training" policy — some providers do not train on data but still retain it for abuse scanning or legal reasons; OpenRouter gives separate controls over both retention and training policies ^[raw/document/openrouter/openrouter-044-guides-features-zdr-2026-04-29.md]
- OpenRouter tracks per-endpoint data policies, which may differ from a provider's general policy; special agreements with providers can result in more privacy-focused policies than their defaults ^[raw/document/openrouter/openrouter-044-guides-features-zdr-2026-04-29.md]
- If a provider or endpoint data policy cannot be confirmed, OpenRouter conservatively assumes the endpoint both retains and trains on data ^[raw/document/openrouter/openrouter-044-guides-features-zdr-2026-04-29.md]
- OpenRouter itself has a ZDR policy: prompts are not retained unless the user opts in to prompt logging ^[raw/document/openrouter/openrouter-044-guides-features-zdr-2026-04-29.md]
- Input & Output Logging stores data in isolated Google Cloud Storage with AES-256 encryption at rest; OpenRouter does not access or use logged data for model training, analytics, or any other purpose ^[raw/document/openrouter/openrouter-048-guides-features-input-output-logging-2026-04-29.md]
- Data Discount Logging (enabled in Privacy settings) is a separate feature from Input & Output Logging (enabled in Observability settings); it grants 1% discount on all model usage in exchange for allowing OpenRouter to use data to improve the product ^[raw/document/openrouter/openrouter-048-guides-features-input-output-logging-2026-04-29.md]
- For organization accounts, only admins can view stored prompt and response content from Input & Output Logging; non-admin members cannot access it ^[raw/document/openrouter/openrouter-048-guides-features-input-output-logging-2026-04-29.md]
- When Privacy Mode is enabled for a [[concepts/broadcast|Broadcast]] destination (such as ClickHouse), prompt and completion content is excluded from traces while all other trace data — token usage, costs, timing, model information, and custom metadata — is sent normally ^[raw/document/openrouter/openrouter-052-guides-features-broadcast-clickhouse-2026-04-29.md]
- OpenRouter samples a small number of prompts for anonymous categorization to power reporting and model ranking; if a user is not opted in to OpenRouter use of inputs/outputs, categorization is stored completely anonymously and never associated with the account or user ID; categorization is performed by a model with a zero-data-retention policy ^[raw/document/openrouter/openrouter-067-guides-privacy-data-collection-2026-04-29.md]
- Metadata (prompt/completion token counts, latency, etc.) is stored for every request regardless of opt-in status; metadata does not include the content of prompts or responses, only information about the request itself ^[raw/document/openrouter/openrouter-067-guides-privacy-data-collection-2026-04-29.md]
- Each AI provider on OpenRouter has its own data handling policies for training on prompts and data retention; these are reflected in structured data on each endpoint ^[raw/document/openrouter/openrouter-068-guides-privacy-provider-logging-2026-04-29.md]
- Users can opt out of routing to providers that may train on data via account settings, with separate controls for paid and free models; this setting only affects provider routing and has no bearing on OpenRouter's own data policies ^[raw/document/openrouter/openrouter-068-guides-privacy-provider-logging-2026-04-29.md]
- OpenRouter does not enforce routing rules based on provider data retention policies, but surfaces retention information so users can filter providers manually ^[raw/document/openrouter/openrouter-068-guides-privacy-provider-logging-2026-04-29.md]
- Enterprise EU in-region routing processes prompts and completions within the European Union using `https://eu.openrouter.ai`; available only for enterprise customers by request ^[raw/document/openrouter/openrouter-068-guides-privacy-provider-logging-2026-04-29.md]

## Details

OpenRouter acts as a proxy, forwarding requests to model providers for completion. The privacy model operates at two levels: OpenRouter's own logging policy (zero prompt/completion logging by default) and provider-level policies (OpenRouter negotiates with providers to avoid logging and training use). Chatroom conversations are stored locally on the user's device and do not sync across devices, though they can be exported and imported via the settings menu. ^[raw/document/openrouter/openrouter-015-faq-2026-04-29.md]

Provider-level data policies cover two distinct concerns: whether a provider may train on user prompts, and how long a provider retains data. OpenRouter gives separate controls for each — the training opt-out setting controls routing to providers that train, while data retention policies are surfaced for user information but not enforced in routing. For enterprise customers requiring data sovereignty, EU in-region routing ensures all processing stays within the European Union. ^[raw/document/openrouter/openrouter-068-guides-privacy-provider-logging-2026-04-29.md]

## Related

- [[entities/openrouter]]
- [[concepts/credit_system]]
- [[concepts/provider_fallback]]
- [[concepts/authentication]]
- [[summaries/openrouter-faq]]
- [[concepts/zero_data_retention]]
- [[summaries/openrouter-guides-features-zdr]]
- [[concepts/input_output_logging]]
- [[summaries/openrouter-guides-features-input-output-logging]]
- [[concepts/data_collection_policy]]
- [[summaries/openrouter-guides-privacy-data-collection]]
- [[concepts/provider_logging]]
- [[summaries/openrouter-guides-privacy-provider-logging]]