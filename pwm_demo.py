"""
circuit:
          
GPIO18     LED         R
 (V+) ___  ▶|  ____ /\/\/\ _______
        |                        |  
        |__ voltage indicator ___|
                                 ⏚

Can you write a script to automatically go through duty cycles
in steps of 10% so that you can record the voltage along the way
on the indicator?              
"""

import time
import RPi.GPIO as GPIO

# Use the GPIO numbers, *not* the physical pin numbers
GPIO.setmode(GPIO.BCM)

# Use GPIO 18, which is physical pin 12
pin = 18
GPIO.setup(pin, GPIO.OUT)

# Set the PWM frequency (Hz)
freq = 50 

p = GPIO.PWM(pin, freq)  
p.start(0)
try:
    while 1:
        for dc in range(0, 101, 5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
        for dc in range(100, -1, -5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
except KeyboardInterrupt:
    pass
p.stop()
GPIO.cleanup()
