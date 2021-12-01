"""
circuit:

GPIO18     LED         R
 (V+) ___  ▶|  ____ /\/\/\ ______
                                 ⏚  GND

where V+ is roughly 3.3V when in a high state.  Measure it!               
"""


import time
import RPi.GPIO as GPIO

# Use the GPIO numbers, *not* the physical pin numbers
GPIO.setmode(GPIO.BCM)

# Use GPIO 18, which is physical pin 12
pin = 18
GPIO.setup(pin, GPIO.OUT)

 # wait 2 seconds so we're ready to watch
time.sleep(2)

# turn it on and wait 2 more seconds
GPIO.output(pin, GPIO.HIGH)
time.sleep(2) 

# turn it back off
GPIO.output(pin, GPIO.LOW)
