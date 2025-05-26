class Perro:
    patas = 4

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def habla(self):
        print(f"Guau soy {self.nombre} tengo {self.edad} anios")


Perro.patas = 3
mi_perro = Perro("Copito", 15)
mi_perro2 = Perro("Milo", 1)
print(Perro.patas)
print(mi_perro2.patas)
