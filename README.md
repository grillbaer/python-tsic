# python-tsic

Receive temperature readings from TSic sensor chips connected to Raspberry Pi GPIO. 

Supported:
* TSic 206/306
* TSic 506
* TSic 706

The module `tsic.py` requires Python 3 and the great library `pigpio` for GPIO access with precise timing. 

Note: Python 2 will not work.

It provides the following classes:
* `TsicInputChannel` receive temperature measurements
* `Measurement` a temperature measurement
* `TsicType` TSic type definition with instances `TSIC206`, `TSIC306`, `TSIC506`, `TSIC716` (206 and 306 are currently equivalent)
* `ZacWireInputChannel` receive byte packets over ZACWire protocol (low-level handler for TsicInputChannel)

See `example.py` for API usage or start `tsic.py <gpio-bcm> [--type {206,506,716,306}] [--loop]` to read temperatures from a GPIO pin (Broadcom numbering). See `tsic.py --help` for command line usage.

Example:
```
pi@raspi3:~/python-tsic $ ./tsic.py 19 --type 306
Receiving data from TSic 206/306...
Measurement 17.90°C at 2018-11-10 16:16:11.419573
```

Greetings from Bavaria  
Holger
