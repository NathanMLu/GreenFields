from tracemalloc import start
import requests
import RPi.GPIO as GPIO
import threading
import time
import json

from pumpHandler import *
from sensorHandler import *
from calculate import getScore
        
temp = str(67)
damp = int(hasWater())
score = getScore()


result = {"dampness": damp, "score": score, "temp": temp}
print(result)


res = requests.post('https://aqueous-tor-90407.herokuapp.com/data', json=result)

def search():
    print("Started search")
    while True:
        res = requests.get('https://aqueous-tor-90407.herokuapp.com/water')
        print(res)
        time.sleep(2)
        startPumping()
        time.sleep(2)
        stopPumping()

t1 = threading.Thread(target = search)
t1.start()
t1.join()

GPIO.cleanup() 