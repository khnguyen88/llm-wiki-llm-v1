---
title: "Model Quantization"
type: concept
date: 2026-04-23
sources:
  - raw/articles/How to navigate LLM model names.md
  - raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md
  - raw/articles/LLM Model Naming Conventions_ How to Read Names and Why They Matter.md
  - raw/articles/LLM Naming Explained (What do the options mean_).md
  - raw/articles/Understanding Naming Conventions Of LLM Files_ A Comprehensive Guide.md
tags:
  - llm
  - quantization
  - inference
  - deployment
---

# Model Quantization

Quantization is the process of reducing the numerical precision of model weights, shrinking file size and memory requirements at a potential cost to accuracy and response quality.

## Core Principle

Models are originally trained in high-precision formats (typically FP32 or BF16). Quantization converts weights to lower bit-widths for deployment. The trade-off is between resource efficiency (lower bits) and quality retention (higher bits).

## Precision Formats

| Format | Bits | Description | Typical Use |
|--------|------|-------------|-------------|
| **FP32** | 32 | Full precision, gold standard | Training reference |
| **BF16** | 16 | Brain Float 16 (same range as FP32) | Default for LLM training |
| **FP16** | 16 | Half precision | GPU inference |
| **FP8** | 8 | 8-bit float | Cutting-edge training/inference |
| **INT8** | 8 | 8-bit integer | Post-training quantization |
| **INT4 / FP4** | 4 | 4-bit, aggressive compression | Local inference on constrained hardware |

## GGUF Quantization Scheme

GGUF (GPT-Generated Unified Format) uses a naming scheme: `Q[bits]_[method]_[size]`

- **Q** = quantized
- **Number** = bits per weight (2, 3, 4, 5, 6, 8)
- **K** = K-quant method (smarter bit allocation across layers)
- **S / M / L** = Small / Medium / Large block size

### GGUF Levels (7B model reference)

| Level | Bits | Size | Quality | Recommendation |
|-------|------|------|---------|----------------|
| Q2_K | 2 | ~2.7 GB | Poor | Emergency only |
| Q3_K_S | 3 | ~2.9 GB | Fair | Very constrained hardware |
| Q3_K_M | 3 | ~3.1 GB | Fair | Tight budgets |
| Q4_K_S | 4 | ~3.6 GB | Good | Budget hardware |
| **Q4_K_M** | 4 | ~3.8 GB | Good (~92% retention) | **Mainstream default** |
| Q5_K_S | 5 | ~4.6 GB | Very good | Between Q4 and Q6 |
| Q5_K_M | 5 | ~4.8 GB | Very good | Extra RAM available |
| Q6_K | 6 | ~5.5 GB | Excellent | Quality-sensitive tasks |
| Q8_0 | 8 | ~7 GB | Near-lossless | When VRAM isn't a concern |
| F16 | 16 | ~14 GB | Perfect | Maximum quality baseline |

### K-Quant Method

K-quants use two-level quantization. Weights are grouped into 32-weight blocks packed into 256-weight "super-blocks." Per-block scale factors are computed and then quantized again (double quantization). The S/M/L suffix controls which layers get extra precision.

### I-Quants (Importance Matrix)

Newer quantization family (IQ2_M, IQ3_M, IQ4_XS) uses importance matrices to protect critical weights. IQ4_XS can compress more aggressively than Q4_K_M with comparable quality.

## GPU-Native Quantization

These formats run faster on NVIDIA GPUs but lack CPU fallback:

| Format | Creator | Key Advantage |
|--------|---------|---------------|
| **AWQ** | MIT / NVIDIA | Activation-aware, ~95% quality at 4-bit |
| **GPTQ** | Frantar et al. | First practical LLM quantization |
| **EXL2** | turboderp | Per-layer mixed bit-widths (2-8 bit) |

These are stored as safetensors and run via vLLM, ExLlamaV2, or HuggingFace Transformers.

## When to Use What

- **CPU or mixed CPU/GPU** → GGUF (Q4_K_M default)
- **NVIDIA GPU, maximum throughput** → AWQ with Marlin kernel
- **NVIDIA GPU, maximum quality-per-byte** → EXL2
- **Apple Silicon** → MLX (native unified memory)

## Key Insight

Prefer a larger model at lower quantization over a smaller model at higher quantization. A 14B model at Q4_K_M almost always beats a 7B model at Q8_0.

## Related

- [[concepts/llm_naming_conventions]]
- [[concepts/parameter_counts]]
- [[concepts/model_formats]]
- [[summaries/llm-model-names-decoded]]
- [[summaries/llm-naming-explained]]
- [[summaries/understanding-naming-conventions-of-llm-files]]
