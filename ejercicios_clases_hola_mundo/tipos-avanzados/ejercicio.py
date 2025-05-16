from pprint import pprint
string = "Hola mundo este es un string"


def quita_espacio(texto):
    return [char for char in texto if char != " "]


def cuenta_caracteres(lista):
    char_dict = {}
    for char in lista:

        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict


def ordena(dict):
    return sorted(
        dict.items(),
        key=lambda key: key[1],
        reverse=True
    )


def mayores_tuplas(lista):
    maximo = lista[0][1]
    respuesta = {}
    for orden in lista:
        if maximo > orden[1]:
            break
        respuesta[orden[0]] = orden[1]
    return respuesta


def crea_mensaje(diccionario):
    mensaje = 'Los mensajes que mas se repiten son: \n'
    for key, valor in diccionario.items():
        mensaje += f' - {key} con valor {valor} repeticiones \n'
    return mensaje


sin_espacio = quita_espacio(string)
caracteres_contados = cuenta_caracteres(sin_espacio)
ordenados = ordena(caracteres_contados)
mayores = mayores_tuplas(ordenados)
mensaje = crea_mensaje(mayores)
print(mensaje)
