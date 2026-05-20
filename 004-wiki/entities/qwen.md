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
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Qwen

Alibaba's LLM family. The Qwen 3.5 generation (Apache 2.0) offers the widest size range of any model family, from 0.8B dense to 397B MoE, with hybrid thinking/non-thinking mode and a Gated DeltaNet architecture. ^[001a-raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]

## Key Facts

| Model | Params | Architecture | Context | Notes |
|---|---|---|---|---|
| Qwen3.5-0.8B | 0.8B | Dense | 262K | Smallest variant |
| Qwen3.5-4B | 4B | Dense | 262K | |
| Qwen3.5-9B | 9B | Dense | 262K | |
| Qwen3.5-27B | 27B | Dense | 262K | |
| Qwen3.5-35B-A3B | 35B / 3B active | MoE | 262K | Runs on 8GB+ VRAM at Q4_K_M |
| Qwen3.5-122B-A10B | 122B / 10B active | MoE | 262K | Near-frontier quality |
| Qwen3.5-397B-A17B | 397B / 17B active | MoE | 262K | Frontier-class |

^[001a-raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]

- Supports 201 languages; strong coding capability via Qwen2.5-Coder (14B scores ~85% on HumanEval) ^[001a-raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]
- Most popular base for community fine-tunes ^[001a-raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]
- Naming example: `bartowski/Qwen3.5-32B-Instruct-GGUF-Q4_K_M` -- organization bartowski, family Qwen3.5, 32B parameters, instruct-tuned, GGUF format, Q4_K_M quantization ^[001a-raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]

## Related

- [[004-wiki/concepts/mixture_of_experts]]
- [[004-wiki/concepts/model_naming]]
- [[004-wiki/concepts/quantization]]
- [[004-wiki/entities/ollama]]
- [[004-wiki/entities/deepseek]]
