---
title: "Quantization"
summary: "Technique that reduces the numerical precision of LLM weights to shrink file size and speed up inference, trading accuracy for efficiency"
type: concept
sources:
  - raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md
  - raw/articles/LLM Model Naming Conventions_ How to Read Names and Why They Matter.md
  - raw/articles/LLM Naming Explained (What do the options mean_).md
  - raw/articles/How to navigate LLM model names.md
tags:
  - llm
  - quantization
  - compression
  - inference
created: "2026-05-01T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: merged
---

# Quantization

Quantization reduces the numerical precision of model weights — storing each weight in fewer bits. This shrinks file size and speeds up inference at the cost of some accuracy. Full-precision models store weights as 16-bit or 32-bit floating point numbers; quantization compresses these down to 8-bit, 4-bit, or even 2-bit representations. ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]

## Key Points

- Q4_K_M is the mainstream default, retaining ~92% of original quality while cutting file size by ~75% compared to FP16 ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]
- Rule of thumb: prefer a larger model at lower quantization over a smaller model at higher quantization — a 14B at Q4_K_M almost always beats a 7B at Q8_0 ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]
- Precision formats range from FP32 (full precision, gold standard for training) through BF16/FP16 (default LLM precisions) down to INT4/FP4 (aggressive compression for constrained hardware) ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]
- K-quants use a two-level scheme: weights grouped into 32-weight blocks packed into 256-weight "super-blocks," with double quantization of scale factors to preserve more information than naive bit reduction ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]
- I-quants (IQ2_M, IQ3_M, IQ4_XS) use importance matrices to identify and protect critical weights during quantization; IQ4_XS can compress more aggressively than Q4_K_M with comparable quality ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]
- Memory estimation from model names: raw weight storage ≈ P × b/8 bytes, where P is parameter count and b is bits per weight; e.g., 8B at FP16 ≈ 16 GB, 8B at 4-bit ≈ 4 GB (before KV cache and framework overhead) ^[raw/articles/LLM Model Naming Conventions_ How to Read Names and Why They Matter.md]
- Quantization tags in model names (Q4, int8, 4bit) signal compressed variants but may omit the method (NF4, GPTQ, AWQ), creating ambiguity that risks unexpected quality drops; always verify the quantization scheme in the model card ^[raw/articles/LLM Model Naming Conventions_ How to Read Names and Why They Matter.md]
- Quantization tradeoffs are analogous to video resolution: FP16 ≈ 1080p (high quality, large), Q4_K_M ≈ 720p (balanced), Q2_K ≈ 480p (small but significant quality loss) ^[raw/articles/LLM Naming Explained (What do the options mean_).md]
- Suffix 0 or 1 indicates uniform quantization; suffix K indicates K-quant method; suffixes _S/_M/_L control block size (Small = low memory, lower precision; Medium = balanced; Large = more precision, more memory) ^[raw/articles/LLM Naming Explained (What do the options mean_).md]
- Concrete vRAM impact: Llama 405B drops from 900+ GB at fp16 to ~450 GB at fp8 ^[raw/articles/How to navigate LLM model names.md]
- Neural Magic notation "w4a16" indicates 4-bit weights with 16-bit activations, enabling advanced quantization with minimal accuracy loss ^[raw/articles/How to navigate LLM model names.md]
- FP16 is full precision 16-bit floating point — least compressed, highest quality, but massive file size; FP32 is lossless but absolutely huge and not recommended for most use cases ^[raw/articles/LLM Naming Explained (What do the options mean_).md]

## Details

### GGUF Quantization Levels

GGUF quantization naming follows the pattern **Q [bits] _ [method] _ [size]**. The S/M/L suffix controls which layers get extra precision: S (Small) stores all tensors at base bit-width; M (Medium) promotes some attention and feed-forward tensors to higher bit-width; L (Large) promotes more tensors. For example, Q4_K_M stores most tensors at 4-bit but promotes half of the attention and feed-forward weights to 6-bit. ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]

The quantization ladder from minimum to maximum quality: Q3_K_M (noticeable quality loss, very constrained hardware), Q4_K_M (mainstream default, 92% quality), Q5_K_M (near-imperceptible loss, extra RAM), Q6_K or Q8_0 (effectively lossless, plenty of RAM). ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]

### GPU-Native Quantization

### Quantization Comparison Table

Reference table for GGUF quantization levels with quality and recommendation guidance: ^[raw/articles/LLM Naming Explained (What do the options mean_).md]

| Category | Size | Method | Quality Impact | Recommendation |
|---|---|---|---|---|
| Q2_K | smallest | K-quant | extreme quality loss | Not Recommended |
| Q3_K / Q3_K_M | very small | K-quant | very high quality loss | Not Recommended |
| Q3_K_S | very small | K-quant | very high quality loss | Not Recommended |
| Q4_0 | small | Uniform | very high quality loss | prefer Q3_K_M |
| Q4_1 | small | Uniform | substantial quality loss | prefer Q3_K_L |
| Q4_K_S | small | K-quant | significant quality loss | Not Recommended |
| Q4_K / Q4_K_M | medium | K-quant | balanced quality | Recommended |
| Q5_0 | medium | Uniform | balanced quality | prefer Q4_K_M |
| Q5_1 | medium | Uniform | low quality loss | prefer Q5_K_M |
| Q5_K_S | large | K-quant | low quality loss | Recommended |
| Q5_K / Q5_K_M | large | K-quant | very low quality loss | Recommended |
| Q6_K | very large | K-quant | extremely low quality loss | — |
| Q8_0 | very large | Uniform | extremely low quality loss | Not Recommended |
| F16 / FP16 | extremely large | N/A | virtually no quality loss | Not Recommended |
| F32 / FP32 | absolutely huge | N/A | lossless | Not Recommended |

Key preference rules from the table: prefer K-quant over uniform at similar bit-widths (Q4_0 → Q3_K_M, Q4_1 → Q3_K_L, Q5_0 → Q4_K_M, Q5_1 → Q5_K_M). Higher bit-widths (Q6_K, Q8_0, FP16, FP32) are not recommended because the marginal quality gain does not justify the large increase in file size. ^[raw/articles/LLM Naming Explained (What do the options mean_).md]

AWQ (Activation-Aware Weight Quantization) achieves ~95% quality at 4-bit with the fastest throughput via the Marlin kernel, but requires NVIDIA GPU. GPTQ was the first practical LLM quantization method with wide tool support. EXL2 uses per-layer mixed bit-widths (2-8 bit) for fastest interactive inference on NVIDIA GPU. These produce safetensors files (not GGUF) and have no CPU fallback. ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]

### Decision Framework

- On CPU or mixed CPU/GPU: GGUF (Q4_K_M default)
- On NVIDIA GPU, maximum throughput: AWQ with Marlin kernel
- On NVIDIA GPU, maximum quality-per-byte: EXL2 ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]

## Related

- [[concepts/gguf]]
- [[concepts/safetensors]]
- [[entities/ollama]]
- [[entities/hugging_face]]
- [[concepts/model_naming]]