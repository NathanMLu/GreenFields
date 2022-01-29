
import RPi.GPIO as GPIO
import time


def setup():
    GPIO.setmode(GPIO.BCM)
    pinOn(11)


def pinOn(pin):
    GPIO.setup(pin, GPIO.OUT)
    print ("Turning on pin ", pin)
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(10)
    GPIO.output(pin, GPIO.LOW)
    print("Turning off pin ", pin)

    GPIO.cleanup()

setup()