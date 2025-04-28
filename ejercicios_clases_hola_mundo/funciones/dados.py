import random


# def tirar_dados(veces):
#     cara_1 = 0
#     cara_2 = 0
#     cara_3 = 0
#     cara_4 = 0
#     cara_5 = 0
#     cara_6 = 0
#     if veces == 1:
#         resultado = random.randint(1, 6)
#         return print(f"Salió la cara: {resultado}")
#     if veces <= 0:
#         return print("Error: El número de lanzamientos debe ser mayor a 0.")
#     for _ in range(veces):
#         resultado = random.randint(1, 6)
#         if resultado == 1:
#             cara_1 += 1
#         elif resultado == 2:
#             cara_2 += 1
#         elif resultado == 3:
#             cara_3 += 1
#         elif resultado == 4:
#             cara_4 += 1
#         elif resultado == 5:
#             cara_5 += 1
#         elif resultado == 6:
#             cara_6 += 1
#     cara_1 = (cara_1 / veces) * 100
#     cara_2 = (cara_2 / veces) * 100
#     cara_3 = (cara_3 / veces) * 100
#     cara_4 = (cara_4 / veces) * 100
#     cara_5 = (cara_5 / veces) * 100
#     cara_6 = (cara_6 / veces) * 100
#     print(f"Porcentaje de veces que salió la cara 1: {cara_1:.2f}%")
#     print(f"Porcentaje de veces que salió la cara 2: {cara_2:.2f}%")
#     print(f"Porcentaje de veces que salió la cara 3: {cara_3:.2f}%")
#     print(f"Porcentaje de veces que salió la cara 4: {cara_4:.2f}%")
#     print(f"Porcentaje de veces que salió la cara 5: {cara_5:.2f}%")
#     print(f"Porcentaje de veces que salió la cara 6: {cara_6:.2f}%")
def tirar_dados(veces):
    frecuencias = {i: 0 for i in range(1, 7)}
    if veces <= 0:
        return "Error: El número de lanzamientos debe ser mayor a 0."
    for _ in range(veces):
        resultado = random.randint(1, 6)
        frecuencias[resultado] += 1
    for cara, frecuencia in frecuencias.items():
        porcentaje = (frecuencia / veces) * 100
        print(
            f"Porcentaje de veces que salió la cara {cara}: {porcentaje:.2f}%")


tirar_dados(10)
