class OverheatingError(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje


def check_cpu_temperature(temp):
    if temp >= 100:
        raise OverheatingError(
            'La temperatura de tu PC ha alcanzado el limite critico de 100 grados centigrados')
    elif temp >= 90:
        print("Advertencia: la temperatura de tu PC es muy alta")
    elif temp >= 75:
        print("Advertencia: La temperatura de tu PC esta elevada")
    else:
        print('La temperatura de tu PC es normal')


try:
    temperatura_actual = 101
    check_cpu_temperature(temperatura_actual)
except OverheatingError as e:
    print(e)
