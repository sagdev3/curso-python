mascotas = ["Cheldon", "Simba", "Cielo",
            "Cheldon", "Milo", "Ardillita", "Oreo"]

print(mascotas.count('Cheldon'))

if "Cheldon" in mascotas:
    print(mascotas.index("Cheldon"))
else:
    print('"Error!!!", No existe')
