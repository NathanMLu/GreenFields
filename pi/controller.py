from sensorHandler import *
from pumpHandler import *
from pumpStopper import *

while True:
        
    if hasWater:
        pump()
    else:
        stop()