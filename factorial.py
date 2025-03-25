# Recursividad

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)


# facrotial_5 = print(factorial(5))


# Fibonacci

# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)


# number = 33
# print(fibonacci(number))


# sumatoria de numeros naturales

def suma_naturales(n):

    if n == 0:
        return 0
    else:
        return n + suma_naturales(n-1)


suma = print(suma_naturales(8))
