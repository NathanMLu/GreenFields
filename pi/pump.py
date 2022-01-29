
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
soilPin = 11

GPIO.setup(soilPin, GPIO.IN)

def pinOn(pin):
    GPIO.setup(pin, GPIO.OUT)
    print ("Turning on pin ", pin)
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(10)
    GPIO.output(pin, GPIO.LOW)
    print("Turning off pin ", pin)

    GPIO.cleanup()

def callback(soilPin):
    if GPIO.input(soilPin):
        print("No water detected")
    else:
        print("Water detected")

GPIO.add_event_detect(soilPin, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(soilPin, callback)

while True:
    print("Still going")
    #callback(11)
    time.sleep(1)