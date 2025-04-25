
from random import *


numero_secreto = randint(1,50)
intento = 1
numero = None #para que permita ingresarlo en el bucle
print('¡Bienvenido al juego "Adivina el Número"!\n Estoy pensando en un número entre 1 y 50.')

while numero != numero_secreto:
    try:
        numero= int(input((f"intento {intento} - Ingresa el número: ")))
        if numero < numero_secreto:
            print("el número secreto es mayor")
        elif numero > numero_secreto:
            print("el número secreto es menor")
        else:
            print(f" ¡Felicidades! Has adivinado el número secreto: {numero_secreto}")
            break  # Para salir del bucle

            #para que aumente el # de intentos dependiendo de 
            #si la entrada del user fue valida
        intento+=1

    except ValueError:
        print("no ingresaste un número válido...")


       
