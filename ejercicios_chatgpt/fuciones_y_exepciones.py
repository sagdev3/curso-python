def dividir(a, b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print("No se puede dividir para 0")
    except ValueError:
        print('Solo se pueden ingresar numeros')


try:
    a = float(input('Ingrese un numero '))
    b = float(input('Ingrese un numero '))
    dividir(a, b)
except ValueError:
    print('solo ingrese numeros')
