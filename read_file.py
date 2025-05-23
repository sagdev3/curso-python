# Leer un archivo linea por linea
# with open('caperucita.txt', 'r') as file:
#     for lineas in file:
#         print(lineas.strip())

# leer todas las lineas en una lista
# with open('caperucita.txt', 'r') as file:
#     lineas = file.readlines()
#     print(lineas)

# Agregar texto
"""with open("caperucita.txt", 'a') as file:
    file.write("\n\nBy:Santiago Giler")"""

# Sobre escribir el texto

# with open("caperucita.txt", 'w') as file:
#     file.write("\n\nBy:Santiago Giler")


with open('caperucita.txt', 'r') as file:

    for i, linea in enumerate(file, 1):
        print(f'{i}. {linea.strip()}')

with open('caperucita.txt', 'r') as file:
    lineas = file.readlines()
    print('Numero de lineas', len(lineas))
