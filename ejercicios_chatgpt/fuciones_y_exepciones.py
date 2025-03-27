# def dividir(a, b):
#     try:
#         print(a/b)
#     except ZeroDivisionError:
#         print("No se puede dividir para 0")
#     except ValueError:
#         print('Solo se pueden ingresar numeros')


# try:
#     a = float(input('Ingrese un numero '))
#     b = float(input('Ingrese un numero '))
#     dividir(a, b)
# except ValueError:
#     print('solo ingrese numeros')

print("INGRESA UN RANGO DE NUMEROS")

try:
    inicio = int(input("Ingresa el inicio del rango: "))
    fin = int(input("Ingresa hasta donde llega el rango: "))
    if fin < inicio:
        print("El valor del inicio debe ser menor que el del final")
    else:
        rango = range(inicio, fin+1)
        # squared = list(map(lambda x: x**2, rango))
        for x in rango:
            print(f"{x}² = {x**2}")
        # print(squared)
except ValueError:
    print("Ingresa numeros no caracteres ni letras")
