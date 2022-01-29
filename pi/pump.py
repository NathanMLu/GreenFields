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






setup()