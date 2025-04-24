def aplicar_descuento(total, descuento_porcentaje):
    descuento = (total * descuento_porcentaje)/100
    valor_a_pagar = total - descuento
    return valor_a_pagar


total = 1000
descuento = 1004


if descuento > 100:
    print("Este descuento no se puede aplicar")
elif descuento == 100:
    print("Felicidades tu valor es gratis!!!")
elif descuento <= 0:
    print(f"Ups!! Lo sentimos no tienes descuento tu valor a pagar es {total}")
else:
    a_pagar = aplicar_descuento(total, descuento)
    print(
        f'Tienes un descuento del {descuento}% por lo cual tu valor a pagar es ${a_pagar}')
