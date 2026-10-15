"""Run: python3 test_profiles.py  — fixture covers vendor-scoped abstract parents, name clashes, set/backup/copy."""
import os, tempfile
from pathlib import Path

tmp = Path(tempfile.mkdtemp())
os.environ["PROFILES_BACKUP_DIR"] = str(tmp / "backups")
import profiles as P

(tmp / "vendor").mkdir(); (tmp / "filament").mkdir()
(tmp / "vendor/Acme.ini").write_text(
    "[filament:*common*]\ntemperature = 200\nretract = 1\n"
    "[filament:*PET*]\ninherits = *common*\ntemperature = 240\n"
    "[filament:Generic PETG]\ninherits = *common*; *PET*\ncompatible_printers_condition = acme\n")
(tmp / "vendor/PrusaResearch.ini").write_text(
    "[filament:*common*]\ntemperature = 999\nretract = 9\n"
    "[filament:Generic PETG]\ninherits = *common*\ncompatible_printers_condition = prusa\n")
(tmp / "filament/Mine.ini").write_text(
    "# generated\ninherits = Generic PETG\ncompatible_printers_condition = acme\ntemperature = 245\nretract = 1\n")

v = P.load_vendors(tmp)
eff = P.resolve("filament", "Mine", v, tmp)
assert eff["temperature"] == ("245", "user"), eff
assert eff["retract"] == ("1", "Acme:*common*"), eff  # same as parent -> not a user override; Acme not Prusa *common*
assert P.resolve("filament", "Generic PETG", v, tmp)["temperature"][0] == "999"  # no hint -> PrusaResearch preferred

P.apply_set("filament", "Mine", {"temperature": "235"}, root=tmp)
assert P.resolve("filament", "Mine", P.load_vendors(tmp), tmp)["temperature"][0] == "235"
assert list((tmp / "backups").rglob("Mine.ini")), "no backup written"

P.apply_set("filament", "Generic PETG", {"retract": "0.5"}, copy="Tuned", root=tmp)
t = P.parse_kv((tmp / "filament/Tuned.ini").read_text())
assert t["inherits"] == "Generic PETG" and t["retract"] == "0.5" and "renamed_from" not in t, t

for bad in (lambda: P.apply_set("filament", "Generic PETG", {"retract": "1"}, root=tmp),
            lambda: P.apply_set("filament", "Mine", {"no_such_key": "1"}, root=tmp)):
    try: bad(); raise AssertionError("should refuse")
    except SystemExit: pass
print("ok")
