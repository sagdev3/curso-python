# FIFO first In First Out
# Primero en entrar primero en salir

from collections import deque

fila = deque([1, 2])
fila.append(3)
fila.append(4)
fila.append(5)

print(fila)
fila.popleft()

print(fila)

if not fila:
    print("Fila Vacia")
