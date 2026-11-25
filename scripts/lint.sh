#!/usr/bin/env bash
# Lint, format check and type check (AGENTS.md "Commands"), in the versions of requirements-dev.txt.
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
run() { uv run --quiet --no-project --with-requirements requirements-dev.txt -- "$@"; }
run ruff check .
run ruff format --check --quiet .
run mypy
