import RPi.GPIO as GPIO
import time
import threading

PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)

def startPumping():
    print("pumping")
    global PIN
    GPIO.output(PIN, 0)
    time.sleep(5)


def stopPumping():
    print("stopping")
    global PIN
    GPIO.output(PIN, 1)
    time.sleep(5)

"""
def pumpLoop():
    while True:
        print("Starting pump")
        startPumping()
        time.sleep(5)
        print("Stopping pump")
        stopPumping
        time.sleep(5)
        
t1 = threading.Thread(target = pumpLoop)
t1.start()
t1.join()
"""
GPIO.cleanup() 