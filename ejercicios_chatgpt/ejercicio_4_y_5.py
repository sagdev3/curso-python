# frase = input("Escribe tu frase favorita: ")
# reemplazar = input("Que palabra en la frase te gustaria reemplazar: ")
# reemplazo = input("Porque palabra te gustaria reemplazar en la frase: ")

# print(frase.lower())
# print(frase.upper())

# print(frase.replace(reemplazar, reemplazo))

# Calculadora de propina

sub_total = float(input('Ingrese el valor de la cuenta: '))
porcentaje_propina = float(input('Ingrese el porcentaje de la propina: '))

valor_propina = (sub_total * porcentaje_propina)/100

total_a_pagar = sub_total + valor_propina

print(
    f'''\n\f\f\fEl valor de la cuenta es: ${sub_total}\n 
    El porcentaje de la propina es del: {porcentaje_propina}%\n 
    El valor de la propina es: ${valor_propina}\n 
    Total a pagar ${total_a_pagar}''')
