import RPi.GPIO as GPIO
import time

PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)

def startPumping():
    print("pumping")
    global PIN
    GPIO.output(PIN, 0)


def stopPumping():
    print("stopping")
    global PIN
    GPIO.output(PIN, 1)
  


