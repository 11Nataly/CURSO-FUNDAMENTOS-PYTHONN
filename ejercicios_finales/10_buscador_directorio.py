import os

def buscar_archivos(directorio, subcadena):
    try:
        # Listar el contenido del directorio
        contenido = os.listdir(directorio)
        
        # Lista donde se almacenarán los archivos encontrados
        archivos_encontrados = []
        
        # Recorremos cada archivo o carpeta en el directorio
        for archivo in contenido:
            # Crear la ruta completa del archivo
            ruta_completa = os.path.join(directorio, archivo)
            
            # Verificamos si es un archivo y si contiene la subcadena
            es_archivo = os.path.isfile(ruta_completa)  # Verifica si es un archivo
            contiene_subcadena = subcadena in archivo  # Verifica si la subcadena está en el nombre
            
            # Si ambos son verdaderos, agregamos el archivo a la lista de encontrados
            if es_archivo and contiene_subcadena:
                archivos_encontrados.append(archivo)
        
        # Mostrar los resultados
        if archivos_encontrados:
            print(f"Archivos encontrados que contienen '{subcadena}':")
            for archivo in archivos_encontrados:
                print(archivo)
        else:
            print(f"No se encontraron archivos con la subcadena '{subcadena}'.")

    except FileNotFoundError:
        print("El directorio no existe.")
    except PermissionError:
        print("No tienes permisos para acceder a este directorio.")
    except Exception as e:
        print("Ocurrió un error:", e)

# Solicitar al usuario la ruta del directorio y la subcadena
directorio = input("Ingrese la ruta del directorio: ")
subcadena = input("Ingrese la subcadena a buscar en los nombres de archivo: ")

# Llamar a la función para buscar los archivos
buscar_archivos(directorio, subcadena)