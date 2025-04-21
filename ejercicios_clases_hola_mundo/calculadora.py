while True:
    print('Para salir escribe X')
    print("""Las operaciones son Suma(+), Resta(-),
    Multiplicacion(*) y Division(/)""")
    num = input('Ingrese Un numero: ')
    if num.lower() == 'salir':
        print('Hasta luego')
        break
    if num == '':
        print("\nDebe de ingresar un numero\n")
    else:
        op = input("Ingresa una operacion valida: ")
        if op == '+':
            num2 = input('Ingresa el siguiente numero: ')
            if num2.lower() == 'salir':
                print('Hasta luego')
                break
            elif num2 == '':
                print("\nDebe de ingresar un numero\n")
            else:
                print(float(num) + float(num2))
        elif op == '-':
            num2 = input('Ingresa el siguiente numero: ')

            if num2.lower() == 'salir':
                print('Hasta luego')
                break
            elif num2 == '':
                print("\nDebe de ingresar un numero\n")
            else:
                print(float(num) - float(num2))
        elif op == '*':
            num2 = input('Ingresa el siguiente numero: ')
            if num2.lower() == 'salir':
                print('Hasta luego')
                break
            elif num2 == '':
                print("\nDebe de ingresar un numero\n")
            else:
                print(float(num) * float(num2))
        elif op == '/':
            num2 = input('Ingresa el siguiente numero: ')

            if num2.lower() == 'salir':
                print('Hasta luego')
                break
            elif num2 == '':
                print("\nDebe de ingresar un numero\n")
            else:
                print(float(num) / float(num2))
        elif op.lower() == 'salir':
            print('Hasta luego')
            break
        else:
            print('Ingrese una operacion valida')
