---
title: "LLM Model Names Decoded: A Developer's Guide to Parameters, Quantization & Formats"
type: summary
date: 2026-04-23
sources:
  - raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md
tags:
  - llm
  - naming-conventions
  - quantization
  - model-formats
  - moe
  - local-inference
---

# LLM Model Names Decoded

**Author:** [[entities/dylan_boudro|Dylan Boudro]]  
**Source:** [Starmorph Blog](https://blog.starmorph.com/blog/llm-model-names-decoded)  
**Published:** 2026-04-05

## Summary

A comprehensive developer's guide decoding every component of open-weight LLM model names, including parameter counts, training variants, quantization schemes, file formats, architecture types (Dense vs MoE), and community fine-tunes. Includes a 2026 model landscape overview and decision framework for choosing models.

## Anatomy of a Model Name

General pattern: `[Org/] Family-Version-Size [-Active] -Training [-Format] [-Quantization]`

Example: `bartowski/Qwen3.5-32B-Instruct-GGUF-Q4_K_M`
- Organization: `bartowski` (community quantizer)
- Family: `Qwen3.5`
- Size: `32B` (32 billion parameters)
- Training: `Instruct`
- Format: `GGUF`
- Quantization: `Q4_K_M` (4-bit K-quant, medium blocks)

## Parameters and Size Tiers

| Tier | Range | RAM (Q4_K_M) | Best For |
|------|-------|--------------|----------|
| Tiny | 1-3B | 2-3 GB | Edge devices |
| Small | 4-9B | 3-6 GB | General chat |
| Medium | 13-14B | 8-10 GB | Coding, reasoning |
| Large | 27-32B | 18-22 GB | Complex reasoning |
| Extra Large | 70B+ | 40+ GB | Near-frontier quality |

Rule of thumb for Q4_K_M GGUF: multiply parameter count in billions by ~0.6 for approximate file size in GB.

## Training Variants

- **Base**: Pretrained only, next-token prediction. For fine-tuning and research.
- **Instruct / IT**: Fine-tuned on instruction-response pairs. The default choice for most use cases.
- **Chat**: Further optimized for multi-turn conversations via RLHF or DPO.
- **Other suffixes**: `-DPO`, `-RLHF`, `-reasoning`, `-vision`, `-coder`.

## Quantization

### Precision Formats
| Format | Bits | Typical Use |
|--------|------|-------------|
| FP32 | 32 | Training reference |
| BF16 | 16 | Default LLM training |
| FP16 | 16 | GPU inference |
| FP8 | 8 | Cutting-edge inference |
| INT8 | 8 | Post-training quantization |
| INT4 / FP4 | 4 | Local inference |

### GGUF Quantization Levels
Q4_K_M is the mainstream default, retaining ~92% quality while cutting file size by ~75% compared to FP16.

### GPU-Native Quantization
- **AWQ**: Activation-aware, ~95% quality at 4-bit, fastest with Marlin kernel (NVIDIA only).
- **GPTQ**: First practical LLM quantization, wide tool support (NVIDIA only).
- **EXL2**: Per-layer mixed bit-widths, fastest interactive inference (NVIDIA only).

## Model Formats

- **GGUF**: Single-file format for local inference (Ollama, LM Studio, llama.cpp). CPU-friendly.
- **Safetensors**: Hugging Face secure serialization standard. Fast loading, no arbitrary code execution risk.
- **MLX**: Apple Silicon-native, leverages unified memory.
- **ONNX / TensorRT / PyTorch .bin**: Specialized or legacy formats.

## Mixture of Experts (MoE)

MoE models encode total and active parameters (e.g., `35B-A3B`). RAM is based on total parameters; compute cost is based on active parameters. Examples: Qwen3.5-35B-A3B, Llama 4 Scout (109B total / 17B active), DeepSeek-V3 (671B total / 37B active).

## Community Fine-Tunes and Variants

Common derivative suffixes: `-distilled`, `-abliterated`, `-uncensored`, `-reasoning`, `-LoRA`.

Key community contributors:
- **bartowski**: Most prolific GGUF quantizer on HuggingFace.
- **unsloth** (Daniel Han): Dynamic 2.0 quantization, 2-5x faster fine-tuning.
- **Nous Research** (Teknium): Hermes series fine-tunes.
- **Eric Hartford**: Dolphin uncensored model family.
- **TheBloke**: Pioneer of community quantization (less active since 2024).

## 2026 Model Landscape

- **Gemma 4** (Google): Natively multimodal across all sizes. 26B-A4B MoE near-31B quality.
- **Qwen 3.5** (Alibaba): Widest size range, hybrid thinking mode, Gated DeltaNet architecture.
- **Llama 4** (Meta): First MoE generation. Scout: 10M token context window.
- **DeepSeek R1**: Best local reasoning via distillation.
- **Phi-4** (Microsoft): 14B beats 671B models on some math benchmarks.
- **GLM-5** (Zhipu AI): 744B/40B active, MIT license.

## Decision Framework

1. Know hardware limits first.
2. Explore community usage (Ollama library, HuggingFace trending, OpenRouter, LMSYS Arena).
3. Choose quantization: Q4_K_M default, Q5_K_M for extra RAM, Q6_K/Q8_0 for quality-sensitive tasks.
4. Match format to tool: GGUF for local, Safetensors for training/fine-tuning, MLX for Apple Silicon.

## Key Claims

- A well-trained 14B model can outperform a mediocre 70B. Training data quality and architecture matter as much as parameter count.
- Prefer a larger model at lower quantization over a smaller model at higher quantization.
- MoE is everywhere in 2026: massive total parameters for knowledge, small active parameters for speed.

## Related

- [[concepts/llm_naming_conventions]]
- [[concepts/model_quantization]]
- [[concepts/parameter_counts]]
- [[concepts/model_formats]]
- [[concepts/training_variants]]
- [[concepts/mixture_of_experts]]
- [[concepts/model_distillation]]
- [[entities/dylan_boudro]]
- [[entities/bartowski]]
- [[entities/unsloth]]
