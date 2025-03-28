class Libro():
    def __init__(self, titulo, autor, fecha_libro, ingreso_del_libro, cantidad=0, ):
        self.titulo = titulo
        self.autor = autor
        self.fecha_libro = fecha_libro
        self.ingreso_del_libro = ingreso_del_libro
        self.cantidad = cantidad
        self.disponible = self.cantidad > 0

    def prestamo(self):
        if self.disponible == True:
            self.cantidad -= 1
            print(
                f'El libro {self.titulo} ha sido prestado,\n Quedan {self.cantidad} disponibles')
        else:
            print(f'El libro {self.titulo} no esta disponible')
