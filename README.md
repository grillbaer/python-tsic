# python-tsic

Receive temperature readings from TSic sensor chips connected to Raspberry Pi GPIO. 

Supported:
* TSic 206/306
* TSic 506
* TSic 716

Don't forget the bypass capacitor as near as possible to the sensor's power supply pins to get stable behavior.

## Dependencies

The package `tsic` requires Python 3 and the great library `pigpio` for GPIO access with precise timing. Note that Python 2 will not work.

## Installation

Install from Python package index [PyPI](https://pypi.org/project/tsic/):
```
pip3 install tsic
```

## Usage

The module `tsic` provides the following classes:
* `TsicInputChannel` receive temperature measurements
* `Measurement` a temperature measurement
* `TsicType` TSic type definition with instances `TSIC206`, `TSIC306`, `TSIC506`, `TSIC716` (206 and 306 are currently equivalent)
* `ZacWireInputChannel` receive byte packets over ZACWire protocol (low-level handler for `TsicInputChannel`)

### Command Line Test Tool

Run `tsic <gpio-bcm> [--type {206,506,716,306}] [--loop]` to read temperatures from a GPIO pin (Broadcom numbering). See `tsic --help` for command line usage.

```
pi@raspi3:~ $ sudo tsic 19 --type 306
Receiving data from TSic 206/306...
Measurement 17.90°C at 2018-11-10 16:16:11.419573
```

### Examples 

From file `example.py`:
```python
import time
import pigpio

from tsic import TsicInputChannel, Measurement, TSIC306

# TsicInputChannel and ZacWireInputChannel require pigpio
# for GPIO access with precise timing:
pi = pigpio.pi()

tsic = TsicInputChannel(pigpio_pi=pi, gpio=17, tsic_type=TSIC306)

print('\nA. Single measurement:')
print(tsic.measure_once(timeout=1.0))

print('\nB. All measurements for 1 second:')
tsic.start(lambda measurement: print(measurement))
time.sleep(1)
tsic.stop()

print('\nC. One measurement per second for 3 seconds:')

# start receiving in a context:
with tsic:
    for i in range(3):
        time.sleep(1)
        measurement = tsic.measurement
        if measurement == Measurement.UNDEF:
            print(measurement)
        else:
            print('{:d} {:.1f}°C'.format(i+1, measurement.degree_celsius))

pi.stop()
```

## Source Code

Hosted on [github.com/grillbaer/python-tsic](https://github.com/grillbaer/python-tsic)

With greetings from Bavaria,
Holger
