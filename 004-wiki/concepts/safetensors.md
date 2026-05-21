---
title: "Safetensors"
summary: "Hugging Face's secure tensor serialization format that replaced PyTorch's pickle format, the standard for GPU inference, training, and fine-tuning"
type: concept
sources:
  - raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md
tags:
  - llm
  - file-format
  - security
  - gpu-inference
created: "2026-05-01T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Safetensors

Safetensors is Hugging Face's secure tensor serialization format -- pure data with no executable code. It replaced PyTorch's pickle format, which had arbitrary code execution vulnerabilities. Safetensors loads 76x faster than pickle on CPU and is the standard format for training, fine-tuning, and GPU inference. ^[001a-raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]

## Key Characteristics

- Secure by design: pure data, no executable code -- eliminates the arbitrary code execution vulnerability of PyTorch pickle ^[001a-raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]
- Fast loading: 76x faster than pickle on CPU ^[001a-raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]
- Standard format on Hugging Face for model weights; the canonical format for full-precision model distribution ^[001a-raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]
- Required starting point for fine-tuning: you cannot fine-tune from GGUF ^[001a-raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]
- Runs on vLLM, HuggingFace Transformers, TGI, SGLang ^[001a-raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]
- GPU-native quantization formats (AWQ, GPTQ, EXL2) produce safetensors files, not GGUF ^[001a-raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]

## Ecosystem Role

Safetensors and GGUF serve different ecosystems. GGUF is for local inference (Ollama, LM Studio, llama.cpp). Safetensors is for everything else: GPU inference with vLLM, training, fine-tuning, and as the canonical format on Hugging Face. Ollama can import safetensors models via a Modelfile and auto-converts them to GGUF internally. ^[001a-raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]

Full-precision safetensors models require substantial VRAM since weights are stored at BF16 or FP16. This is why quantized GGUF variants are popular for local inference -- they trade some accuracy for dramatically smaller file sizes. ^[001a-raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]

## Related

- [[004-wiki/concepts/gguf]]
- [[004-wiki/concepts/quantization]]
- [[004-wiki/entities/hugging-face]]
