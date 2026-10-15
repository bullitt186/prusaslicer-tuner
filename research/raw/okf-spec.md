# OKF specification research

## SOURCE_METADATA

Canonical `SPEC.md` on `main`, inspected 2026-10-13; specified version 0.2.

## COVERAGE

Frontmatter, provenance, trust, timestamps, bundle structure, links, reserved files, migration and tooling availability.

## CLAIMS

It requires only a non-empty `type` for concepts; `title`, `description`, `resource` and `tags` are recommended. v0.2 adds `sources`, `generated`, `verified`, lifecycle fields and attested computations. Source entries use `resource` and may use stable `id` values for body footnotes. `generated.at` and other timestamps require ISO 8601 with an explicit offset. `index.md` and `log.md` are reserved.

## PROCEDURES

Migrate `timestamp` to `generated`, move body citations into `sources`, retain legacy fallbacks and preserve unknown fields.

## NUMERICAL_VALUES

Version 0.2; one universally required concept field; two reserved filenames; two explicit v0.1 migration points.

## CONFLICTS_OR_LIMITS

The two relevant v0.1 migrations are legacy `timestamp` → `generated` and body citation lists → `sources`. Unknown fields/types and missing optional metadata remain consumer-tolerable. No official standalone validator was found.

## GAPS

Historical issues, all upstream tests and downstream implementations were not exhaustively inspected.

## CITATIONS

- https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/main/SPEC.md
- https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/main/README.md
