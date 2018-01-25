#!/usr/bin/python3

"""
Examples of how to use the TSIC 206/306 temperature reading class
on a Raspberry PI.
"""

__author__ = 'Holger Fleischmann'
__copyright__ = 'Copyright 2018, Holger Fleischmann, Bavaria/Germany'
__license__ = 'Apache License 2.0'

import pigpio
from tsic import TsicInputChannel
import time

# TsicInputChannel and ZacWireInputChannel require pigpio
# for GPIO access with precise timing:
pi = pigpio.pi()

tsic = TsicInputChannel(pigpio_pi=pi, gpio=17)

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
        print('{:d} {:.1f}°C'.format(i+1, tsic.measurement.degree_celsius))

pi.stop()
