#!/usr/bin/env bash
# Mutation testing with mutmut ([mutmut] in setup.cfg) of kg.py and profiles.py.
#
# Usage:
#   scripts/mutate.sh            mutate the modules changed against origin/main
#   scripts/mutate.sh --all      mutate both (the weekly workflow does this)
#   scripts/mutate.sh --results  list the surviving mutants of the last run
#
# The tests are scripts; tests/test_scripts.py runs them in-process for mutmut. Results are
# cached in mutants/; delete it to start over. MUTATE_BASE overrides the base.
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
run() { uv run --quiet --no-project --with-requirements requirements-dev.txt -- "$@"; }

patterns=()
case "${1:-}" in
    --results) run mutmut results; exit 0 ;;
    --all) ;;
    "")
        base=$(git merge-base "${MUTATE_BASE:-origin/main}" HEAD)
        for module in kg profiles; do
            git diff --quiet "$base" -- "$module.py" || patterns+=("$module.*")
        done
        if [ ${#patterns[@]} -eq 0 ]; then
            echo "kg.py and profiles.py did not change against ${MUTATE_BASE:-origin/main}; nothing to mutate."
            exit 0
        fi
        ;;
    *) echo "usage: scripts/mutate.sh [--all|--results]" >&2; exit 2 ;;
esac

run mutmut run ${patterns[@]+"${patterns[@]}"}
run mutmut export-cicd-stats
python3 - <<'PY'
import json
d = json.load(open("mutants/mutmut-cicd-stats.json"))
tested = d["killed"] + d["survived"] + d["timeout"] + d["suspicious"] + d["no_tests"]
print(f"Score: {100 * (d['killed'] + d['timeout']) / tested:.1f}% of {tested}" if tested else "Score: n/a")
PY
echo "List the surviving mutants with 'scripts/mutate.sh --results'."
