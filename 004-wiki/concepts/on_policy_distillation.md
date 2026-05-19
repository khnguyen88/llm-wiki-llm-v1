---
title: "On-Policy Distillation"
summary: "Multi-teacher distillation technique where a student model samples from its own policy distribution and learns from multiple domain experts via token-level reverse KL divergence"
type: concept
sources:
  - raw/articles/baidu-ernie-5.1-0508-release.md
tags:
  - llm
  - training
  - distillation
  - reinforcement-learning
  - baidu
created: "2026-05-12T12:00:00Z"
updated: "2026-05-12T12:00:00Z"
confidence: 0.85
provenance: extracted
---

# On-Policy Distillation

Multi-Teacher On-Policy Distillation (MOPD) is a training technique where a student model samples from its own policy distribution and concurrently learns from multiple domain expert teachers via token-level reverse KL divergence. This efficiently consolidates diverse expert capabilities into a unified parameter space while eliminating the multi-objective optimization conflicts ("seesaw" effect) that arise when trying to fuse all capabilities in a single training stage. ^[raw/articles/baidu-ernie-5.1-0508-release.md]

## The Four-Stage Pipeline

| Stage | Name | Description |
|-------|------|-------------|
| 1 | Unified SFT | Multi-domain instruction fine-tuning establishing foundational capabilities |
| 2 | Domain Expert Training | Parallel training of domain-specific experts (code, reasoning, agentic) with dedicated reward signals |
| 3 | On-Policy Distillation (OPD) | Student samples from own policy, learns from multiple teachers via token-level reverse KL |
| 4 | General Online RL | Online RL for high-entropy tasks (open-ended chat, creative writing) where OPD is insufficient |

^[raw/articles/baidu-ernie-5.1-0508-release.md]

## Why OPD Alone Is Not Enough

Not all tasks are amenable to token-level KL-based distillation. Tasks with high-entropy output distributions — particularly open-ended chat and creative writing — suffer from low distillation efficiency and excessive probability smoothing. The General-RL stage (Stage 4) addresses this by applying online RL directly to the post-OPD model for these domains. ^[raw/articles/baidu-ernie-5.1-0508-release.md]

## The Seesaw Problem

Traditional sequential post-training (SFT → Mixed RL) creates multi-objective optimization conflicts: improving one capability often degrades another. MOPD solves this by training domain experts independently in Stage 2 (eliminating mutual interference) and then fusing their capabilities through OPD in Stage 3. ^[raw/articles/baidu-ernie-5.1-0508-release.md]

## Related

- [[concepts/distillation]]
- [[concepts/disaggregated_rl]]
- [[concepts/elastic_training]]
- [[entities/ernie]]
- [[entities/baidu]]
- [[summaries/baidu-ernie-5.1-0508-release]]