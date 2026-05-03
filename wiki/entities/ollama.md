---
title: "Ollama"
summary: "Local LLM inference tool that runs GGUF models via command line, with a model library for discovery and automatic format conversion"
type: entity
sources:
  - raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md
tags:
  - llm
  - local-inference
  - tools
created: "2026-05-01T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Ollama

A local LLM inference tool that runs GGUF-format models via a command-line interface. Ollama provides a model library for discovering and downloading models and supports automatic conversion from safetensors to GGUF. ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]

## Key Facts

- Uses GGUF as its primary format; supports safetensors via automatic conversion through a `Modelfile` ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]
- On Apple Silicon, Ollama uses MLX as its backend (since March 2026) ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]
- Default quantization level is Q4_K_M ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]
- Model library (ollama.com/library) shows available models, download counts, sizes, and quantization tags ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]
- Runs on CPU and mixed CPU/GPU setups; does not support AWQ, GPTQ, or EXL2 formats ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]
- Quick-start commands: `ollama run gemma4:4b` (small), `ollama run qwen3.5:9b` (medium), `ollama run qwen3.5:27b` (large) ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]
- Specify quantization explicitly: `ollama run qwen3.5:9b-q5_K_M` ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]

## Related

- [[concepts/gguf]]
- [[concepts/quantization]]
- [[concepts/model_naming]]
- [[entities/hugging_face]]
