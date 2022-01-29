import RPi.GPIO as GPIO
import time

def startPump():

    GPIO.setmode(GPIO.BCM)
    print ("starting pump!")

    GPIO.setup(7, GPIO.OUT)

    GPIO.output(7, GPIO.HIGH)
    time.sleep(10)

    print("stopping pump!")
    GPIO.output(7, GPIO.LOW)


startPump()