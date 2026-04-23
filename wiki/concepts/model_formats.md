---
title: "Model Formats"
type: concept
date: 2026-04-23
sources:
  - raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md
  - raw/articles/LLM Model Naming Conventions_ How to Read Names and Why They Matter.md
  - raw/articles/Understanding Naming Conventions Of LLM Files_ A Comprehensive Guide.md
tags:
  - llm
  - file-formats
  - deployment
  - inference
---

# Model Formats

The file format determines which tools can load the model and what quantization methods are supported. Format choice is one of the most common sources of deployment confusion.

## GGUF

- **Created by:** Georgi Gerganov (llama.cpp project)
- **Extension:** `.gguf`
- **What it is:** A single-file format packaging weights, tokenizer, and metadata. Designed for local inference with extensive quantization support.
- **Runs on:** Ollama, LM Studio, llama.cpp, KoboldCpp
- **Pros:** Single-file portability, CPU-friendly, quantization from 2-bit to 8-bit
- **Cons:** Requires conversion from safetensors, slower than GPU-native formats on NVIDIA

## Safetensors

- **Created by:** Hugging Face
- **Extension:** `.safetensors`
- **What it is:** A secure serialization format — pure data, no executable code. Replaced PyTorch's pickle format which had arbitrary code execution vulnerabilities.
- **Runs on:** vLLM, HuggingFace Transformers, TGI, SGLang
- **Pros:** Secure, fast loading (76x faster than pickle on CPU), standard for training/fine-tuning
- **Cons:** Full-precision models require substantial VRAM

## MLX

- **Created by:** Apple Machine Learning Research
- **Extension:** `.safetensors` (MLX-converted)
- **What it is:** Apple Silicon-native format leveraging unified memory. No data copying between CPU and GPU.
- **Runs on:** MLX framework, LM Studio (Mac), Ollama (Mac, since March 2026)
- **Pros:** Optimized for Apple Silicon, leverages all system RAM
- **Cons:** Apple Silicon only

## Other Formats

| Format | Use Case | Note |
|--------|----------|------|
| **ONNX** | Cross-platform/mobile/browser | Not commonly used for LLMs |
| **TensorRT** | Maximum NVIDIA GPU throughput | GPU-architecture-specific, not portable |
| **PyTorch .bin** | Legacy | Being replaced by safetensors |
| **.tflite** | TensorFlow Lite | Mobile and edge deployment |
| **.pt** | PyTorch | Native PyTorch ecosystem |

## Key Insight

- **GGUF is for local inference** (Ollama, LM Studio, llama.cpp).
- **Safetensors is for everything else** — GPU inference with vLLM, training, fine-tuning, and as the canonical format on HuggingFace.
- **MLX is for Apple Silicon** native execution.

You cannot fine-tune from GGUF. If you want to fine-tune, start with safetensors, train with LoRA/QLoRA, then convert the result to GGUF for serving.

## Format Compatibility Matrix

| Format | Ollama | LM Studio | vLLM | llama.cpp | ExLlamaV2 | HF Transformers |
|--------|--------|-----------|------|-----------|-----------|-----------------|
| GGUF | Yes | Yes | — | Yes | — | — |
| Safetensors | Yes (auto-converts) | Yes | Yes | — | — | Yes |
| AWQ | — | — | Yes | — | — | Yes |
| GPTQ | — | — | Yes | — | Yes | Yes |
| EXL2 | — | — | — | — | Yes | — |
| MLX | Yes (Mac) | Yes (Mac) | — | — | — | — |

## Related

- [[concepts/llm_naming_conventions]]
- [[concepts/model_quantization]]
- [[summaries/llm-model-names-decoded]]
- [[summaries/understanding-naming-conventions-of-llm-files]]
