class Productos:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        self.disponible = True

    def vender(self):
        if self.disponible:
            self.disponible = False
            print(
                f'El producto {self.nombre} se vendio\n Precio: ${self.precio}')
        else:
            print('El producto no se encuentra disponible')

    def comprobar_disponibilidad(self):
        return self.disponible

    def get_precio(self):
        return self.precio


class Venta:
    def __init__(self, valor_pagado):
        self.valor_pagado = valor_pagado
        self.productos_vendidos = []

    def venta_producto(self, producto: Productos):
        if producto.comprobar_disponibilidad():
            producto.vender()

            cambio = max(0, self.valor_pagado - producto.get_precio())
            cambio = self.valor_pagado - producto.precio
            self.productos_vendidos.append({
                "Producto": producto.nombre,
                "Precio": producto.get_precio(),
                "Cambio": cambio})
            print(f"Venta realizada. Cambio: ${cambio}")
        else:
            print(f"El producto {producto.nombre} no está disponible.")


class CajaRegistradora:
    def __init__(self):
        self.inventario = []

    def add_productos(self, producto: Productos):
        self.inventario.append(producto)
        print(f'El producto {producto.nombre} ha sido agregado')

    def productos_disponibles(self):
        print(" *** PRODUCTOS DISPONIBLES *** ")
        print('--------------------------------')
        for producto in self.inventario:
            estado = "Disponible" if producto.comprobar_disponibilidad() else "No Disponible"
            print(f'{producto.nombre} - Precio ${producto.precio} - Estado: {estado}')


producto1 = Productos('Uvas', 45)
producto2 = Productos("Manzana", 3)

caja = CajaRegistradora()

caja.add_productos(producto1)
caja.add_productos(producto2)

caja.productos_disponibles()

venta = Venta(50)
venta.venta_producto(producto1)

caja.productos_disponibles()
