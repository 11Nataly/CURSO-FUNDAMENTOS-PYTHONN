def conversiones_unidades (valor, conversion_unidad):
    try:
        if conversion_unidad == 1:
            return f"resultado: {valor} cm = {valor/ 2.54} pulgadas "
        elif conversion_unidad == 2:
            return f"resultado: {valor} km = {valor/ 1.609} milla(s) "
        #si no pone la opcion 1 ni 2 es invalida
        else:
            print("conversión elegida invalida")
        
        #capturar cualquier error que suceda
    except Exception  as errorcito:
        print("Error: ", errorcito)
  

conversion_unidad= int(input(("seleccione la conversión:\n 1. Centímetros a pulgadas \n 2. Kilómetros a millas\n  ")))
valor = float(input("Ingrese el valor que desea convertir: "))

#guardar el uso de la función en una variables
resultado= conversiones_unidades(valor,conversion_unidad)
print(resultado)



