import RPi.GPIO as GPIO
import time

channel = 17

def callback(channel):  
	if GPIO.input(channel):
		print ("Sensor off")
	else:
		print ("Sensor on")


GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)
GPIO.add_event_detect(channel, GPIO.BOTH)
ouncetime =300
GPIO.add_event_callback(channel, callback)
while True:
    time.sleep(0.1)
