---
title: "Claude Code Voice Dictation"
summary: "Voice dictation in Claude Code CLI lets users speak prompts with live transcription, supporting hold-to-record and tap-to-record modes, 20 languages, and coding-optimized vocabulary recognition"
type: summary
sources:
  - raw/document/claude code/claude-code-114-voice-dictation-2026-04-29.md
tags:
  - claude-code
  - voice
  - dictation
  - transcription
  - accessibility
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Claude Code Voice Dictation

## Key Points

- Voice dictation streams recorded audio to Anthropic's servers for transcription; audio is not processed locally and the service requires a Claude.ai account (not available with API key, Bedrock, Vertex AI, or Foundry authentication) ^[raw/document/claude code/claude-code-114-voice-dictation-2026-04-29.md]
- Two recording modes: hold mode (push-to-talk, default, requires v2.1.69+) and tap mode (tap to start/stop, requires v2.1.116+); both default to the Space key ^[raw/document/claude code/claude-code-114-voice-dictation-2026-04-29.md]
- Transcription does not consume Claude messages or tokens and does not count toward `/usage` limits ^[raw/document/claude code/claude-code-114-voice-dictation-2026-04-29.md]
- Speech is transcribed live and inserted at the cursor position, allowing mixed voice and typing in the same prompt ^[raw/document/claude code/claude-code-114-voice-dictation-2026-04-29.md]
- Transcription is tuned for coding vocabulary; common development terms like `regex`, `OAuth`, `JSON`, and `localhost` are recognized correctly, and the current project name and git branch name are added as recognition hints ^[raw/document/claude code/claude-code-114-voice-dictation-2026-04-29.md]
- Supports 20 dictation languages controlled by the `language` setting; defaults to English if unset ^[raw/document/claude code/claude-code-114-voice-dictation-2026-04-29.md]
- Not available in remote environments (Claude Code on the Web, SSH sessions, VS Code Remote) because it requires local microphone access ^[raw/document/claude code/claude-code-114-voice-dictation-2026-04-29.md]

## Quotes

- "Speak your prompts instead of typing them in the Claude Code CLI. Your speech is transcribed live into the prompt input, so you can mix voice and typing in the same message." ^[raw/document/claude code/claude-code-114-voice-dictation-2026-04-29.md]
- "Hold detection requires your terminal to send key-repeat events, so it cannot detect a held key if key-repeat is disabled at the OS level." ^[raw/document/claude code/claude-code-114-voice-dictation-2026-04-29.md]

## Notes

- The dictation key is bound to `voice:pushToTalk` in the `Chat` context in `keybindings.json`; modifier combinations like `meta+k` start recording on first keypress with no warmup, avoiding the key-repeat limitation of bare letter keys in hold mode
- Tap mode auto-submits when the transcript is at least three words long; shorter transcripts are inserted but not submitted to prevent accidental sends
- On Linux, audio recording uses a native module, falling back to `arecord` (ALSA utils) or `rec` (SoX) if the native module cannot load
- WSL requires WSLg for audio access (included with WSL2 on Windows 11); on Windows 10 or WSL1, run Claude Code natively on Windows instead

## Related

- [[concepts/voice_dictation]]
- [[entities/claude_code]]
- [[concepts/commands]]
- [[concepts/terminal_config]]
- [[concepts/statusline]]
- [[entities/claude_code_web]]