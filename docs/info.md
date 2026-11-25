## How it works

The Hydraulic Fault Detector is a digital ASIC designed
to identify abnormal conditions in hydraulic systems
using pressure and flow signals.

The circuit uses four digital inputs:

- UI0: Low pressure.
- UI1: High pressure.
- UI2: Low flow.
- UI3: High flow.

The circuit generates four digital outputs:

- UO0: Possible water leak.
- UO1: Possible obstruction.
- UO2: Low pressure warning.
- UO3: General alarm.

A possible leak is indicated when low pressure and
high flow are detected simultaneously.

A possible obstruction is indicated when high pressure
and low flow are detected simultaneously.

The general alarm is activated when any programmed
fault condition or contradictory input is detected.

The design uses combinational logic and does not
require an external clock.

## How to test

Apply digital signals to inputs UI0 through UI3
and observe outputs UO0 through UO3.

The following table describes the expected results.

| UI[3:0] | UO[3:0] | Condition |
|---------|---------|-----------|
| 0000 | 0000 | Normal operation |
| 0001 | 1100 | Low pressure |
| 1001 | 1101 | Possible leak |
| 0110 | 1010 | Possible obstruction |
| 0101 | 1100 | Low pressure and low flow |
| 0011 | 1000 | Invalid pressure inputs |
| 1100 | 1000 | Invalid flow inputs |
| 1111 | 1000 | Contradictory inputs |

All 16 possible input combinations are verified
using automated Cocotb simulation tests.

## External hardware

Pressure sensor, flow sensor, external signal
conditioning circuits and digital output indicators.

The sensor signals must be converted into compatible
digital logic levels before connecting to the ASIC.

The hydraulic fault detection rules require
experimental validation under real operating conditions.
