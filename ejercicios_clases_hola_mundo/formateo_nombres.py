nombre = input("Cual es tu primer nombre?: ").strip().capitalize()

while not nombre or nombre.lower() == 'exit':
    print('No ingresaste nada')
    nombre = input("Cual es tu primer nombre?: ").strip().capitalize()

segundo_nombre = input(
    "Cual es tu segundo nombre? (Opcional): ").strip().capitalize()
apellido = input("Cual es tu primer apellido?: ").strip().capitalize()

while not apellido or apellido.lower() == 'exit':
    print('No ingresaste nada')
    apellido = input("Cual es tu primer apellido?: ").strip().capitalize()

segundo_apellido = input(
    "Cual es tu segundo apellido? (Opcional):  ").strip().capitalize()

nombre_completo = f'{nombre} {segundo_nombre if segundo_nombre else ''.strip()} {apellido} {segundo_apellido if segundo_apellido else ''.strip()}'
print(nombre_completo)
