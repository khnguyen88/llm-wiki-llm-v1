---
title: "Worktrees"
summary: "Git worktrees that create isolated working directories for parallel Claude Code sessions, each with its own files and branch while sharing the same repository history"
type: concept
sources:
  - raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md
  - raw/document/claude code/claude-code-115-vs-code-2026-04-29.md
tags:
  - claude-code
  - git
  - worktrees
  - parallel
  - isolation
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Worktrees

Git worktrees create separate working directories that each have their own files and branch, while sharing the same repository history and remote connections. They enable parallel Claude Code sessions to work on different tasks without file conflicts. ^[raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]

## Key Points

- Use `claude --worktree <name>` (or `-w`) to create an isolated worktree and start Claude in it; the value becomes the worktree directory name and branch name ^[raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]
- Worktrees are created at `<repo>/.claude/worktrees/<name>` and branch from the default remote branch (`origin/HEAD`); omit the name to auto-generate one ^[raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]
- Subagents can also use worktrees for isolation by adding `isolation: worktree` to the agent frontmatter; each subagent gets its own worktree that is automatically cleaned up when it finishes without changes ^[raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]
- On exit, worktrees with no changes are removed automatically; worktrees with changes prompt you to keep or remove them ^[raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]
- Orphaned subagent worktrees from crashes or interrupted runs are removed at startup once they are older than `cleanupPeriodDays` (default 30), provided they have no uncommitted changes, untracked files, or unpushed commits ^[raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]
- Add `.claude/worktrees/` to `.gitignore` to prevent worktree contents from appearing as untracked files in the main repository ^[raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]
- The `.worktreeinclude` file (using `.gitignore` syntax) specifies which gitignored files to copy to new worktrees; only files matching a pattern that are also gitignored get copied (e.g., `.env`, `.env.local`, `config/secrets.json`) ^[raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]
- `origin/HEAD` is a local reference set once during cloning; if the remote default branch changes, run `git remote set-head origin -a` to re-sync, or set a specific branch with `git remote set-head origin <branch>` ^[raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]
- For full control over worktree creation (including base branch), configure a WorktreeCreate hook in settings.json; the hook replaces Claude Code's default `git worktree` logic entirely ^[raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]
- For non-git version control (SVN, Perforce, Mercurial), configure WorktreeCreate and WorktreeRemove hooks to provide custom worktree creation and cleanup; `.worktreeinclude` is not processed when custom hooks are active ^[raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]
- Worktrees created with `--worktree` are never removed by the automatic cleanup sweep; only orphaned subagent worktrees are eligible ^[raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]
- In VS Code, the `--worktree` / `-w` flag starts Claude in an isolated worktree with its own files and branch; each worktree maintains independent file state while sharing git history, preventing Claude instances from interfering with each other ^[raw/document/claude code/claude-code-115-vs-code-2026-04-29.md]

## Details

Each worktree is a full checkout of the repository at a specific branch, allowing Claude sessions to work independently without stepping on each other's changes. The branch naming convention is `worktree-<name>` where `<name>` is the value passed to `--worktree`. When creating a worktree during a session (e.g., by asking Claude to "work in a worktree"), the same isolation guarantees apply.

For manual worktree management outside of Claude, use standard Git commands: `git worktree add <path> -b <branch>` to create, `git worktree list` to view, and `git worktree remove <path>` to clean up. Each worktree requires its own development environment setup (dependency installation, virtual environments, etc.) since it is a fresh checkout. ^[raw/document/claude code/claude-code-048-common-workflows-2026-04-29.md]

## Related

- [[concepts/parallel_sessions]]
- [[concepts/sessions]]
- [[concepts/subagents]]
- [[concepts/hooks]]
- [[entities/github]]
- [[entities/claude_code]]
- [[entities/vs_code_extension]]
- [[summaries/claude-code-common-workflows]]