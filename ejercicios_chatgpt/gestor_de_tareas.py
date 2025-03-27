
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
        elif opcion == '3':
            marcar_completada(tareas)
        elif opcion == '4':
            eliminar_tarea(tareas)
        else:
            print("Debe escoger una opcion valida ❌")


def agregar_tarea(lista):
    tarea = input("Esscribe una nueva tarea: ")
    fecha = input("Escribe la fecha límite (YYYY-MM-DD): ")
    lista.append({"tarea": tarea, "completada": False, "fecha": fecha})

    print("✅ Tarea agregada")


def ver_tareas(lista):
    if not lista:
        print("📭 No hay tareas registradas.")
    else:
        print("\n📋 Lista de tareas:")
        for i, t in enumerate(lista, start=1):
            estado = "✔️" if t["completada"] else "❌"
            print(f"{i}. {t['tarea']} [{estado} ] - Fecha: {t['fecha']}")


def marcar_completada(lista):
    ver_tareas(lista)
    try:
        num = int(input("Marque el numero de la tarea completada: "))
        lista[num - 1]["completada"] = True
        print("✔️ Tarea completada...")
    except (ValueError, IndexError):
        print('⚠️ numero incorrecto')


def eliminar_tarea(lista):
    ver_tareas(lista)
    try:
        num = int(input("Marque el numero de la tarea a eliminar: "))
        tarea_eliminada = lista.pop(num-1)
        print(f'🚮 Tarea "{tarea_eliminada["tarea"]}" Eliminada')
    except (ValueError, IndexError):
        print('⚠️ numero incorrecto')


total_tareas()
