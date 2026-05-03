---
title: "DeepSeek"
summary: "Open-weight LLM family known for DeepSeek-R1, with automated prompt caching on OpenRouter where cache writes cost the same as regular input tokens"
type: entity
sources:
  - raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md
  - raw/articles/LLM Naming Explained (What do the options mean_).md
  - raw/articles/How to navigate LLM model names.md
  - raw/document/openrouter/openrouter-070-guides-best-practices-prompt-caching-2026-04-29.md
tags:
  - llm
  - model-family
  - distillation
  - reasoning
  - prompt-caching
created: "2026-05-01T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: merged
---

# DeepSeek

Open-weight LLM family. DeepSeek-V3 is a 671B total / 37B active MoE model focused on coding and general tasks. DeepSeek-R1 (671B) pioneered practical distillation of frontier reasoning capabilities into smaller models, using chain-of-thought processing to work through questions internally before delivering a final response. ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md] ^[raw/articles/How to navigate LLM model names.md]

## Key Facts

- DeepSeek-V3: 671B total / 37B active (MoE), strong at coding and general tasks ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]
- DeepSeek-R1-Distill-Qwen-32B: a Qwen 2.5 32B model fine-tuned on 800,000 chain-of-thought reasoning samples from DeepSeek-R1 (671B); outperforms OpenAI o1-mini on multiple benchmarks despite being ~20x smaller ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]
- Known as the best local reasoning model via distillation ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]
- Model naming example: `deepseek-r1:70b-llama-distill-q4_K_M` combines R1 reasoning with Llama architecture at 4-bit K-quant medium compression ^[raw/articles/LLM Naming Explained (What do the options mean_).md]
- Put reasoning models on the map for the general public, taking the stock market by storm ^[raw/articles/How to navigate LLM model names.md]
- Prompt caching with DeepSeek is automated and requires no additional configuration on OpenRouter ^[raw/document/openrouter/openrouter-070-guides-best-practices-prompt-caching-2026-04-29.md]
- Cache writes are charged at the same price as regular input tokens (unlike most other providers that offer free cache writes) ^[raw/document/openrouter/openrouter-070-guides-best-practices-prompt-caching-2026-04-29.md]
- Cache reads are charged at a reduced multiplier of the original input pricing ^[raw/document/openrouter/openrouter-070-guides-best-practices-prompt-caching-2026-04-29.md]

## Related

- [[concepts/distillation]]
- [[concepts/mixture_of_experts]]
- [[concepts/model_naming]]
- [[entities/qwen]]
- [[entities/openrouter]]
- [[concepts/prompt_caching]]
- [[summaries/openrouter-guides-best-practices-prompt-caching]]
