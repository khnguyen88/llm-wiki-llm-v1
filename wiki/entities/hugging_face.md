---
title: "Hugging Face"
summary: "The primary platform for hosting and distributing open-weight LLMs, with model repositories, model cards, and community quantizations"
type: entity
sources:
  - raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md
  - raw/articles/LLM Model Naming Conventions_ How to Read Names and Why They Matter.md
  - raw/articles/Naming Conventions of LLM Models.md
tags:
  - llm
  - model-hub
  - platform
created: "2026-05-01T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: merged
---

# Hugging Face

The primary platform for hosting and distributing open-weight LLMs. Model repositories follow the format `organization/model-name`, and official releases sit alongside community quantizations in separate repos. ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]

## Key Facts

- Repository naming convention: `organization/model-name` -- e.g., `google/gemma-4-4b-it` (official), `bartowski/Qwen3.5-27B-GGUF` (community quantization) ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]
- Key files in a model repo: `README.md` (model card), `config.json` (architecture blueprint), `model.safetensors` (weights, possibly sharded), `tokenizer.json`, `generation_config.json` ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]
- Created the safetensors format as a secure replacement for PyTorch's pickle format (which had arbitrary code execution vulnerabilities) ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]
- Community quantizers like bartowski and unsloth publish GGUF variants in separate repos under their own organization namespace ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]
- Model cards include license, parameter count, architecture (dense vs MoE), context length, quantization availability, and benchmark scores ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]
- The central registry for open-source model checkpoints, hosting every variant (base, instruct, Q4_K_M, GGUF) with the `huggingface_hub` Python library for programmatic metadata inspection via `model_info()` ^[raw/articles/LLM Model Naming Conventions_ How to Read Names and Why They Matter.md]
- The `-hf` suffix in open-source model names (e.g., `Llama-2-7b-chat-hf`) indicates the Hugging Face format/distribution variant ^[raw/articles/Naming Conventions of LLM Models.md]
- To find quantized variants of an official model, check repos like `bartowski/<model-name>-GGUF` (standard GGUF quantizations), `unsloth/<model-name>-GGUF` (dynamic quantization), and `mlx-community/<model-name>-MLX` (Apple Silicon format) ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]

## Related

- [[concepts/safetensors]]
- [[concepts/gguf]]
- [[concepts/quantization]]
- [[concepts/model_naming]]
- [[entities/ollama]]
- [[entities/bartowski]]
