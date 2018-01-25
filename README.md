# python-tsic

Receive temperature readings from TSIC 206/306 chips connected to Raspberry Pi GPIO.
The module `tsic.py` requires Python 3 and the great library `pigpio` for GPIO access with precise timing.

It provides three major classes:
* `TsicInputChannel` receive temperature measurements
* `Measurement` a temperature measurement
* `ZacWireInputChannel` received byte packets over ZACWire protocol (low-level handler for TsicInputChannel)

See `example.py` for API usage or start `tsic.py <gpio-bcm> [--loop]` to read temperatures from a GPIO pin (Broadcom numbering).

Greetings from Bavaria  
Holger Fleischmann
