# AGENTS.md

<!-- repo-kit:begin v2 (managed, do not edit; https://github.com/bullitt186/repo-kit) -->
## How to work in this repository (all coding agents)

This block is shared by all repositories of this maintainer and kept in sync by
[repo-kit](https://github.com/bullitt186/repo-kit). Repository-specific
instructions follow below it. They add detail; where they contradict this block,
this block wins, unless an ADR in `docs/adr/` records the exception.

A pull request that follows this block passes review without rework. The
maintainer reviews against the same rules: the **Definition of Done** in
`CONTRIBUTING.md`.

### Build the right thing

1. Read this file to the end, `CONTRIBUTING.md`, `docs/SCOPE.md` and the
   architecture decision records in `docs/adr/` (start with `docs/adr/README.md`).
   An *Accepted* ADR and the scope are binding. If your change needs a different
   decision, write a new ADR that supersedes the old one, in the same pull request.
2. Work from an issue. A feature or behaviour change needs an issue the maintainer
   has labelled `accepted`; if there is none, open one, describe the problem (not
   only the solution) and wait. Only a **small fix** may skip the issue: it repairs
   documented behaviour, changes fewer than about 50 lines of code, and adds no
   dependency, interface, setting or file format.
3. Build what the issue asks for and nothing else. Ideas you have on the way become
   a new issue, not part of this pull request. No reformatting, renaming or
   refactoring that the change does not need.
4. Prefer the smallest complete change: reuse what the repository already has
   (helpers, patterns, dependencies) before adding anything; no new dependency for
   a few lines. Fix the root cause, not the symptom.
5. Never guess protocol values, API fields or hardware behaviour. Take them from a
   source and name it; mark anything unconfirmed as an assumption.

### Design first

Write the design down before the code: the behaviour that changes, the modules
and interfaces involved, and how it is tested. Put it in the issue or the pull
request description; for a small change the commit message is enough.

Write an ADR (`docs/adr/`, see its README) when the change:

- adds, removes or replaces a runtime dependency or external service,
- changes a public interface: API, CLI, configuration keys, file or data formats,
  entity or topic names, anything users or other systems rely on,
- changes the architecture: module boundaries, data flow, persistence, threading,
- sets a security, privacy or compatibility rule,
- reverses or replaces an earlier ADR, or changes `docs/SCOPE.md`.

Bug fixes and refactorings inside existing decisions need no ADR.

### Tests

Design the test cases from the specification, then implement the change together
with them. A one-test-at-a-time red/green cycle is not required.

- A bug fix starts with a regression test that reproduces the bug. Run it and
  confirm it fails **for the reason the bug describes**, not because of a build,
  import or signature error. Then fix the bug and commit the test with the fix.
- Expected values come from the specification: documentation, a protocol table,
  a manual, the issue, or a recorded real payload. Never from running the code
  under test and copying its output; such a test only proves the code does what
  it does.
- Assert observable results (output, state, sent request, raised error), not only
  that something was called.
- Tests are fast, deterministic and offline. A flaky test is a bug to fix, not to
  re-run.
- Changing an expected value in an existing test needs a reason in the commit
  message that names the source of the new value.
- Coverage shows what ran, not whether a test notices a wrong result. Run mutation
  testing on every line your change touches, including the callers you edited,
  not only new functions (see Commands below); kill a surviving mutant
  with a test, or say in the pull request why it is equivalent. Without a
  mutation tool, mutate by hand: for each changed branch or condition, break it
  (invert, drop, return a constant), run the tests, revert, and list each mutant
  with its result in the pull request. Reasoning about mutants without running
  them does not count.
- Do not weaken lint rules, thresholds or checks to make a change pass; fix the
  code. A justified exception gets a comment next to it and a note in the commit
  message. Thresholds are only ever raised.

### Documentation

Documentation changes in the same pull request as the behaviour it describes:
README, `docs/`, configuration examples, the ADRs and `CHANGELOG.md`. Outdated
documentation counts as a bug. Relative links in Markdown must point to files
that exist.

Changelog entries go under `[Unreleased]`, in the Keep a Changelog sections in
this order: Added, Changed, Deprecated, Removed, Fixed, Security. Write them for the user of the
project: what changes for them and what they have to do, not which functions
moved. A breaking change gets an entry under "Upgrade notes" with the steps.
Name outside contributors and link their issue or pull request: write the issue
reference with your entry (on GitHub a link; on Forgejo the bare `#N`, because a
link would put the forge's host name into the repository), and add your handle and the pull request link to it as soon
as the pull request exists. Releases, tags
and version numbers are the maintainer's
([release standard](https://github.com/bullitt186/repo-kit/blob/main/docs/RELEASING.md)).

### Commits and branches

- One branch per topic from the current default branch; never commit to the
  default branch. Agents working in parallel use their own git worktree; never
  run checkout, switch, reset, stash or clean in a checkout someone else uses.
- Commit each completed step with a Conventional Commits message (`feat:`,
  `fix:`, `docs:`, `test:`, `refactor:`, `chore:`, `ci:`); the body says why.
  Code, comments, commit messages and pull requests are in English.
- Reference the issue: `Closes #N` on GitHub; `Refs #N` on Forgejo, which closes
  an issue as soon as a commit with `Closes` is pushed.
- Never commit or push on red; never use `--no-verify` or skip hooks; treat every
  hook finding as work to do.

### Before you open the pull request

- Run the repository's **fast check** before every commit and the **full check**
  when your change can affect what it covers (see Commands below). Both must pass.
- Merge or rebase onto the current default branch and run the checks again.
- Fill in the pull request template completely; tick only what you did and say
  why anything stays unticked.
- After pushing, watch CI yourself. A red check on your pull request is your work,
  also when it looks unrelated.
- No secrets, tokens, personal data, local paths, host names or IP addresses in
  code, tests, fixtures, logs, commits or pull request text.

### Continuous integration

CI follows the repo-kit [CI standard](https://github.com/bullitt186/repo-kit/blob/main/docs/CI_STANDARD.md):
tests, lint and format, type check, build, secret scan, dependency review, static
analysis and `PR hygiene`. PR hygiene fails when code changes come without a test
change or a `CHANGELOG.md` entry, when `docs/SCOPE.md` changes without an ADR,
when an ADR is malformed or missing from the index, when a changed Markdown file
has a broken relative link, when code from an outside contributor links no issue,
or when a pull request changes more than about 800 lines of code and tests. Only
the maintainer can waive a rule (labels `no-test-change`, `skip-changelog`,
`large-change`). Do not ask for a waiver when a test, entry or split is possible.

### Respect

Do not change CI configuration, branch protection, release workflows, licence,
`docs/SCOPE.md` or this block unless the issue asks for it. Maintainer decisions
recorded in issues and ADRs are not up for silent change.
<!-- repo-kit:end -->

## This repository

### Purpose

Scope and non-goals: [docs/SCOPE.md](docs/SCOPE.md)

prusaslicer-tuner lets an AI agent read, explain, diff and (with the user's
approval) edit PrusaSlicer printer, print and filament profiles, and diagnose
print defects from a curated FDM knowledge graph. It ships as an MCP server
(`server.py`) and as a Claude Code skill (`SKILL.md`); users are people tuning
their own printers. See `README.md`.

### Layout

| Path | Content |
|---|---|
| `profiles.py` | profile CLI `list`/`show`/`diff`/`set`, standard library only |
| `server.py` | MCP server (stdio, `uv run`); its instructions are the body of `SKILL.md` |
| `SKILL.md` | the agent workflow, also used as the MCP server instructions |
| `knowledge/` | OKF v0.2 knowledge bundle; rules in `knowledge/maintenance.md`, schema in `knowledge/schema.yaml` |
| `kg.py`, `kg_viewer.html` | knowledge-graph compiler (`check`, `fix`, `build`, `keys`) and viewer template |
| `prusaslicer_defaults.ini`, `prusaslicer_keys.json` | PrusaSlicer built-in defaults and the key list derived from them |
| `research/` | per-source reports (`research/raw/`), coverage and mapping tables; not knowledge |
| `test_prints/` | `fetch.sh` downloads calibration STLs; the STLs are not committed |
| `test_kg.py`, `test_profiles.py` | tests |
| `.githooks/` | privacy gate, knowledge check and viewer rebuild hooks |

### Commands

| Task | Command |
|---|---|
| Install / set up | Python 3.10+ and [uv](https://docs.astral.sh/uv/); once per clone `git config core.hooksPath .githooks` |
| Fast check (before every commit, also the stop hook) | `uv run --locked kg.py check && uv run --locked test_kg.py && python3 test_profiles.py && scripts/lint.sh` (`scripts/lint.sh`: `ruff check`, `ruff format --check`, `mypy`) |
| Full check (before every pull request; what CI `knowledge-graph` runs) | `uv run --locked kg.py check && uv run --locked kg.py fix -q && git diff --exit-code -- knowledge && uv run --locked test_kg.py && python3 test_profiles.py && scripts/lint.sh` |
| Mutation testing of changed code | `scripts/mutate.sh` (mutmut on `kg.py`/`profiles.py` when changed against `origin/main`; `--results` lists survivors; weekly in `scheduled.yml`) |

Lint, format and type check: Ruff (`ruff.toml`) and mypy (`mypy.ini`, strict except that
functions without annotations are allowed; annotate a function when you change it), in the
versions of `requirements-dev.txt`. The scripts pin their dependencies in `*.py.lock`
(`uv lock --script <file>`); refresh a lock with `--upgrade` after changing the PEP 723 header.

### Rules specific to this repository

- Facts about a particular user's printers (hardware, host names, own
  calibration values) never go into this repository; they belong in the user's
  own skill or notes (ADR-0003, `SKILL.md` "Integrating with your own printer
  context"). The optional pre-commit privacy gate enforces a user's own pattern
  list.
- Knowledge changes follow `knowledge/maintenance.md`: frontmatter is the single
  source of truth, every claim maps to a source ID or is labelled a hypothesis
  or starting value, prefer an edge or `altLabel` over a new file (ADR-0002).
- Never hand-edit `<!-- generated:… -->` blocks, `knowledge/index.md` catalog
  or `knowledge/graph.json`; run `uv run kg.py fix`, which writes nothing while
  any error exists.
- `profiles.py` stays standard library only. It never writes vendor files and
  backs up a profile before it edits it.
- Raw source reports in `research/raw/` are not knowledge; consolidate them into
  `knowledge/` and record the source in `research/coverage.md`.
- After a PrusaSlicer upgrade, regenerate `prusaslicer_defaults.ini` (command in
  `profiles.py`) and then `uv run kg.py keys`.
- `test_prints/` STLs are not redistributed; only `test_prints/fetch.sh` is
  committed.
