---
title: "DeepSeek"
summary: "Open-weight LLM family known for DeepSeek-R1, which pioneered practical distillation of frontier reasoning into smaller models"
type: entity
sources:
  - raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md
  - raw/articles/LLM Naming Explained (What do the options mean_).md
tags:
  - llm
  - model-family
  - distillation
  - reasoning
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# DeepSeek

Open-weight LLM family. DeepSeek-V3 is a 671B total / 37B active MoE model focused on coding and general tasks. DeepSeek-R1 (671B) pioneered practical distillation of frontier reasoning capabilities into smaller models. ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]

## Key Facts

- DeepSeek-V3: 671B total / 37B active (MoE), strong at coding and general tasks ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]
- DeepSeek-R1-Distill-Qwen-32B: a Qwen 2.5 32B model fine-tuned on 800,000 chain-of-thought reasoning samples from DeepSeek-R1 (671B); outperforms OpenAI o1-mini on multiple benchmarks despite being ~20x smaller ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]
- The distillation approach: a smaller "student" model learns to replicate a larger "teacher" model's outputs, transferring capability at smaller scale ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]
- Best local reasoning via distillation ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]
- DeepSeek R1 70B can be distilled into Llama architecture; the variant `deepseek-r1:70b-llama-distill-q4_K_M` combines R1 reasoning with Llama at 4-bit K-quant medium compression ^[raw/articles/LLM Naming Explained (What do the options mean_).md]

## Related

- [[concepts/distillation]]
- [[concepts/mixture_of_experts]]
- [[entities/qwen]]