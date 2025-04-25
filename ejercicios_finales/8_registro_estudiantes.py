# Ejercicio 2: Administrador de Estudiantes

estudiantes = {'Ana': 90, 'Luis': 78, 'Carlos': 85}

def agregar_estudiante(estudiante, calificacion):
    if estudiante in estudiantes:
        return "No puedes agregar un estudiante ya existente."
    else:
        estudiantes[estudiante] = calificacion
        return f"Estudiante agregado: {estudiante} - {calificacion}"

def actualizar_cal(estudiante, calificacion):
    if estudiante in estudiantes:
        estudiantes[estudiante] = calificacion
        return f"Calificación actualizada: {estudiante} - {calificacion}"
    else:
        return "No se encuentra al estudiante."

def eliminar_estudiante(estudiante):
    if estudiante in estudiantes:
        del estudiantes[estudiante]
        return f"Eliminando... '{estudiante}'"
    else:
        return "No se encuentra al estudiante."

def listar_estudiantes():
    if estudiantes:
        print("Listado de estudiantes:")
        for estudiante, calificacion in estudiantes.items():
            print(f"{estudiante} - {calificacion}")
    else:
        print("No hay estudiantes registrados.")

# Menú interactivo
accion = 0
while accion != 5:
    try:
        print("\nMenú:")
        accion = int(input("1. Agregar estudiante\n2. Actualizar calificación\n3. Eliminar estudiante\n4. Listar estudiantes\n5. Salir\nSeleccione una opción: "))

        if accion == 1:
            estudiante = input("Ingrese el nombre del estudiante a agregar: ")
            calificacion = float(input(f"Ingrese la calificación de '{estudiante}': "))
            print(agregar_estudiante(estudiante, calificacion))

        elif accion == 2:
            estudiante = input("Ingrese el nombre del estudiante a actualizar: ")
            calificacion = float(input(f"Ingrese la nueva calificación de '{estudiante}': "))
            print(actualizar_cal(estudiante, calificacion))

        elif accion == 3:
            estudiante = input("Ingrese el nombre del estudiante a eliminar: ")
            print(eliminar_estudiante(estudiante))

        elif accion == 4:
            listar_estudiantes()

        elif accion == 5:
            print("Saliendo del sistema...")
        else:
            print("Opción no válida.")

    except ValueError:
        print("Error: Ingrese un número válido.")
