# text = "Hola mundo"

# iter_text = iter(text)

# for char in iter_text:
#     print(char)

# Iterador para impares
# limite = 10
# odd_itter = iter(range(1, limite+1, 2))
# for numero_impar in odd_itter:
#     print(numero_impar)


# def my_generador():
#     yield 1
#     yield 2
#     yield 3


# for value in my_generador():
#     print(value)

# # Fibonacci


# def fibonacci(limite):
#     a, b = 0, 1
#     while a < limite:
#         yield a
#         a, b = b, a+b


# for num in fibonacci(100):
#     print(num)

# Numero pares e impares

def pares(limite):
    a = 2
    while a < limite:
        yield a
        a += 2


for num in pares(100):
    print(num)


def impares(limite):
    a = 1
    while a < limite:
        yield a
        a += 2


for num in impares(100):
    print(num)
