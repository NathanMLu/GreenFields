import requests
import RPi.GPIO as GPIO
import threading
import json

from sensorHandler import hasWater
from calculate import getScore
        
temp = str(67)
damp = int(hasWater())
score = getScore()


result = {"dampness": damp, "score": score, "temp": temp}
print(result)

res = requests.post('https://aqueous-tor-90407.herokuapp.com/data', json=result)
