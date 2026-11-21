"""Model inspection, orientation candidates and 3MF projects that carry resolved presets.

A slicer started with an empty --datadir (Prusa Connect Local's server-slicing) slices with
the settings saved inside the 3MF, so the project must carry the whole flattened config.
"""
import io, math, zipfile
from pathlib import Path

import numpy as np
import trimesh

import profiles

# Per-preset bookkeeping that must not leak into the flat project config: print and filament
# both define compatible_printers_condition/inherits, and a flat file can hold only one.
DROP_KEYS = {"inherits", "renamed_from", "alias", "compatible_printers", "compatible_printers_condition",
             "compatible_prints", "compatible_prints_condition"}
# A flattened export with these at 0 segfaults the CLI (exit 139), see the CLI runbook.
CRASH_KEYS = {"bed_temperature_extruder", "wipe_tower_extruder"}
OVERHANG_DEG = 45


def load_mesh(path):
    m = trimesh.load(str(path), force="mesh")
    if not isinstance(m, trimesh.Trimesh) or m.is_empty:
        raise ValueError(f"no mesh in {path}")
    return m


def inspect(path):
    m = load_mesh(path)
    return {"size_mm": [round(float(x), 2) for x in m.extents], "triangles": len(m.faces),
            "volume_cm3": round(float(m.volume) / 1000, 2) if m.is_watertight else None,
            "watertight": bool(m.is_watertight)}


def _down(normal):
    """Rotation that turns `normal` to -Z (that face lies on the bed)."""
    return trimesh.geometry.align_vectors(normal, [0, 0, -1])


def _score(m, rot):
    r = m.copy(); r.apply_transform(rot)
    z0 = r.bounds[0][2]
    n, area, cz = r.face_normals, r.area_faces, r.triangles_center[:, 2]
    on_bed = (n[:, 2] < -0.999) & (cz - z0 < 0.05)
    over = (n[:, 2] < -math.cos(math.radians(OVERHANG_DEG))) & ~on_bed
    return {"height_mm": round(float(r.extents[2]), 2),
            "bed_contact_mm2": round(float(area[on_bed].sum()), 1),
            "overhang_mm2": round(float(area[over].sum()), 1)}


def orient_candidates(path, n=6):
    """As loaded plus the largest flat faces turned down; the caller (the AI) picks one."""
    m = load_mesh(path)
    cands = [("as loaded", np.eye(4))]
    if len(m.facets):
        for i in np.argsort(m.facets_area)[::-1][: n - 1]:
            cands.append((f"flat face {len(cands)} down ({m.facets_area[i]:.0f} mm²)", _down(m.facets_normal[i])))
    out, seen = [], set()
    for label, rot in cands:
        s = _score(m, rot)
        key = (s["height_mm"], s["bed_contact_mm2"], s["overhang_mm2"])
        if key in seen:
            continue
        seen.add(key)
        out.append({"id": len(out), "label": label, **s, "rotation": np.round(rot[:3, :3], 6).tolist()})
    return out


def flat_config(printer, print_, filament, overrides=None, root=None):
    """Printer < print < filament < overrides, as PrusaSlicer layers them; values only."""
    vendors = profiles.load_vendors(root)
    cfg = {}
    for typ, name in (("printer", printer), ("print", print_), ("filament", filament)):
        cfg.update({k: v for k, (v, _src) in profiles.resolve(typ, name, vendors, root).items()})
    cfg.update(overrides or {})
    cfg.update(printer_settings_id=printer, print_settings_id=print_, filament_settings_id=filament)
    for k in DROP_KEYS:
        cfg.pop(k, None)
    for k in CRASH_KEYS:
        if cfg.get(k) == "0":
            del cfg[k]
    return cfg


def _bed_center(cfg):
    pts = [tuple(map(float, p.split("x"))) for p in cfg.get("bed_shape", "0x0,200x0,200x200,0x200").split(",")]
    xs, ys = zip(*pts)
    return (min(xs) + max(xs)) / 2, (min(ys) + max(ys)) / 2


def build_3mf(model, out, printer, print_, filament, overrides=None, rotation=None, root=None, slicer_version="2.9.7"):
    """Write a 3MF with the mesh rotated, dropped on the bed, centred, and the flat config embedded.
    `slicer_version`: the PrusaSlicer that will slice it; Connect's server-slicing refuses projects
    not marked as PrusaSlicer and ones marked newer than the slicer the job gets."""
    cfg = flat_config(printer, print_, filament, overrides, root)
    m = load_mesh(model)
    if rotation is not None:
        rot = np.eye(4); rot[:3, :3] = np.asarray(rotation, dtype=float)
        m.apply_transform(rot)
    cx, cy = _bed_center(cfg)
    lo, hi = m.bounds
    m.apply_translation([cx - (lo[0] + hi[0]) / 2, cy - (lo[1] + hi[1]) / 2, -lo[2]])

    v = "".join(f'<vertex x="{x:.6f}" y="{y:.6f}" z="{z:.6f}"/>' for x, y, z in m.vertices)
    t = "".join(f'<triangle v1="{a}" v2="{b}" v3="{c}"/>' for a, b, c in m.faces)
    name = Path(model).stem.replace("&", "").replace("<", "").replace('"', "")
    model_xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
                 '<model unit="millimeter" xml:lang="en-US" xmlns="http://schemas.microsoft.com/3dmanufacturing/core/2015/02">'
                 f'<metadata name="Application">PrusaSlicer-{slicer_version}</metadata>'
                 '<metadata name="slic3rpe:Version3mf">1</metadata>'
                 f'<resources><object id="1" name="{name}" type="model"><mesh><vertices>{v}</vertices>'
                 f'<triangles>{t}</triangles></mesh></object></resources><build><item objectid="1"/></build></model>')
    config = f"; generated by PrusaSlicer {slicer_version} (prusaslicer-tuner)\n" + "".join(f"; {k} = {val}\n" for k, val in sorted(cfg.items()))
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml",
                   '<?xml version="1.0" encoding="UTF-8"?>\n<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
                   '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
                   '<Default Extension="model" ContentType="application/vnd.ms-package.3dmanufacturing-3dmodel+xml"/></Types>')
        z.writestr("_rels/.rels",
                   '<?xml version="1.0" encoding="UTF-8"?>\n<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
                   '<Relationship Target="/3D/3dmodel.model" Id="rel0" '
                   'Type="http://schemas.microsoft.com/3dmanufacturing/2013/01/3dmodel"/></Relationships>')
        z.writestr("3D/3dmodel.model", model_xml)
        z.writestr("Metadata/Slic3r_PE.config", config)
    Path(out).write_bytes(buf.getvalue())
    return {"path": str(out), "keys": len(cfg), "size_mm": [round(float(x), 2) for x in m.extents]}
