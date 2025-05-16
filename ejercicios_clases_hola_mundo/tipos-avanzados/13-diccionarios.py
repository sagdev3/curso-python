punto = {"x": 25, "y": 50}
print(punto)

print(punto["x"])
print(punto["y"])

punto["z"] = 45

print(punto)

if "a" in punto:
    print(f'Encontre a, {punto["a"]}')
else:
    print('No existe "a"')


print(punto.get("x"))
print(punto.get("a", 97))


del punto["x"]
del (punto["y"])

print(punto)

punto["x"] = 25

for valor in punto:
    print(valor, punto[valor])

for valor in punto.items():
    print(valor)

for llave, valor in punto.items():
    print(llave, valor)

usuarios = [
    {"id": 5, "nombre": "Santiago"},
    {"id": 2, "nombre": "Javier"},
    {"id": 1, "nombre": "Dayana"},
    {"id": 3, "nombre": "Dani"},
    {"id": 4, "nombre": "Dome"},
]

for usuario in usuarios:
    print(usuario["nombre"])
