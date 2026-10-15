# IEMAI PC-CF source research: community reports

## SOURCE_METADATA

- **Source:** r/prusa3d thread (full text pasted manually) and Prusa Forum threads (search-result excerpts only; the pages themselves were not opened).
- **Research date:** 2026-10-13 (Europe/Berlin)
- **Corpus size:** 1 Reddit thread with 13 comments, 3 Prusa Forum threads.
- **Method:** Reddit blocks WebFetch, curl (403 or bot wall) and the Chrome extension, so the thread text was pasted manually. Prusa Forum content comes from WebSearch excerpts.
- **Evidence notation:** as in the other community reports. **C** = a pattern several users report; **D** = a single user report.

## CORPUS_SELECTION

| ID | Thread | Context |
|---|---|---|
| I01 | [IEMAI PC-CF troubleshooting (r/prusa3d)](https://www.reddit.com/r/prusa3d/comments/1qm59iy/iemai_pccf_troubleshooting/), about 2026-01 | MK4S, Core One L, Core One+; Prusament PC/PC-CF profiles as the starting point |
| I02 | [Printing with PC-CF, keeps lifting off print bed](https://forum.prusa3d.com/forum/prusa-core-one-how-do-i-print-this-printing-help/printing-with-pc-cf-keeps-lifting-off-print-bed) | Core One, IEMAI PC-CF, adhesion, EM test |
| I03 | [pc cf horizontal layer ripples](https://forum.prusa3d.com/forum/prusa-core-one-how-do-i-print-this-printing-help/pc-cf-horizontal-layer-ripples) | Core One, stock Prusament PC-CF profile, ripples |
| I04 | [upgraded now bad prusament pccf](https://forum.prusa3d.com/forum/original-prusa-mk3-5-assembly-and-first-prints-troubleshooting/upgraded-now-bad-prusament-pccf) | MK3.5, PC-CF quality after an upgrade |

## FINDINGS

- **The Prusament EM of 1.04 over-extrudes IEMAI (C).** I01 OP: 1.04 gave a messy top layer and blobs; 0.92 was clearly better and the OP suspected it could go lower. Another I01 user: 0.95 gave a nicer top and no blobbing. I02: EM tests settled on about 0.85, because 1.00 made walls about 0.15 mm too wide; 0.90–0.95 also seemed plausible. I03: the stock 1.04 was diagnosed as over-extrusion, with 0.85–0.90 suggested.
- **Counter-report on EM (D).** One I01 user found exactly 1.00 best in PrusaSlicer and 0.95 in OrcaSlicer, and warned that gaps in the bottom layer mean the part looks tidy but is weak. Takeaway: the community range is 0.85–1.00, so calibrate per spool and printer, and check both the top surface (ridges = too much) and the bottom (gaps = too little).
- **Diameter (D).** One roll measured 1.72 mm. CF fill makes the surface rough, so caliper readings run high (observed in this repo's session).
- **Temperature trade-off (D, consistent with PC physics).** 265 °C prints well. 275 °C or more bonds layers better but warps more. One user ran 285 °C first layer and 275 °C after that. The manufacturer range quoted in I01 is 250–280 °C. A Core One+ user at 285 °C reported clogs.
- **Surface and overhangs (C).** Several users find IEMAI coarser and more matte than Prusament PC Blend CF. One user called it "nasty on overhangs", which they attributed to short fibres and PC shrinkage, so they recommend it for small parts. Ironing helped top surfaces.
- **Adhesion (C).** Poor on satin and textured sheets. Glue stick (thinned with water), Magigoo PC or a Cryogrip plate solved it. One user suspected that over-extrusion causes lifting, because the nozzle drags over blobs and pulls corners up.
- **Other settings reported working (D).** Bed 110 °C, chamber 50 °C, volumetric flow 10 mm³/s; the speeds from the Prusa PC-CF profile were "spot on".
- **Mixed verdicts (C).** Two users abandoned it for Prusament PC-CF. One called it too brittle, while another found it "tough, not brittle" and less stiff than PLA.

## GAPS

- None of the reports discuss stringing or travel between islands.
- No Klipper or Voron reports; all are Prusa printers with Prusa firmware.
- No controlled strength tests.
