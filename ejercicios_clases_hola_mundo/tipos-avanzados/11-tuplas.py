numeros = (1, 2, 3) + (4, 5, 6)

print(numeros)

punto = [1, 2]

punto = tuple(punto)
print(punto)

menosNumeros = numeros[:2]

print(menosNumeros)

primero, segundo, *otro = numeros

print(primero, segundo, otro)

for n in numeros:
    print(n)

listaNumeros = list(numeros)

listaNumeros[0] = 'Chanchito Feliz'

print(listaNumeros)
