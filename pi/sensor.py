import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
channel = 17
GPIO.setup(channel, GPIO.IN)
GPIO.add_event_detect(channel, GPIO.BOTH)
ouncetime =300
GPIO.add_event_callback(channel, callback)
while True:
    time.sleep(0.1)
