class CuentaDeBanco:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True

    def deposito(self, amount):
        if self.is_active:
            self.balance += amount
            print(
                f'Se han depositado ${amount}\n Saldo Actual ${self.balance}')
        else:
            print('No se puede depositar, Cuenta inactiva')

    def retirar(self, amount):
        if self.is_active:
            if self.balance >= amount:
                self.balance -= amount
                print(
                    f'Se ha retirado el monto de ${amount}\n Saldo actual ${self.balance}')
            else:
                print(
                    f'Su saldo es insuficiente\n Actualmente tiene un monto de ${self.balance}')
        else:
            print('Esta cuenta no esta activa')

    def desactivar_cuenta(self):
        self.is_active = False
        print(f'La cuenta ha sido desactivada')

    def activar_cuenta(self):
        self.is_active = True
        print(f'La cuenta ha sido activada')


cuenta1 = CuentaDeBanco("Santiago", 500)

cuenta1.deposito(200)

cuenta1.retirar(500)

cuenta1.desactivar_cuenta()

cuenta1.activar_cuenta()
cuenta1.deposito(200)
