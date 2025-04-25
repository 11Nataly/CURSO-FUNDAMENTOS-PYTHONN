#ejercicio 1: calculadora avanzada

#funciones con if/else para cada operacion

def calculadora (num1,num2, operador):
    if operador == '+':
        return f"{num1} + {num2} = {num1 + num2}"
    
    elif operador == '-':
        return f"{num1} - {num2} = {num1 - num2}"
        
    elif operador == '*':
        return f"{num1} * {num2} = {num1 * num2}"
         
    elif operador == '/':
        return f"{num1} / {num2} = {num1 / num2}"
         
    elif operador == '**':
        return f"{num1} ** {num2} = {num1 ** num2}"
         
    elif operador == '//':
        return f"{num1} // {num2} = {num1 // num2}"
         
    else: 
        print('No ha ingresado un operador correcto')

 #pedirle al usuario que ingrese número y devolverle el resultado si todo es corrrecto   
try:
    num1 = int(input('Ingrese el primero número: '))
    num2 = int(input('Ingrese el segundo número: '))
    operador = input('Ingrese el operador que desea utilizar (+, -, *, /, **, //): ')
    resultado = calculadora(num1, num2, operador)
    print("Resultado:", resultado)

#gestionar excepciones
except  ZeroDivisionError:
    print("No se puede dividir entre cero")

except  ValueError:
    print("Valor Ingresado no valido")

    