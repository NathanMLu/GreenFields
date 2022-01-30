from sensorHandler import *
from pumpHandler import *
from pumpStopper import *

while True:
    if hasWater:
        print("pumping")
        pump()
