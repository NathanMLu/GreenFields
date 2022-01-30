from sensorHandler import *
from pumpHandler import *
from pumpStopper import *

while True:
    time.sleep(0.5)
    if hasWater:
        print("pumping")
        pump()
