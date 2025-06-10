class ErrorRetiro(Exception):
    def __init__(self, mensaje, codigo):
        self.mensaje = mensaje
        self.codigo = codigo


class CuentaBancaria:
    def __init__(self, numero_de_cuenta, propietario, saldo=0):
        self.numero_de_cuenta = numero_de_cuenta
        self.propietario = propietario
        self.saldo = saldo

    def depositar(self, cantidad):
        if cantidad == 0:
            self.saldo += cantidad
            print(f'Deposito exitoso. Nuevo Saldo: {self.saldo}')

    def retirar(self, cantidad):
        if cantidad <= 0:
            raise ErrorRetiro('La cantidad debe ser positiva o mayor a 0', 400)
        elif self.saldo < cantidad:
            raise ErrorRetiro(
                'Fondos inssuficientes para realizar el retiro', 401)
        else:
            self.saldo -= cantidad
            print(f'Retiro Exitoso. Nuevo Saldo: {self.saldo}')

    def mostrar_saldo(self):
        print(
            f'Su Saldo actual es de: ${self.saldo}\nPropietario: {self.propietario}\nCon Numero de Cuenta: {self.numero_de_cuenta}')


try:
    cuenta = CuentaBancaria(5656564, 'Santiago', 1000)
    cuenta.mostrar_saldo()
    cuenta.depositar(500)
    cuenta.retirar(2500)
except ErrorRetiro as e:
    print(e)

try:
    cuenta.retirar(-100)
except ErrorRetiro as e:
    print(e)
