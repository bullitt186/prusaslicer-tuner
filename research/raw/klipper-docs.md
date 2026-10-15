# Klipper documentation research

## SOURCE_METADATA

Official Klipper documentation, inspected 2026-10-13.

## COVERAGE

Pressure Advance, Resonance Compensation, Measuring Resonances, Rotation Distance, Kinematics, Configuration Reference, G-Codes, Command Templates, Configuration Checks, Configuration Changes and Slicers.

## CLAIMS

The documentation covers firmware-owned `rotation_distance`, `pressure_advance`, input shaper, motion limits, firmware retraction, PID and macro state.

## PROCEDURES

Measured extruder calibration; PA square-tower tuning with separate direct-drive/Bowden factors; resonance measurement with shaping and PA disabled; shaper selection based on residual vibration versus smoothing; PID calibration per heater; explicit macro state preservation.

## NUMERICAL_VALUES

PA factors `.005` direct drive and `.020` long Bowden; default PA smoothing `0.040 s`; default square-corner velocity `5 mm/s`; values are procedure-specific.

## CONFLICTS_OR_LIMITS

Acceleration remains printer-specific, and the documentation lacks a universal flow/temperature tower or complete slicer PA/retraction contract.

## GAPS

No universal material-to-PA table or complete safe-acceleration method is provided.

## CITATIONS

- https://www.klipper3d.org/Pressure_Advance.html
- https://www.klipper3d.org/Resonance_Compensation.html
- https://www.klipper3d.org/Rotation_Distance.html
- https://www.klipper3d.org/Config_Reference.html
- https://www.klipper3d.org/Command_Templates.html
