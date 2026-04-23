---
title: "LLM Naming Conventions"
type: concept
date: 2026-04-23
sources:
  - raw/articles/How to navigate LLM model names.md
  - raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md
  - raw/articles/LLM Model Naming Conventions_ How to Read Names and Why They Matter.md
  - raw/articles/LLM Naming Explained (What do the options mean_).md
  - raw/articles/Naming Conventions of LLM Models.md
  - raw/articles/Understanding Naming Conventions Of LLM Files_ A Comprehensive Guide.md
tags:
  - llm
  - naming-conventions
  - deployment
---

# LLM Naming Conventions

LLM model names encode structured metadata about architecture, size, training stage, format, and quantization. While not strictly standardized, the conventions are consistent enough to serve as a first-pass filter for model selection.

## General Pattern

Open-weight models typically follow:
`[organization/]family-version-size[-active]-training[-format][-quantization]`

Paid/proprietary models follow a product-oriented pattern:
`[family][version][variant/capability tier]`

## Common Components

| Component | Example | Meaning |
|-----------|---------|---------|
| **Organization** | `meta-llama/`, `google/`, `bartowski/` | Publisher or quantizer |
| **Family** | `Llama`, `Gemma`, `Qwen`, `GPT` | Model lineage |
| **Version** | `3.1`, `4`, `v0.3` | Release generation |
| **Size** | `7B`, `70B`, `278M` | Parameter count (billions or millions) |
| **Active (MoE)** | `35B-A3B`, `8x7B` | Total params + active params per token |
| **Training** | `Instruct`, `Chat`, `Base`, `Code` | Post-training specialization |
| **Context** | `8k`, `32k`, `128k`, `10M` | Maximum context window |
| **Format** | `GGUF`, `safetensors`, `MLX` | File/serialization format |
| **Quantization** | `Q4_K_M`, `FP16`, `INT8` | Weight precision and compression method |

## Paid vs Open-Source Naming

- **Paid models** (GPT-4o, Gemini 1.5 Pro, Claude 3 Sonnet) use branding tiers: Pro, Flash, Ultra, Mini, Turbo. Designed for non-technical users.
- **Open-source models** (Llama-3.1-8B-Instruct-GGUF-Q4_K_M) are engineering artifacts with explicit technical metadata in the name.

## Common Suffixes

| Suffix | Meaning |
|--------|---------|
| `Base` | Pretrained only, next-token prediction |
| `Instruct` / `IT` | Instruction-tuned for prompt following |
| `Chat` | Optimized for multi-turn conversation |
| `Vision` / `VL` | Supports image input |
| `Code` / `Coder` | Fine-tuned for code generation |
| `Embedding` | Generates vector embeddings |
| `Guard` / `Guardian` | Safety/content filtering |
| `Reasoning` / `Thinking` | Chain-of-thought optimized |
| `Distilled` / `Distill` | Smaller model trained from a larger teacher |
| `LoRA` | Fine-tuned with Low-Rank Adaptation adapters |
| `Abliterated` | Safety refusals removed post-training |
| `Uncensored` | Trained on unfiltered data |

## Size Hierarchy

General convention: `xxl > xl > large > base > small > mini`

Parameter counts: `M` = millions, `B` = billions.

## Key Insight

Naming conventions are useful heuristics, not guarantees. A name helps narrow choices quickly, but you should still verify the model card and benchmark on your specific task set before deployment.

## Related

- [[concepts/parameter_counts]]
- [[concepts/model_quantization]]
- [[concepts/model_formats]]
- [[concepts/training_variants]]
- [[concepts/mixture_of_experts]]
- [[concepts/model_distillation]]
- [[summaries/how-to-navigate-llm-model-names]]
- [[summaries/llm-model-names-decoded]]
- [[summaries/llm-model-naming-conventions]]
- [[summaries/llm-naming-explained]]
- [[summaries/naming-conventions-of-llm-models]]
- [[summaries/understanding-naming-conventions-of-llm-files]]
