#import libraries
import time
import RPi.GPIO as GPIO

#GPIO setup ---- Pump = pin 7, GPIO 4
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

GPIO.ouput(7,True)

	