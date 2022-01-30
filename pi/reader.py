import requests
import RPi.GPIO as GPIO
import threading
import json
        
temp = 67
damp = 5
score = 10

def set_default(obj):
    if isinstance(obj, set):
        return list(obj)
    raise TypeError

result = json.dumps({"dampness": damp, "score": score, "temp": temp}, default=set_default)
print(result)
#print("temp ", temp, " damp ", damp, " score ", score)

res = requests.post('https://aqueous-tor-90407.herokuapp.com/data', json=result)
