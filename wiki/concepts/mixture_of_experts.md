---
title: "Mixture of Experts"
summary: "Architecture where a router selects only a fraction of parameters (experts) per token, giving large-model knowledge at small-model compute cost"
type: concept
sources:
  - raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md
tags:
  - llm
  - architecture
  - moe
  - efficiency
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Mixture of Experts

Mixture of Experts (MoE) is an architecture where the model contains multiple "expert" sub-networks and a router selects only a few experts per token — the rest stay idle. This gives the knowledge capacity of a much larger model at a fraction of the compute cost per token, but requires enough RAM to hold all parameters since the router needs access to every expert. ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]

## Key Points

- MoE models encode their size as TotalB-AActiveB (e.g., 35B-A3B means 35B total parameters, 3B active per token) ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]
- RAM requirement is based on total parameters (all experts must be in memory); compute cost is based on active parameters (only selected experts run) ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]
- Almost every major 2026 LLM release uses MoE: Qwen 3.5, Gemma 4, Llama 4, DeepSeek-V3, GLM-5 ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]
- Practical example: Qwen3.5-35B-A3B has 35B total parameters (~20GB at Q4_K_M) but runs at the speed of a 3B model ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]
- Dense models (all parameters active on every token) are named by just the parameter count (e.g., 32B, 70B) ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]

## Details

The tradeoff is memory for intelligence. An MoE model gives knowledge capacity of a much larger model at a fraction of the compute cost per token, but requires RAM for all parameters. The router needs access to every expert even if it only activates a few at a time. ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]

Notable MoE models as of April 2026: Qwen3.5-35B-A3B and 122B-A10B and 397B-A17B, Llama 4 Scout (109B/17B, 16 experts) and Maverick (400B/17B, 128 experts), Gemma 4 26B-A4B, DeepSeek-V3 (671B/37B), GLM-5 (744B/40B), and Mistral Large 3 (675B/41B). ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]

## Related

- [[concepts/quantization]]
- [[concepts/gguf]]
- [[entities/qwen]]
- [[entities/gemma]]
- [[entities/llama]]
- [[entities/deepseek]]