#!/usr/bin/env bash
# Download the calibration test prints referenced by knowledge/tuning/*.md into this folder.
# Not committed: the Ellis Print-Tuning-Guide repo has no license, so we link and fetch instead of redistributing.
set -euo pipefail
cd "$(dirname "$0")"
repo=AndrewEllis93/Print-Tuning-Guide
curl -sfL "https://api.github.com/repos/$repo/git/trees/main?recursive=1" |
  python3 -I -c 'import json,sys; [print(t["path"]) for t in json.load(sys.stdin)["tree"] if t["type"]=="blob" and t["path"].startswith("test_prints/")]' |
  while read -r f; do
    out=${f#test_prints/}; mkdir -p "$(dirname "$out")"
    curl -sfL "https://raw.githubusercontent.com/$repo/main/$(python3 -I -c 'import sys,urllib.parse;print(urllib.parse.quote(sys.argv[1]))' "$f")" -o "$out"
  done
# Klipper PA tower (GPLv3, Klipper3d/klipper docs/prints/square_tower.stl)
curl -sfL https://www.klipper3d.org/prints/square_tower.stl -o square_tower_klipper_PA_tower.stl
echo "$(find . -name '*.stl' | wc -l | tr -d ' ') STL files in $(pwd)"
