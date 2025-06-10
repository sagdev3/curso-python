try:
    n1 = int(input('Ingresa primer numero: '))
except Exception as e:
    print('Ingrese un valor que corresponda')
else:
    print("No ocurrio ni un error")
finally:
    print("Se ejecuta siempre")
