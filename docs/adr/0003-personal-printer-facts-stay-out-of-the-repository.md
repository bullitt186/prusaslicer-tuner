# ADR-0003: Personal printer facts stay out of the repository

- **Status:** Accepted
- **Date:** 2026-11-24

## Context

The repository is public and used by people with different printers. Facts about
one user's setup (hardware, host names and access paths, own calibration results
per printer and filament) are neither generally valid knowledge nor safe to
publish. This ADR records the rule as it stands in `README.md` and `SKILL.md`;
it was made before ADRs existed.

## Decision

The repository holds only generally valid knowledge and tools. Facts about a
user's own printers belong in that user's own skill, agent memory or notes; a
personal "printer manager" skill can load them and send generally valid findings
back as knowledge contributions. The pre-commit hook offers an optional privacy
gate that blocks added lines matching a pattern list kept outside the repository.

## Consequences

`SKILL.md` tells the agent to ask for and record missing printer facts in the
user's own context, not here. The tool has no access to printers or firmware
configuration; it uses whatever access the environment provides.

## Alternatives considered

Not recorded.
