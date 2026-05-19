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
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Gemma

Google's open-weight LLM family. The Gemma 4 generation (Apache 2.0) is natively multimodal across all sizes -- the E4B variant supports audio, video, and image understanding at 4.5B parameters. ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]

## Key Facts

| Model | Params | Architecture | Context | Modalities |
|---|---|---|---|---|
| Gemma 4 E2B | 2.3B | Dense | 128K | Text, Image, Video, Audio |
| Gemma 4 E4B | 4.5B | Dense | 128K | Text, Image, Video, Audio |
| Gemma 4 26B-A4B | 26B total / 4B active | MoE | 256K | Text, Image, Video |
| Gemma 4 31B | 31B | Dense | 256K | Text, Image, Video |

^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]

- The 26B MoE achieves near-31B quality with only 4B active parameters ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]
- Naming example: `google/gemma-4-26B-A4B-it` -- organization google, family gemma-4, 26B total / 4B active (MoE), instruction-tuned ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]

## Related

- [[concepts/mixture_of_experts]]
- [[concepts/instruction_tuning]]
- [[concepts/model_naming]]
- [[entities/qwen]]
- [[entities/llama]]
