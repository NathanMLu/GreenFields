import RPi.GPIO as GPIO
import time

PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)

def stop():
    GPIO.output(PIN, 1)

stop()

