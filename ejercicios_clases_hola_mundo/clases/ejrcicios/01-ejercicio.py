class CajaRegistrador:
    def __init__(self):
        self.productos = []

    def agregar_productos(self, nombre, precio):
        self.productos.append({'nombre': nombre, 'precio': precio})

    def obtener_total(self):
        return sum(producto['precio'] for producto in self.productos)

    def listar_productos(self):
        return self.productos

    def dar_cambio(self, pago):
        total = self.obtener_total()

        if pago < total:
            return ('El pago es insuficiente')

        self.productos = []
        return pago-total


caja = CajaRegistrador()

caja.agregar_productos('Naranja', 0.5)
caja.agregar_productos('Arroz', 25)

print(f'Productos\n {caja.listar_productos()}')


print("Total:", caja.obtener_total())
print("Cambio:", caja.dar_cambio(26))

print(f'Productos\n {caja.listar_productos()}')
