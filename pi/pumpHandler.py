import RPi.GPIO as GPIO
import time

PIN = 18
PUMPING = True

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

def pump():
    global PUMPING, PIN

    if not PUMPING:
        GPIO.output(PIN, 1)
        time.sleep(10)
        GPIO.output(PIN, 0)

    PUMPING = False

while True:
    pump()

