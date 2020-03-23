import RPi.GPIO as GPIO
from time import sleep 

GPIO.setmode(GPIO.BOARD)
#GPIO.setwarnings(False)

rojo = 12
naranja = 37
verde = 36
amarillo = 38
azul = 33
GPIO.setup(rojo, GPIO.OUT)
GPIO.setup(naranja, GPIO.OUT)
GPIO.setup(verde, GPIO.OUT)
GPIO.setup(azul, GPIO.OUT)
GPIO.setup(amarillo, GPIO.OUT)
try:	
	while True:
		
		GPIO.output(rojo, True)
		GPIO.output(naranja, True)
		GPIO.output(verde, True)
		GPIO.output(amarillo, True)
		GPIO.output(azul,True)
	
		sleep(.5)
		GPIO.output(rojo, False)
		GPIO.output(naranja, False)
		GPIO.output(verde, False)
		GPIO.output(amarillo, False)
		GPIO.output(azul,False)
		sleep(.5)
except KeyboardInterrupt:
	GPIO.cleanup()


