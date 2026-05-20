---
title: "ERNIE"
summary: "Baidu's family of large language models using MoE architecture, elastic pre-training, and multi-teacher on-policy distillation; ERNIE 5.1 ranks 4th globally on Arena Search"
type: entity
sources:
  - raw/articles/baidu-ernie-5.1-0508-release.md
tags:
  - llm
  - baidu
  - ernie
  - moe
  - chinese-ai
  - model-family
created: "2026-05-12T12:00:00Z"
updated: "2026-05-12T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# ERNIE

Baidu's family of large language models (Enhanced Representation through kNowledge IntEgration). ERNIE 5.1, released May 8, 2026, inherits ERNIE 5.0's pre-training foundation while compressing total parameters to ~1/3 and active parameters to ~1/2, achieving leading performance at its scale with only ~6% of comparable models' pre-training cost. ^[raw/articles/baidu-ernie-5.1-0508-release.md]

## Key Facts

- ERNIE 5.1: compressed from ERNIE 5.0 — ~1/3 total params, ~1/2 active params ^[raw/articles/baidu-ernie-5.1-0508-release.md]
- Pre-training cost: ~6% of comparable models at the same scale ^[raw/articles/baidu-ernie-5.1-0508-release.md]
- Arena Search score: 1,223 (4th globally, 1st among Chinese models) as of May 9, 2026 ^[raw/articles/baidu-ernie-5.1-0508-release.md]
- AIME26 (with tool use): 99.6, second only to Gemini 3.1 Pro ^[raw/articles/baidu-ernie-5.1-0508-release.md]
- Agentic capabilities: surpasses DeepSeek-V4-Pro on τ³-bench and SpreadsheetBench-Verified ^[raw/articles/baidu-ernie-5.1-0508-release.md]
- Creative writing: approaches Gemini 3.1 Pro in internal evaluations ^[raw/articles/baidu-ernie-5.1-0508-release.md]
- Uses MoE architecture with elastic depth, width, and sparsity ^[raw/articles/baidu-ernie-5.1-0508-release.md]
- Trained using PaddlePaddle's disaggregated RL infrastructure ^[raw/articles/baidu-ernie-5.1-0508-release.md]
- Post-training: four-stage MOPD pipeline (SFT → Expert Training → OPD → General RL) ^[raw/articles/baidu-ernie-5.1-0508-release.md]

## Related

- [[004-wiki/entities/baidu]]
- [[004-wiki/entities/paddlepaddle]]
- [[004-wiki/entities/deepseek]]
- [[004-wiki/concepts/mixture_of_experts]]
- [[004-wiki/concepts/elastic_training]]
- [[004-wiki/concepts/disaggregated_rl]]
- [[004-wiki/concepts/on_policy_distillation]]
- [[004-wiki/concepts/distillation]]
- [[004-wiki/summaries/baidu-ernie-5.1-0508-release]]