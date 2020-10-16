# blink.py
# a template for blinking led lights

# modules
from time import sleep
# for the GPIO wires
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# set on GPIO4
GPIO.setup(4, GPIO.OUT)
# turn LED on
GPIO.output(4, True)
sleep(1)
# turn LED off after a second
GPIO.output(4, False)

# required:
# Raspberry Pi 3
# Red and black wire
# Red wire in GPIO4
# Black wire in GND (ground)
# 220 resistor
# Led light
