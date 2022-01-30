#PIN 11
import RPi.GPIO as GPIO
import threading
import time

soilPin = 11
water = False
GPIO.setmode(GPIO.BOARD)
GPIO.setup(soilPin, GPIO.IN)




def callback(soilPin):
    global water

    if not GPIO.input(soilPin):
        water = False
        print("No water detected")
    else:
        water = True
        print("Water detected")

def hasWater():
    return water

GPIO.add_event_detect(soilPin, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(soilPin, callback)
"""

def sensorLoop():
    while True:
        time.sleep(1)
        
t1 = threading.Thread(target = sensorLoop)
"""
while True:
    time.sleep(1)
