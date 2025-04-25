from datetime import *


def dias_faltantes (fecha):
    hoy= datetime.today()
    diferencia = fecha - hoy
    return f"días faltantes: {diferencia.days}"
    
    
try:
    fecha_texto = input("Ingrese una fecha (DD/MM/AAAA): ")
    fecha_objeto = datetime.strptime(fecha_texto, "%d/%m/%Y")

    #manejar si el usuario da una fecha menor a la actual y así no de en negativo
    if fecha_objeto< datetime.today():
        print("ingrese una fecha mayor a la actual ")
    else:
        print(dias_faltantes(fecha_objeto))
except ValueError:
    print("fecha ingresada no valida")



