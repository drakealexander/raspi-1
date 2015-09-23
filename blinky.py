"""My super awesome blinky light modules"""

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
pins = [22,6,13,26]
GPIO.setup(pins, GPIO.OUT, initial=GPIO.HIGH)

def drag(sleep=0.10, count=1):
	for n in range(count):
		for p in pins:
			GPIO.output(p,1)
			time.sleep(sleep)
		for p in pins[:]:
			GPIO.output(p,0)
			time.sleep(sleep)

def blink(sleep=0.25, count=1):
	for n in range(count):
        	GPIO.output(pins,1)
        	time.sleep(sleep)
        	GPIO.output(pins,0)
        	time.sleep(sleep)
	
