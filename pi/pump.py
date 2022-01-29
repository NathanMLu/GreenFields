
"""
import RPi.GPIO as GPIO
import time


def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(7, GPIO.OUT)
    startPump()

def startPump():
    print ("starting pump!")
    GPIO.output(7,GPIO.LOW)
    time.sleep(10)
    GPIO.output(7, GPIO.HIGH)
    print("stopping pump!")

    GPIO.cleanup()
    """
import RPi.GPIO as GPIO            # import RPi.GPIO module  
from time import sleep
GPIO.setwarnings(False)             # lets us have a delay  
GPIO.setmode(GPIO.BCM)             # choose BCM or BOARD  
GPIO.setup(7, GPIO.OUT)           # set GPIO24 as an output   
  

GPIO.output(7, 1)         # set GPIO24 to 1/GPIO.HIGH/True  
sleep(10)                 # wait half a second  
GPIO.output(7, 0)         # set GPIO24 to 0/GPIO.LOW/False  
 
GPIO.cleanup()  


