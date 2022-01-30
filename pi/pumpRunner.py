import time
import keyboard
import RPi.GPIO as GPIO

pin = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)


while (True):
    GPIO.output(pin, 1)
    time.sleep(25)
    GPIO.output(pin, 0)

	