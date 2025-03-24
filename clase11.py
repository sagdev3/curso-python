numeros = {1: 'uno', 2: 'dos', 3: 'tres', 4: 'cuatro', 5: 'cinco'}
print(numeros)

print(numeros[2])

informacion = {'nombre': 'Santiago', 'edad': 30, 'ciudad': 'Quito'}
print(informacion)
print(informacion['nombre'])
del informacion['edad']
print(informacion)

clave = informacion.keys()
print(clave)
print(type(clave))

values = informacion.values()
print(values)
print(type(values))

pairs = informacion.items()
print(pairs)
print(type(pairs))

contacto = {"Santiago": {'nombre': 'Santiago', 'numero': 1234567890},
            "Juan": {'nombre': 'Juan', 'numero': 1546546546},
            "Maria": {'nombre': 'Maria', 'numero': 6789054321}}
print(contacto)
print(contacto['Santiago'])
