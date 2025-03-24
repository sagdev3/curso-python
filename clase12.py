# numeros = [1, 2, 3, 4, 5, 6]

# for i in numeros:
#     print(i)

# for i in range(10):
#     print(i)

# for i in range(1, 100):
#     if i % 2 == 0:
#         print(i)
# frutas = ["Manzanas", "Pera", "Uva", "Naranja", "Tomate"]
# for fruta in frutas:
#     print(fruta)
#     if "Naranja" in fruta:
#         print(fruta, "encontrada")

x = 0
while x < 5:
    if x == 3:
        break
    print(x)
    x += 1

numeros = [1, 2, 3, 4, 5, 6]

for i in numeros:
    if i == 3:
        print('Aqui es igual a ', i)
        continue

    print(i)
