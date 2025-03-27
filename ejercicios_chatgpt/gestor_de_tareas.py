
tareas = []


def total_tareas():
    while True:
        print("Seleccione una Opcion: ")
        print("1 Agregar tarea")
        print("2 Ver tareas")
        print("3 Marcar como completada")
        print("4 Eliminar tarea")
        print("5 Salir")

        opcion = input('Escoja una opcion: ')

        if opcion == '5':
            print("Muchas gracias...")
            break
        elif opcion == '1':
            agregar_tarea(tareas)
        elif opcion == '2':
            ver_tareas(tareas)


def agregar_tarea(lista):
    tarea = input("Esscribe una nueva tarea: ")
    lista.append({"tarea": tarea, "completada": False})
    print("✅ Tarea agregada")


def ver_tareas(lista):
    if not lista:
        print("📭 No hay tareas registradas.")
    else:
        print("\n📋 Lista de tareas:")
        for i, t in enumerate(lista, start=1):
            estado = "✔️" if t["completada"] else "❌"
            print(f"{i}. {t['tarea']} [{estado}]")


total_tareas()
