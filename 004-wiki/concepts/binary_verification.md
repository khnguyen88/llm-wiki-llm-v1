---
title: "Binary Verification"
summary: "Integrity and authenticity verification for Claude Code releases using signed manifests, GPG key fingerprints, and platform-native code signatures"
type: concept
sources:
  - raw/document/claude code/claude-code-102-setup-2026-04-29.md
tags:
  - claude-code
  - security
  - code-signing
  - verification
  - gpg
  - integrity
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Binary Verification

Binary verification ensures the authenticity and integrity of Claude Code releases through a chain of trust: Anthropic's GPG key signs the release manifest, and the manifest contains SHA256 checksums for every platform binary. Individual binaries also carry platform-native code signatures where supported. ^[raw/document/claude code/claude-code-102-setup-2026-04-29.md]

## Key Points

- Each release publishes a `manifest.json` at `https://downloads.claude.ai/claude-code-releases/<version>/manifest.json` containing SHA256 checksums for every platform binary ^[raw/document/claude code/claude-code-102-setup-2026-04-29.md]
- The manifest is signed with Anthropic's GPG key; the detached signature is at `manifest.json.sig`; verifying the signature transitively verifies every binary checksum listed in the manifest ^[raw/document/claude code/claude-code-102-setup-2026-04-29.md]
- The Anthropic release signing key fingerprint is `31DD DE24 DDFA B679 F42D 7BD2 BAA9 29FF 1A7E CACE`; the key is published at `https://downloads.claude.ai/keys/claude-code.asc` ^[raw/document/claude code/claude-code-102-setup-2026-04-29.md]
- Manifest signatures are available for releases from `2.1.89` onward; earlier releases publish checksums in `manifest.json` without a detached signature ^[raw/document/claude code/claude-code-102-setup-2026-04-29.md]
- macOS binaries are signed by "Anthropic PBC" and notarized by Apple (verify with `codesign --verify --verbose ./claude`); Windows binaries are signed by "Anthropic, PBC" (verify with `Get-AuthenticodeSignature .\claude.exe`); Linux binaries are not individually code-signed ^[raw/document/claude code/claude-code-102-setup-2026-04-29.md]
- Package manager installations (apt, dnf, apk) verify signatures automatically using the repository signing key; direct downloads should be verified against the manifest ^[raw/document/claude code/claude-code-102-setup-2026-04-29.md]

## Details

### Verification Process

To verify a release binary: (1) import the public key from `https://downloads.claude.ai/keys/claude-code.asc` and confirm its fingerprint matches `31DD DE24 DDFA B679 F42D 7BD2 BAA9 29FF 1A7E CACE`; (2) download the manifest and its detached signature for the target version; (3) verify the manifest signature with `gpg --verify manifest.json.sig manifest.json` — a valid result reports "Good signature from Anthropic Claude Code Release Signing"; (4) compare the SHA256 checksum of the downloaded binary against the corresponding entry under `platforms.<platform>.checksum` in `manifest.json`. Steps 1–3 require a POSIX shell with `gpg` and `curl`; on Windows, run them in Git Bash or WSL. Step 4 includes a PowerShell option using `Get-FileHash`. ^[raw/document/claude code/claude-code-102-setup-2026-04-29.md]

GPG prints `WARNING: This key is not certified with a trusted signature!` for any freshly imported key. This is expected; the "Good signature" line confirms the cryptographic check passed, and the fingerprint comparison in Step 1 confirms the key itself is authentic. ^[raw/document/claude code/claude-code-102-setup-2026-04-29.md]

### Repository Signing Keys

The apt, dnf, and apk package repositories are all signed with the same Claude Code release signing key. Each installation method documents how to verify the key before trusting it: apt requires manual GPG fingerprint verification (`gpg --show-keys`), dnf prompts for fingerprint confirmation on first install, and apk requires verifying the SHA256 of the downloaded RSA public key (`395759c1f7449ef4cdef305a42e820f3c766d6090d142634ebdb049f113168b6`). ^[raw/document/claude code/claude-code-102-setup-2026-04-29.md]

## Related

- [[entities/claude_code]]
- [[concepts/release_channels]]
- [[concepts/secure_deployment]]