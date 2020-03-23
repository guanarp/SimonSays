import RPI.GPIO as GPIO
from time import sleep 

GPIO.setmode(GPIO.BOARD)
#GPIO.setwarnings(False)

rojo = 12
naranja = 37
verde = 36
amarillo = 38
azul = 35

GPIO.setup(rojo, GPIO.OUT)
GPIO.output(rojo, True)
GPIO.output(naranja, True)
GPIO.output(verde, True)
GPIO.output(amarillo, True)

sleep(1)
GPIO.output(rojo,False)
GPIO.output(rojo, False)
GPIO.output(naranja, False)
GPIO.output(verde, False)
GPIO.output(amarillo, False)


