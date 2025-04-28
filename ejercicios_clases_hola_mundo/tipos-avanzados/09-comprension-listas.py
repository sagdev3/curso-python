usuarios = [["Santiago", 4], ["Dayana", 1], ["Dani", 5]]

nombres = [nombre[0] for nombre in usuarios]
print(nombres)

nombres2 = [usuario for usuario in usuarios if usuario[1] > 2]
print(nombres2)

nombres3 = [usuario[0] for usuario in usuarios if usuario[1] > 2]
print(nombres3)
