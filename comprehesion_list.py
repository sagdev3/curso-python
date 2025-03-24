# squares = [x**2 for x in range(1, 11)]
# print(squares)


# celcius = [x*10 for x in range(0, 5)]
# print(celcius)
# farenheit = [(temp * 9/5)+32 for temp in celcius]
# print(farenheit)


# numeros = [0+x for x in range(1, 100)]

# numeros_pares = [x for x in numeros if x % 2 == 0]
# print(numeros_pares)

# numeros_impares = [i for i in numeros if i % 2 != 0]
# print(numeros_impares)

matrix = [[1+x+3 * i for x in range(3)] for i in range(3)]
print(matrix)

transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transposed)

transposed2 = [list(row) for row in zip(*matrix)]
print(transposed2)
