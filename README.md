# prusaslicer-tuner

Lets an AI agent read, explain, diff and (with your approval) edit **PrusaSlicer** printer, print and filament profiles, and diagnose print defects from photos or descriptions using a curated 3D-printing knowledge graph.

- `profiles.py`: stdlib CLI with `list`, `show`, `diff` and `set`. It resolves vendor `inherits` chains (including vendor-scoped `*abstract*` parents) and built-in defaults, tags each value as `user`, `Vendor:Section` or `default`, and backs up profiles before editing them.
- `server.py`: MCP server (stdio) exposing the profile tools plus `lookup`, `card` and `read_knowledge` over the knowledge graph. Its instructions are generated from `SKILL.md`.
- `SKILL.md`: the same workflow as a Claude Code skill.
- `knowledge/`: topic-oriented OKF v0.2 bundle covering FDM fundamentals, defects, causes, tuning procedures, materials, hardware, firmware and mechanical behavior. It is mapped to PrusaSlicer keys and Klipper / Prusa firmware parameters.
- `kg.py`: knowledge-graph compiler (`uv run kg.py check|fix|build|keys`). It validates `knowledge/` against `knowledge/schema.yaml`, generates the index, Relations blocks, views and `knowledge/graph.json`, and builds the viewer `build/graph.html`.
- `research/`: auditable per-source reports and coverage metadata. The consolidated knowledge lives under `knowledge/`.

## Install

Requires Python ≥ 3.10 and [uv](https://docs.astral.sh/uv/) for the MCP server and `kg.py`. `profiles.py` itself is stdlib-only.

**Profile directory:** set `PRUSASLICER_DIR` if your profiles aren't in PrusaSlicer's default data dir (macOS `~/Library/Application Support/PrusaSlicer`, Linux `~/.config/PrusaSlicer`, Windows `%APPDATA%\PrusaSlicer`).

**MCP, Claude Code:**
```sh
claude mcp add -s user -e PRUSASLICER_DIR="/path/to/PrusaSlicer" prusaslicer-tuner -- uv run /path/to/prusaslicer-tuner/server.py
```
**MCP, Claude Desktop** (`claude_desktop_config.json`):
```json
"prusaslicer-tuner": {
  "command": "uv",
  "args": ["run", "/path/to/prusaslicer-tuner/server.py"],
  "env": { "PRUSASLICER_DIR": "/path/to/PrusaSlicer" }
}
```
**Skill instead of MCP:** symlink the repo to `~/.claude/skills/prusaslicer-tuner`.

Keep facts about *your* printers (hardware, hosts, your own calibration values) in your own skill or notes, not in this repo. `SKILL.md` explains how to integrate a personal "printer manager" skill.

## Contributing knowledge

Enable the hooks once: `git config core.hooksPath .githooks`. They run `kg.py check` before commits and pushes, and CI repeats the checks. Rules: `knowledge/maintenance.md`.

**Optional privacy gate:** list regexes for your private hostnames and names in `~/.config/prusaslicer-tuner/private-patterns.txt` (or `$PRUSASLICER_TUNER_PRIVATE_PATTERNS`), and the pre-commit hook will refuse commits that add matching lines.

Tests: `python3 test_profiles.py` and `uv run test_kg.py`.

## License and attribution

- Code: [MIT](LICENSE).
- `knowledge/` and `research/`: [CC BY 4.0](knowledge/LICENSE).
- Knowledge is paraphrased and attributed per document (`sources` frontmatter). Main sources:
  - [Ellis' Print Tuning Guide](https://ellis3dp.com/Print-Tuning-Guide/)
  - the 3D printing Troubleshooting Guide dataset by J. Kang, K. Ahn and H. Kim (Konkuk University, CC BY 4.0)
  - Prusa Knowledge Base, Klipper and Voron documentation, Teaching Tech, CNC Kitchen
  - community reports, cited per claim

  All trademarks belong to their owners.
