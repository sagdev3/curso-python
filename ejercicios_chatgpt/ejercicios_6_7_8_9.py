lista_de_compras = ['manzanas', 'pan', 'leche', 'huevos']

print("Lista inicial:", lista_de_compras)

# Añadir un producto
nuevo_producto = input('Ingrese un nuevo producto a la lista: ')
lista_de_compras.append(nuevo_producto)
print("Lista actualizada:", lista_de_compras)

# Eliminar un producto
eliminar_producto = input('¿Qué producto deseas eliminar de la lista? ')

if eliminar_producto in lista_de_compras:
    lista_de_compras.remove(eliminar_producto)
    print(f"'{eliminar_producto}' fue eliminado.")
else:
    print(f"Error: '{eliminar_producto}' no está en la lista.")

# Ordenar la lista (in-place)
lista_de_compras.sort()
print("Lista ordenada:", lista_de_compras)
