import RPi.GPIO as GPIO
import time

def startPump():

    GPIO.setmode(GPIO.BOARD)
    print ("starting pump!")

    GPIO.setup(7, GPIO.OUT)

    GPIO.output(7, GPIO.LOW)

    GPIO.output(7, GPIO.HIGH)
    time.sleep(10)
    GPIO.output(7, GPIO.LOW)
    print("stopping pump!")
    GPIO.output(7, GPIO.LOW)


startPump()