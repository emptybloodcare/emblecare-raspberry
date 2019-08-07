import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)

try:
    while True:
	GPIO.output(2, True)
        
        time.sleep(1)


except KeyboardInterrupt:
    GPIO.cleanup()
