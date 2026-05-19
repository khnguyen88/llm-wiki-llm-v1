---
title: "OAuth PKCE"
summary: "Proof Key for Code Exchange — an OAuth extension that lets public clients (SPAs, mobile apps) authenticate users without exposing a client secret, using a code verifier/challenge pair"
type: concept
sources:
  - raw/document/openrouter/openrouter-012-guides-overview-auth-oauth-2026-04-29.md
tags:
  - oauth
  - pkce
  - authentication
  - security
  - openrouter
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# OAuth PKCE

Proof Key for Code Exchange (PKCE, pronounced "pixy") is an OAuth 2.0 extension that secures authorization code flows for public clients — such as single-page apps and native applications — that cannot safely store a client secret. Instead of a secret, the client generates a random `code_verifier` and derives a `code_challenge` from it, sending only the challenge during the authorization request and proving possession of the verifier when exchanging the code. ^[raw/document/openrouter/openrouter-012-guides-overview-auth-oauth-2026-04-29.md]

## Key Points

- Three challenge methods exist: `S256` (recommended, SHA-256 hash of the verifier base64url-encoded), `plain` (verifier sent as-is), or no challenge at all (optional parameter) ^[raw/document/openrouter/openrouter-012-guides-overview-auth-oauth-2026-04-29.md]
- The S256 code challenge is generated using the Web Crypto API (`crypto.subtle.digest('SHA-256', ...)`) and the Buffer API for base64url encoding; a bundler is required to use Buffer in the browser ^[raw/document/openrouter/openrouter-012-guides-overview-auth-oauth-2026-04-29.md]
- OpenRouter's PKCE flow has three steps: (1) redirect the user to `https://openrouter.ai/auth` with `callback_url` and `code_challenge` parameters, (2) exchange the returned `code` for a user-controlled API key at `POST /api/v1/auth/keys` by sending `code`, `code_verifier`, and `code_challenge_method`, (3) use the resulting API key for OpenRouter API requests ^[raw/document/openrouter/openrouter-012-guides-overview-auth-oauth-2026-04-29.md]
- Localhost apps should use `http://localhost:3000` as the callback URL during development, replacing it with a public GitHub repo URL or project website URL in production ^[raw/document/openrouter/openrouter-012-guides-overview-auth-oauth-2026-04-29.md]
- Error responses include `400 Invalid code_challenge_method` (method mismatch between authorization and exchange), `403 Invalid code or code_verifier` (user not logged in or incorrect verifier), and `405 Method Not Allowed` (must use POST over HTTPS) ^[raw/document/openrouter/openrouter-012-guides-overview-auth-oauth-2026-04-29.md]

## Details

In the OpenRouter PKCE flow, the app sends the user to `https://openrouter.ai/auth?callback_url=<URL>&code_challenge=<CHALLENGE>&code_challenge_method=S256`. After the user logs in and authorizes, they are redirected back to the `callback_url` with a `code` query parameter. The app extracts this code using the browser's `URLSearchParams` API and POSTs it to `https://openrouter.ai/api/v1/auth/keys` along with the original `code_verifier` and `code_challenge_method`. The response contains a `key` field — a user-controlled API key that can be stored in the browser or a backend database and used for subsequent OpenRouter API calls. ^[raw/document/openrouter/openrouter-012-guides-overview-auth-oauth-2026-04-29.md]

The resulting API key enables end users to choose and pay for their own models through OpenRouter, rather than the app developer bearing the cost. This aligns with OpenRouter's principle that the future is multi-model and multi-provider, where users control their own model selection and billing. ^[raw/document/openrouter/openrouter-012-guides-overview-auth-oauth-2026-04-29.md]

## Related

- [[entities/openrouter]]
- [[concepts/authentication]]
- [[concepts/llm_gateway]]