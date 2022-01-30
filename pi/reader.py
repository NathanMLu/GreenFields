import requests
import RPi.GPIO as GPIO
import time
import threading

from calculate import *

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


def sensorLoop():
    while True:
        time.sleep(1)
        


temp = 67
damp = hasWater()
score = getScore()

print("temp ", temp, " damp ", damp, " score ", score)
res = requests.post('https://aqueous-tor-90407.herokuapp.com/data', json={temp, damp, score})

t1 = threading.Thread(target = sensorLoop)
t1.start()
t1.join()

