# PLC Manual Sample

## Emergency Stop Reset

When an emergency stop is triggered, verify that all E-stop buttons are physically released before resetting the safety relay. Confirm that the PLC diagnostic buffer does not show an active safety input fault.

Recommended checks:

1. Confirm lockout and safe machine state before opening the panel.
2. Inspect safety relay indicators.
3. Check E-stop chain wiring continuity.
4. Confirm the PLC input mapped to the safety relay changes state.
5. Reset the fault from the HMI only after the safety circuit is healthy.

## Motor Overload Fault

For overload faults, inspect mechanical jams, motor current, overload relay trip state, and drive fault codes. Review previous maintenance records for repeated overload events.
