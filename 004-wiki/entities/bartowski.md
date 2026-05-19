---
title: "Bartowski"
summary: "The most prolific community GGUF quantizer on Hugging Face, providing multiple quantization levels for every major model release"
type: entity
sources:
  - raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md
tags:
  - llm
  - community
  - quantization
  - gguf
  - hugging-face
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
---

# Bartowski

Bartowski is the most prolific community GGUF quantizer on Hugging Face, providing multiple quantization levels (Q2_K through Q8_0) for every major model release. They inherited the role from TheBloke, who was the pioneer of community quantization but has been less active since 2024. ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]

## Key Facts

- Most prolific quantizer on HuggingFace -- produces multiple quant levels for every major release ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]
- Repository naming convention: `bartowski/<model-name>-GGUF` (e.g., `bartowski/Qwen3.5-27B-GGUF`, `bartowski/gemma-4-31B-it-GGUF`) ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]
- Inherited the primary community quantization role from TheBloke (who pioneered GGUF/GPTQ quantization but became less active after 2024) ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]
- Bartowski's GGUF quantizations are the standard way to find quantized models alongside unsloth's dynamic quantization variants ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]

## Related

- [[concepts/gguf]]
- [[concepts/quantization]]
- [[entities/hugging_face]]
