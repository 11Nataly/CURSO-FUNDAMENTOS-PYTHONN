import random
import string


def crear_contraseña (longitud):
        caracteres = string.ascii_uppercase+string.ascii_lowercase+string.digits+string.punctuation
        caracteres_lista = list(caracteres)
        caracteres_contraseña= random.sample(caracteres_lista,longitud)
        contraseña = ''.join(caracteres_contraseña) # '' antes del join para los elementos se unen en un string sin ningún carácter entre ellos.
        return f"su contraseña es:  {contraseña}"
    

try:
    longitud= int(input("ingrese la longitud de la contraseña: "))
    if longitud >0:
        print(crear_contraseña(longitud))
    else: 
        print("la longitud debe ser mayor a 0")
    

except Exception as error:
    print("error: ", error)