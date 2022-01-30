import threading
import RPi.GPIO as GPIO
import time

from sensorHandler import *
from sensorHandler import *
from pumpHandler import *
from pumpStopper import *

GPIO.setmode(GPIO.BOARD)

""" MOISTURE SENSOR """

soilPin = 11
water = False

GPIO.setup(soilPin, GPIO.IN)

def callback(soilPin):
    global water

    if not GPIO.input(soilPin):
        water = False
        print("No water detected")
    else:
        water = True
        print("Water detected")

GPIO.add_event_detect(soilPin, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(soilPin, callback)

def sensorLoop():
    while True:
        time.sleep(1)


""" PUMP """

PIN = 12
GPIO.setup(PIN, GPIO.OUT)

def startPumping():
    print("pumping")
    global PIN
    GPIO.output(PIN, 0)
    time.sleep(5)


def stopPumping():
    print("stopping")
    global PIN
    GPIO.output(PIN, 1)
    time.sleep(5)

def pumpLoop():
    while True:
        print("Starting pump")
        startPumping()
        time.sleep(5)
        print("Stopping pump")
        stopPumping
        time.sleep(5)

# Threading  

t1 = threading.Thread(target = sensorLoop)
t2 = threading.Thread(target = pumpLoop)
t1.start()
t2.start()
t1.join()
t2.join()
        





