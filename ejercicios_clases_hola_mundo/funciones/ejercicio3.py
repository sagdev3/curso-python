def promedio(*numeros):
    if not numeros:
        return 0
    return sum(numeros) / len(numeros)


print(promedio(10, 5))
