# LIFO
# Last in First Out
# Ultimo en entrar Primero en Salir

pila = []

pila.append(1)
pila.append(2)
pila.append(3)

print(pila)
ultimoElemento = pila.pop()
print(ultimoElemento)
print(pila)
ultimoElemento = pila.pop()
ultimoElemento = pila.pop()

if not pila:
    print("Pila Vacia")
    print(pila)
