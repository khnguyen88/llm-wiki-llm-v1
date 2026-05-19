---
title: "Grouped Query Attention (GQA)"
summary: An attention variant that shares key-value heads across groups of query heads, interpolating between Multi-Head Attention and Multi-Query Attention to reduce KV cache memory while maintaining near-MHA quality
type: concept
sources:
  - raw/transcripts/adam-rosler-2026-05-12.md
tags:
  - attention
  - kv-cache
  - inference
  - transformers
created: "2026-05-12T12:00:00Z"
updated: "2026-05-12T12:00:00Z"
confidence: 0.85
provenance: inferred
---

# Grouped Query Attention (GQA)

An attention variant introduced by Ainslie et al. (2023) that shares key-value heads across groups of query heads, interpolating between Multi-Head Attention (MHA, where each query head has its own KV head) and Multi-Query Attention (MQA, where all query heads share a single KV head). GQA uses G groups where 1 < G < H, providing a tunable trade-off between quality and inference speed.^[raw/transcripts/adam-rosler-2026-05-12.md]

## Key Properties

- GQA-1 (G=1) is equivalent to MQA; GQA-H (G=H) is equivalent to MHA
- Existing MHA checkpoints can be converted to GQA by mean-pooling KV heads within groups, then fine-tuned with ~5% of original pre-training compute
- GQA-8 achieves quality close to MHA with speed close to MQA

## Memory Impact

For Llama 3 70B at 8K context (FP16):

| Attention Type | KV Heads | KV Cache Size | vs MHA |
|---------------|----------|---------------|--------|
| MHA | 64 | 20.00 GB | 1x |
| GQA-8 | 8 | 2.50 GB | 8x smaller |
| MQA | 1 | 0.31 GB | 64x smaller |

At 128K context, MHA would require 320 GB of KV cache alone, while GQA-8 reduces this to 40 GB.

## Model Adoption

| Model | Size | Attention | Query/KV Heads |
|-------|------|-----------|----------------|
| Llama 3 70B | 70B | GQA | 64Q / 8KV |
| Llama 3 8B | 8B | GQA | 32Q / 8KV |
| Mistral 7B | 7B | GQA | 32Q / 8KV |

## Related

- [[concepts/kv_cache]]
- [[concepts/attention_mechanism]]
- [[concepts/multi_query_attention]]
- [[summaries/adam-rosler-kv-cache-2026-05-12]]