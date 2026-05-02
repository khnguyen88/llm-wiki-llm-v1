---
title: "GGUF"
summary: "Single-file format for local LLM inference, created for llama.cpp, packaging weights, tokenizer, and metadata with extensive quantization support"
type: concept
sources:
  - raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md
tags:
  - llm
  - file-format
  - local-inference
  - quantization
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# GGUF

GPT-Generated Unified Format (GGUF) is a single-file format for local LLM inference, created by Georgi Gerganov for the llama.cpp project. It packages weights, tokenizer, and metadata in one file with extensive quantization support from 2-bit to 8-bit. GGUF is the format for Ollama, LM Studio, and llama.cpp. ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]

## Key Points

- Single-file format: one .gguf file contains everything (weights, tokenizer, metadata) for portability ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]
- CPU-friendly: designed for local inference, runs on CPU and mixed CPU/GPU setups with no GPU required ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]
- Supports quantization from 2-bit (Q2_K) to 16-bit (F16), with Q4_K_M as the mainstream default (~92% quality retention) ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]
- Requires conversion from safetensors; cannot be used directly for fine-tuning ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]
- Slower than GPU-native formats (AWQ, EXL2) on NVIDIA hardware ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]
- Compatible tools: Ollama, LM Studio, llama.cpp, KoboldCpp ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]

## Details

GGUF quantization uses a naming scheme: Q [bits] _ [method] _ [size]. The "K" method (K-quant) uses a two-level scheme where weights are grouped into 32-weight blocks packed into 256-weight "super-blocks," with per-block scale factors that are quantized again (double quantization). The S/M/L suffix controls which layers get extra precision: S stores all tensors at base bit-width, M promotes some attention and feed-forward tensors, L promotes more. ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]

The file size rule of thumb for Q4_K_M GGUF: parameter count in billions × ~0.6 = approximate file size in GB (e.g., 7B ≈ 4GB, 32B ≈ 19GB, 70B ≈ 40GB). ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]

GGUF is for local inference. If you want to fine-tune, start with safetensors, train with LoRA/QLoRA, then convert the result to GGUF for serving. ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]

## Related

- [[concepts/safetensors]]
- [[concepts/quantization]]
- [[entities/ollama]]