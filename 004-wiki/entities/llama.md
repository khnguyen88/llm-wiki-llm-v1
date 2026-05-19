---
title: "Llama"
summary: "Meta's LLM family; the Llama 4 generation introduced MoE architecture with industry-leading context windows"
type: entity
sources:
  - raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md
  - raw/articles/LLM Naming Explained (What do the options mean_).md
  - raw/articles/How to navigate LLM model names.md
tags:
  - llm
  - model-family
  - moe
created: "2026-05-01T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: merged
---

# Llama

Meta's LLM family. The name Llama is derived from the acronym "Large Language Model Meta AI." The Llama 4 generation is Meta's first MoE architecture, featuring Scout with a 10M token context window and Maverick with 128 experts. ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md] ^[raw/articles/How to navigate LLM model names.md]

## Key Facts

| Model | Total Params | Active Params | Experts | Context |
|---|---|---|---|---|
| Llama 4 Scout | 109B | 17B | 16 | 10M |
| Llama 4 Maverick | 400B | 17B | 128 | 1M |
| Llama 4 Behemoth | ~2T | 288B | 16 | TBD (preview) |

^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]

- Llama 4 Scout fits on a single H100 GPU with a 10-million-token context window, industry-leading for long context use cases ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]
- Llama 4 Maverick beats GPT-4o on many benchmarks ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]
- Licensing: Llama Community License has commercial restrictions above 700M monthly users ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]
- Llama 3.3 70B instruct (`llama3.3-70b-instruct-q4_K_M`) is commonly used as a naming convention example ^[raw/articles/LLM Naming Explained (What do the options mean_).md]
- Llama naming uses the `PxE` MoE convention (e.g., `Llama-4-Scout-17B-16E` = 16 experts, 17B active) ^[raw/articles/How to navigate LLM model names.md]
- Concrete hardware example: Llama-3.1-405b-instruct requires 900+ GB vRAM across sixteen H100s ^[raw/articles/How to navigate LLM model names.md]

## Related

- [[concepts/mixture_of_experts]]
- [[concepts/model_naming]]
- [[entities/qwen]]
- [[entities/gemma]]
- [[entities/deepseek]]
