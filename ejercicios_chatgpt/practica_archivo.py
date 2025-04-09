with open('nombres.txt', 'w') as file:
    file.write('Santiago\n')
    file.write('Dayana\n')
    file.write('Dalia\n')

with open('nombres.txt', 'a') as file:
    file.write('Dani\n')
    file.write('Dome')

with open('nombres.txt', 'r') as file:
    contenido = file.read()
    print(contenido)

with open('nombres.txt', 'r') as file:
    for i, linea in enumerate(file, 1):
        print(f'{i}. {linea.strip()}')

with open('nombres.txt', 'r') as file:
    primera_linea = file.readline()
    segunda_linea = file.readline()

    print(primera_linea.strip())
    print(segunda_linea.strip())

with open('nombres.txt', 'r') as file:
    lineas = file.readlines()

    print(lineas)

    for linea in lineas:
        print(linea)


# Reto 2
# 1. Usa readlines() para guardar todas las líneas en una lista.
with open('nombres.txt', 'r') as file:

    nombres = file.readlines()
    nombres_limpios = [nombre.strip() for nombre in nombres]
    print(nombres)
    print(nombres_limpios)

# 2. Cuenta cuántos nombres hay en total.
with open('nombres.txt', 'r') as file:

    for i, nombre in enumerate(file, 1):
        print(f'{nombre.strip()}. {i}')

with open('nombres.txt', 'r') as file:
    nombre = file.readlines()

    print(f'Hay {len(nombre)} nombres')

with open('nombres.txt', 'r') as file:

    nombres = file.readlines()
    nombres_limpios = [nombre.strip() for nombre in nombres]

    nombres_d = [nombre.upper()
                 for nombre in nombres_limpios if nombre[0] == 'D']
    print(nombres_d)

with open('nombres.txt', 'r') as file:
    nombres = [nombre.strip() for nombre in file.readline()]

    nombres_d = [nombre.upper() for nombre in nombres_d if nombre[0] == 'D']
    print(nombres_d)
