
def calcular_frecuencia(texto):
    try:
        #pasar el texto a minuscula
        texto = texto.lower()

        # Reemplazar signos de puntuación comunes por espacio
        for signo in [",", ".", ";", ":", "!", "?", '"', "¿", "¡"]:
            #reemplaza el singo por espacio
            texto = texto.replace(signo, "")

        #divide las palabras según los espacios (entonces, lo elimina)
        palabras_texto = texto.split()
        #iniciar diccionario
        frecuencia = {}

        for palabra in palabras_texto:
            if palabra in frecuencia:
                frecuencia[palabra] += 1 #con esto accedemos a una clave en el diccionario frecuencia
            else:
                frecuencia[palabra] = 1

        print("\nFrecuencia de palabras:")
        for palabra in frecuencia: #vemos las palabras en el diccionario (ej: hola)
            conteo = frecuencia[palabra] # guardamos en conteo la clave de cada palabra (ej: 3)
            #vemos la palabra ingresada y la clave de esa palabra (como el número al lado de hola ej: hola: 3)
            print(f" {palabra}: {conteo}")

    except:
        print('Error. Vuelve a intentarlo')

# Pedir entrada al usuario
texto_cliente = input("Ingrese un texto: ")
#usamos la función con la  y la cadena de texto que ponga el cliente como argumento

calcular_frecuencia(texto_cliente) 
#la función misma incluye un retorno que produce una salida procesada:::::
#como la función ya tiene en el try el bucle for para que muestre la
#frecuencia de palabras entonces no es necesario guardarla en una variable



