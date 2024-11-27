def gestionar_calificaciones():
    calificaciones = {} 

    while True:
        accion = input("¿Qué deseas hacer? (agregar/buscar/salir): ").lower()

        if accion == "agregar":
            nombre = input("Nombre del estudiante: ").strip()
            calificacion = int(input(f"Calificación de {nombre}: "))
            calificaciones[nombre] = calificacion
            print(f"Calificación de {nombre} guardada.")

        elif accion == "buscar":
            nombre = input("Nombre del estudiante a buscar: ").strip()
            if nombre in calificaciones:
                print(f"{nombre} tiene una calificación de {calificaciones[nombre]}.")
            else:
                print(f"No se encontró la calificación de {nombre}.")

        elif accion == "salir":
            print("Saliendo del programa.")
            break
        else:
            print("Acción no válida. Intenta de nuevo.")
gestionar_calificaciones()
