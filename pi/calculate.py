score = 100

from pumpHandler import *
from sensorHandler import *

def getScore():
    global score

    if not hasWater:
        score = 75
    else:
        score = 100

    return score