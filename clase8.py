to_do = ['Dirigirnos al hotel',
         'ir a almorzar',
         'visitar el museo',
         'volvemos al hotel',]

print(to_do)

numeros = [1, 2, 3, 4, "5", 'cinco']
print(numeros)

print(type(numeros))

mix = ['uno', 2, 3.14, True, [1, 2, 3]]
print(mix)

print(len(mix))
print("Primer elemento de la lista mix:", mix[0])
print("Ultimo elemento de la lista mix:", mix[-1])
string = 'Hola mundo'
print(string[0])
print(string[-1])

print(mix[0:2])
print(mix[:2])
print(mix[2:])
print(mix[2:-2])

print(mix)
mix.append(False)
print(mix)
mix.append(['a', 'b'])
print(mix)

mix.insert(1, ['x', 'y'])
print(mix)

print(mix.index(3.14))

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Mayor:", max(numeros))
print("Menor:", min(numeros))
print("Suma:", sum(numeros))

del numeros[-1]
print(numeros)

del numeros[:2]
print(numeros)

# del numeros
# print(numeros)
