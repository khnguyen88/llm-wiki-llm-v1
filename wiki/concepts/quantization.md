---
title: "Quantization"
summary: "Technique that reduces the numerical precision of LLM weights to shrink file size and speed up inference, trading accuracy for efficiency"
type: concept
sources:
  - raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md
  - raw/articles/LLM Model Naming Conventions_ How to Read Names and Why They Matter.md
  - raw/articles/LLM Naming Explained (What do the options mean_).md
  - raw/articles/How to navigate LLM model names.md
  - raw/articles/Understanding Naming Conventions Of LLM Files_ A Comprehensive Guide.md
  - raw/document/openrouter/openrouter-018-guides-routing-provider-selection-2026-04-29.md
tags:
  - llm
  - quantization
  - compression
  - inference
created: "2026-05-01T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: merged
---

# Quantization

Quantization reduces the numerical precision of model weights -- storing each weight in fewer bits. This shrinks file size and speeds up inference at the cost of some accuracy. Full-precision models store weights as 16-bit or 32-bit floating point numbers; quantization compresses these down to 8-bit, 4-bit, or even 2-bit representations. ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]

## Precision Formats

| Format | Bits per Weight | Description | Typical Use |
|---|---|---|---|
| FP32 | 32 | Full precision, gold standard | Training reference |
| BF16 | 16 | Brain Float 16 (same range as FP32, lower precision) | Default for LLM training |
| FP16 | 16 | Half precision (narrower range than BF16) | GPU inference |
| FP8 | 8 | 8-bit float | Cutting-edge training/inference |
| INT8 | 8 | 8-bit integer, fixed-point | Post-training quantization |
| INT4 / FP4 | 4 | 4-bit, aggressive compression | Local inference on constrained hardware |

^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]

## GGUF Quantization Levels

GGUF quantization naming follows the pattern **Q [bits] _ [method] _ [size]**. The K-quant method uses a two-level scheme: weights grouped into 32-weight blocks packed into 256-weight "super-blocks" with double quantization of scale factors for greater precision. ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]

| Level | Bits | Size (7B model) | Quality | Recommendation |
|---|---|---|---|---|
| Q2_K | 2 | ~2.7 GB | Poor | Emergency only |
| Q3_K_S | 3 | ~2.9 GB | Fair | Very constrained hardware |
| Q4_K_S | 4 | ~3.6 GB | Good | Budget hardware |
| **Q4_K_M** | 4 | ~3.8 GB | ~92% retention | **Mainstream default** |
| Q5_K_S | 5 | ~4.6 GB | Very good | Between Q4 and Q6 |
| Q6_K | 6 | ~5.5 GB | Excellent | Quality-sensitive tasks |
| Q8_0 | 8 | ~7 GB | Near-lossless | When VRAM is not a concern |
| F16 | 16 | ~14 GB | Perfect | Maximum quality baseline |

^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]

### K-Quant S/M/L Suffixes

The S/M/L suffix controls which layers get extra precision:
- **S (Small):** All tensors at the base bit-width -- smallest file
- **M (Medium):** Some attention and feed-forward tensors get higher bit-width -- better quality, slightly larger
- **L (Large):** More tensors at higher bit-width -- best quality, largest file

For example, Q4_K_M stores most tensors at 4-bit but promotes half of the attention and feed-forward weights to 6-bit. ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]

### I-Quants (Importance Matrix)

A newer family of quantization (IQ2_M, IQ3_M, IQ4_XS) uses importance matrices to identify and protect critical weights during quantization. IQ4_XS can compress more aggressively than Q4_K_M with comparable quality. These are produced by quantizers like unsloth. ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]

## GPU-Native Quantization Methods

| Format | Creator | Key Advantage | Hardware |
|---|---|---|---|
| AWQ | MIT / NVIDIA | Activation-aware, ~95% quality at 4-bit, fastest with Marlin kernel | NVIDIA GPU only |
| GPTQ | Frantar et al. | First practical LLM quantization, wide tool support | NVIDIA GPU only |
| EXL2 | turboderp | Per-layer mixed bit-widths (2-8 bit), fastest interactive inference | NVIDIA GPU only |

These produce safetensors files (not GGUF) and have no CPU fallback. ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]

## Quantization Decision Guide

- On CPU or mixed CPU/GPU: GGUF (Q4_K_M default)
- On NVIDIA GPU, maximum throughput: AWQ with Marlin kernel
- On NVIDIA GPU, maximum quality-per-byte: EXL2 ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]

Preference hierarchy: prefer a larger model at lower quantization over a smaller model at higher quantization -- a 14B at Q4_K_M almost always beats a 7B at Q8_0. ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]

Concrete vRAM impact: Llama 405B drops from 900+ GB at fp16 to ~450 GB at fp8. ^[raw/articles/How to navigate LLM model names.md] Neural Magic uses notation "w4a16" (4-bit weights with 16-bit activations). ^[raw/articles/How to navigate LLM model names.md]

## OpenRouter Quantization Filtering

On OpenRouter, the `quantizations` field in the `provider` request object filters providers by quantization level. Available values: `int4`, `int8`, `fp4`, `fp6`, `fp8`, `fp16`, `bf16`, `fp32`, and `unknown`. By default, requests are load-balanced across all providers ordered by price; specifying quantizations restricts routing to providers offering those levels. Quantized models may exhibit degraded performance for certain prompts depending on the method used. ^[raw/document/openrouter/openrouter-018-guides-routing-provider-selection-2026-04-29.md]

## Related

- [[concepts/gguf]]
- [[concepts/safetensors]]
- [[concepts/model_naming]]
- [[concepts/provider_routing]]
- [[entities/openrouter]]
- [[entities/ollama]]
- [[entities/hugging_face]]
- [[summaries/openrouter-guides-routing-provider-selection]]
