# lista_de_compras = ['manzanas', 'pan', 'leche', 'huevos']

# print("Lista inicial:", lista_de_compras)

# # Añadir un producto
# nuevo_producto = input('Ingrese un nuevo producto a la lista: ')
# lista_de_compras.append(nuevo_producto)
# print("Lista actualizada:", lista_de_compras)

# # Eliminar un producto
# eliminar_producto = input('¿Qué producto deseas eliminar de la lista? ')

# if eliminar_producto in lista_de_compras:
#     lista_de_compras.remove(eliminar_producto)
#     print(f"'{eliminar_producto}' fue eliminado.")
# else:
#     print(f"Error: '{eliminar_producto}' no está en la lista.")

# # Ordenar la lista (in-place)
# lista_de_compras.sort()
# print("Lista ordenada:", lista_de_compras)

# frutas = ('guineo', 'manzana', 'uva', 'pera', 'fresa')

# print(frutas[0])
# print(frutas[-2], frutas[-1])
# print('Hay un total de', len(frutas), 'frutas')

# notas = [
#     [8.5, 9.0, 7.5],  # Estudiante 1
#     [6.0, 7.0, 8.0],  # Estudiante 2
#     [9.0, 8.5, 9.5]   # Estudiante 3
# ]


# for i, fila in enumerate(notas):
#     promedio = sum(fila)/len(fila)
#     print(f'Estidiante {i+1} - Promedio: {promedio:.2f}')\


# promedios = [sum(fila)/len(fila) for fila in notas]

# print(promedios)
datos = {
    "nombre": "Juan",
    "edad": 30,
    "correo": "juan@mail.com"
}
print(datos)

edad_nueva = int(input("Ingresa la nueva edad "))

nuevos_datos = {**datos, "edad": edad_nueva}
print(nuevos_datos)
