import RPi.GPIO as GPIO
import time

init = False

def init_output(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    GPIO.output(pin, GPIO.HIGH)

def pump_on(p_pin = 7, delay = 1)
    init_output(p_pin)
    GPIO.output(p_pin, GPIO.LOW)
    time.sleep(1)
    GPIO.ouput(p_pin, GPIO.HIGH)
