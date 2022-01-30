#PIN 11
import RPi.GPIO as GPIO
import time

soilPin = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(soilPin, GPIO.IN)

def callback(soilPin):
    if not GPIO.input(soilPin):
        print("No water detected")
    else:
        print("Water detected")

GPIO.add_event_detect(soilPin, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(soilPin, callback)

while True:
    time.sleep(1)