import time
import keyboard
import RPi.GPIO as GPIO

pin = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)


while (True):
    if keyboard.is_pressed("space"):
        GPIO.output(pin, 0)
    else:
        GPIO.output(pin, 1)

	