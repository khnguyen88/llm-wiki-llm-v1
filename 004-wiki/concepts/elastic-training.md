---
title: "Elastic Training"
summary: "Training technique where sub-models of varying depths, expert capacities, and routing sparsity are jointly optimized in a single pre-training run, enabling efficient model extraction at multiple scales"
type: concept
sources:
  - raw/articles/baidu-ernie-5.1-0508-release.md
tags:
  - llm
  - training
  - moe
  - efficiency
  - baidu
created: "2026-05-12T12:00:00Z"
updated: "2026-05-12T12:00:00Z"
confidence: 0.85
provenance: extracted
---

# Elastic Training

Elastic training (also called multi-dimensional elastic pre-training or the Once-For-All framework) is a training paradigm where a large number of sub-models with varying depths, expert capacities, and routing sparsity levels are jointly optimized within a single pre-training run. This constructs a sub-model matrix spanning diverse parameter scales and computational budgets, allowing an optimal sub-network to be extracted at any desired scale without retraining. ^[001a-raw/articles/baidu-ernie-5.1-0508-release.md]

## Three Elastic Dimensions

| Dimension | Mechanism | Effect |
|-----------|-----------|--------|
| Elastic depth | Randomly vary active Transformer layers during training | Sub-models at different depths share weights and learn shallow/deep representations |
| Elastic width / expert capacity | Dynamically vary the number of experts participating in routing | Models learn under full and reduced expert-pool configurations |
| Elastic sparsity | Variable Top-k routing mechanism | Fewer active experts reduces inference cost; more enhances capability |

^[001a-raw/articles/baidu-ernie-5.1-0508-release.md]

## Key Result

ERNIE 5.1, extracted from the ERNIE 5.0 elastic training matrix, compresses total parameters to ~1/3 and active parameters to ~1/2 of ERNIE 5.0 while achieving leading performance at its scale with only ~6% of the pre-training cost of comparable models. ^[001a-raw/articles/baidu-ernie-5.1-0508-release.md]

## Origins

- Proposed by Baidu's R&D team for the ERNIE model family ^[001a-raw/articles/baidu-ernie-5.1-0508-release.md]
- Builds on the Once-For-All (OFA) network architecture concept from MIT Han Lab's earlier work on training skinny sub-networks from a single super-network

## Related

- [[004-wiki/concepts/mixture-of-experts]]
- [[004-wiki/entities/ernie]]
- [[004-wiki/entities/baidu]]
- [[004-wiki/concepts/disaggregated-rl]]
- [[004-wiki/summaries/baidu-ernie-5.1-0508-release]]