# def generar_ticket(productos):
#     contador_productos = {}
#     total = 0

#     for producto in productos:
#         nombre = producto["nombre"]
#         if nombre in contador_productos:
#             contador_productos[nombre]['cantidad'] += 1
#         else:
#             contador_productos[nombre] = {
#                 'precio': producto['precio'], 'cantidad': 1}

#     print("-----------------")
#     print("Ticket de compra:")
#     print("-----------------")
#     for nombre, info in contador_productos.items():
#         precio = info['precio']
#         cantidad = info['cantidad']
#         subtotal = precio * cantidad
#         total += subtotal
#         print(f"{nombre} x{cantidad} - ${subtotal:.2f}")
#         print("-----------------")
#         print(f"Total: ${total:.2f}")
#         print("-----------------")


# productos = [{'nombre': 'Manzana', 'precio': 0.5},
#              {'nombre': 'Manzana', 'precio': 0.5},
#              {'nombre': 'Pan', 'precio': 1.0},
#              {'nombre': 'Leche', 'precio': 1.5}]
# generar_ticket(productos)

# def aplicar_promocion(compras):
#     cliente_con_promocion = []

#     for cliente, monto in compras.items():
#         if monto >= 150:
#             cliente_con_promocion.append(cliente)

#     return cliente_con_promocion


# compras = {
#     'Cliente1': 100,
#     'Cliente2': 160,
#     'Cliente3': 300
# }

# cliente_promocion = aplicar_promocion(compras)
# print(cliente_promocion)

# def aplicar_promocion(compras):
#     clientes_con_promocion = [cliente for cliente,
#                               monto in compras.items() if monto > 150]
#     cuenta_clientes_con_promocion = {
#         cliente: monto for cliente, monto in compras.items() if monto > 150}
#     for cliente, monto in cuenta_clientes_con_promocion.items():
#         cuenta_clientes_con_promocion[cliente] = round(monto * 0.9, 2)

#     return [clientes_con_promocion, cuenta_clientes_con_promocion]


# compras = {
#     'Cliente1': 200,
#     'Cliente2': 100,
#     'Cliente3': 180
# }

# print(aplicar_promocion(compras))

def aplica_promocion(compras):
    cuentas_clientes_con_promocion = {
        cliente: monto for cliente, monto in compras.items() if monto > 150}
    costo_promocion = 0
    for cliente, monto in cuentas_clientes_con_promocion.items():
        cuentas_clientes_con_promocion[cliente] = round(monto * 0.9, 2)
        costo_promocion += monto - cuentas_clientes_con_promocion[cliente]
    return [costo_promocion]


compras = {
    'Cliente1': 200,
    'Cliente2': 100,
    'Cliente3': 180
}

print(aplica_promocion(compras))
