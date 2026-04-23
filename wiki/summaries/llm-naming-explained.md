---
title: "LLM Naming Explained (What do the options mean?)"
type: summary
date: 2026-04-23
sources:
  - raw/articles/LLM Naming Explained (What do the options mean_).md
tags:
  - llm
  - naming-conventions
  - quantization
  - beginner-friendly
---

# LLM Naming Explained

**Author:** [[entities/martin_kollie|Martin Kollie]]  
**Source:** [martinkollie.com](https://martinkollie.com/blog/llm-naming-explained-what-does-it-mean)  
**Published:** 2025-02-08

## Summary

A beginner-friendly guide to reading LLM model names, focusing on three core components: parameter count, instruction tuning, and quantization type. Uses the analogy of video resolution (1080p vs 720p vs 480p) to explain quantization trade-offs.

## Core Components

1. **Parameters**: The number after the model name (e.g., 70b = 70 billion). Higher numbers mean greater capacity and complexity but require better hardware.
2. **Instruction Model**: Fine-tuned to follow user instructions. Best choice for chat-like interactions (e.g., ChatGPT-style usage).
3. **Quantization Type**: Compression level applied to the model.

## Quantization Codes Explained

- **fp16**: Full precision 16-bit floating point. Least compressed, highest quality, largest file size.
- **q** prefix: Quantization levels (q2 through q8). Higher levels need more memory.
- **Suffixes**:
  - `0` or `1`: Uniform quantization.
  - `K`: K-quant method.
  - `_S`, `_M`, `_L`: Small, Medium, or Large block size (small = lower memory, lower precision).

## Quantization Quality Table

| Category | Size | Method | Quality Impact | Recommendation |
|----------|------|--------|----------------|----------------|
| Q2_K | smallest | K-quant | extreme loss | Not Recommended |
| Q3_K/Q3_K_M | very small | K-quant | very high loss | Not Recommended |
| Q4_K_M | medium | K-quant | balanced | Recommended |
| Q5_K_M | large | K-quant | very low loss | Recommended |
| Q6_K | very large | K-quant | extremely low loss | Not Specified |
| Q8_0 | very large | Uniform | extremely low loss | Not Recommended |
| F16/FP16 | extremely large | N/A | virtually no loss | Not Recommended |
| F32/FP32 | absolutely huge | N/A | lossless | Not Recommended |

## Key Takeaway

`q4_K_M` is the default recommendation for most use cases because it offers a good balance between performance and accuracy.

## Example Decoding

`deepseek-r1:70b-llama-distill-q4_K_M`
- DeepSeek R1, 70 billion parameters, distilled into Llama, q4 K-quantization medium block size.

## Related

- [[concepts/llm_naming_conventions]]
- [[concepts/model_quantization]]
- [[concepts/parameter_counts]]
- [[entities/martin_kollie]]
