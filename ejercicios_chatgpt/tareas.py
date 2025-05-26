from abc import ABC, abstractmethod


class Tarea(ABC):
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.completada = False

    @abstractmethod
    def completar(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class TareaSimple(Tarea):
    def completar(self):
        self.completada = True

    def __str__(self):
        estado = '✔️' if self.completada == True else "✖️"
        return f"Tarea simpl: {self.descripcion} [{estado} ]"


class TareaPrioritaria(Tarea):

    def __init__(self, descripcion, prioridad):
        super().__init__(descripcion)
        self.prioridad = prioridad

    def completar(self):
        self.completada = True

    def __str__(self):
        estado = "✔️" if self.completada else "❌"
        return f"Tarea prioritaria ({self.prioridad}): {self.descripcion} [{estado} ]"


class GestorTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea: Tarea):
        self.tareas.append(tarea)
        print("✅ Tarea agregada.")

    def listar_tareas(self):
        if not self.tareas:
            print("No hay tareas.")
            return
        for idx, tarea in enumerate(self.tareas, 1):
            print(f"{idx}. {tarea}")

    def completar_tarea(self, indice):
        if 0 < indice <= len(self.tareas):
            self.tareas[indice - 1].completar()
            print("✅ Tarea marcada como completada.")
        else:
            print("❌ Índice inválido.")

# Menú para probar


def menu():
    gestor = GestorTareas()

    while True:
        print("\n--- Gestor de Tareas ---")
        print("1. Agregar tarea simple")
        print("2. Agregar tarea prioritaria")
        print("3. Listar tareas")
        print("4. Completar tarea")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == '1':
            desc = input("Descripción de la tarea: ")
            tarea = TareaSimple(desc)
            gestor.agregar_tarea(tarea)

        elif opcion == '2':
            desc = input("Descripción de la tarea: ")
            prioridad = input("Prioridad (Alta/Media/Baja): ")
            tarea = TareaPrioritaria(desc, prioridad)
            gestor.agregar_tarea(tarea)

        elif opcion == '3':
            gestor.listar_tareas()

        elif opcion == '4':
            gestor.listar_tareas()
            try:
                idx = int(input("Número de tarea a completar: "))
                gestor.completar_tarea(idx)
            except ValueError:
                print("❌ Por favor ingresa un número válido.")

        elif opcion == '5':
            print("¡Hasta luego!")
            break

        else:
            print("❌ Opción inválida. Intenta de nuevo.")


if __name__ == '__main__':
    menu()
