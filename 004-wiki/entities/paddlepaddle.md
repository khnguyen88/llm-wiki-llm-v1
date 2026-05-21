---
title: "PaddlePaddle"
summary: "Baidu's open-source deep learning framework, serving as the training infrastructure for ERNIE models including disaggregated RL training"
type: entity
sources:
  - raw/articles/baidu-ernie-5.1-0508-release.md
tags:
  - deep-learning
  - framework
  - baidu
  - training-infrastructure
created: "2026-05-12T12:00:00Z"
updated: "2026-05-12T12:00:00Z"
confidence: 0.85
provenance: extracted
---

# PaddlePaddle

Baidu's deep learning framework, used as the foundation for ERNIE's training infrastructure. PaddlePaddle provides a unified training-inference framework that supports ERNIE 5.1's disaggregated RL architecture, including FP8 operator libraries and the Rollout Router Replay (R3) technique for minimizing training-inference divergence in MoE models. ^[001a-raw/articles/baidu-ernie-5.1-0508-release.md]

## Key Facts

- Serves as the training platform for ERNIE model family ^[001a-raw/articles/baidu-ernie-5.1-0508-release.md]
- Provides unified training-inference framework supporting FP8 precision ^[001a-raw/articles/baidu-ernie-5.1-0508-release.md]
- Enables Rollout Router Replay (R3) for training-inference consistency in MoE models ^[001a-raw/articles/baidu-ernie-5.1-0508-release.md]
- Supports heterogeneous elastic resource scheduling (CPU pooling for verifiers and sandboxes) ^[001a-raw/articles/baidu-ernie-5.1-0508-release.md]

## Related

- [[004-wiki/entities/baidu]]
- [[004-wiki/entities/ernie]]
- [[004-wiki/concepts/disaggregated-rl]]