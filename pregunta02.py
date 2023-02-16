#2. Crea un programa en Python que mantenga un historial de tareas pendientes. 
#El programa debe permitir al usuario agregar una tarea al inicio de la lista, 
#eliminar una tarea del final de la lista y mostrar todas las tareas en la lista 
#en orden inverso al que se agregaron. Además, el programa debe contar la 
#cantidad total de tareas en la lista y mostrar ese número al usuario.

tareas_pendientes = []  # Creamos una lista vacía para almacenar las tareas pendientes

while True:
    # Mostramos al usuario las opciones que tiene disponibles
    print("Opciones:")
    print("1. Agregar una tarea al inicio de la lista")
    print("2. Eliminar la última tarea de la lista")
    print("3. Mostrar todas las tareas en la lista en orden inverso al que se agregaron")
    print("4. Mostrar la cantidad total de tareas en la lista")
    print("5. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        # Pedimos al usuario que introduzca la tarea a agregar y la agregamos al inicio de la lista
        tarea = input("Introduce el nombre de la tarea: ")
        tareas_pendientes.insert(0, tarea)
        print(f"Tarea {tarea} agregada al inicio de la lista de tareas pendientes.")

    elif opcion == "2":
        if len(tareas_pendientes) == 0:
            print("La lista de tareas pendientes está vacía.")
        else:
            # Eliminamos la última tarea de la lista
            ultima_tarea = tareas_pendientes.pop()
            print(f"Tarea {ultima_tarea} eliminada de la lista de tareas pendientes.")

    elif opcion == "3":
        if len(tareas_pendientes) == 0:
            print("La lista de tareas pendientes está vacía.")
        else:
            # Mostramos la lista de tareas pendientes en orden inverso al que se agregaron
            print("Lista de tareas pendientes en orden inverso:")
            for i, tarea in enumerate(reversed(tareas_pendientes), start=1):
                print(f"{i}. {tarea}")

    elif opcion == "4":
        # Mostramos la cantidad total de tareas en la lista
        print(f"Hay {len(tareas_pendientes)} tareas pendientes en la lista.")

    elif opcion == "5":
        # Salimos del programa
        print("¡FIN!")
        break

    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")