---
title: "ERNIE 5.1 Officially Released"
summary: "Baidu's ERNIE 5.1 achieves leading performance at its model scale with ~6% of comparable models' pre-training cost, using elastic pre-training, disaggregated RL, and multi-teacher on-policy distillation"
type: summary
sources:
  - raw/articles/baidu-ernie-5.1-0508-release.md
tags:
  - llm
  - baidu
  - ernie
  - moe
  - reinforcement-learning
  - distillation
  - chinese-ai
created: "2026-05-12T12:00:00Z"
updated: "2026-05-12T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# ERNIE 5.1 Officially Released

## Summary

Baidu officially released ERNIE 5.1 on May 8, 2026, inheriting ERNIE 5.0's pre-training foundation while compressing total parameters to approximately one-third and active parameters to approximately one-half. The model achieves leading foundational performance at its scale using only about 6% of the pre-training cost of comparable models. ERNIE 5.1 scored 1,223 on the Arena Search leaderboard, ranking 4th globally and 1st among Chinese models. ^[raw/articles/baidu-ernie-5.1-0508-release.md]

## Performance Highlights

| Benchmark | Result | Context |
|-----------|--------|---------|
| Arena Search (May 9, 2026) | 1,223 points | 4th globally, 1st among Chinese models |
| τ³-bench (agentic) | Surpasses DeepSeek-V4-Pro | Approaching top closed-source models |
| SpreadsheetBench-Verified (agentic) | Surpasses DeepSeek-V4-Pro | Approaching top closed-source models |
| GPQA (knowledge) | Approaches leading closed-source models | — |
| MMLU-Pro (knowledge) | Approaches leading closed-source models | — |
| AIME26 w/ tool use (reasoning) | 99.6 | 2nd only to Gemini 3.1 Pro |
| Creative writing (internal eval) | Approaches Gemini 3.1 Pro | — |

^[raw/articles/baidu-ernie-5.1-0508-release.md]

## Multi-Dimensional Elastic Pre-Training

ERNIE 5.1 is derived from ERNIE 5.0 using an innovative **Once-For-All** elastic training framework. Rather than requiring separate pre-training runs for different model scales, ERNIE 5.0 jointly optimizes sub-models with varying depths, expert capacities, and routing sparsity levels in a single pre-training run, constructing a sub-model matrix spanning diverse parameter scales and compute budgets. ^[raw/articles/baidu-ernie-5.1-0508-release.md]

### Three Elastic Dimensions

| Dimension | Mechanism | Effect |
|-----------|-----------|--------|
| Elastic depth | Randomly vary active Transformer layers during training | Sub-models at different depths share weights |
| Elastic width / expert capacity | Dynamically vary the number of experts participating in routing | Improve expert utilization efficiency |
| Elastic sparsity | Variable Top-k routing mechanism | Trade off inference cost vs. capability |

^[raw/articles/baidu-ernie-5.1-0508-release.md]

The result: ERNIE 5.1 compresses total parameters to ~1/3 and active parameters to ~1/2 of ERNIE 5.0, with pre-training compute at only 6% of comparable models at the same scale. ^[raw/articles/baidu-ernie-5.1-0508-release.md]

## Disaggregated Fully-Asynchronous RL Training

Baidu built a disaggregated RL infrastructure on [[entities/paddlepaddle|PaddlePaddle]] with four decoupled subsystems — training, inference, reward, and agent loop — centered on an RL Controller. Key innovations include: ^[raw/articles/baidu-ernie-5.1-0508-release.md]

| Innovation | Description | Benefit |
|------------|-------------|---------|
| Disaggregated architecture | Control plane fully decoupled from data plane; each subsystem independently deployed and scaled | Pipeline overlap, scalable long-horizon RL |
| FP8 training-inference consistency | Unified FP8 operator library + Rollout Router Replay (R3) with computation-communication overlap | K3 KL divergence reduced by 50%, near-zero latency overhead |
| Heterogeneous elastic scheduling | CPU pooling for logic-intensive tasks (code sandboxes, verifiers) | Better resource utilization, reduced iteration time |

## Multi-Teacher On-Policy Distillation (MOPD)

ERNIE 5.1's post-training uses a four-stage pipeline that decouples expert training from unified capability fusion: ^[raw/articles/baidu-ernie-5.1-0508-release.md]

| Stage | Name | Description |
|-------|------|-------------|
| 1 | Unified SFT | Multi-domain instruction data fine-tuning; establishes foundational instruction-following and tool invocation |
| 2 | Domain Expert Training | Multiple domain-specific expert models (code, reasoning, agentic) trained in parallel with dedicated reward signals |
| 3 | On-Policy Distillation (OPD) | SFT model as student, expert models as teachers; student samples from own policy distribution, learns via token-level reverse KL divergence |
| 4 | General Online RL | Online RL for open-ended chat and creative writing — tasks not amenable to token-level KL distillation due to high-entropy distributions |

Stage 4 (General-RL) is specifically designed for tasks where OPD is insufficient: open-ended chat and creative writing tend to suffer from low distillation efficiency and excessive output probability smoothing when distilled via token-level KL. ^[raw/articles/baidu-ernie-5.1-0508-release.md]

## Creative Capabilities

ERNIE 5.1 emphasizes creative writing performance, claiming precise alignment of "inspiration–emotion–expression" in creative writing, coordinated control of "logic–character–pacing" in long-form narrative, and balanced "knowledge accuracy–stylistic adaptability" in professional content. The model is being progressively rolled out on over ten creative production agent platforms including ISEKAI ZERO, Mulan AI, Diting Huanliu, and Storymaster. ^[raw/articles/baidu-ernie-5.1-0508-release.md]

## Key Quotes

> "ERNIE 5.1 compresses total parameters to approximately one-third and active parameters to approximately one-half, achieving leading foundational performance at its model scale using only about 6% of the pre-training cost of comparable models." ^[raw/articles/baidu-ernie-5.1-0508-release.md]

> "We built an entirely new disaggregated fully-asynchronous reinforcement learning infrastructure, specifically addressing the global optimization challenges posed by training-inference divergence, low resource utilization, and long-tail effects." ^[raw/articles/baidu-ernie-5.1-0508-release.md]

> "Attempting to fuse all capabilities within a single training stage introduces severe multi-objective optimization conflicts, making it extremely difficult to balance performance across different domain tasks and achieve Pareto optimality — improvements in one capability often come at the cost of regressions in another." ^[raw/articles/baidu-ernie-5.1-0508-release.md]

> "Tasks characterized by high-entropy distributions — such as open-ended chat or creative writing — tend to suffer from low distillation efficiency and may cause excessive smoothing of the output probability distribution." ^[raw/articles/baidu-ernie-5.1-0508-release.md]

## Related

- [[entities/baidu]]
- [[entities/ernie]]
- [[entities/paddlepaddle]]
- [[concepts/mixture_of_experts]]
- [[concepts/distillation]]
- [[concepts/elastic_training]]
- [[concepts/disaggregated_rl]]
- [[concepts/on_policy_distillation]]
- [[entities/deepseek]]