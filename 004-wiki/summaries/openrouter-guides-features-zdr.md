---
title: "Openrouter Guides Features Zdr"
summary: "OpenRouter's Zero Data Retention (ZDR) policy: account-wide and per-request enforcement, the distinction between retention and training, and how in-memory caching relates to ZDR"
type: summary
sources:
  - raw/document/openrouter/openrouter-044-guides-features-zdr-2026-04-29.md
tags:
  - openrouter
  - zdr
  - data-privacy
  - provider-routing
  - caching
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Openrouter Guides Features Zdr

## Key Points

- Zero Data Retention (ZDR) means a provider will not store user data for any period; OpenRouter offers an account-wide setting at `/settings/privacy` that restricts routing to ZDR endpoints only ^[001a-raw/document/openrouter/openrouter-044-guides-features-zdr-2026-04-29.md]
- ZDR is stricter than "no training on data" — some providers do not train on data but still retain it for abuse scanning or legal reasons; OpenRouter gives controls over both policies ^[001a-raw/document/openrouter/openrouter-044-guides-features-zdr-2026-04-29.md]
- OpenRouter tracks per-endpoint data policies, which may differ from the provider's general policy; in some cases, OpenRouter creates special agreements with providers for more privacy-focused policies than their defaults ^[001a-raw/document/openrouter/openrouter-044-guides-features-zdr-2026-04-29.md]
- If a provider or endpoint policy cannot be confirmed, OpenRouter takes a conservative stance and assumes the endpoint both retains and trains on data ^[001a-raw/document/openrouter/openrouter-044-guides-features-zdr-2026-04-29.md]
- Per-request ZDR enforcement is available via the `provider.zdr` parameter in API calls, operating as an OR with the account-wide setting — it can ensure ZDR for a specific request but cannot override account-wide ZDR enforcement ^[001a-raw/document/openrouter/openrouter-044-guides-features-zdr-2026-04-29.md]
- In-memory caching of prompts (kept temporarily in a provider's datacenter for repeated prompt processing) is not considered "retaining" data and is allowed under ZDR routing ^[001a-raw/document/openrouter/openrouter-044-guides-features-zdr-2026-04-29.md]
- OpenRouter itself has a ZDR policy: prompts are not retained unless the user opts in to prompt logging ^[001a-raw/document/openrouter/openrouter-044-guides-features-zdr-2026-04-29.md]

## Notes

- A list of ZDR endpoints is available programmatically at `https://openrouter.ai/api/v1/endpoints/zdr` and is automatically updated when provider data policies change ^[001a-raw/document/openrouter/openrouter-044-guides-features-zdr-2026-04-29.md]
- The provider logging and data retention list is at `/docs/guides/privacy/provider-logging` — this shows default provider policies, which may differ from specific endpoint policies ^[001a-raw/document/openrouter/openrouter-044-guides-features-zdr-2026-04-29.md]

## Related

- [[004-wiki/entities/openrouter]]
- [[004-wiki/concepts/zero_data_retention]]
- [[004-wiki/concepts/data_privacy]]
- [[004-wiki/concepts/data_collection_policy]]
- [[004-wiki/concepts/provider_routing]]
- [[004-wiki/concepts/prompt_caching]]