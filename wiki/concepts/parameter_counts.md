---
title: "Parameter Counts"
type: concept
date: 2026-04-23
sources:
  - raw/articles/How to navigate LLM model names.md
  - raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md
  - raw/articles/LLM Model Naming Conventions_ How to Read Names and Why They Matter.md
  - raw/articles/Naming Conventions of LLM Models.md
  - raw/articles/Understanding Naming Conventions Of LLM Files_ A Comprehensive Guide.md
tags:
  - llm
  - parameters
  - hardware
  - sizing
---

# Parameter Counts

Parameter counts are the most prominent numerical indicator in LLM names, expressed in billions (B) or millions (M). They indicate model capacity, complexity, and hardware requirements.

## Size Tiers

| Tier | Parameter Range | RAM Needed (Q4_K_M) | Best For |
|------|-----------------|---------------------|----------|
| **Tiny** | 1-3B | 2-3 GB | Edge devices, quick tasks, mobile |
| **Small** | 4-9B | 3-6 GB | General chat, summarization, simple coding |
| **Medium** | 13-14B | 8-10 GB | Strong coding, reasoning, creative writing |
| **Large** | 27-32B | 18-22 GB | Complex reasoning, nuanced writing |
| **Extra Large** | 70B+ | 40+ GB | Near-frontier quality, research |

## Memory Estimation

Approximate raw weight storage: `Memory_weights ≈ P × (b / 8)` where P is parameter count and b is bits per weight.

Rule of thumb for Q4_K_M GGUF: multiply parameter count in billions by ~0.6 for approximate file size in GB.

- 7B model ≈ 4 GB at Q4_K_M
- 32B model ≈ 19 GB at Q4_K_M
- 70B model ≈ 40 GB at Q4_K_M

Examples from sources:
- `granite-3.2-8b-instruct`: fits on an A10 GPU with 24 GB VRAM.
- `llama-3.1-405b-instruct`: requires 900+ GB VRAM at FP16, commonly run on sixteen H100s.

## Bigger Is Not Always Better

A well-trained 14B model can outperform a mediocre 70B model. Training data quality, architecture choices, and fine-tuning matter as much as raw parameter count. Examples:
- Phi-4-reasoning at 14B beats DeepSeek-R1 (671B total) on some math benchmarks.
- Qwen2.5-Coder at 14B scores ~85% on HumanEval, competitive with models 5x its size.

## MoE Parameter Notation

Mixture of Experts models use two numbers:
- **Total parameters**: All experts loaded in memory (determines RAM).
- **Active parameters**: Experts activated per token (determinates compute/speed).

Notation examples:
- `35B-A3B`: 35B total, 3B active.
- `8x7B`: 8 experts, 7B active each (total is not simply 56B due to shared parameters).

## Related

- [[concepts/llm_naming_conventions]]
- [[concepts/model_quantization]]
- [[concepts/mixture_of_experts]]
- [[summaries/llm-model-names-decoded]]
- [[summaries/how-to-navigate-llm-model-names]]
