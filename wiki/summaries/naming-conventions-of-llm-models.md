---
title: "Naming Conventions Of Llm Models"
summary: "Explains LLM naming patterns distinguishing paid models (product-oriented: family + version + tier) from open-source models (engineering-oriented: org + family + version + size + variant + format)"
type: summary
sources:
  - raw/articles/Naming Conventions of LLM Models.md
tags:
  - llm
  - naming-conventions
  - model-selection
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Naming Conventions Of Llm Models

## Key Points

- LLM model names encode practical metadata: model family, version, capability tier, parameter size, fine-tuning variant, and format ^[raw/articles/Naming Conventions of LLM Models.md]
- Common suffix meanings: Turbo (speed + cost optimized), Mini (smaller + cheaper), Pro (high capability), Flash (ultra-fast), Instruct (fine-tuned for instructions), Chat (conversation-optimized), rlhf (trained with human feedback) ^[raw/articles/Naming Conventions of LLM Models.md]
- Size hierarchy: xxl > xl > large > base > small; size indicators use parameter counts (7B, 13B, 70B) ^[raw/articles/Naming Conventions of LLM Models.md]
- Paid models follow pattern: [Model Family] + [Version] + [Variant/Capability Tier] — naming prioritizes simplicity, branding, and product differentiation for non-technical users ^[raw/articles/Naming Conventions of LLM Models.md]
- Open-source models follow pattern: [organization]/[model-family]-[version]-[size]-[variant]-[format] — naming is technical and architecture-oriented ^[raw/articles/Naming Conventions of LLM Models.md]
- Versioning tags (v0.1, v1, v2) indicate iterations of fine-tuning ^[raw/articles/Naming Conventions of LLM Models.md]
- Paid models are designed like products; open-source models are designed like engineering artifacts ^[raw/articles/Naming Conventions of LLM Models.md]

## Quotes

- "Paid models are designed like products — Open-source models are designed like engineering artifacts" ^[raw/articles/Naming Conventions of LLM Models.md]

## Notes

- Source is a concise introductory blog post (~460 words); covers naming fundamentals but lacks depth on ambiguity, validation, or decision frameworks found in other sources

## Related

- [[concepts/model_naming]]
- [[concepts/instruction_tuning]]
- [[concepts/quantization]]
- [[entities/hugging_face]]