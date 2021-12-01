"""
circuit:

3.3V      SPST      
 (V+) _____/ ____(GPIO17)
                   
To close the switch, touch the two leads! 

**DO NOT DO THIS WITH 5V!!!**

"""


import time
import RPi.GPIO as GPIO

# Use the GPIO numbers, *not* the physical pin numbers
GPIO.setmode(GPIO.BCM)

# Use GPIO 17, which is physical pin 11
pin = 17
GPIO.setup(pin, GPIO.IN)

start_time = time.time()
elapsed_time = 0.0
while elapsed_time < 10:

    if GPIO.input(pin) == GPIO.HIGH:
        print("It's pressed!!!")

    time.sleep(0.1) 
    elapsed_time = time.time() - start_time


def my_callback(channel):
    print("Hello from the other sideeeeee")

GPIO.add_event_detect(pin, GPIO.RISING)
GPIO.add_event_callback(pin, my_callback)

print("Now, we wait for an event!  Type Ctl+C to quit.")
try:
    while True:
        
        if GPIO.event_detected(pin):
            print("Hello, is it me you're looking for?")
            break 
except KeyboardInterrupt:
    pass

GPIO.cleanup()


