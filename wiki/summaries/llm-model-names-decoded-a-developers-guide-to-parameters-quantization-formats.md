---
title: "LLM Model Names Decoded: A Developer's Guide to Parameters, Quantization & Formats"
summary: "Decodes every component of LLM model names — parameter counts, training variants, quantization levels, file formats, and architecture types — with comparison tables and a decision framework for model selection"
type: summary
sources:
  - raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md
tags:
  - llm
  - quantization
  - model-selection
  - local-inference
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# LLM Model Names Decoded: A Developer's Guide to Parameters, Quantization & Formats

## Key Points

- LLM model names follow a general pattern: `[Org/] Family-Version-Size [-Active] -Training [-Format] [-Quantization]`, though naming is convention rather than standard ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]
- "B" stands for billions of parameters; a well-trained 14B model can outperform a mediocre 70B — training data quality and architecture matter as much as raw parameter count ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]
- Q4_K_M is the mainstream default quantization, retaining ~92% of original quality while cutting file size by ~75% compared to FP16 ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]
- GGUF is the format for local inference (Ollama, LM Studio, llama.cpp); safetensors is the format for GPU inference, training, and fine-tuning ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]
- Mixture of Experts models give knowledge capacity of large models at a fraction of compute per token, but still require RAM for all parameters ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]
- For general use, always pick the instruct/IT variant; base models are for researchers and fine-tuners ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]
- The rule of thumb for Q4_K_M GGUF: parameter count in billions × ~0.6 = approximate file size in GB ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]

## Quotes

- "A well-trained 14B model frequently outperforms a mediocre 70B. Training data quality, architecture choices, and fine-tuning matter as much as raw parameter count." ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]
- "Prefer a larger model at lower quantization over a smaller model at higher quantization. A 14B at Q4_K_M almost always beats a 7B at Q8_0." ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]
- "You cannot fine-tune from GGUF. If you want to fine-tune, start with the safetensors version, train with LoRA/QLoRA, then convert the result to GGUF for serving." ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]

## Notes

- Companion guide to a local LLM inference tools article; this guide focuses on decoding model names rather than running models
- As of April 2026, major open-weight families include Qwen 3.5, Gemma 4, Llama 4, DeepSeek, GLM-5, MiniMax M2, and Phi-4
- The 2026 landscape is dominated by MoE architectures, hybrid reasoning modes, distillation-based small models, and growing context windows

## Related

- [[concepts/quantization]]
- [[concepts/mixture_of_experts]]
- [[concepts/gguf]]
- [[concepts/safetensors]]
- [[concepts/distillation]]
- [[concepts/instruction_tuning]]
- [[entities/ollama]]
- [[entities/hugging_face]]
- [[entities/qwen]]
- [[entities/gemma]]
- [[entities/llama]]
- [[entities/deepseek]]