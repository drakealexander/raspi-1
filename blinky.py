"""My super awesome blinky light modules"""

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
pins = [22,6,13,26]


#####Three
threeone = [22]
threetwo = [22,6]
threethree = [22, 6, 13]
threefour = [22, 6, 13,26]

#####Jump
jumpone = [22, 6]
jumptwo = [13,26]
jumpthree = [6,13]

#####Out
outone = [22,26]
outtwo = [6,13]
outthree = [22,13]
outfour = [6,26]

#####Space
spaceone = [6,13]
spacetwo = [26,22]

######Swipe
swipeone = [22]
swipetwo = [6]
swipethree = [13]
swipefour = [26]

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

def three(sleep=0.25, count=1):
	for n in range(count):
		GPIO.output(threeone,1)	
		time.sleep(0.50)
		GPIO.output(threetwo,1)
		time.sleep(0.50)
		GPIO.output(threethree,1)
		time.sleep(0.50)
		GPIO.output(threefour,1)

def jump(sleep=0.25, count=1):
	for n in range(count):
			GPIO.output(jumpone,1)
			time.sleep(sleep)
			GPIO.output(jumpone,0)
			GPIO.output(jumptwo,1)
			time.sleep(sleep)
			GPIO.output(jumptwo,0)
			GPIO.output(jumpthree,1)

def out(sleep=0.25, count=1):
	for n in range(count):
		GPIO.output(outone,1)
		time.sleep(0.50)
		GPIO.output(outone,0)
		GPIO.output(outtwo,1)
		time.sleep(0.50)
		GPIO.output(outtwo,0)
		GPIO.output(outthree,1)
		time.sleep(0.50)
		GPIO.output(outthree,0)
		GPIO.output(outfour,1)

def spike(sleep=0.05, count=5):
	for n in range(count):
		GPIO.output(pins,1)
		time.sleep(sleep)
		GPIO.output(pins,0)
		time.sleep(sleep)
                

def space(sleep=0.25, count=1):
	for n in range(count):
		GPIO.output(spaceone,1)
		time.sleep(sleep)
		GPIO.output(spaceone,0)
		time.sleep(sleep)
		GPIO.output(spacetwo,1)
		time.sleep(sleep)
		GPIO.output(spacetwo,0)

def swipe(sleep=0.05, count=2):
    for n in range(count):
        GPIO.output(swipeone,1)
        time.sleep(sleep)
        GPIO.output(swipeone,0)
        time.sleep(sleep)
        GPIO.output(swipetwo,1)
        time.sleep(sleep)
        GPIO.output(swipetwo,0)
        time.sleep(sleep)
        GPIO.output(swipethree,1)
        time.sleep(sleep)
        GPIO.output(swipethree,0)
        time.sleep(sleep)
        GPIO.output(swipefour,1)
        time.sleep(sleep)
        GPIO.output(swipefour,0)
        time.sleep(sleep)
        GPIO.output(swipethree,1)
        time.sleep(sleep)
        GPIO.output(swipethree,0)
        time.sleep(sleep)
        GPIO.output(swipetwo,1)
        time.sleep(sleep)
        GPIO.output(swipetwo,0)
        time.sleep(sleep)
        GPIO.output(swipeone,1)
        time.sleep(sleep)
        GPIO.output(swipeone,0)
        time.sleep(sleep)

def base(sleep=1.5, count=1):
    GPIO.output(pins,1)
    time.sleep(sleep)
