import time
import RPi.GPIO as GPIO

pin = 18

GPIO.setmode(GPIO.BCM) #setting boardset
GPIO.setup(pin, GPIO.OUT)


while (True):
 
    GPIO.output(pin, 1)
    time.sleep(1)
    GPIO.output(pin, 0)
    time.sleep(1)


	