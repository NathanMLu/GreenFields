from tracemalloc import start
import requests
import RPi.GPIO as GPIO
import threading
import time
import json

from pumpHandler import *
from sensorHandler import hasWater
from calculate import getScore
        
temp = str(67)
damp = int(hasWater())
score = getScore()


result = {"dampness": damp, "score": score, "temp": temp}
print(result)


res = requests.post('https://aqueous-tor-90407.herokuapp.com/data', json=result)

def search():
    while True:
        time.sleep(2)
        res = requests.get('https://aqueous-tor-90407.herokuapp.com/water')
        if (res):
            startPumping()

t1 = threading.Thread(target = search)
t1.start()
t1.join()

GPIO.cleanup() 