---
title: "Naming Conventions of LLM Models"
type: summary
date: 2026-04-23
sources:
  - raw/articles/Naming Conventions of LLM Models.md
tags:
  - llm
  - naming-conventions
  - paid-models
  - open-source
---

# Naming Conventions of LLM Models

**Author:** [[entities/sudarshan|Sudarshan]]  
**Source:** [TO THE NEW](https://www.tothenew.com/blog/naming-conventions-of-llm-models/)  
**Published:** 2026-03-30

## Summary

A concise comparison of naming conventions between paid (proprietary) and open-source LLMs, showing how paid models are designed like products while open-source models are designed like engineering artifacts.

## Common Patterns

| Suffix | Meaning |
|--------|---------|
| Turbo | Optimized for speed + cost |
| Mini | Smaller + cheaper |
| Pro | High capability |
| Flash | Ultra-fast |
| Instruct | Fine-tuned to follow instructions |
| Chat | Optimized for conversations |
| rlhf | Trained with human feedback |

## Size Hierarchy

`xxl > xl > large > base > small`

## Size Indicators

`7B`, `13B`, `70B` → billions of parameters

## Versioning

`v0.1`, `v1`, `v2` → iteration of fine-tuning

## Paid Models

Designed for simplicity, branding, and positioning. General pattern: `[Model Family] + [Version] + [Variant / Capability Tier]`

Examples:
- **GPT-4o**: GPT family, 4th generation, "o" = omni (multimodal).
- **Gemini 1.5 Pro**: Gemini family, 1.5 upgrade, Pro = high capability. Other variants: Flash (faster, cheaper), Ultra (most powerful).

## Open-Source Models

More technical and architecture-oriented. General pattern: `[organization]/[model-family]-[version]-[size]-[variant]-[format]`

Examples:
- **meta-llama/Llama-2-7b-chat-hf**: Meta organization, Llama-2 family, 7B params, chat-optimized, Hugging Face format.
- **mistralai/Mistral-7B-Instruct-v0.1**: Mistral base 7B, instruction-following, fine-tuning version 0.1.

## Key Claims

- Paid models are designed like products; open-source models are designed like engineering artifacts.
- Understanding this difference helps select better models for specific requirements.

## Related

- [[concepts/llm_naming_conventions]]
- [[concepts/parameter_counts]]
- [[concepts/training_variants]]
- [[entities/sudarshan]]
