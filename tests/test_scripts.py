"""pytest entry point for the test scripts, used by mutation testing (mutmut needs pytest).

The repository's tests are plain scripts (`uv run test_kg.py`, `python3 test_profiles.py`) that
assert at module level. Running them in-process with runpy lets mutmut see which functions of
kg.py and profiles.py each script exercises. Each script runs once per process: both set
module-level state (kg.ROOT, PROFILES_BACKUP_DIR) for their fixtures, so the module under test
is imported afresh for each script.
"""

import runpy
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))


def run_script(name, module):
    sys.modules.pop(module, None)
    runpy.run_path(str(ROOT / name), run_name="__main__")


def test_kg_script():
    run_script("test_kg.py", "kg")


def test_profiles_script():
    run_script("test_profiles.py", "profiles")
