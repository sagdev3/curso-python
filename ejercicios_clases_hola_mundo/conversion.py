print('BIENVENIDO A TU PROGRAMA DE CONVERSION DE DIVISAS')


def conver_usd_mxn(moneda):
    cambio = moneda * 20.28
    print(f'{moneda} USD = {cambio:.2f} MXN\n')


def conver_mxn_usd(moneda):
    cambio = moneda / 20.28
    print(f'{moneda} MXN = {cambio:.2f} USD\n')


def conver_usd_eur(moneda):
    cambio = moneda * 0.95
    print(f'{moneda} USD = {cambio:.2f} EUR\n')


def conver_eur_usd(moneda):
    cambio = moneda / 0.95
    print(f'{moneda} EUR = {cambio:.2f} USD\n')


def conver_eur_mxn(moneda):
    cambio = moneda * 21.36
    print(f'{moneda} EUR = {cambio:.2f} MXN\n')


def conver_mxn_eur(moneda):
    cambio = moneda / 21.36
    print(f'{moneda} MXN = {cambio:.2f} EUR\n')


print("Escoje que cambios necesitas Realizar")

print("""1. USD -- MXN\n2. MXN -- USD\n3. USD  -- EUR\n4. EUR -- USD\n5. EUR -- MXN\n6. MXN -- EUR\n""")
print("Para salir presiona la letra X\n")


monto = 0
while True:
    op = ''

    op = input("Escoje una opcion de acuerdo al cambio que quieras realizar: ")

    if op.upper() == 'X':
        print("Saliendo del conversor de monedas...")
        break
    if op == '1':
        monto = float(input("\nIngresa el monto a calcular: "))
        conver_usd_mxn(monto)
    elif op == '2':
        monto = float(input("\nIngresa el monto a calcular: "))
        conver_mxn_usd(monto)
    elif op == '3':
        monto = float(input("\nIngresa el monto a calcular: "))
        conver_usd_eur(monto)
    elif op == '4':
        monto = float(input("\nIngresa el monto a calcular: "))
        conver_eur_usd(monto)
    elif op == '5':
        monto = float(input("\nIngresa el monto a calcular: "))
        conver_eur_mxn(monto)
    elif op == '6':
        monto = float(input("\nIngresa el monto a calcular: "))
        conver_mxn_eur(monto)
    else:
        print("\nEscoja una opcion correcta...\n")
