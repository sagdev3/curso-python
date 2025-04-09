with open('archivo.txt', 'w') as archivo:
    archivo.write('Escribiendo mi primer registro')

with open('archivo.txt', 'a') as archivo:
    archivo.write('\nEscribiendo otra linea de prueba')


with open('archivo.txt', 'r') as archivo:
    contenido = archivo.read()
    print(contenido)
