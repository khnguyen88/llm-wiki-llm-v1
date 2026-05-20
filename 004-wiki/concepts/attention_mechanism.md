---
title: "Attention Mechanism"
summary: The core operation in transformers where each token computes query, key, and value vectors; attention scores determine how much each token attends to every other token, enabling parallel processing during training but sequential processing during inference
type: concept
sources:
  - raw/transcripts/adam-rosler-2026-05-12.md
tags:
  - attention
  - transformers
  - inference
  - self-attention
created: "2026-05-12T12:00:00Z"
updated: "2026-05-12T12:00:00Z"
confidence: 0.95
provenance: extracted
---

# Attention Mechanism

The core operation in transformers that enables every token to look at every other token. For each token, the model computes three vectors from its embedding: a **query** (what the token is searching for), a **key** (what the token advertises), and a **value** (what the token contributes). The query dots against every prior key to produce attention scores, which weight the corresponding values. The weighted sum of values becomes the input for predicting the next token.^[raw/transcripts/adam-rosler-2026-05-12.md]

## Key, Value, and Query

| Vector | Role | How computed |
|--------|------|-------------|
| Key (K) | What the token advertises if another token looks at it | Embedding multiplied by a learned key matrix |
| Value (V) | What the token contributes if selected | Embedding multiplied by a learned value matrix |
| Query (Q) | What the current token is searching for | Embedding multiplied by a learned query matrix |

Splitting each token's role into "advertising" (key) and "contributing" (value) allows the model to learn different patterns of advertisement and contribution. The key and value matrices are stored in the model file and were learned during pre-training.^[raw/transcripts/adam-rosler-2026-05-12.md]

## Parallel Training, Sequential Inference

The 2017 "Attention Is All You Need" paper made training dramatically faster by enabling every token to attend to every other token in parallel. But at inference time, each new token depends on the tokens before it, forcing sequential generation. This is the fundamental tension that makes [[004-wiki/concepts/kv_cache|KV cache]] essential.^[raw/transcripts/adam-rosler-2026-05-12.md]

## Computational Cost

Multiplying a 4,000-dimensional embedding by a 4,000x4,000 matrix requires 16 million multiplications. Across 40 stacked layers, each doing its own attention, this yields approximately 600 million multiplications per token for keys alone, and the same for values -- roughly 2 billion math operations per token just for attention setup.^[raw/transcripts/adam-rosler-2026-05-12.md]

## Attention Variants

| Variant | KV Heads | Quality | Speed | Used By |
|---------|----------|---------|-------|---------|
| Multi-Head Attention (MHA) | H (one per query head) | Best | Slowest | GPT-3, original Transformer |
| Multi-Query Attention (MQA) | 1 | Degraded | Fastest | PaLM 540B, Falcon 40B |
| Grouped Query Attention (GQA) | G (1 < G < H) | Near-MHA | Near-MQA | Llama 3, Mistral |
| Multi-Head Latent Attention (MLA) | Low-rank compressed | Near-MHA | High | DeepSeek-V2 |

## Related

- [[004-wiki/concepts/kv_cache]]
- [[004-wiki/concepts/token_embedding]]
- [[004-wiki/summaries/adam-rosler-kv-cache-2026-05-12]]