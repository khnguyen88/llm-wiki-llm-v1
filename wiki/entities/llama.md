---
title: "Llama"
summary: "Meta's LLM family; the Llama 4 generation introduced MoE architecture with industry-leading context windows"
type: entity
sources:
  - raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md
  - raw/articles/LLM Naming Explained (What do the options mean_).md
tags:
  - llm
  - model-family
  - moe
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Llama

Meta's LLM family. The Llama 4 generation is Meta's first MoE architecture, featuring Scout with a 10M token context window and Maverick with 128 experts. ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]

## Key Facts

- Llama 4 Scout: 109B total / 17B active, 16 experts, 10M context window — fits on a single H100 GPU ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]
- Llama 4 Maverick: 400B total / 17B active, 128 experts, 1M context window — beats GPT-4o on many benchmarks ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]
- Llama 4 Behemoth: ~2T total / 288B active, 16 experts, in preview ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]
- Best for long context use cases; Scout's 10M token context window is industry-leading ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]
- Licensing: Llama Community License has commercial restrictions above 700M users ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]
- Llama 3.3 70B instruct (`llama3.3-70b-instruct-q4_K_M`) is a 70-billion parameter instruction-tuned variant commonly used as a naming convention example ^[raw/articles/LLM Naming Explained (What do the options mean_).md]

## Related

- [[concepts/mixture_of_experts]]
- [[entities/qwen]]
- [[entities/gemma]]
- [[entities/deepseek]]