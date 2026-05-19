---
title: "LLM Model Names Decoded: A Developer's Guide to Parameters, Quantization & Formats"
summary: "Comprehensive guide by Dylan Boudro (Starmorph, April 2026) decoding every component of LLM model names -- parameters, training variants, quantization levels, file formats, MoE architecture, community fine-tunes, and a decision framework for model selection"
type: summary
sources:
  - raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md
tags:
  - llm
  - naming-conventions
  - quantization
  - gguf
  - safetensors
  - moe
  - distillation
  - model-selection
created: "2026-05-01T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
---

# LLM Model Names Decoded: A Developer's Guide to Parameters, Quantization & Formats

## Summary

This extensive guide by Dylan Boudro (April 2026) provides a complete reference for decoding LLM model names. It covers the anatomy of model names, parameter sizes, training variants, quantization precision formats, GGUF quantization levels, GPU-native quantization methods (AWQ, GPTQ, EXL2), file formats (GGUF, Safetensors, MLX), format compatibility, dense vs MoE architectures, community fine-tunes, the 2026 model landscape, Hugging Face model cards, a decision framework, and a glossary. ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]

## Anatomy of a Model Name

The general pattern: `[Org/] Family-Version-Size [-Active] -Training [-Format] [-Quantization]`

| Component | Example Value | Meaning |
|---|---|---|
| Organization | `bartowski` | Community quantizer who published the variant |
| Family | `Qwen3.5` | Model family and generation |
| Size | `32B` | 32 billion parameters |
| Training | `Instruct` | Instruction-tuned (follows prompts) |
| Format | `GGUF` | File format for local inference |
| Quantization | `Q4_K_M` | 4-bit precision, K-quant method, medium block size |

^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]

## Parameter Size Tiers

| Tier | Parameter Range | Approx Q4_K_M Size | Best For |
|---|---|---|---|
| Tiny | 1-3B | 2-3 GB | Edge devices, mobile |
| Small | 4-9B | 3-6 GB | Chat, summarization, simple coding |
| Medium | 13-14B | 8-10 GB | Strong coding, reasoning |
| Large | 27-32B | 18-22 GB | Complex reasoning |
| Extra Large | 70B+ | 40+ GB | Near-frontier quality |

Rule of thumb: parameter count in billions x 0.6 = approximate file size in GB at Q4_K_M. ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]

## GGUF Quantization Levels

| Level | Bits | Size (7B model) | Quality | Recommendation |
|---|---|---|---|---|
| Q2_K | 2 | ~2.7 GB | Poor | Emergency only |
| Q3_K_S | 3 | ~2.9 GB | Fair | Very constrained |
| Q4_K_S | 4 | ~3.6 GB | Good | Budget hardware |
| **Q4_K_M** | 4 | ~3.8 GB | 92% retention | **Mainstream default** |
| Q5_K_S | 5 | ~4.6 GB | Very good | Between Q4 and Q6 |
| Q6_K | 6 | ~5.5 GB | Excellent | Quality-sensitive |
| Q8_0 | 8 | ~7 GB | Near-lossless | Plenty of RAM |
| F16 | 16 | ~14 GB | Perfect | Maximum quality baseline |

^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]

## Model Format Comparison

| Format | Creator | Extension | Best For | Pros | Cons |
|---|---|---|---|---|---|
| GGUF | Georgi Gerganov (llama.cpp) | .gguf | Local inference | Single-file, CPU-friendly, 2-8 bit quantization | Needs conversion from safetensors, slower than GPU-native |
| Safetensors | Hugging Face | .safetensors | Training, GPU inference | Secure (no code exec), 76x faster load than pickle | Full-precision requires substantial VRAM |
| MLX | Apple ML Research | .safetensors (MLX) | Apple Silicon | Leverages unified memory, optimized for Mac | Apple Silicon only |

^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]

## Key Quotes

> "GGUF is for local inference. Safetensors is for everything else -- GPU inference with vLLM, training, fine-tuning, and as the canonical format on HuggingFace."

> "The sweet spot for most users is Q4_K_M. It's the default quantization in Ollama, retains ~92% of the original model's quality, and cuts file size by roughly 75% compared to FP16."

> "A well-trained 14B model frequently outperforms a mediocre 70B. Training data quality, architecture choices, and fine-tuning matter as much as raw parameter count."

> "You cannot fine-tune from GGUF. If you want to fine-tune, start with the safetensors version, train with LoRA/QLoRA, then convert the result to GGUF for serving."
