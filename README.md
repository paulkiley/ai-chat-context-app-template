AI Chat Context App (Template)

This is a minimal example app that consumes the AI Chat Context Keeper framework to save and retrieve AI chat context safely.

Install

- Create venv: `uv venv`
- Install: `uv pip install -e .`

Config

- Preferred env vars (framework-compatible):
  - `CHM_HISTORY_BASE_DIR` – base history dir
  - `CHM_READ_ONLY=1` – prevent writes (use with `aiapp save --dry-run`)

Usage

- Save from stdin:
  - `pbpaste | uv run aiapp save --project MyProj --topic Setup --summary "Initial setup"`
- Retrieve:
  - `uv run aiapp retrieve --project MyProj --topic Setup --limit 2`

