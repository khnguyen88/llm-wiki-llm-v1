---
title: "Gemma"
summary: "Google's open-weight LLM family (Gemma 4 generation), natively multimodal across all sizes, Apache 2.0 licensed"
type: entity
sources:
  - raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md
tags:
  - llm
  - model-family
  - multimodal
  - apache-2.0
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Gemma

Google's open-weight LLM family. The Gemma 4 generation (Apache 2.0) is natively multimodal across all sizes — the E4B variant supports audio, video, and image understanding at 4.5B parameters. ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]

## Key Facts

- Gemma 4 variants: E2B (2.3B dense, 128K context), E4B (4.5B dense, 128K context), 26B-A4B (MoE, 256K context), 31B (dense, 256K context) ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]
- The 26B MoE achieves near-31B quality with only 4B active parameters ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]
- Natively multimodal: text, image, video across all sizes; E2B and E4B also support audio ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]
- Example model name decoded: `google/gemma-4-26B-A4B-it` — organization google, family gemma-4, 26B total / 4B active (MoE), instruction-tuned ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]

## Related

- [[concepts/mixture_of_experts]]
- [[concepts/instruction_tuning]]
- [[entities/qwen]]
- [[entities/llama]]