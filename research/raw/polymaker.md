# Polymaker official wiki — material processing research

## SOURCE_METADATA

- **Source:** Polymaker Wiki, <https://wiki.polymaker.com/>
- **Scope requested:** PLA/PETG/ABS/ASA/PC/PA/TPU, CF/GF variants, drying, nozzle, temperature, chamber, cooling, speed, storage, safety, and troubleshooting.
- **Access date:** 2026-10-13.
- **Primary-source policy:** Product TDS pages and current product pages were used for SKU-specific settings. Generic “by material type” and troubleshooting pages are separated as cross-material guidance. Search snippets were not used as evidence.
- **Interpretation:** “Nozzle temperature” means Polymaker’s recommended extrusion range; “chamber/environment” is reported exactly as the source states. Values are normally based on a 0.4 mm nozzle unless the page says otherwise.
- **Evidence grades used below:**
  - **A:** exact value from a Polymaker typed TDS page.
  - **B:** exact current product-page recommendation/FAQ, including Fiberon pages whose current guidance is not yet reproduced in typed TDS.
  - **C:** official generic material/troubleshooting guidance; useful for diagnosis but not a substitute for the SKU page.
  - **D:** limitation, ambiguity, or evidence gap identified during reconciliation; not a recommended setting.

## COVERAGE

### SKU-specific coverage

| Family | Covered products / variants |
|---|---|
| PLA | PolyLite PLA; PolyMax PLA; PolyLite PLA-CF; PolyLite CosPLA; general PLA guidance; current PLA Pro/HT-PLA values where the wiki’s comparison/TDS guide exposes them |
| PET/PETG | PolyLite PETG; Polymaker PETG (new); PolyMax PETG; Fiberon PETG-rCF08; PETG-ESD; PET-CF17; PET-GF15 |
| ABS/ASA | PolyLite ABS; Polymaker ASA; Fiberon ASA-CF08; current ABS Pro/ABS Max FAQ claims |
| TPU | PolyFlex TPU90; TPU95; TPU95-HF |
| PC | PolyLite PC; PolyMax PC; PolyMax PC-FR; Polymaker PC-ABS |
| PA/nylon | PolyMide CoPA; Fiberon PA6-CF20; PA6-GF25; PA612-CF15; PA12-CF10 |
| PPS (additional engineering comparison) | Fiberon PPS-CF10; PPS-GF20 |

### Topics covered

Drying and in-print moisture control; sealed storage; abrasive-nozzle requirements; nozzle/bed/chamber/fan/speed/retraction; annealing and moisture conditioning; warping/delamination/layer adhesion/curling/wet-filament/brittle-spool troubleshooting; acetone and ventilation safety; product status and documentation limits.

## CLAIMS

### 1. Baseline processing matrix

The ranges below are directly transcribed as compact data, not universal presets. Start at the middle of the SKU range, then tune for printer, nozzle diameter, geometry, and layer height.

| Product | Nozzle °C | Bed °C | Fan | Speed mm/s | Chamber / environment | Drying | Retraction mm / mm/s | Evidence |
|---|---:|---:|---|---:|---|---|---|---|
| PolyLite PLA | 190–230 | 25–60 | On | 50–200 | No chamber | 55°C × 6 h | 1–3 / 20–40 | A |
| PolyMax PLA | 190–230 | 25–60 | On | 50–200 | No chamber | 55°C × 6 h | 1–3 / 20–40 | A |
| PolyLite PLA-CF | 190–230 | 25–60 | On | 50–300 | No chamber | 55°C × 6 h | 1–3 / 20–40 | A |
| PolyLite CosPLA | 190–230 | 25–60 | On | 50–300 (formula A); 50–200 (formula B) | No chamber | 55°C × 6 h | 1–3 / 20–40 | A/D |
| PolyLite PETG | 230–260 | 70–80 | Off–20% | 50–100 | No chamber | 65°C × 6 h | 1–3 / 20–40 | A |
| PolyMax PETG | 230–260 | 70–80 | Off–20% | 50–100 | No chamber | 65°C × 6 h | 1–3 / 20–40 | A |
| PolyLite ABS | 245–265 | 90–100 | Off | 50–200 | Enclosure needed; TDS says ambient-temperature chamber | 70°C × 6 h | 1–3 / 20–40 | A |
| Polymaker ASA | 230–260 | 75–95 | Off | 50–200 | Enclosure needed; ambient chamber | 70°C × 7 h | 1–3 / 20–40 | A |
| PolyFlex TPU90 | 210–230 | 25–60 | On | 30–70 | No chamber | 70°C × 8 h | 3–6 / 40–60 | A |
| PolyFlex TPU95 | 210–230 | 25–60 | On | 30–50 | No chamber | 70°C × 8 h | 3–6 / 40–60 | A |
| PolyFlex TPU95-HF | 200–230 | 25–50 | On | 30–100 | No chamber | 70°C × 8 h | 3–6 / 40–60 | A |
| PolyLite PC | 250–270 | 90–105 | Off | 50–200 | Enclosure; 70–100°C heated chamber for large parts | 75°C × 6 h | 1–3 / 20–40 | A |
| PolyMax PC | 250–270 | 90–105 | Off | 50–200 | Enclosure; 70–100°C heated chamber for large parts | 75°C × 6 h | 1–3 / 20–40 | A |
| PolyMax PC-FR | 250–270 | 90–105 | Off | 50–200 | Enclosure; 70–100°C heated chamber for large parts | 75°C × 6 h | 1–3 / 20–40 | A |
| Polymaker PC-ABS | 250–270 | 90–105 | Off | 50–250 | Enclosure; 90–100°C heated chamber for large parts | 75°C × 6 h | 1–3 / 20–40 | A |
| PolyMide CoPA | 250–270 | 25–50 | Off | 50–200 | Enclosure, ambient temperature | 100°C × 8 h | 3–6 / 40–60 | A/B |
| Fiberon PA6-CF20 | 280–300 | 40–50 | 0% | 30–300 | Room temperature; doors open; keep plate/ambient ≤50°C | Dryer while printing | — | B |
| Fiberon PA6-GF25 | 280–300 | 40–50 | 0% | 30–300 | Room temperature; doors open; keep plate/ambient ≤50°C | Dryer while printing | — | B |
| Fiberon PA612-CF15 | 250–300 | 40–50 | 0% | 30–300 | Room temperature; doors open; keep plate/ambient ≤50°C | Dryer while printing | — | B |
| Fiberon PA12-CF10 | 280–300 | 40–50 | 0% | 30–300 | Room temperature; doors open; keep plate/ambient ≤50°C | Dryer while printing | — | B |
| Fiberon ASA-CF08 | 260–280 | 90–100 | 0% | up to 350 | Enclosure recommended, not required | Dry if popping; keep dry | — | B |
| Fiberon PETG-rCF08 | 240–270 | 60–70 | 0%; product tip max 50% if adhesion requires | 30–300 | Room temperature; door open if enclosed | Keep dry; page does not give a time/temperature | — | B/D |
| Fiberon PET-CF17 | 270–300 | 70–80 | 0% | 30–300 | Room temperature; door open if enclosed | Dryer may be environment-dependent | — | B |
| Fiberon PET-GF15 | 280–310 | 70–80 | 0% | 30–250 | Room temperature; enclosure/heated chamber recommended for best results | Dryer may be humidity-dependent | — | B |
| Fiberon PPS-CF10 | 310–350 | 80–90 | 0% | 30–300 | 25–80°C; no heated chamber required | Moisture-insensitive; no extensive pre-dry claim | — | B |
| Fiberon PPS-GF20 | 310–350 | 80–90 | 0% | up to 250 | 25–80°C; no heated chamber required | 100°C × 10 h if damp | — | B |

### 2. Product-specific material behavior and requirements

- **PLA:** Polymaker’s generic PLA page gives 190–230°C nozzle, 40–60°C bed, and 100% cooling for detail. The PolyLite TDS is more specific: 25–60°C bed, 50–200 mm/s, fan on, and 55°C × 6 h if drying is needed. PLA normally has low warp risk, but large/dense parts may benefit from heat and a brim. Evidence A/C.
- **PLA-CF:** PolyLite PLA-CF keeps the PLA temperature/bed/fan envelope but is abrasive: use hardened steel/ruby/tungsten-carbide rather than brass. Its TDS gives up to 300 mm/s, but generic guidance and actual part quality can require slower printing. Evidence A/C.
- **PETG:** PolyLite PETG is explicitly recommended with PolyBox and resealable-bag storage. The typed TDS says fan off to 20%, 70–80°C bed, and 65°C × 6 h drying. Generic PETG guidance says 30–50% fan and ≤60 mm/s; this is a material-class starting point, not a PolyLite PETG SKU requirement. Evidence A/C.
- **ABS/ASA:** Polymaker says both require an enclosure for proper printing and that ambient air over 45°C helps avoid warping/delamination. SKU TDS values are tighter: PolyLite ABS 245–265°C / 90–100°C / fan off; ASA 230–260°C / 75–95°C / fan off. ASA adds UV/weather resistance and a matte finish. Both PolyLite products may be acetone-smoothed; acetone is hazardous. Evidence A/B.
- **TPU:** TPU90 is softer (90A) and Polymaker recommends direct drive; TPU95 is easier than TPU90 but still benefits from direct drive. TPU95-HF has the same 95A hardness but higher flow and a wider 30–100 mm/s range. All three use fan on and 70°C × 8 h drying in the TDS. Evidence A/B.
- **PC:** PolyLite, PolyMax, PC-FR, and PC-ABS all use 250–270°C nozzle, fan off, 90–105°C bed, and drying at 75°C × 6 h. The PC-family pages call for an enclosure; large parts need a 70–100°C chamber. PC-ABS is a blend with 50–250 mm/s and a 90–100°C chamber reference. Evidence A.
- **PA/nylon:** CoPA is moisture-sensitive, should be used/stored below 20% RH, and can permanently bond to itself if support is left in place while wet. Brass wear is common; Polymaker recommends wear-resistant nozzles. Its published mechanical values are explicitly separated into dry and wet status, showing why drying matters. Evidence A/B.
- **Warp-Free Fiberon nylons:** PA6-CF20, PA6-GF25, PA612-CF15, and PA12-CF10 deliberately use low bed/ambient temperatures (40–50°C plate; open doors) to control Warp-Free behavior, then rely on annealing and moisture conditioning for final performance. This conflicts with the intuitive “heat the chamber for nylon” approach. Evidence B.
- **Fiberon ASA-CF08:** 8% CF, abrasive and brittle on the spool; all-metal ≥260°C hotend, hardened nozzle, clear filament path, ventilation, and enclosure recommended. It does not require annealing. Evidence B.
- **Fiberon PET-CF17 / PET-GF15:** Both use hardened nozzles and fan off. PET-CF17 is described as relatively moisture-insensitive but may need a dryer in humid conditions; PET-GF15 is explicitly moisture-sensitive and suggests ≤20% RH storage. Annealing is optional for ordinary PET-GF15 use but required for higher HDT; PET-CF17’s normal recommendation is 120°C × 10 h. Evidence B.
- **Fiberon PETG-rCF08:** Requires a hardened nozzle, is printable at room temperature without an enclosure, and should use at most 50% fan when layer adhesion needs help. Evidence B.
- **PPS:** PPS-CF10 and PPS-GF20 are high-temperature, abrasive, and require ≥310°C hotends plus hardened nozzles. Both use fan off and 310–350°C extrusion. PPS-CF10 is brittle on the spool and Polymaker advises a direct path rather than AMS; PPS-GF20 is also brittle but the current page says it works with Bambu AMS, with caveats. Evidence B.

### 3. Drying, storage, and moisture diagnosis

- Polymaker says all filament is pre-dried, vacuum-sealed with desiccant, and generally ready to print if the seal remains intact. This does not remove the need for dry storage after opening. Evidence C.
- Strongest moisture-sensitive classes in the wiki: PA/nylon, TPU, PETG/PET, and many Fiberon composites. ABS/ASA and PLA are less sensitive but can still become wet in humid storage. Evidence C.
- Store opened filament airtight with desiccant, ideally in a dry box or PolyDryer; keep humidity low and avoid prolonged open-air exposure. Product-specific RH guidance includes CoPA and ASA-CF08/PET-GF15 below 20% RH. Evidence B/C.
- Popping, crackling, hissing, bubbling, rough extrusion, stringing/oozing, weak layers, and inconsistent extrusion are moisture indicators. Dry using the SKU’s specified cycle; do not substitute a generic temperature when the TDS gives one. Evidence C.
- PA-CF and PA-GF product pages require drying during printing, not merely a one-time pre-dry. After annealing, Polymaker says nylon parts are dry and should be moisture-conditioned; cited test conditioning is immersion in 60°C water for 48 h after 100°C × 16 h annealing. Evidence B.

### 4. Nozzle, cooling, chamber, and safety

- Brass is acceptable for unfilled PLA/ABS/PETG/TPU in normal use; CF/GF/abrasive additives require hardened steel, ruby, or tungsten carbide. Evidence C/B.
- Cooling is material-specific: PLA/TPU generally fan on; ABS/ASA/PC/PA/PPS generally off; PETG ranges from off–20% on typed TDS to higher generic guidance. Evidence A/C.
- Ventilate/enclose ABS/ASA and especially ASA-CF08: Polymaker explicitly mentions VOCs such as styrene and recommends good ventilation/filtration for ASA-CF08. Acetone smoothing is hazardous and requires chemical safety precautions. Evidence B.
- Fiberon spools can be brittle. Keep the filament path short and free of sharp bends; this is particularly important for ASA-CF08, PPS-CF10/PPS-GF20, and the PA-CF/GF family. Evidence B.

## PROCEDURES

### A. Initial profile procedure

1. Identify the exact SKU and formula/brand generation; do not use the generic material page if a TDS/product page exists.
2. Check nozzle material. Install hardened steel/ruby/tungsten carbide for any CF/GF or other abrasive composite.
3. Open with the midpoint of the SKU’s nozzle and bed ranges, fan state, and speed range above; use the page’s chamber/environment requirement.
4. Use a first-layer test and a small temperature/speed tower. Change one variable at a time in 5°C or modest speed increments.
5. Keep a brim for ABS/ASA and large/high-shrinkage parts; use the specified adhesion surface/adhesive. For PET/PETG composites on textured PEI, wait for a fully cooled plate before removal.

### B. Moisture procedure

1. Inspect the vacuum seal and desiccant. If intact, Polymaker says most spools can print immediately.
2. If opened, store sealed with desiccant or feed directly from a dry box. For PA-CF/GF, keep the filament in a heated dryer for the entire print.
3. If popping/crackling, bubbling, stringing, or weak/rough extrusion occurs, stop and use the SKU’s listed drying cycle.
4. Do not infer a drying cycle for a Fiberon product when the current product page only says “keep dry” or “dry if damp”; mark that as an unresolved value and use the manufacturer’s support channel or current TDS.

### C. Warping / delamination procedure

1. Confirm first-layer height, clean plate, bed temperature, and adhesion. Add brim/raft where appropriate.
2. For ABS/ASA/PC, eliminate drafts and use the required enclosure/chamber. For ABS/ASA, target an ambient above 45°C only where the printer and material page support that approach; do not apply this to Warp-Free PA Fiberon.
3. Reduce cooling on materials whose TDS says off; raise nozzle temperature modestly within the SKU range and slow down if layer adhesion is poor.
4. For Warp-Free PA Fiberon, keep bed and ambient below 50°C with doors open; do not “fix” warping by heating the chamber. Anneal and condition afterward.

### D. Wet-filament / extrusion troubleshooting

1. Distinguish moisture symptoms (pops, hiss, bubbles, roughness, stringing) from a worn/clogged nozzle or under-extrusion.
2. Dry first if moisture is plausible; then cold-pull/clean and inspect the nozzle.
3. For CF/GF, inspect for nozzle wear and filament path friction/breakage. A worn brass nozzle can mimic under-extrusion.
4. If layer adhesion remains poor, stay inside the SKU range, increase temperature slightly, slow down, turn off cooling where the TDS calls for it, and consider a larger nozzle.

### E. Annealing / conditioning procedure

- PolyMax PC / PC-FR / PC-ABS: 90°C × 2 h is the typed TDS recommendation.
- CoPA: 80°C × 6 h; the TDS test specimens were also dried for 48 h before testing.
- PA6-CF20 / PA6-GF25 / PA612-CF15 / PA12-CF10: 100°C × 16 h, then moisture-condition; Polymaker’s test protocol cites 60°C water for 48 h.
- PET-CF17: 120°C × 10 h for best layer adhesion/temperature resistance; thin parts may deform, so staged heating or 100°C for longer is suggested.
- PET-GF15: 120°C × 16 h only when higher HDT is needed; ordinary use does not require annealing.
- PPS-CF10: 125°C × 16 h; PPS-GF20: 130°C × 10 h for the standard high-temperature improvement, with 230°C cited for maximum PPS-GF20 heat performance. Use dimensional supports/fixtures where deformation is possible.

## NUMERICAL_VALUES

### Published comparison values useful for profile selection

From Polymaker’s technical-data-at-a-glance page; these are material-test values, not slicer settings. Fiberon/nylon values are generally annealed where noted.

| Product | Density g/cm³ | XY tensile MPa | HDT @0.45 MPa | Vicat °C | Impact XY kJ/m² |
|---|---:|---:|---:|---:|---:|
| PolyLite PLA | 1.17 | 52.3 | 60 | 63 | 3.3 |
| PolyLite PLA Pro | 1.23 | 49.8 | 59 | 63 | 17.1 |
| Polymaker PLA Pro (new) | 1.237 | 39.93 | 58.1 | 63.5 | 20.76 |
| PolyMax PLA | 1.20 | 41.3 | 55 | 62 | 38.9 |
| PLA-CF | 1.29 | 31.2 | 54 | 64 | 5.5 |
| HT-PLA, annealed | 1.287 | 42.86 | 107.2 | 155.2 | 4.67 |
| HT-PLA-GF, annealed | 1.337 | 50.2 | 114.7 | 148.3 | 4.92 |
| Polymaker PETG | 1.30 | 47.96 | 65 | 75 | 4.95 |
| PolyLite PETG | 1.25 | 50.8 | 78 | 84 | 2.6 |
| PolyMax PETG | 1.24 | 37.9 | 76 | 82 | 11.6 |
| PETG-rCF08 | 1.30 | 59.8 | 68.6 | 81.6 | 4.0 |
| PET-CF17, annealed | 1.34 | 65.9 | 147.5 | 238.4 | 5.1 |
| PET-GF15, annealed | 1.43 | 59.9 | 133.7 | 232.6 | 8.7 |
| PolyLite ABS | 1.04 | 33.4 | 100 | 104 | 18 |
| ABS Pro | 1.04 | 34.94 | 106.4 | 116.1 | 17.32 |
| ABS Max | 1.06 | 35.66 | 118.1 | 127.4 | 10.51 |
| Polymaker ASA | 1.13 | 43.8 | 103 | 105 | 10.3 |
| ASA-CF08 | 1.09 | 43.5 | 103 | 110.8 | 5.5 |
| TPU90 / TPU95 / TPU95-HF | 1.21 / 1.22 / 1.16 | — | — | — | 592.0% / 551.2% / 495.8% elongation |
| PolyLite PC | 1.19 | 69.1 | 111 | 120 | 4.1 |
| PolyMax PC | 1.19 | 53.44 | 114 | 117 | 21.28 |
| PC-ABS | 1.10 | 39.9 | 112 | 135 | 25.8 |
| CoPA, annealed | 1.12 | 78 | 111 | 180 | 6.9 |
| PA612-CF15, annealed | 1.03 | 91.9 | 175 | 206.2 | 8.1 |
| PA6-CF20, annealed | 1.17 | 109.3 | 215 | 219.2 | 11 |
| PA6-GF25, annealed | 1.20 | 80.1 | 191 | 211.7 | 10 |
| PA12-CF10, annealed | 1.06 | 77.4 | 131 | 170.2 | 9.9 |
| PPS-CF10, annealed | 1.29 | 59.4 | 252.5 | 267.5 | 5.3 |
| PPS-GF20, annealed | 1.36 | 64.1 | 236.3 | 272.5 | 7.3 |

### Important numerical caveats

- The “technical data at a glance” table mixes products, test conditions, and annealed/unannealed states; do not convert it into a universal strength ranking.
- TDS values are typical/reference values and Polymaker explicitly disclaims design-specification use. Part design, orientation, printer, temperatures, cooling, and environment materially affect results.
- Product pages can be newer than typed TDS pages. Current Fiberon pages contain settings and FAQs that are not present in the older typed TDS index.

## CONFLICTS_OR_LIMITS

1. **Generic versus SKU cooling:** generic PETG says 30–50% fan, while PolyLite and PolyMax PETG TDS says off–20%. Use the SKU TDS first; treat 30–50% as a class-level troubleshooting experiment only.
2. **Generic versus SKU speed:** generic PETG says ≤60 mm/s, while PolyLite/PolyMax PETG TDS allows 50–100 mm/s. Generic TPU says ≤30 mm/s, while SKU TDS ranges 30–70, 30–50, or 30–100 mm/s. Use the exact product page.
3. **ABS/ASA bed ranges:** generic guidance says ABS 100–110°C and ASA 90–110°C, but PolyLite ABS TDS says 90–100°C and ASA says 75–95°C. The TDS is the stronger product-specific source.
4. **Chamber strategy for nylon:** generic nylon guidance expects drying and often an enclosure, but current Warp-Free Fiberon PA pages explicitly require doors open and plate/ambient ≤50°C. Do not apply high-chamber recommendations to these SKUs.
5. **PPS flame-retardancy wording:** current PPS-CF10 product prose says V0, but its FAQ says there is no UL94 certification at this time. PPS-GF20 page reports UL94 V0 at 1.5 mm and links an internal report. Treat PPS-CF10 as not certified unless a current report is supplied.
6. **AMS compatibility:** Polymaker says all redesigned spools roll in AMS, but also warns abrasive/brittle Fiberon can damage or snap in multi-material paths. PPS-CF10 should use a direct path; PPS-GF20 is described as Bambu-AMS compatible with curvature caveats; ASA-CF08 requires caution.
7. **New versus legacy names:** “Polymaker PETG [NEW]” replaces/displaces older PolyLite PETG in product-family prose, while both remain documented. “ABS Pro/ABS Max” are current FAQ products but their complete TDS processing rows were not exposed in the pages inspected.
8. **CosPLA has two formulas:** the same page gives different bed/speed ranges for formula A/B. Treat formula identity as required input; do not collapse to one profile.
9. **Unfilled versus fiber-filled nozzle advice:** generic nozzle guidance lists brass for PLA/ABS/PETG, but every CF/GF page inspected requires hardened nozzle. Fiber weight percentage alone does not determine a safe brass-wear rate.
10. **Annealing is not equivalent to as-printed performance:** comparison-table values marked annealed cannot be used to promise the same HDT or strength from an unannealed print.

## GAPS

- Complete typed TDS processing rows for current Polymaker PETG [NEW], ABS Pro, ABS Max, Fiberon PA6-CF20, PA6-GF25, PA612-CF15, PA12-CF10, PET-CF17, PET-GF15, PETG-rCF08, PPS-CF10, and PPS-GF20 were not exposed as text in the TDS pages during this pass; current product pages were used instead where available.
- Current product-page drying temperatures/times are missing for several Fiberon materials (for example ASA-CF08 and PET-CF17); only “keep dry”/humidity-dependent guidance is exposed.
- No single official table maps all SKUs to PrusaSlicer-specific volumetric flow, max volumetric speed, accelerations, first-layer temperature, or nozzle diameter. The listed speed values are product-page printing-speed ranges, not calibrated flow limits.
- Storage guidance is qualitative for many products. Exact equilibrium-RH targets are only explicit for selected materials (notably CoPA, ASA-CF08, PET-GF15), while “dry” is used elsewhere.
- Safety coverage is not a substitute for the product SDS. The wiki SDS index links documents, but this report did not exhaustively extract every SDS hazard/first-aid/disposal field for every SKU.
- “Temperature,” “chamber,” and “environment” terms are not consistently standardized across pages. Where a product page says “room temperature” or “ambient,” this is retained rather than inferred into a numeric chamber target.

## CITATIONS

### Core TDS / processing pages

- [PolyLite PLA TDS](https://wiki.polymaker.com/polymaker-products/more-about-our-products/documents/technical-data-sheets/pla/polylite-tm-pla)
- [PolyMax PLA TDS](https://wiki.polymaker.com/polymaker-products/more-about-our-products/documents/technical-data-sheets/pla/polymax-tm-pla)
- [PolyLite PLA-CF TDS](https://wiki.polymaker.com/polymaker-products/more-about-our-products/documents/technical-data-sheets/pla/pla-cf)
- [CosPLA TDS](https://wiki.polymaker.com/polymaker-products/more-about-our-products/documents/technical-data-sheets/pla/cospla-tm)
- [PolyLite PETG TDS](https://wiki.polymaker.com/polymaker-products/more-about-our-products/documents/technical-data-sheets/petg-pet/polylite-tm-petg)
- [PolyMax PETG TDS](https://wiki.polymaker.com/polymaker-products/more-about-our-products/documents/technical-data-sheets/petg-pet/polymax-tm-petg)
- [PolyLite ABS TDS](https://wiki.polymaker.com/polymaker-products/more-about-our-products/documents/technical-data-sheets/abs-asa/polylite-tm-abs)
- [Polymaker ASA TDS](https://wiki.polymaker.com/polymaker-products/more-about-our-products/documents/technical-data-sheets/abs-asa/polymaker-tm-asa)
- [TPU90 TDS](https://wiki.polymaker.com/polymaker-products/more-about-our-products/documents/technical-data-sheets/tpu/polyflex-tm-tpu90), [TPU95 TDS](https://wiki.polymaker.com/polymaker-products/more-about-our-products/documents/technical-data-sheets/tpu/polyflex-tm-tpu95), [TPU95-HF TDS](https://wiki.polymaker.com/polymaker-products/more-about-our-products/documents/technical-data-sheets/tpu/polyflex-tm-tpu95-hf)
- [PolyLite PC TDS](https://wiki.polymaker.com/polymaker-products/more-about-our-products/documents/technical-data-sheets/polycarbonate/polylite-tm-pc), [PolyMax PC TDS](https://wiki.polymaker.com/polymaker-products/more-about-our-products/documents/technical-data-sheets/polycarbonate/polymax-tm-pc), [PolyMax PC-FR TDS](https://wiki.polymaker.com/polymaker-products/more-about-our-products/documents/technical-data-sheets/polycarbonate/polymax-tm-pc-fr), [PC-ABS TDS](https://wiki.polymaker.com/polymaker-products/more-about-our-products/documents/technical-data-sheets/polycarbonate/polymaker-pc-abs)
- [PolyMide CoPA TDS](https://wiki.polymaker.com/polymaker-products/more-about-our-products/documents/technical-data-sheets/nylon/polymide-tm-copa)
- [Technical data at a glance](https://wiki.polymaker.com/polymaker-products/polymaker-filaments/technical-data-at-a-glance)

### Current Fiberon product pages

- [PA6-CF20](https://wiki.polymaker.com/polymaker-products/polymaker-filaments/fiberon-tm/fiberon-tm-pa6-cf20)
- [PA6-GF25](https://wiki.polymaker.com/polymaker-products/polymaker-filaments/fiberon-tm/fiberon-tm-pa6-gf25)
- [PA612-CF15](https://wiki.polymaker.com/polymaker-products/polymaker-filaments/fiberon-tm/fiberon-tm-pa612-cf15)
- [PA12-CF10](https://wiki.polymaker.com/polymaker-products/polymaker-filaments/fiberon-tm/fiberon-tm-pa12-cf10)
- [ASA-CF08](https://wiki.polymaker.com/polymaker-products/polymaker-filaments/fiberon-tm/fiberon-tm-asa-cf08)
- [PET-CF17](https://wiki.polymaker.com/polymaker-products/polymaker-filaments/fiberon-tm/fiberon-tm-pet-cf17)
- [PET-GF15](https://wiki.polymaker.com/polymaker-products/polymaker-filaments/fiberon-tm/fiberon-tm-pet-gf15)
- [PETG-rCF08](https://wiki.polymaker.com/polymaker-products/polymaker-filaments/fiberon-tm/fiberon-tm-petg-rcf08)
- [PPS-CF10](https://wiki.polymaker.com/polymaker-products/polymaker-filaments/fiberon-tm/fiberon-tm-pps-cf10)
- [PPS-GF20](https://wiki.polymaker.com/polymaker-products/polymaker-filaments/fiberon-tm/fiberon-tm-pps-gf20)

### Generic processing, storage, troubleshooting, and safety

- [PLA](https://wiki.polymaker.com/the-basics/3d-printing-materials/pla)
- [By material type](https://wiki.polymaker.com/printing-tips/by-material-type)
- [ABS and ASA FAQ](https://wiki.polymaker.com/polymaker-products/polymaker-filaments/prime-materials/abs-and-asa)
- [Wet filament](https://wiki.polymaker.com/printing-tips/common-printing-issues/wet-filament)
- [Warping](https://wiki.polymaker.com/printing-tips/common-printing-issues/warping)
- [Poor layer adhesion](https://wiki.polymaker.com/printing-tips/common-printing-issues/poor-layer-adhesion)
- [Brittle filament](https://wiki.polymaker.com/printing-tips/common-printing-issues/brittle-filament)
- [Nozzles](https://wiki.polymaker.com/the-basics/3d-printers/diagram-of-a-3d-printer/nozzles)
- [We dry our filament before shipping](https://wiki.polymaker.com/polymaker-products/more-about-our-products/other-polymaker-information/we-dry-our-filament-before-shipping)
- [Safety-data-sheet index](https://wiki.polymaker.com/polymaker-products/more-about-our-products/documents/safety-data-sheets)
- [Technical-data-sheet index](https://wiki.polymaker.com/polymaker-products/more-about-our-products/documents/technical-data-sheets)
