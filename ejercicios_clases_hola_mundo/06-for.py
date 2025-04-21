# for numero in range(0, 5):
#     print(numero+1, (numero + 1) * 'Hola Mundo')


buscar = 10
for numero in range(5):
    print(numero)
    if numero == buscar:
        print(f'Encontrado {numero} es igual a {buscar}')
        break
else:
    print('No se encontro el numero')

for char in "Ultimate Python":
    print(char)
