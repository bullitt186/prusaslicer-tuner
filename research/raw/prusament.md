# Prusament FDM material source research

## SOURCE_METADATA

- **Source owner:** Prusa Polymers / Prusa Research, official Prusament site.
- **Entry point inspected:** <https://prusament.com/materials/>
- **Research date:** 2026-10-13.
- **Source policy:** Official Prusament product pages and the technical-datasheet links exposed by those pages. No search-result snippets were used as evidence; search was used only to locate the official TPU page and to resolve official document URLs.
- **Evidence grades used below:**
  - **A:** official product page and an official TDS agree or jointly provide the claim.
  - **B:** official product page claim without a separately verified TDS value.
  - **C:** official TDS, but dated/version-scoped or retrieved from a ZIP bundle; do not silently treat it as the current page state.
  - **D:** source limitation, missing value, or explicit manufacturer caveat; not a product claim to generalize.
- **Important interpretation rule:** “Temperature resistance” on a product page is generally presented as a heat-deflection-style headline; it is not a universal continuous-use temperature. TDS HDT values include the applied load and test method.

## COVERAGE

### Core materials

Covered: Prusament PLA, PETG, ASA, PC Blend, PA11 (nylon/polyamide 11), and TPU 95A.

### Filled, reinforced, recycled, or special-condition variants

Covered: PLA High Speed, PETG Carbon Fiber, PETG Ultraglow Green, PETG Magnetite 40%, PETG Tungsten 75%, PETG V0, PC Blend Carbon Fiber, PC Space Grade Black, PA11 Carbon Fiber, PP Carbon Fiber, PP Glass Fiber, and Woodfill.

### Not treated as interchangeable

Prusament PLA, PLA High Speed, and PLA Blend are separate products. Likewise PETG, PETG CF, PETG Ultraglow, PETG Magnetite, PETG Tungsten, and PETG V0 are not interchangeable profiles. “PA/nylon” is not one generic Prusament setting: the pages cover PA11 and PA11 CF, with materially different guidance and TDS values.

## CLAIMS

### Product-by-product print guidance

| Product / condition | Manufacturer guidance and properties | Evidence |
|---|---|---|
| **PLA (regular)** | Nozzle **210 ± 10 °C**; bed **40–60 °C**; fan **100%**; up to **200 mm/s** in the 2022 TDS. Page: bed 40–60, nozzle 210 ± 10, heated bed optional, enclosure not required, fan required at 100%. Page describes low warping, easy printing, brittleness, and low heat resistance; headline temperature resistance **55 °C**. | **A/C:** page + official TDS v1.1, 2022-07-27. |
| **PLA High Speed** | Nozzle **210 ± 20 °C**; bed **50 ± 10 °C**; fan **100%**; up to **300 mm/s**. A high-flow/CHT nozzle is required to reach maximum speed. TDS HDT **57 °C at 0.45 MPa**, **55 °C at 1.80 MPa**; page headline **57 °C**. | **A:** official 2026-06-17 TDS and page. |
| **PETG (regular)** | Nozzle **250 ± 10 °C**; bed **80 ± 10 °C**; fan **50%**; up to **200 mm/s**. Heated bed recommended; enclosure not required. Page headline temperature resistance **68 °C**, low warping, high toughness, strong bed adhesion and possible stringing. | **A:** official TDS v1.1, 2022-02-16, plus page. |
| **PETG Carbon Fiber Black** | Nozzle **265 ± 10 °C**; bed **90 ± 10 °C**; fan **50%**; up to **200 mm/s**; hardened nozzle required. Official TDS v1.0, 2022-12-20: diameter **1.75 ± 0.02 mm**, density **1.27 g/cm³**, HDT **96 °C / 0.45 MPa** and **80 °C / 1.80 MPa**. Page claims better dimensional stability, temperature resistance and modulus than PETG, but lower toughness. | **A/C:** official page + official TDS ZIP, version/date above. |
| **PETG Ultraglow Green** | Nozzle **260 ± 10 °C**; bed **85 ± 10 °C**; fan **50%**, **100% for bridges**; up to **200 mm/s**. Hardened nozzle required; **0.6 mm** nozzle recommended. Filled with strontium aluminate; very abrasive. TDS HDT **91 °C at 0.45 MPa**, **78 °C at 1.80 MPa**; density **1.50 g/cm³**. | **A:** official page + TDS v1.0, 2026-02-19. |
| **PETG Magnetite 40%** | Page identifies a paramagnetic, high-density PETG filled variant. Hardened nozzle required; lower layer adhesion than pure PETG. Page headline temperature resistance **93 °C**, low warping, high abrasivity. The page’s visible extract does not expose complete printer temperatures or a verified TDS value. | **B/D:** official page; do not substitute regular PETG values without a product-specific TDS/profile. |
| **PETG Tungsten 75%** | Hardened steel nozzle required; high abrasivity. Page reports low toughness, low warping, fast print speed and temperature resistance **94 °C**. It is a high-density radiation-shielding product; “75%” is part of the product name and must not be generalized to other PETG fillers. | **B:** official page; complete TDS values not verified in this pass. |
| **PETG V0** | Self-extinguishing/UL-certified product page; hygroscopic and says drying is needed before every use. Page headline temperature resistance **68 °C**, high moisture absorption, low warping, moderate toughness. Do not equate the fire classification with regular PETG mechanical performance; page explicitly says mechanical properties are slightly worse than regular PETG. | **B:** official page; complete TDS values not verified in this pass. |
| **ASA** | Page: nozzle **260 ± 5 °C**, bed **110 ± 5 °C**, fan **30%**, heated bed and skirt/enclosure recommended; PEI or glass surfaces listed. Official 2024 TDS instead says nozzle **260 ± 10 °C**, same bed, fan **30% (0–50%)**, up to **200 mm/s**. TDS diameter **1.75 ± 0.04 mm**, density **1.07 g/cm³**, HDT **93 °C / 0.45 MPa** and **86 °C / 1.80 MPa**. UV-stable, acetone-processable, but hygroscopic and prone to large-model warping. | **A:** product page + TDS v1.1, 2024-05-20; page/TDS nozzle tolerance conflict is recorded below. |
| **PC Blend** | Nozzle **275 ± 10 °C**; bed **110 ± 10 °C**; fan **20% (0–30%)**; up to **200 mm/s**. Page calls for advanced users, high nozzle/bed temperatures, separation agent, and reports high temperature resistance up to **113 °C**. TDS diameter **1.75 ± 0.03 mm**, density **1.22 g/cm³**, HDT **113 °C / 0.45 MPa** and **93 °C / 1.80 MPa**. Large parts may warp; drying before printing is not needed according to the page. | **A:** official TDS v1.1, 2022-02-16, plus page. |
| **PC Blend Carbon Fiber (PCCF)** | Nozzle **285 ± 10 °C**; bed **110 ± 10 °C**; fan **0% (0–20%)**; up to **200 mm/s**. TDS says hardened nozzle, satin/powder-coated/smooth PEI (glue on smooth), and no general brim. Page: enclosure not needed and drying not needed; annealing can raise resistance from headline **114 °C** to **130 °C**. TDS diameter **1.75 ± 0.04 mm**, density **1.22 g/cm³**, HDT **114 / 106 °C** at 0.45/1.80 MPa. | **A:** official TDS v2.0-OY, 2023-04-19, plus page. |
| **PC Space Grade Black** | Nozzle **290 ± 10 °C**; bed **120 ± 10 °C**; fan **0%**, only bridge cooling at 100%; up to **100 mm/s**; hardened nozzle, brim recommended, satin/TXT/PP sheet. TDS diameter **1.75 ± 0.04 mm**, density **1.21 g/cm³**, HDT **137.6 / 128.8 °C** at 0.45/1.80 MPa. Page says ESD-safe, very low outgassing, common desktop printers possible, and drying may be required. | **A:** official TDS v1.0, 2025-09-24, plus page. ESD/EMC caveat below. |
| **PA11 (nylon)** | Current official TDS retrieved from the page’s 2026 URL: nozzle **275 ± 10 °C**, bed **100 ± 10 °C**, chamber **55 ± 5 °C**, maximum volumetric speed **10 mm³/s**, fan **15–20%**, PA Nylon sheet. Diameter **1.75 ± 0.02 mm**, density **1.02 g/cm³**, HDT **58.7 / 49.9 °C** at 0.45/1.80 MPa, anisotropy coefficient **0.84**. Page separately emphasizes hygroscopicity, strong warping, odor/active filtration, special sheet, and annealed temperature resistance up to **122.5 °C**. | **A:** current official TDS v1.0, 2026-07-22, plus page. Do not use older PA11 settings in place of this sheet. |
| **PA11 Carbon Fiber** | Nozzle **285 ± 5 °C**; bed **110 ± 10 °C**; fan **20%**; up to **100 mm/s**; special PA Nylon sheet, hardened nozzle, brim for larger parts. TDS diameter **1.75 ± 0.04 mm**, density **1.11 g/cm³**, moisture absorption **0.20%/24 h** and **0.50%/7 d**, HDT **192 / 152 °C** at 0.45/1.80 MPa. Page says occasional drying, high heat/chemical resistance, and high odor. | **A:** official TDS v1.0, 2022-06-29, plus page. |
| **TPU 95A** | Bed **65 ± 10 °C**; nozzle **230 ± 10 °C**; enclosure not required. Recommended surfaces include PA Nylon and satin; smooth PEI requires separation layer. Shore **95A**, HDT **78.6 °C at 1.80 MPa**, slow speed, high elasticity, high wear resistance, low moisture absorption. Drying is usually unnecessary, but poor/high-moisture storage can require **at least 4 h at 60 °C**, then drybox storage. Nextruder profiles are available; older printers may need idler/feed adjustments. | **A/B:** official page; linked TDS is present but not text-verified in this pass. |
| **PP Carbon Fiber** | Filled PP with recycled carbon fibers; page gives tolerance **±0.04 mm**, temperature resistance **120 °C**, chemical resistance and dimensional stability. Drying not necessary; hardened nozzle and special sheet/separation layer required; lower interlayer adhesion than pure PP. Complete page extract did not expose verified nozzle/bed temperatures. | **B/D:** official page; retain product-specific profile and do not fill missing settings with generic PP. |
| **PP Glass Fiber** | Filled PP with glass fibers; page gives tolerance **±0.04 mm**, temperature resistance **138 °C**, chemical resistance and dimensional stability. Drying not necessary; hardened nozzle and special sheet/separation layer required; lower layer adhesion than pure PP. Complete page extract did not expose verified nozzle/bed temperatures. | **B/D:** official page; retain product-specific profile and do not fill missing settings with generic PP. |
| **Woodfill** | Wood-filled filament with tolerance **±0.04 mm**. Page headline temperature resistance **60 °C**, easy printability, brittle behavior, strong adhesion on smooth PEI, and separation layer required there. Unlike many wood-filled products, Prusament says standard **0.4 mm brass nozzle** is usable and drying is not required. | **B:** official page; complete printer-temperature/TDS values not verified in this pass. |

### Material properties and conditions that must stay attached to the source

- Values reported as “up to” or “temperature resistance” are product-page headlines; TDS HDT values are load-specific. Example: regular PETG is **68 °C at both 0.45 and 1.80 MPa** in its TDS, whereas ASA is **93 °C / 0.45 MPa** and **86 °C / 1.80 MPa**.
- TDS mechanical results are not intrinsic, universal print constants. Prusa states they depend significantly on printer, settings, operator experience and surroundings. The cited sheets identify printer, slicer, layer height, infill, speed, temperatures and orientation for their test specimens.
- Filled products change hardware requirements: PETG CF, Ultraglow, Magnetite, Tungsten, PCCF, PC Space Grade, PA11 CF, PP CF and PP GF call for hardened nozzles; Ultraglow specifically recommends 0.6 mm, while Woodfill explicitly permits a standard 0.4 mm brass nozzle.
- Moisture guidance is product-specific: regular PC Blend and PCCF say no pre-drying is needed; PC Space Grade may require drying; PA11 is hygroscopic; PA11 CF says occasional drying; TPU 95A gives a conditional 4 h/60 °C procedure; PETG V0 says dry before every use; PP CF/GF and Woodfill say drying is not necessary.

## PROCEDURES

1. **Select the exact product name and condition first.** Record filler, color/grade, and whether the source is a page or a TDS. Do not map “PLA,” “PETG,” “PC,” or “nylon” to a family default.
2. **Use the official TDS where available.** Capture TDS version, last-update date, diameter tolerance, nozzle/bed/chamber settings, speed, fan, bed type, and test conditions.
3. **Apply page-only handling when the TDS is missing or bundled.** Preserve the page’s wording and mark unverified fields as gaps; never backfill with the base polymer.
4. **For moisture-sensitive products, treat storage as an operating condition.** TPU 95A’s explicit fallback is 4 h at 60 °C followed by drybox storage; this procedure must not be copied to PA11, PETG V0, or PC Space Grade without their own source.
5. **For filled/abrasive filaments, verify nozzle and nozzle diameter.** Hardened steel is explicitly required by several products; Ultraglow’s 0.6 mm recommendation is product-specific.
6. **For high-warp products, follow the stated surface/separation guidance.** ASA, PC Blend, PA11 and PA11 CF have different sheet/separation/enclosure advice. A glue layer may be a protection/separation layer, not merely an adhesion booster.
7. **Treat TDS test properties as comparative evidence only.** Preserve load, direction, specimen print process and test method with every numeric property.

## NUMERICAL_VALUES

### Verified print settings

| Product | Nozzle °C | Bed °C | Chamber °C | Speed | Fan |
|---|---:|---:|---:|---:|---:|
| PLA | 210 ± 10 | 40–60 | — | up to 200 mm/s | 100% |
| PLA High Speed | 210 ± 20 | 50 ± 10 | — | up to 300 mm/s | 100% |
| PETG | 250 ± 10 | 80 ± 10 | — | up to 200 mm/s | 50% |
| PETG CF Black | 265 ± 10 | 90 ± 10 | — | up to 200 mm/s | 50% |
| PETG Ultraglow Green | 260 ± 10 | 85 ± 10 | — | up to 200 mm/s | 50%; bridge 100% |
| ASA | 260 ± 10 (TDS); page says ±5 | 110 ± 5 | — | up to 200 mm/s | 30% (0–50%) |
| PC Blend | 275 ± 10 | 110 ± 10 | — | up to 200 mm/s | 20% (0–30%) |
| PC Blend CF | 285 ± 10 | 110 ± 10 | — | up to 200 mm/s | 0% (0–20%) |
| PC Space Grade Black | 290 ± 10 | 120 ± 10 | — | up to 100 mm/s | 0%; bridge 100% |
| PA11 | 275 ± 10 | 100 ± 10 | 55 ± 5 | max volumetric 10 mm³/s | 15–20% |
| PA11 CF | 285 ± 5 | 110 ± 10 | — | up to 100 mm/s | 20% |
| TPU 95A | 230 ± 10 | 65 ± 10 | — | slow; no verified numeric TDS value here | not exposed on page |

### Verified tolerances and selected TDS properties

| Product / TDS scope | Diameter tolerance | Density | HDT at 0.45 / 1.80 MPa |
|---|---:|---:|---:|
| PLA, TDS v1.1 2022 | 1.75 ± 0.02 mm | 1.24 g/cm³ | 55 / 55 °C |
| PETG, TDS v1.1 2022 | 1.75 ± 0.02 mm | 1.27 g/cm³ | 68 / 68 °C |
| PETG CF Black, TDS v1.0 2022 | 1.75 ± 0.02 mm | 1.27 g/cm³ | 96 / 80 °C |
| ASA, TDS v1.1 2024 | 1.75 ± 0.04 mm | 1.07 g/cm³ | 93 / 86 °C |
| PC Blend, TDS v1.1 2022 | 1.75 ± 0.03 mm | 1.22 g/cm³ | 113 / 93 °C |
| PC Blend CF, TDS v2.0-OY 2023 | 1.75 ± 0.04 mm | 1.22 g/cm³ | 114 / 106 °C |
| PC Space Grade Black, TDS v1.0 2025 | 1.75 ± 0.04 mm | 1.21 g/cm³ | 137.6 / 128.8 °C |
| PA11, TDS v1.0 2026 | 1.75 ± 0.02 mm | 1.02 g/cm³ | 58.7 / 49.9 °C |
| PA11 CF, TDS v1.0 2022 | 1.75 ± 0.04 mm | 1.11 g/cm³ | 192 / 152 °C |
| PETG Ultraglow Green, TDS v1.0 2026 | 1.75 ± 0.04 mm | 1.50 g/cm³ | 91 / 78 °C |

### Moisture / drying values explicitly found

- **TPU 95A:** usually no drying; if moisture-related print issues follow poor storage, dry **at least 4 h at 60 °C**, then use a drybox.
- **PETG V0:** product page says drying before every use.
- **PA11:** page calls it hygroscopic; current TDS reports **0.26% at 24 h** and **0.46% at 7 days** at 25 °C / 30% RH.
- **PA11 CF:** TDS reports **0.20% at 24 h** and **0.50% at 7 days** at 24 °C / 22% RH; page says occasional drying.
- **PETG:** TDS reports **0.07% at 24 h** and **0.10% at 7 days** at 24 °C / 22% RH.
- **ASA:** TDS reports **0.16% at 24 h** and **0.17% at 7 days** at 24 °C / 22% RH; page calls it hygroscopic but gives no drying schedule in the inspected extract.
- **PC Blend:** TDS reports **0.13% / 0.15%** at 24 h / 7 days; page says no pre-drying is needed.
- **PC Blend CF:** TDS reports **0.09% / 0.11%**; page says no pre-drying is needed.
- **PC Space Grade:** TDS reports **0.18% / 0.20%**; page says it may require drying.
- **PP CF, PP GF, Woodfill:** pages explicitly say drying is not necessary.

## CONFLICTS_OR_LIMITS

1. **ASA nozzle tolerance:** current page says **260 ± 5 °C**; official 2024 TDS says **260 ± 10 °C**. Keep both with source/version metadata; prefer the dated TDS for TDS-driven configuration, while preserving the current page value for page-derived behavior.
2. **Older versus current product generations:** the regular PLA/PETG/PC Blend and PA11 CF TDS files are dated 2022; PA11, PLA High Speed, PETG Ultraglow and PC Space Grade have newer 2025–2026 sheets. A newer product page does not prove that an older TDS still describes every current color or production lot.
3. **TDS test conditions vary:** humidity, printer, slicer, cooling, speed, layer height, infill and orientation differ. Numerical mechanical values must not be pooled as if measured under one protocol.
4. **Page “temperature resistance” versus TDS HDT:** use the TDS load-specific values when available. Do not use a headline value as a safe continuous service temperature.
5. **PC Space Grade ESD wording:** the TDS provides resistivity and outgassing measurements, but explicitly says the methods are supporting documentation for ESD/EMC analysis and not direct evidence of ECSS compliance.
6. **TDS links in ZIP archives:** PLA and PETG CF links resolve to official ZIP bundles. The English PDFs were extracted locally for inspection; the web citation should point to the official product page and linked bundle rather than inventing a standalone PDF URL.
7. **Binary retrieval/timeouts:** the PA11 TDS link initially timed out through the browser tool; the official URL was retrieved and text-inspected separately. This is documented so the 2026 values remain traceable rather than appearing to come from the page alone.
8. **Incomplete variant settings:** the inspected product-page text for PETG Magnetite 40%, PETG Tungsten 75%, PETG V0, PP CF, PP GF and Woodfill did not expose a complete verified TDS settings table in this pass. Do not populate missing temperatures from the parent polymer.

## GAPS

- No verified standalone TDS extraction for TPU 95A in this pass; the official page supplies the manufacturer’s temperatures, material properties and conditional drying procedure.
- No complete current TDS settings/property extraction for PETG Magnetite 40%, PETG Tungsten 75%, PETG V0, PP Carbon Fiber, PP Glass Fiber or Woodfill.
- No systematic inspection here of Prusament recycled PLA/PETG, rPLA, PEI 1010, PVB, or other non-requested families; they should not be silently represented by the nearest base polymer.
- Storage humidity, sealed-package shelf life, desiccant specification and post-drying moisture endpoint were generally not stated on the inspected product pages/TDS files. “Drybox” is not equivalent to a quantified RH requirement.
- Chamber/enclosure values are only reported where the official product source states them. Absence of a chamber number is not evidence that a chamber is unnecessary.
- Safety data sheets were not used to make material-performance claims; they remain a separate source class for occupational/safety handling.

## CITATIONS

### Official index and product pages

- Materials index: <https://prusament.com/materials/>
- PLA: <https://prusament.com/materials/pla/>
- PLA High Speed: <https://prusament.com/materials/prusament-pla-high-speed/>
- PETG: <https://prusament.com/materials/prusament-petg/>
- PETG Carbon Fiber: <https://prusament.com/materials/prusament-petg-carbon-fiber/>
- PETG Ultraglow: <https://prusament.com/materials/prusament-petg-ultraglow/>
- PETG Magnetite 40%: <https://prusament.com/materials/prusament-petg-magnetite-40/>
- PETG Tungsten 75%: <https://prusament.com/materials/prusament-petg-tungsten-75/>
- PETG V0: <https://prusament.com/materials/prusament-petg-v0/>
- ASA: <https://prusament.com/materials/prusament-asa/>
- PC Blend: <https://prusament.com/materials/prusament-pc-blend/>
- PC Blend Carbon Fiber: <https://prusament.com/materials/prusament-pc-blend-carbon-fiber/>
- PC Space Grade: <https://prusament.com/materials/prusament-pc-space-grade/>
- PA11: <https://prusament.com/materials/prusament-pa11/>
- PA11 Carbon Fiber: <https://prusament.com/materials/prusament-pa11-nylon-carbon-fiber/>
- TPU 95A: <https://prusament.com/materials/prusament-tpu-95a/>
- PP Carbon Fiber: <https://prusament.com/materials/prusament-pp/>
- PP Glass Fiber: <https://prusament.com/materials/prusament-pp-glass-fiber/>
- Woodfill: <https://prusament.com/materials/prusament-woodfill/>

### Official technical datasheets

- PETG TDS v1.1, last update 2022-02-16: <https://storage.googleapis.com/prusa3d-content-prod-14e8-wordpress-prusament-prod/2023/10/9f8d2165-tds_prusament-petg_n_en.pdf>
- ASA TDS v1.1, last update 2024-05-20: <https://storage.googleapis.com/prusa3d-content-prod-14e8-wordpress-prusament-prod/2024/05/bc8551ef-tds_prusament-asa_2024_en.pdf>
- PC Blend TDS v1.1, last update 2022-02-16: <https://prusament.com/wp-content/uploads/2022/10/PCBlend_Prusament_TDS_2022_16_EN.pdf>
- PC Blend Carbon Fiber TDS v2.0-OY, last update 2023-04-19: <https://prusament.com/wp-content/uploads/2023/04/TDS_Prusament-PCCF_2023_EN.pdf>
- PA11 Carbon Fiber TDS v1.0, last update 2022-06-29: <https://prusament.com/wp-content/uploads/2022/08/TDS_PA11CFB.pdf>
- PETG Ultraglow Green TDS v1.0, last update 2026-02-19: <https://storage.googleapis.com/prusa3d-content-prod-14e8-wordpress-prusament-prod/2026/05/a150c178-prusament-petg-ultraglow-filament-technical-data-sheet.pdf>
- PLA High Speed TDS v1.0, last update 2026-06-17: <https://storage.googleapis.com/prusa3d-content-prod-14e8-wordpress-prusament-prod/2026/06/269cd3c8-prusament-pla-hs-technical-datasheet.pdf>
- PC Space Grade Black TDS v1.0, last update 2025-09-24: <https://storage.googleapis.com/prusa3d-content-prod-14e8-wordpress-prusament-prod/2025/09/e032493a-tds_pc_space_grade_en.pdf>
- PA11 TDS v1.0, last update 2026-07-22: <https://storage.googleapis.com/prusa3d-content-prod-14e8-wordpress-prusament-prod/2026/08/2d2145fc-pa11_tds_eng.pdf>
- PLA TDS bundle (official product-page download; English PDF inside): <https://storage.googleapis.com/prusa3d-content-prod-14e8-wordpress-prusament-prod/2024/05/7ca620c4-prusament-pla-plablend.zip>
- PETG Carbon Fiber TDS bundle (official product-page download; English PDF inside): <https://prusament.com/wp-content/uploads/2023/02/TDS_Prusament-PETG-CF-Black.zip>

