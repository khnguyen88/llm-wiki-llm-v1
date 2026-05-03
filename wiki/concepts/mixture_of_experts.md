---
title: "Mixture of Experts"
summary: "Architecture where a router selects only a fraction of parameters (experts) per token, giving large-model knowledge at small-model compute cost"
type: concept
sources:
  - raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md
  - raw/articles/How to navigate LLM model names.md
tags:
  - llm
  - architecture
  - moe
  - efficiency
created: "2026-05-01T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: merged
---

# Mixture of Experts

Mixture of Experts (MoE) is an architecture where the model contains multiple "expert" sub-networks and a router selects only a few experts per token -- the rest stay idle. This gives the knowledge capacity of a much larger model at a fraction of the compute cost per token, but requires enough RAM to hold all parameters since the router needs access to every expert. ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]

## Naming Conventions

MoE models encode their size in a special format indicating both total and active parameters. Two conventions exist:

| Convention | Example | Format | Meaning |
|---|---|---|---|
| Active-in-name | Qwen3.5-35B-A3B | `TotalB-A-ActiveB` | 35B total, 3B active per token |
| Experts-in-name | Llama-4-Scout-17B-16E | `ActiveB-NExperts` | 16 experts, 17B active per token |
| Legacy | Mixtral-8x7B-v0.1 | `NxP` | 8 experts, 7B active per token |

^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md] ^[raw/articles/How to navigate LLM model names.md]

Key distinction: MoE total parameter count is always less than experts x active params because some parameters are shared across all experts. Mixtral's 8x7B is 46B total, not 56B; Llama 4 Scout's 17B-16E is 109B total, not 272B. ^[raw/articles/How to navigate LLM model names.md]

## Tradeoffs

- RAM requirement: based on total parameters (all experts must be in memory)
- Compute cost: based on active parameters (only selected experts run)
- An MoE model trades memory for intelligence -- more RAM for the knowledge of a larger model at the speed of a smaller one ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]

## Notable MoE Models (2026)

| Model | Total Params | Active Params | Experts | Key Feature |
|---|---|---|---|---|
| Qwen3.5-35B-A3B | 35B | 3B | MoE | Runs on 8GB+ VRAM at Q4_K_M |
| Qwen3.5-122B-A10B | 122B | 10B | MoE | Near-frontier quality |
| Qwen3.5-397B-A17B | 397B | 17B | MoE | Frontier-class open model |
| Llama 4 Scout | 109B | 17B | 16 | 10M token context window |
| Llama 4 Maverick | 400B | 17B | 128 | Beats GPT-4o on many benchmarks |
| Gemma 4 26B-A4B | 26B | 4B | MoE | Near-31B quality at 4B compute |
| DeepSeek-V3 | 671B | 37B | MoE | Strong coding + general |
| GLM-5 | 744B | 40B | MoE | MIT licensed, trained on Huawei chips |
| Mistral Large 3 | 675B | 41B | MoE | Apache 2.0, strong multilingual |

^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]

## 2026 Trends

Almost every major 2026 LLM release uses MoE. The pattern is massive total parameters for knowledge, small active parameters for speed. The landscape also features hybrid reasoning (models like Qwen 3.5 toggle between fast responses and chain-of-thought), distillation economy, and growing context windows (Llama 4 Scout: 10M tokens). ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]

## Related

- [[concepts/quantization]]
- [[concepts/model_naming]]
- [[entities/qwen]]
- [[entities/gemma]]
- [[entities/llama]]
- [[entities/deepseek]]
