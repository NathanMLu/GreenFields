import RPi.GPIO as GPIO
import time

PIN = 18
PUMPING = False

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)

def pump():
    
    print("pumping")
    global PUMPING, PIN

    if not PUMPING:
        GPIO.output(PIN, 0)
        time.sleep(10)
        GPIO.output(PIN, 1)
        time.sleep(10)
        
        

    PUMPING = False
  

while True:
    pump()


