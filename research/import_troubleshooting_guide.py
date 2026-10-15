#!/usr/bin/env python3
"""Split the 3D-Printing Troubleshooting Guide dataset into one raw file per problem.

  python3 research/import_troubleshooting_guide.py [path/to/clone]

Without a path the pinned commit is cloned into a temp dir. Output: research/raw/troubleshooting-guide/
(rewritten each run, deterministic). The dataset concatenates three sources with restarting numbering:
Simplify3D (#1-27), Prusa Knowledge Base (#28-33), All3DP (#1-42). Resin/SLA entries are skipped.
Raw files are research input, not knowledge: consolidate them into knowledge/ via the mapping table.
"""
import re
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = "https://github.com/hyungjungkim/3D-printing-troubleshooting-guide"
COMMIT = "cedd5fb"
FILE = "3D-Printer-Troubleshooting-Guide-Markdown.md"
OUT = Path(__file__).resolve().parent / "raw" / "troubleshooting-guide"
BLOCKS = {  # block id -> (title, original index URL)
    "simplify3d": ("Simplify3D Print Quality Troubleshooting Guide", "https://www.simplify3d.com/resources/print-quality-troubleshooting/"),
    "prusa-kb": ("Prusa Knowledge Base — Print quality troubleshooting", "https://help.prusa3d.com/category/print-quality-troubleshooting_225"),
    "all3dp": ("All3DP — Common 3D printing problems", "https://all3dp.com/1/common-3d-printing-problems-troubleshooting-3d-printer-issues/"),
}
SLA = {("prusa-kb", 30), ("prusa-kb", 31), ("prusa-kb", 32), ("prusa-kb", 33)} | {("all3dp", n) for n in range(35, 43)}
CITATION = ("Kang, J., Ahn, K., Kim, H. (Konkuk University): 3D Printing Troubleshooting Guide dataset, "
            "CC BY 4.0, https://data.mendeley.com/datasets/88pcwt65yp")


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:60]


def split(text):
    """Yield (block, number, title, body)."""
    block, last, cur = "simplify3d", 0, None
    for line in text.splitlines():
        m = re.match(r"^# (\d+)\\?\.\s*(.+?)\s*$", line)
        if m:
            if cur:
                yield cur
            n = int(m[1])
            if n < last:  # numbering restarts -> All3DP block
                block = "all3dp"
            elif block == "simplify3d" and n >= 28:
                block = "prusa-kb"
            last = n
            cur = [block, n, m[2].replace("\\", ""), []]
        elif cur:
            cur[3].append(line)
    if cur:
        yield cur


def main():
    src = Path(sys.argv[1]) if len(sys.argv) > 1 else None
    if src is None:
        src = Path(tempfile.mkdtemp())
        subprocess.run(["git", "clone", "-q", REPO, str(src)], check=True)
        subprocess.run(["git", "-C", str(src), "checkout", "-q", COMMIT], check=True)
    text = (src / FILE).read_text(encoding="utf-8-sig")
    OUT.mkdir(parents=True, exist_ok=True)
    for old in OUT.glob("*.md"):
        old.unlink()
    kept, skipped = [], []
    for block, n, title, body in split(text):
        if (block, n) in SLA:
            skipped.append(f"{block} #{n} {title}")
            continue
        name = f"{block}-{n:02d}-{slug(title)}.md"
        causes = [re.sub(r"^#+\s*\d*\\?\)?\s*", "", l).strip() for l in body if l.startswith("## ")]
        body_text = re.sub(r"\n{3,}", "\n\n", "\n".join(body)).strip()
        (OUT / name).write_text(
            f"---\nsource_block: {block}\nentry: {n}\ntitle: \"{title}\"\norigin: {BLOCKS[block][1]}\n"
            f"dataset: {REPO}/blob/{COMMIT}/{FILE}\ncitation: \"{CITATION}\"\n---\n# {title}\n\n{body_text}\n",
            encoding="utf-8")
        kept.append((name, title, causes))
    with open(OUT / "_index.md", "w", encoding="utf-8") as f:
        f.write(f"# Troubleshooting Guide dataset, split ({REPO} @ {COMMIT})\n\n{CITATION}\n\n")
        f.write(f"{len(kept)} FDM entries; {len(skipped)} resin/SLA entries skipped.\n\n")
        for name, title, causes in kept:
            f.write(f"- `{name}`: {title}" + (f" — {'; '.join(causes)}" if causes else "") + "\n")
        f.write("\nSkipped (resin/SLA):\n" + "".join(f"- {s}\n" for s in skipped))
    print(f"wrote {len(kept)} entries to {OUT}, skipped {len(skipped)} SLA")


if __name__ == "__main__":
    main()
