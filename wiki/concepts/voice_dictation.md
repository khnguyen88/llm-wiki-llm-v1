---
title: "Voice Dictation"
summary: "Live speech-to-text input for Claude Code CLI prompts, supporting hold-to-record and tap-to-record modes with coding-optimized transcription across 20 languages"
type: concept
sources:
  - raw/document/claude code/claude-code-114-voice-dictation-2026-04-29.md
tags:
  - claude-code
  - voice
  - dictation
  - input
  - accessibility
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Voice Dictation

Voice dictation transcribes spoken prompts live into the Claude Code CLI input, allowing mixed voice and typed input in the same message. It uses Anthropic's server-side speech-to-text service and requires a Claude.ai account. ^[raw/document/claude code/claude-code-114-voice-dictation-2026-04-29.md]

## Key Points

- Audio streams to Anthropic's servers for transcription; it is not processed locally and does not consume Claude messages, tokens, or `/usage` limits ^[raw/document/claude code/claude-code-114-voice-dictation-2026-04-29.md]
- Two recording modes: hold mode (push-to-talk, default, v2.1.69+) and tap mode (toggle recording with a single keypress, v2.1.116+) ^[raw/document/claude code/claude-code-114-voice-dictation-2026-04-29.md]
- Transcription is tuned for coding vocabulary (e.g., `regex`, `OAuth`, `JSON`, `localhost`); the current project name and git branch name are added as recognition hints automatically ^[raw/document/claude code/claude-code-114-voice-dictation-2026-04-29.md]
- The dictation key is bound to `voice:pushToTalk` in the `Chat` keybinding context, defaulting to Space; rebind in `~/.claude/keybindings.json` ^[raw/document/claude code/claude-code-114-voice-dictation-2026-04-29.md]
- Not available in remote environments (Claude Code on the Web, SSH sessions, VS Code Remote including Dev Containers and Codespaces) because it requires local microphone access ^[raw/document/claude code/claude-code-114-voice-dictation-2026-04-29.md]

## Details

### Hold Mode

Hold mode is push-to-talk: recording runs while the key is held and stops on release. It is the default mode. Hold detection works by watching for rapid key-repeat events from the terminal, which introduces a brief warmup period before recording starts. During warmup, the footer shows `keep holding…`, then switches to a live waveform once recording is active. The first couple of key-repeat characters type into the input during warmup and are removed automatically. A single Space tap still types a space since hold detection only triggers on rapid repeat. ^[raw/document/claude code/claude-code-114-voice-dictation-2026-04-29.md]

Hold detection cannot work if key-repeat is disabled at the OS level. In that case, switch to tap mode or rebind to a modifier combination (e.g., `meta+k`) which starts recording on the first keypress with no warmup. Avoid binding bare letter keys in hold mode since they type into the prompt during warmup. ^[raw/document/claude code/claude-code-114-voice-dictation-2026-04-29.md]

Speech appears in the prompt as it is spoken, dimmed until finalized. The transcript inserts at the cursor position and the cursor stays at the end, enabling mixed typing and dictation in any order. By default, releasing the key inserts the transcript and waits for Enter. Setting `"autoSubmit": true` in the `voice` settings sends the prompt automatically when released, provided the transcript is at least three words long. ^[raw/document/claude code/claude-code-114-voice-dictation-2026-04-29.md]

### Tap Mode

Tap mode toggles recording with a single keypress: tap once to start, speak, then tap again to send. There is no warmup, so any key works as the dictation key. The first tap only starts recording when the prompt input is empty, so normal space typing is preserved. The second tap stops recording regardless of input contents. Recording also stops automatically after 15 seconds of silence or two minutes total. ^[raw/document/claude code/claude-code-114-voice-dictation-2026-04-29.md]

### Language Support

Dictation uses the `language` setting that also controls Claude's response language, defaulting to English if unset. In the VS Code extension, if `language` is empty, dictation falls back to VS Code's `accessibility.voice.speechLanguage` setting before defaulting to English. If the `language` setting is not in the supported list (20 languages including Czech, Danish, Dutch, English, French, German, Greek, Hindi, Indonesian, Italian, Japanese, Korean, Norwegian, Polish, Portuguese, Russian, Spanish, Swedish, Turkish, Ukrainian), `/voice` warns on enable and falls back to English for dictation without affecting Claude's text responses. ^[raw/document/claude code/claude-code-114-voice-dictation-2026-04-29.md]

### Platform Requirements

On Linux, audio recording uses a built-in native module. If it cannot load, Claude Code falls back to `arecord` from ALSA utils or `rec` from SoX. If neither is available, `/voice` prints an install command for the package manager. On WSL, voice dictation requires WSLg for audio access (included with WSL2 on Windows 11); on Windows 10 or WSL1, run Claude Code natively on Windows. The VS Code extension also supports voice dictation with the same Claude.ai account requirement but not in VS Code Remote sessions. ^[raw/document/claude code/claude-code-114-voice-dictation-2026-04-29.md]

### Enabling and Configuring

Run `/voice` to toggle dictation. The first enable runs a microphone check; on macOS, this triggers the system microphone permission prompt. `/voice` accepts mode arguments: `/voice hold` (hold mode), `/voice tap` (tap mode), `/voice off` (disable). Voice settings persist across sessions and can be set directly in the user settings file under the `voice` key with `enabled` (boolean) and `mode` (`"hold"` or `"tap"`). The `autoSubmit` boolean (hold mode only) sends the prompt automatically on key release when the transcript is at least three words long. ^[raw/document/claude code/claude-code-114-voice-dictation-2026-04-29.md]

## Related

- [[entities/claude_code]]
- [[entities/claude_code_web]]
- [[concepts/commands]]
- [[concepts/terminal_config]]
- [[concepts/statusline]]