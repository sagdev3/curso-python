def add(a, b): return a+b


print(add(10, 4))


def multiply(a, b): return a*b


print(multiply(10, 4))


# El cuadrado de cada numero
numbers = range(11)
squared_numbers = list(map(lambda x: x**2, numbers))

print(squared_numbers)


# Numeros pares

even_number = list(filter(lambda x: x % 2 == 0, numbers))
print(even_number)
