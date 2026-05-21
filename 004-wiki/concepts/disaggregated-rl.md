---
title: "Disaggregated RL"
summary: "Reinforcement learning training architecture that fully decouples training, inference, reward, and agent loop subsystems for efficient, stable, long-horizon agentic RL"
type: concept
sources:
  - raw/articles/baidu-ernie-5.1-0508-release.md
tags:
  - llm
  - reinforcement-learning
  - training
  - infrastructure
  - baidu
created: "2026-05-12T12:00:00Z"
updated: "2026-05-12T12:00:00Z"
confidence: 0.85
provenance: extracted
---

# Disaggregated RL

Disaggregated fully-asynchronous reinforcement learning is a training architecture that decouples the RL control plane into four independent subsystems — training, inference, reward, and agent loop — bridged through high-performance network-based data components. Each subsystem can be independently deployed and scaled, enabling pipeline overlap for long-horizon agentic RL training. ^[001a-raw/articles/baidu-ernie-5.1-0508-release.md]

## Architecture

| Subsystem | Role | Scaling |
|-----------|------|---------|
| Training | Model parameter updates | Independent GPU config |
| Inference | Rollout generation | Independent GPU config |
| Reward | Reward signal computation | Independent GPU config |
| Agent loop | Environment interaction and tool use | Independent CPU/GPU config |

The four subsystems form a pipeline that can be fully overlapped, establishing a scalable foundation for long-horizon asynchronous training. ^[001a-raw/articles/baidu-ernie-5.1-0508-release.md]

## Key Optimizations

- **FP8 training-inference consistency**: Unified FP8 low-precision operator library minimizes precision divergence. Rollout Router Replay (R3) with two-stage computation-communication overlap, dynamic bit-width communication compression, and multi-level KV-Cache pooling reduces K3 KL divergence by 50% with near-zero latency overhead. ^[001a-raw/articles/baidu-ernie-5.1-0508-release.md]
- **Heterogeneous elastic scheduling**: CPU pooling strategy leverages idle cluster CPU compute for logic-intensive tasks (code sandboxes, verifiers), improving resource utilization and reducing training iteration time. ^[001a-raw/articles/baidu-ernie-5.1-0508-release.md]

## Problems Addressed

- Training-inference divergence in long-horizon RL for MoE models ^[001a-raw/articles/baidu-ernie-5.1-0508-release.md]
- Low resource utilization in traditional RL training ^[001a-raw/articles/baidu-ernie-5.1-0508-release.md]
- Long-tail effects in complex agentic tasks ^[001a-raw/articles/baidu-ernie-5.1-0508-release.md]

## Related

- [[004-wiki/entities/ernie]]
- [[004-wiki/entities/baidu]]
- [[004-wiki/entities/paddlepaddle]]
- [[004-wiki/concepts/on-policy-distillation]]
- [[004-wiki/concepts/mixture-of-experts]]
- [[004-wiki/summaries/baidu-ernie-5.1-0508-release]]