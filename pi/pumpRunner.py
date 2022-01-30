import time
import keyboard
import RPi.GPIO as GPIO

pin = 2

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)


print("Turning pin on")    
GPIO.output(pin, 1)
time.sleep(25)
GPIO.output(pin, 0)
print("Turning pin off")

GPIO.cleanup()  

	