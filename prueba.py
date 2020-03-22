import RPI.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
#GPIO.setwarnings(False)

ledPin = 12

GPIO.setup(ledPin, GPIO.OUT)
GPIO.output(ledPin, True)
sleep(15)
GPIO.output(ledPin,False)
