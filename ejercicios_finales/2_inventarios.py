#Ejercicio 2: Administrador de Inventarios


inventario = {'manzanas': 50, 'naranjas': 30, 'peras': 20} 


def agregar(producto, cantidad):
    if producto in inventario:
        return " no puedes agregar un producto existente."
    else:
        #agregar fruta al diccionario (toma el producto que dijo el cliente y que está en el diccionario y 
        # le coloca la cantidad que ingrese )
        inventario[producto] = cantidad
        return f" Producto '{producto}' agregado con {cantidad} unidades."

def actualizar(producto, cantidad):
    if producto in inventario:
        inventario[producto] = cantidad
        return f" Stock de '{producto}' a {cantidad}."
    else:
        return " El producto no existe en el inventario."

def eliminar(producto):
    try:
        #usar el método del para borrar el producto
        del inventario[producto]
        return f" eliminando... '{producto}' "
    except:
        return " El producto no se encuentra en el inventario."

# Mostrar inventario inicial
print("inventario inicial: ", inventario)


    # Pedir acción 
producto = input("\nIngrese el nombre del producto: ")
accion = int(input("¿Qué desea hacer con el producto?\n1. Agregar\n2. Actualizar\n3. Eliminar\n "))

 
# Ejecutar la acción elegida
if accion == 1:
    cantidad = int(input(f"Ingrese la cantidad de '{producto}' para agregar: "))
    print(agregar(producto, cantidad))
elif accion == 2:
    cantidad = int(input(f"Ingrese la nueva cantidad de '{producto}': "))
    print(actualizar(producto, cantidad))
elif accion == 3:
    print(eliminar(producto))
else:
    print(" Opción no válida.")

#inventario final
print("inventario final: ", inventario)

