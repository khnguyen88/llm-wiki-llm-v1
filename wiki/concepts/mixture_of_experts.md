---
title: "Mixture of Experts"
type: concept
date: 2026-04-23
sources:
  - raw/articles/How to navigate LLM model names.md
  - raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md
tags:
  - llm
  - moe
  - architecture
  - inference
---

# Mixture of Experts (MoE)

Mixture of Experts is an architectural methodology where only a fraction of the model's parameters are "active" for each request. An expert layer routes each token to a single "expert" sub-network, plus shared parameters used by all experts.

## How MoE Works

- Instead of every token being processed by every parameter, a router selects only a few experts per token.
- This allows models to leverage the knowledge capacity of much larger models while maintaining the inference speed of smaller models.
- **RAM required:** Based on *total* parameters (all experts must be in memory).
- **Compute cost:** Based on *active* parameters (only selected experts run).

## Naming Conventions

Two common patterns appear in model names:

1. **Expert count format**: `Mixtral-8x7B` → 8 experts, 7B active parameters per token. Total size is 46B parameters (not 56B because some parameters are shared).
2. **Total-Active format**: `Llama-4-Scout-17B-16E` or `35B-A3B` → Total parameters and active parameters explicitly stated.

## Notable MoE Models (2026)

| Model | Total Params | Active Params | Experts | Notable Feature |
|-------|-------------|---------------|---------|-----------------|
| Qwen3.5-35B-A3B | 35B | 3B | MoE | Runs on 8GB+ VRAM |
| Qwen3.5-122B-A10B | 122B | 10B | MoE | Near-frontier quality |
| Qwen3.5-397B-A17B | 397B | 17B | MoE | Frontier-class open model |
| Llama 4 Scout | 109B | 17B | 16 | 10M token context window |
| Llama 4 Maverick | 400B | 17B | 128 | Beats GPT-4o on many benchmarks |
| Gemma 4 26B-A4B | 26B | 4B | MoE | Near-31B quality at 4B compute |
| DeepSeek-V3 | 671B | 37B | MoE | Strong coding + general |
| GLM-5 | 744B | 40B | MoE | MIT licensed |

## Key Insight

MoE trades memory for intelligence: you need enough RAM to hold all experts, but inference speed is determined by active parameters. In 2026, MoE is nearly ubiquitous in major releases.

## Related

- [[concepts/llm_naming_conventions]]
- [[concepts/parameter_counts]]
- [[summaries/how-to-navigate-llm-model-names]]
- [[summaries/llm-model-names-decoded]]
