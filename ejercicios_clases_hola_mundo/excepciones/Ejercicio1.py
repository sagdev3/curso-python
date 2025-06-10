class CajaRegistradora:
    def __init__(self):
        self.productos = []

    def agregar_productos(self, nombre, precio):
        self.productos.append({'nombre': nombre, 'precio': precio})

    def obtener_total(self):
        return sum(producto['precio'] for producto in self.productos)

    def dar_cambio(self, pago):
        total = self.obtener_total()

        if pago < total:
            raise ValueError('El Pago es insuficiente')
        return pago - total


caja = CajaRegistradora()
caja.agregar_productos('Manzana', 0.5)
caja.agregar_productos('pan', 1)
print(caja.obtener_total())
print('Cambio', caja.dar_cambio(2))
print('Cambio', caja.dar_cambio(1))
