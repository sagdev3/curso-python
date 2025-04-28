usuarios = [["Santiago", 4], ["Dayana", 1], ["Dani", 5]]


nombres = list(map(lambda usuario: usuario[0], usuarios))
print(nombres)


nombres2 = list(filter(lambda usuario: usuario[1] > 2, usuarios))

print(nombres2)
