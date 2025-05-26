class Caminador:
    def caminar(self):
        print("caminando")


class Volador:
    def volar(self):
        print("volando")


class Nadador:
    def nadador(self):
        print("nadando")


class Chanchito(Caminador, Nadador):
    def programar(self):
        print("Programando")


chanchito = Chanchito()
