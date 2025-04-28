def a_segundos(cantidad, unidad):
    if unidad == "segundo":
        return cantidad
    elif unidad == 'minuto':
        return cantidad * 60
    elif unidad == 'hora':
        return cantidad * 3600
    elif unidad == 'dia':
        return (cantidad*3600) * 24
    elif unidad == 'semana':
        return ((cantidad * 3600)*24)*7
    elif unidad == 'mes':
        return ((cantidad * 3600)*24)*30
    elif unidad == 'año':
        return ((cantidad * 3600)*24)*366
    else:
        return 'Error'


def de_segundo(cantidad, unidad):
    if unidad == 'segundo':
        return cantidad
    elif unidad == 'minuto':
        return cantidad / 60
    elif unidad == 'hora':
        return cantidad / 3600
    elif unidad == 'dia':
        return (cantidad/3600) / 24
    elif unidad == 'semana':
        return ((cantidad / 3600)/24)/7
    elif unidad == 'mes':
        return ((cantidad / 3600)/24)/30
    elif unidad == 'año':
        return ((cantidad / 3600)/24)/366
    else:
        return 'Error'


def convertir(cantidad, unidad_origen, unidad_destino):

    cantidad_en_segundos = a_segundos(cantidad, unidad_origen)
    if cantidad_en_segundos == 'Error':
        return 'Unidad de tiempo invalida'

    cantidad_convertida = de_segundo(cantidad_en_segundos, unidad_destino)
    return f'{cantidad} {unidad_origen}(s) son {cantidad_convertida} {unidad_destino}(s)'


while True:
    unidad_de_origen = input("Ingrese la unidad que desea convertir: ")
    if unidad_de_origen.lower() == 'salir':
        break
    unidad_de_destino = input(
        f'A que unidad desea convertir {unidad_de_origen}: ')
    if unidad_de_destino.lower() == 'salir':
        break
    cantidad = float(input(
        f'Ingrese la cantidad  de {unidad_de_origen}(s) que desea convertir a {unidad_de_destino}(s): '))

    print(convertir(cantidad, unidad_de_origen, unidad_de_destino))
