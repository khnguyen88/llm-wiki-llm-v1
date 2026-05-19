---
title: "Naming Conventions of LLM Models"
summary: "TO THE NEW blog post by Sudarshan (March 2026) comparing paid and open-source LLM naming conventions, with breakdowns of common suffixes, size hierarchies, and versioning patterns"
type: summary
sources:
  - raw/articles/Naming Conventions of LLM Models.md
tags:
  - llm
  - naming-conventions
  - paid-models
  - open-source
  - model-comparison
created: "2026-05-01T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
---

# Naming Conventions of LLM Models

## Summary

This article by Sudarshan (TO THE NEW, March 2026) categorizes LLM naming conventions into two fundamentally different approaches: paid models (product-oriented, branding-focused) and open-source models (engineering artifact-oriented, technically descriptive). The article breaks down common suffixes, size hierarchies, versioning patterns, and provides detailed examples of each category. ^[raw/articles/Naming Conventions of LLM Models.md]

## Common Suffix Meanings

| Suffix | Meaning |
|---|---|
| Turbo | Optimised for speed + cost |
| Mini | Smaller + cheaper |
| Pro | High capability |
| Flash | Ultra-fast |
| Instruct | Fine-tuned to follow instructions |
| Chat | Optimised for conversations |
| rlhf | Trained with human feedback |

^[raw/articles/Naming Conventions of LLM Models.md]

## Paid Model Naming

Paid models follow the pattern: `[Model Family] + [Version] + [Variant / Capability Tier]`. Designed for simplicity, branding, and product positioning targeting non-technical users. ^[raw/articles/Naming Conventions of LLM Models.md]

| Example | Breakdown | Meaning |
|---|---|---|
| GPT-4o | GPT (family) + 4 (gen) + o/omni (multimodal) | 4th-gen model handling text, image, audio |
| Gemini 1.5 Pro | Gemini (family) + 1.5 (version) + Pro (high capability) | Incremental upgrade, high capability tier |

^[raw/articles/Naming Conventions of LLM Models.md]

## Open-Source Model Naming

Open-source models follow the pattern: `[organization]/[model-family]-[version]-[size]-[variant]-[format]`. Designed like engineering artifacts, exposing technical metadata for practitioners. ^[raw/articles/Naming Conventions of LLM Models.md]

| Example | Breakdown | Meaning |
|---|---|---|
| meta-llama/Llama-2-7b-chat-hf | Meta (org) + Llama-2 (family+version) + 7b (size) + chat (variant) + hf (format) | 7B chat-optimized Llama v2 in HF format |
| mistralai/Mistral-7B-Instruct-v0.1 | Mistral (base) + 7B (size) + Instruct (variant) + v0.1 (version) | Instruction-tuned Mistral 7B, early release |

^[raw/articles/Naming Conventions of LLM Models.md]

## Key Quotes

> "Paid models are designed like products -- Open-source models are designed like engineering artifacts."

> "Understanding this difference can help us to select a better model for our specific requirements."
