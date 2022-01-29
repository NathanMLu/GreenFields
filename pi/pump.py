import RPi.GPIO as GPIO
import time

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(7, GPIO.OUT)
    startPump()

def startPump():

    GPIO.output(7,0)
    time.sleep(3)
    print ("starting pump!")
    GPIO.output(7, 1)
    time.sleep(10)
    GPIO.output(7, 0)
    print("stopping pump!")





setup()