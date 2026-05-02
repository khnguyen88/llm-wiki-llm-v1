---
title: "Qwen"
summary: "Alibaba's LLM family (Qwen 3.5 generation) with the widest size range, hybrid thinking mode, and Apache 2.0 license"
type: entity
sources:
  - raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md
tags:
  - llm
  - model-family
  - apache-2.0
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Qwen

Alibaba's LLM family. The Qwen 3.5 generation (Apache 2.0) offers the widest size range of any model family, from 0.8B dense to 397B MoE, with hybrid thinking/non-thinking mode and a Gated DeltaNet architecture. ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]

## Key Facts

- Qwen 3.5 variants span 0.8B (dense) through 397B-A17B (MoE), all with 262K context windows ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]
- MoE variants: 35B-A3B, 122B-A10B, 397B-A17B ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]
- Supports 201 languages; strong coding capability via Qwen2.5-Coder ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]
- The 35B-A3B MoE runs on 8GB+ VRAM with Q4_K_M quantization ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]
- Most popular base for community fine-tunes ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]
- Example model name decoded: `bartowski/Qwen3.5-32B-Instruct-GGUF-Q4_K_M` — organization bartowski, family Qwen3.5, 32B parameters, instruct-tuned, GGUF format, Q4_K_M quantization ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]

## Related

- [[concepts/mixture_of_experts]]
- [[concepts/quantization]]
- [[concepts/gguf]]
- [[entities/ollama]]