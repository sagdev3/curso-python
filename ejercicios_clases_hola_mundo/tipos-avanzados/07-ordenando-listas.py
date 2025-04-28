# numeros = [2, 75, 1, 45, 22]


# numeros.sort()
# print(numeros)

# numeros.sort(reverse=True)
# print(numeros)

# numeros2 = sorted(numeros)
# print(numeros2)

# numeros2 = sorted(numeros, reverse=True)
# print(numeros2)

usuarios = [["Santiago", 4], ["Dayana", 1], ["Dani", 5]]


def ordena(elemento):
    return elemento[1]


usuarios.sort(key=ordena, reverse=True)
print(usuarios)
