---
title: "LLM Naming Explained (What do the options mean?)"
summary: "Martin Kollie's guide (February 2025) explaining LLM model naming conventions with a focus on quantization types, the Q-level system, and practical model selection advice"
type: summary
sources:
  - raw/articles/LLM Naming Explained (What do the options mean_).md
tags:
  - llm
  - naming-conventions
  - quantization
  - gguf
  - model-selection
created: "2026-05-01T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
---

# LLM Naming Explained (What do the options mean?)

## Summary

Martin Kollie's guide (February 2025) focuses on the practical side of LLM naming conventions, particularly the quantization level system. Using the Llama model series as a running example (`llama3.3-70b-instruct-q4_K_M`), it explains the three-component naming pattern of model name, parameter count, fine-tuning type, and quantization type. The guide provides a detailed quantization reference table with quality impact and recommendation guidance sourced from the llama.cpp project. ^[raw/articles/LLM Naming Explained (What do the options mean_).md]

## Quantization Type Reference

| Category | Size | Method | Quality Impact | Recommendation |
|---|---|---|---|---|
| Q2_K | Smallest | K-quant | Extreme quality loss | Not Recommended |
| Q3_K / Q3_K_M | Very small | K-quant | Very high quality loss | Not Recommended |
| Q4_0 | Small | Uniform | Very high quality loss | Prefer Q3_K_M |
| Q4_1 | Small | Uniform | Substantial quality loss | Prefer Q3_K_L |
| Q4_K_S | Small | K-quant | Significant quality loss | Not Recommended |
| **Q4_K / Q4_K_M** | **Medium** | **K-quant** | **Balanced quality** | **Recommended** |
| Q5_0 | Medium | Uniform | Balanced quality | Prefer Q4_K_M |
| Q5_K_S | Large | K-quant | Low quality loss | Recommended |
| Q5_K / Q5_K_M | Large | K-quant | Very low quality loss | Recommended |
| Q6_K | Very large | K-quant | Extremely low quality loss | -- |
| Q8_0 | Very large | Uniform | Extremely low quality loss | Not Recommended |
| F16/FP16 | Extremely large | N/A | Virtually no loss | Not Recommended |
| F32/FP32 | Absolutely huge | N/A | Lossless | Not Recommended |

Key insights: prefer K-quant over uniform at similar bit-widths; higher bit-widths (Q6_K, Q8_0, FP16, FP32) are not recommended because marginal quality gain does not justify the large file size increase. ^[raw/articles/LLM Naming Explained (What do the options mean_).md]

## Suffix Meanings

- **fp16** -- Full precision 16-bit floating point; least compressed, highest quality, massive file size
- **q** -- Quantization levels (q2 through q8); higher levels require more memory
- **0 or 1** -- Uniform quantization
- **K** -- K-quant quantization method (smarter bit allocation across layers)
- **_S, _M, _L** -- Block size: Small (low memory, lower precision), Medium (balanced), Large (more precision, more memory)

If not specified, Q4_K_M is the default quantization for most models. ^[raw/articles/LLM Naming Explained (What do the options mean_).md]

## Analogy

Quantization is compared to video resolution: 1080p (FP16, high quality, large file), 720p (Q4_K_M, balanced), 480p (Q2_K, small but significant quality loss). ^[raw/articles/LLM Naming Explained (What do the options mean_).md]

## Key Quotes

> "Quantization is similar to watching a 1080p video vs. a 720p video vs. a 480p video. You are making tradeoffs between quality (resolution) vs. size/accuracy."

> "For most use cases, you want to go for q4_K_M, which offers a good balance between performance and accuracy. This is also the default quantization for most models."
