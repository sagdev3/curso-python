# and, or, not

gas = True
encendido = True
edad = 18

if gas and (encendido or edad >= 18):
    print('Puede avanzar')
else:
    print('No arrancas')

if gas or encendido:
    print('Puede avanzar')
else:
    print('No arrancas')

if not gas and not encendido:
    print('Puede avanzar')
else:
    print('No arrancas')
