# Changelog

All notable changes are documented here.
Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Versions: [SemVer](https://semver.org/).

## [Unreleased]

### Contributors

- The repo-kit CI standard is complete: CI lints and formats the Python scripts with Ruff and
  type-checks them with mypy; the scripts' dependencies are pinned in `*.py.lock` files (`uv run`
  uses them); a weekly workflow scans those locks for known vulnerabilities and runs mutation
  testing (mutmut) on `kg.py` and `profiles.py`; workflows have read-only token permissions and
  actions pinned to commit SHAs. The code was reformatted by Ruff; behaviour is unchanged.
- One setup for all coding agents and people ([repo-kit](https://github.com/bullitt186/repo-kit)):
  `AGENTS.md` is the single instruction file (`CLAUDE.md` imports it), `CONTRIBUTING.md` holds
  the Definition of Done that every pull request is reviewed against, a pull request template,
  issue forms, and architecture decision records in `docs/adr/` (ADR-0002 knowledge graph,
  ADR-0003 personal printer facts), and `docs/SCOPE.md` with purpose and non-goals. The new `PR hygiene` check fails when code changes come
  without a test or changelog change, or when an ADR or a Markdown link is broken.
- repo-kit v2: `AGENTS.md` names a fast check (run before every commit and by the Claude Code
  stop hook in `.claude/settings.json`), the full check and the state of mutation testing;
  `CONTRIBUTING.md` adds how an idea becomes an accepted issue and the labels `accepted` and
  `out-of-scope`. New `Security` workflow (secret scan, dependency review) and weekly Dependabot
  updates for GitHub Actions.
