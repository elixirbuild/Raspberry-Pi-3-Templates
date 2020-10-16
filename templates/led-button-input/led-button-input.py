# modules
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

sleepTime = .1

GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
  GPIO.output(4, GPIO.inout(17))
  sleep(sleepTime)
finally:
  GPIO.output(4, False)
  GPIO.cleanup()
