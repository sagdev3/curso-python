class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def habla(self):
        print(f"Guau soy {self.nombre} tengo {self.edad} anios")


mi_perro = Perro("Copito", 15)
mi_perro.habla()
