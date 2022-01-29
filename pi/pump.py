import RPi as GPIO
import time

def startPump():

    GPIO.setmode(GPIO.BCM)
    print ("starting pump!")

    GPIO.output(4, GPIO.HIGH)
    time.sleep(10)

    print("stopping pump!")
    GPIO.output(4, GPIO.LOW)


startPump()