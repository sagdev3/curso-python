def suma(a, b, c):
    print(a+b+c)


suma(4, 6, 54)


def suma2(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)


suma2(566, 898, 565, 98, 54, 48, 84, 515, 54, 645)
