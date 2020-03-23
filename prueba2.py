<<<<<<< HEAD
import RPi.GPIO as GPIO
=======
import RPI.GPIO as GPIO
>>>>>>> 0aacc0904b3d39094f04d4deba37aa8c5a4d2aad
from time import sleep 

GPIO.setmode(GPIO.BOARD)
#GPIO.setwarnings(False)

rojo = 12
naranja = 37
verde = 36
amarillo = 38
<<<<<<< HEAD
azul = 33
=======
azul = 35
>>>>>>> 0aacc0904b3d39094f04d4deba37aa8c5a4d2aad

class Luces:
    def __init__(self, port, status = 0 ):
        self.port = port
        self.status = status
        GPIO.setup(self.port, GPIO.OUT)

    def changeStatus(self):
        self.status = (self.status +1)%2
        GPIO.output(self.port,self.status)
<<<<<<< HEAD
=======
        sleep(0.5)
>>>>>>> 0aacc0904b3d39094f04d4deba37aa8c5a4d2aad

lista_luces=[]
lista_luces.append( Luces(rojo) )
lista_luces.append( Luces(naranja) )
lista_luces.append( Luces(verde) )
lista_luces.append( Luces(amarillo) )
lista_luces.append( Luces(azul) )

<<<<<<< HEAD
try:
	while True:
		for i in lista_luces:
			i.changeStatus()
		sleep(0.5)
except KeyboardInterrupt:
	GPIO.cleanup()
	
=======
while True:
    try:
        for i in lista_luces:
            lista_luces[i].changeStatus()


>>>>>>> 0aacc0904b3d39094f04d4deba37aa8c5a4d2aad
