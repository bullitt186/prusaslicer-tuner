# r/functionalprint mechanical-design source research

## SOURCE_METADATA

- **Source:** [Reddit — r/functionalprint](https://www.reddit.com/r/functionalprint/)
- **Research date:** 2026-10-13
- **Scope:** Representative, targeted corpus on mechanical FDM design: print orientation, walls/infill, layer adhesion, materials, creep, fasteners, tolerances, failure modes, and validation.
- **Method:** Targeted Reddit search-result discovery followed by reading the rendered post/comment pages. This is a qualitative corpus, not an exhaustive subreddit history and not a controlled literature review.
- **Evidence labels used below:**
  - **C — controlled/author-reported test:** the post reports a comparison, print parameters, a load test, or a repeated calibration procedure.
  - **D — discussion/anecdote:** advice, interpretation, or a single-use observation in comments; useful for hypotheses and design heuristics, but not a validated material law.
- **Caveat:** Reddit usernames, scores, and relative-age labels can change; claims below are paraphrased, not transcribed. Permalinks are preserved in the citation list.

## CORPUS_SELECTION

Six threads were selected to cover distinct design questions and failure modes rather than to rank popularity:

1. **Orientation and load validation** — three print orientations of one wall hook, tested to failure, with material and slicer settings reported. Posted 2025-04-04 (as surfaced by Reddit search). [R1]
2. **Walls versus infill** — high-engagement community discussion of the “optimal infill” graphic, including geometry-dependent counterexamples and equal-mass concerns. Posted 2021-11-26. [R2]
3. **Screw-fit calibration guide** — a purpose-built guide for screw/bolt hole sizing, with comments reporting orientation/printer variability and caliper checks. Posted 2023-11-26. [R3]
4. **Hole-size gauge and small-test workflow** — a purpose-built gauge and reports of printing small hole tests before committing to a large part. Posted 2021-02-01. [R4]
5. **Material choice for functional prints** — discussion of PLA, PETG, ABS, heat/sun exposure, brittleness, and wall-heavy strategies. Posted 2020-10-09. [R5]
6. **Connector failure and revision** — a recent modular organizer revision prompted by a connector cracking during handling; the designer increased tolerance and changed the connector geometry. Reddit page exposed the post as “4 days ago” during the fetch; exact calendar date was not available in the rendered page. [R6]

This selection deliberately includes both successful validation and failure-driven redesign. It does not claim that these six threads represent all of r/functionalprint, all printers, or all FDM materials.

## COVERAGE

| Topic | Coverage | Strength of evidence |
|---|---|---|
| Orientation / layer direction | Direct three-orientation failure test plus discussion of bending moment and layer adhesion | Strongest in corpus for one geometry/material; generalization limited |
| Walls / infill | Large discussion with many user heuristics and some reported comparisons | Mixed; mostly D, geometry-dependent |
| Layer adhesion | Discussed as the weak direction in vertical/interlaminar loading; no standardized adhesion test | D, with indirect support from R1 |
| Materials | PLA/PETG/ABS and PLA+ anecdotes; heat and brittleness called out | Mostly D; no matched coupon comparison |
| Creep / sustained load | Warned about in comments on the short-term hook test | D; no long-duration test in selected corpus |
| Fasteners / holes | Two calibration-guide threads and a design-revision case | C for the workflow, D for numeric fit claims |
| Tolerance / fit | Printer and orientation variability; fusion and fit failures | C/D mixed |
| Failure modes | Delamination risk, brittle snap, creep, fused joints, connector cracking | D/C mixed |
| Validation | Weights-to-failure, small test coupons/gauges, caliper measurement, iteration | Practical procedures, but weak standardization |

## CLAIMS (conditions + evidence C/D)

### 1. Orientation can dominate strength in a loaded bracket or hook

- **Claim:** For a cantilever-like wall hook, changing only print orientation produced a large change in ultimate load. The author reported failure above 140 lb, 190 lb, and 268 lb for bottom-down, back-down, and side-down orientations respectively — roughly an 80% spread from weakest to strongest.
- **Conditions:** Bambu PLA Basic; “standard Bambu filament settings”; 5 walls; 5 top layers; 5 bottom layers; cubic 30% infill; mounted to a 2×4 with 1-5/8 in deck screws; apparent static weight loading to failure; one geometry and one specimen per orientation are implied, but replication is not reported.
- **Evidence:** **C (R1)** for the comparative result. **D (R1)** comments interpret the weaker cases as relying more on interlayer adhesion and note that the failure location and bending moment matter.
- **Use:** Orient the part so principal tensile/bending stresses stay in the layer plane where practical, but inspect the complete load path; “best layer direction” alone does not determine the best orientation.
- **Uncertainty:** No specimen count, exact failure mode per orientation, ambient temperature, loading rate, dimensions, or safety factor is given. The test is not a design allowable.

### 2. The critical feature and moment arm matter as much as nominal layer direction

- **Claim:** The community explanation for the surprising ranking (back-down beating bottom-down) was that the crack location and lever arm changed; reducing bending moment at the weak section can outweigh a simple “layers horizontal/vertical” rule.
- **Conditions:** Same wall-hook test as R1; the explanation is a post-hoc interpretation, not a measured stress analysis.
- **Evidence:** **D (R1)**.
- **Use:** Put material under the root of a cantilever, shorten the moment arm, add fillets/gussets, and place fastener holes so they do not create a thin, layer-aligned tear path.
- **Uncertainty:** No CAD dimensions or strain measurements are provided; treat as a design hypothesis to verify with a representative prototype.

### 3. More infill is not a universal substitute for more shell or better geometry

- **Claim:** The discussion repeatedly favors extra perimeters/wall thickness for many shell-like parts, while acknowledging that infill can materially improve stiffness/strength for thin flat geometries, large panels, top-surface support, or particular stress paths.
- **Conditions:** Community examples span unspecified printers, materials, nozzle sizes, layer heights, shapes, and loads. One commenter reports 10% infill plus a double wall using 60% less plastic and exceeding a 25% infill comparison, but the underlying test details are absent.
- **Evidence:** **D (R2)** overall; the equal-mass objection and geometry-dependent counterexamples are especially important. The reported 60% result is **C-weak** because the referenced experiment is not documented in the thread.
- **Use:** Choose shell thickness, infill, and geometry together. Start by strengthening load-bearing skins, roots, hole surrounds, and ribs; use infill where it prevents wall buckling, supports top layers, or carries a known load path.
- **Uncertainty:** The thread mixes subjective “feels stronger” reports with unreported tests. Infill percentage is not comparable across patterns unless mass/volume and geometry are controlled.

### 4. Infill comparisons should be normalized by mass and geometry

- **Claim:** Comparing two patterns at the same nominal percentage can be misleading because the actual amount and distribution of plastic differ; the discussion specifically warns that “50% gyroid” and “50% grid” need not have equal mass or equivalent directional behavior.
- **Conditions:** No common test specimen or load protocol in R2.
- **Evidence:** **D (R2)**, but a sound experimental-design caution.
- **Use:** For a slicer-tuning study, compare equal part mass (or equal filament volume), same outer shell, same orientation, same layer height/temperature/speed, and a defined load case.
- **Uncertainty:** The thread contains conflicting opinions about which pattern is strongest; none is decisive without a matched test.

### 5. Hole and fastener fit is printer-, orientation-, and process-dependent

- **Claim:** Users report that nominally identical hole dimensions can print undersize, and that fit varies with vertical versus horizontal bores, printer, slicer, nozzle wear, and likely material/process settings.
- **Conditions:** Screw/bolt pass-through or threaded holes; the posts concern practical fit rather than a standardized dimensional-accuracy test.
- **Evidence:** **C (R3/R4)** for the repeated calibration workflow; **D (R3/R4)** for causes and the extent of variability.
- **Use:** Measure actual hardware with calipers; print a small hole/fit coupon in the same orientation, material, nozzle, layer height, and slicer profile; then apply the measured offset to the production part. Do not assume a community clearance number transfers directly.
- **Uncertainty:** No universal clearance table is established in the corpus. Horizontal bores and thread quality are explicitly left as harder cases.

### 6. Iterative test parts and physical measurement beat nominal CAD dimensions

- **Claim:** A practical, repeatable workflow in the corpus is to print a hole-size gauge or a small set of test holes, inspect fit, and use a caliper or post-processing tool before committing to the full part.
- **Conditions:** R3/R4; the guide author says it is a starting point, while commenters report occasional filing, reaming, or tapping for final fit.
- **Evidence:** **C (R3/R4)** for the existence and intended procedure; **D** for individual success/failure reports.
- **Use:** Treat calibration as part of the design, not as an afterthought. Keep a per-printer/material profile, and retest after nozzle, extrusion, or slicer changes.
- **Uncertainty:** The posts do not provide a reproducible statistical tolerance band.

### 7. Material choice is load- and environment-specific; “stronger” is not one property

- **Claim:** The material discussion distinguishes stiffness/strength, toughness, heat exposure, and creep. PLA is described as easy and often adequate, but more brittle and less suitable for hot/sunny environments; PETG/ABS are suggested for higher temperature exposure or toughness. These are community heuristics, not matched data.
- **Conditions:** General functional parts, including a car/sun/dishwasher context; one commenter reports an eSun PLA+ shelf supporting a 9 lb monitor without visible failure, but dimensions, duration, safety factor, and exact print settings are not supplied.
- **Evidence:** **D (R5)**. The 9 lb shelf is a single anecdote, not a qualification test.
- **Use:** Select material against the actual failure mode: short-term tensile strength, impact/toughness, temperature, UV, chemical exposure, moisture, and long-term creep. Avoid treating PLA’s high short-term strength as proof of long-term load capacity.
- **Uncertainty:** No direct PLA/PETG/ABS comparison under identical geometry/settings appears in this corpus; filament brand and print quality can dominate.

### 8. Short-term failure load does not establish long-term safe load

- **Claim:** Comments on the successful PLA hook test explicitly warn that creep can cause deformation or failure under sustained load even when a short test holds a high weight.
- **Conditions:** PLA hook; the author’s test is a short, monotonic load-to-failure experiment; no duration or environmental conditioning is reported.
- **Evidence:** **D (R1)**.
- **Use:** For permanent loads, add a duration/temperature test, lower the allowable load, redesign toward compression, shorten the lever arm, or add metal reinforcement. Include thermal exposure and seasonal temperature in validation.
- **Uncertainty:** No creep rate, time-to-failure, temperature, or load fraction is measured in the selected r/functionalprint corpus.

### 9. Failure-driven redesign is a valid functional-print validation loop

- **Claim:** The modular bottle-organizer author revised a first version after feedback that a connector fused to the body and after another user’s connector cracked during support removal. The revision increased clearance/tolerance and changed the connector to be more robust and less dependent on small pins.
- **Conditions:** Modular organizer; failure occurred during support removal/handling rather than service loading; V1/V2 geometry and print profiles are not fully specified.
- **Evidence:** **C-weak/D (R6)**: direct report of a failure and a design revision, but not a controlled A/B test.
- **Use:** Validate assembly/disassembly forces, not just final service load. Inspect thin connector roots, support-removal paths, snap features, and stress concentrators; record failure mode and update the CAD parametrically.
- **Uncertainty:** No dimensions, material, orientation, or number of affected prints are provided; one commenter says multiple V1 prints worked aside from the listed issue.

## PROCEDURES

### A. Orientation screening for a new load-bearing part

1. Define the load case: force direction, support/fastener locations, static versus impact/cyclic load, temperature, and required service life.
2. Identify the likely tensile face, bending root, shear planes, and layer-normal interfaces.
3. Print at least three plausible orientations with identical material, nozzle, layer height, walls, top/bottom layers, infill, temperatures, and cooling.
4. Use the real fasteners and a rigid fixture; load progressively with a measured mass or force gauge.
5. Record first damage, permanent deformation, delamination, fastener pull-through, and final failure. Photograph the fracture and report specimen count.
6. Repeat the winner at least three times before assigning a working load; apply an explicit safety factor and a separate long-duration creep check.

### B. Walls/infill screening

1. Hold outer dimensions and shell/top/bottom settings constant.
2. Compare wall-heavy, infill-heavy, and mixed variants at equal mass or equal filament volume.
3. Match infill orientation/pattern settings and report actual mass, not only slicer percentage.
4. Test the expected load mode: bending, tension, compression, shear, bearing around holes, or buckling of a panel.
5. Include a local reinforcement variant (extra walls/rib/fillet) because global infill can miss the critical section.

### C. Hole/fastener calibration

1. Measure the actual screw, bolt, shaft, or insert with calipers.
2. Print a small coupon containing a clearance-hole ladder, press-fit ladder, and threaded/heat-insert trial where relevant.
3. Print the coupon in the same orientation and profile as the production feature; include horizontal and vertical holes if both are used.
4. Test fit before scaling the full model. Record nominal diameter, measured printed diameter, fit force/feel, and post-processing.
5. Recheck after changes to nozzle, filament, extrusion multiplier/flow, layer height, or slicer version.

### D. Environmental/material validation

1. Choose the material for the worst credible temperature, UV/moisture, impact, and chemical condition.
2. Condition specimens as the part will be used (dry/wet, heated, sun-exposed, or assembled under preload).
3. For permanent loads, run a time-at-load test and record deflection versus time; do not use an immediate failure load as a creep-safe load.
4. For impact-prone loads, include drop/jerk/impact or cyclic tests because brittle snap and fatigue may dominate.

## NUMERICAL_VALUES

| Value | Context | Status |
|---|---|---|
| 140 lb / 190 lb / 268 lb | Hook failure thresholds for bottom-down / back-down / side-down orientations | Direct author report, R1 |
| ~80% | Relative difference between strongest and weakest hook orientation | Direct author summary, R1; approximate |
| 5 walls; 5 top; 5 bottom | Hook test slicer settings | Direct author report, R1 |
| 30% cubic | Hook test infill | Direct author report, R1 |
| 1-5/8 in deck screws; 2×4 fixture | Hook test mounting | Direct author report, R1 |
| 10–15% | Common low-infill practice reported by commenters | Discussion anecdotes, R2; not a recommendation |
| 20–40% | One commenter’s “mid-tier” strength-to-weight range | Discussion anecdote, R2 |
| 4–8 walls; 20–30% infill | One commenter’s rough structural starting point | Discussion anecdote, R2 |
| 150–200% of nozzle width | Suggested infill-line width | Discussion anecdote, R2; not independently validated |
| 60% less plastic | Reported double-wall vs 25% infill comparison | Unverifiable in-thread summary, R2 |
| 9 lb monitor | PLA+ shelf anecdote | Single-use anecdote, R5; duration/settings absent |

## CONFLICTS_OR_LIMITS

- **Walls versus infill:** Many comments say walls dominate, but others correctly qualify that infill can matter for thin panels, buckling, top-surface support, and geometry with efficient internal load paths. There is no universal ranking.
- **Infill pattern:** Gyroid is described both as isotropic/strong and as inefficient for equal mass; the disagreement is unresolved because the comparisons differ in mass, geometry, and likely test method.
- **PLA versus PETG/ABS:** PLA is described as high in short-term tensile strength yet brittle and creep-prone; PETG/ABS are described as tougher or more heat-tolerant. These statements refer to different properties and cannot be collapsed into one “strongest material” ordering.
- **Orientation rule:** “Keep force in XY” is useful but incomplete. R1 shows that load path, bending moment, root geometry, and fastener placement can change the ranking.
- **Strength numbers:** R1’s pounds are ultimate results for one hook and one setup, not allowable loads. The author ran out of standardized weights and added shop objects, which reduces repeatability.
- **Tolerance numbers:** The corpus does not support a universal hole clearance. Printer calibration, bore orientation, nozzle wear, material shrinkage, and slicer compensation are all cited or implied sources of variation.
- **Creep:** It is recognized as important but not measured. No selected thread provides a time-temperature-load curve.
- **Source quality:** Reddit comments mix experienced practice, intuition, humor, and unsupported claims. Upvotes indicate engagement, not validation.

## GAPS

- No controlled, replicated coupons for anisotropic tensile, shear, flexural, bearing, pull-out, or fatigue strength.
- No complete print parameters for most posts: nozzle diameter, layer height, line width, extrusion temperature, bed temperature, speed, cooling, filament drying, and printer model are usually missing.
- No controlled material comparison across PLA, PETG, ABS/ASA, nylon, TPU, filled materials, or annealed parts.
- No quantified layer-adhesion tests or systematic layer-height/temperature/flow study.
- No long-duration creep data at room temperature or elevated temperature.
- No validated tolerance distributions by printer/material/orientation; no gauge R&R or repeatability study.
- Little coverage of cyclic loads, shock, fatigue, UV, moisture, chemical exposure, or safety-critical consequences.
- Sparse documentation of fracture surfaces and failure locations; support-removal failures are under-measured.
- No systematic comparison of fillets, gussets, ribs, local wall modifiers, hole bosses, or metal inserts against global infill changes.

## CITATIONS

- **[R1]** [I was curious how much weight this print could hold, so I printed 3 orientations and tested them to failure](https://www.reddit.com/r/functionalprint/comments/1jrmyfm/i_was_curious_how_much_weight_this_print_could/), r/functionalprint, surfaced as 2025-04-04. Direct load-to-failure comparison; material/settings and weights reported in post.
- **[R2]** [A cheat sheet for optimal infill choosing](https://www.reddit.com/r/functionalprint/comments/r2p1q1/a_cheat_sheet_for_optimal_infill_choosing/), r/functionalprint, 2021-11-26. High-engagement discussion of shell thickness, infill, geometry, pattern, and equal-mass comparisons.
- **[R3]** [I made a screw fit guide following a suggestion from my last dimension guide!](https://www.reddit.com/r/functionalprint/comments/1849qkb/i_made_a_screw_fit_guide_following_a_suggestion/), r/functionalprint, 2023-11-26. Screw/bolt fit guide; comments discuss undersize holes, horizontal bores, and caliper checks.
- **[R4]** [One of the handiest things I’ve designed. For determining hole sizes in prints for screws or bolts of any size, pass through or threading in](https://www.reddit.com/r/functionalprint/comments/l9va0k/one_of_the_handiest_things_ive_designed_for/), r/functionalprint, 2021-02-01. Hole-size gauge; comments report small test prints, printer/orientation variability, filing, reaming, and tapping.
- **[R5]** [Advice Requested for functional prints](https://www.reddit.com/r/functionalprint/comments/j83uhu/advice_requested_for_functional_prints/), r/functionalprint, 2020-10-09. Material-selection discussion covering PLA, PETG, ABS, PLA+, heat/sun exposure, brittleness, and wall-heavy printing.
- **[R6]** [Flat-Pack Modular Bottle Organizer V2](https://www.reddit.com/r/functionalprint/comments/1uoyffu/flatpack_modular_bottle_organizer_v2/), r/functionalprint, recent relative date in fetched Reddit page. Failure-driven revision: connector crack during support removal, increased tolerance, and more robust connector geometry.

