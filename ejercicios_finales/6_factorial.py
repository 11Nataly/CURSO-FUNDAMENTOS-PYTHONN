#Multiplica n por todos los números anteriores a él hasta llegar a 1.
def factorial_recursivo(n):
        #en caso de que sea 0 o 1, el factorial será 1
        if  n <= 1:
            return 1
        else:
            #solución recursiva porque la función se llama dentro de la misma función
            #La recursión es una técnica en programación donde una función se llama a sí misma para resolver un problema más pequeño del mismo tipo,
            #  hasta llegar a un caso base que se puede resolver directamente.
            return n * factorial_recursivo(n-1) #  → 4 * factorial_recursivo(3)
                                                #→ 4 * (3 * factorial_recursivo(2))
                                                #→ 4 * (3 * (2 * factorial_recursivo(1)))
                                                # → 4 * 3 * 2 * 1 → 24
        
try:
    num = int(input("Ingrese el numero entero para calcular su factorial:"))
    #probar si es negativo
    if num <0:
        print("el número no puede ser negativo")
    else:
        #si no es negativo muestra el resultado
        print(f"EL factorial de {num} es {factorial_recursivo(num)}") 
        
except ValueError:
        print("El número no es entero")
 


