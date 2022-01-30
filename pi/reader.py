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

result = {"water": 0}
print(result)
res = requests.post('https://aqueous-tor-90407.herokuapp.com/water', json=result)

def search():
    print("Started search")
    while True:
        res = requests.get('https://aqueous-tor-90407.herokuapp.com/water')
        res_json = res.json()

        if (res_json["water"] == 1):
            startPumping()
            time.sleep(10)
            stopPumping()
        else:
            stopPumping()
            print("wrong json")
        
        time.sleep(5)

t1 = threading.Thread(target = search)
t1.start()
t1.join()

GPIO.cleanup() 