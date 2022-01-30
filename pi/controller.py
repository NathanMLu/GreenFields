from sensorHandler import *
from pumpHandler import *
from pumpStopper import *

if hasWater:
    pump()
else:
    stop()