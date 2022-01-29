import RPi.GPIO as GPIO
import time

init = False

def init_output(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    GPIO.output(pin, GPIO.HIGH)
    pump_on()

def pump_on(p_pin = 7, delay = 10):
    init_output(p_pin)
    print("starting pump")
    GPIO.output(p_pin, GPIO.LOW)
    time.sleep(delay)
    GPIO.ouput(p_pin, GPIO.HIGH)
    print("stopping pump")

init_output(7)

