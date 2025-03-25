try:
    divisor = int(input("Ingrese un numero: "))
    resul = 100/divisor
    print(resul)
except ZeroDivisionError as e:
    print("No se puede dividir para 0")
    print("El error es > ", e)
except ValueError as e:
    print("Debes de ingresar un numero")
    print("El error es > ", e)
