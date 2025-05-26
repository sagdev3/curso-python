class Ave:
    def __init__(self):
        self.volador = True

    def vuela(self):
        print('Vuela ave')


class Pato(Ave):
    def __init__(self):
        super().__init__()
        self.nada = True

    def vuela(self):
        super().vuela()
        print('Vuela Pato')


pato = Pato()
pato.vuela()
print(pato.volador, pato.nada)
