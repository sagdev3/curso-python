inventario = {}


def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad: "))
    if nombre in inventario:
        inventario[nombre] += cantidad
    else:
        inventario[nombre] = cantidad
    print(f"Producto {nombre} agregado/actualizado.")


def buscar_producto():
    nombre = input("Ingrese el nombre del producto a buscar: ")
    if nombre in inventario:
        print(f"{nombre}: {inventario[nombre]} unidades")
    else:
        print("Producto no encontrado.")


def mostrar_inventario():
    for producto, cantidad in inventario.items():
        print(f"{producto}: {cantidad} unidades")


while True:
    print("\n1. Agregar producto")
    print("2. Buscar producto")
    print("3. Mostrar inventario")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        buscar_producto()
    elif opcion == "3":
        mostrar_inventario()
    elif opcion == "4":
        break
    else:
        print("Opción no válida. Intente de nuevo.")
