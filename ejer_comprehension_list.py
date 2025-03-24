# palabras = ["sol", "mar", "montaña", "rio", "estrella"]

# palabras_largas = [palabra.upper() for palabra in palabras if len(palabra) > 3]
# print(palabras_largas)

# Numeros pares multiplicados por 2

# list_num = [10, 23, 5, 45, 8, 12, 7]

# pares_mul2 = [x*2 for x in list_num if x % 2 == 0]
# print(pares_mul2)

# frutas = ["manzana", "banana", "pera", "uva", "mango"]

# frutas_con_m = [fruta.upper() for fruta in frutas if fruta[0] == 'm']
# print(frutas_con_m)

# lenguajes = ["python", "java", "c++", "javascript", "go"]
# lenguajes_largos = [lenguaje.upper()
#                     for lenguaje in lenguajes if len(lenguaje) > 4]
# print(lenguajes_largos)

# numeros = [15, 30, 10, 25, 5, 40]
# numeros_divididos = [num/5 for num in numeros if num > 20]
# print(numeros_divididos)

# palabras = ["hola", "adiós", "bien", "mal", "excelente"]

# palabras_cuatro_letras = [palabra.upper()
#                           for palabra in palabras if len(palabra) == 4]
# print(palabras_cuatro_letras)

# personas = [
#     {"nombre": "Ana", "edad": 25},
#     {"nombre": "Luis", "edad": 17},
#     {"nombre": "Carlos", "edad": 30},
#     {"nombre": "Marta", "edad": 16}
# ]

# personas_mayores = [
#     persona["nombre"] for persona in personas if persona["edad"] > 18]
# print(personas_mayores)

# numeros = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# numeros_pares = [
#     num for sublista in numeros for num in sublista if num % 2 == 0]
# print(numeros_pares)

# palabras = ["sol", "luna", "cielo", "nube", "estrella"]
# palabras_largas = [palabra.upper() for palabra in palabras if len(
#     palabra) > 3 and palabra.count('e') > 0]
# print(palabras_largas)

# numeros = [5, -3, 10, -7, 2, -1]
# numeros_negativos = [num * (-1) for num in numeros if num < 0]
# print(numeros_negativos)

# palabras = ["casa", "perro", "gato", "elefante", "oso"]
# palabras_sin_e = [palabra.upper() for palabra in palabras if palabra[0] != 'e']
# print(palabras_sin_e)

# claves = ["nombre", "edad", "ocupación"]
# valores = ["Juan", 30, "Ingeniero"]

# diccionario = {clave: valor for clave, valor in zip(claves, valores)}
# print(diccionario)

# claves = ["nombre", "edad", "ciudad"]
# valores = ["Ana", 25, "Madrid"]

# diccionario = {clave: valor for clave, valor in zip(claves, valores)}
# print(diccionario)

# diccionario = {"nombre": "Juan", "edad": 30}

# diccionario["edad"] = 35
# diccionario["ciudad"] = "Quito"
# print(diccionario)

# diccionario = {"a": 10, "b": 25, "c": 30, "d": 15}

# mayores = {clave: valor for clave, valor in diccionario.items() if valor > 18}
# print(mayores)

# personas = [
#     {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"},
#     {"nombre": "Ana", "edad": 32, "ciudad": "Madrid"},
#     {"nombre": "Pedro", "edad": 35, "ciudad": "Barcelona"},
#     {"nombre": "Laura", "edad": 40, "ciudad": "Madrid"}
# ]

# personas_en_madrid = {persona["nombre"]
#                       for persona in personas if persona["ciudad"] == "Madrid" and persona["edad"] > 30}
# print(personas_en_madrid)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

multiplicados = [x*2 if x % 2 == 0 else x for x in numeros]
print(multiplicados)
