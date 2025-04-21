tw = ''

print('Publica tu twitt\n')

while True:
    tw = input("..> ")

    if tw.lower() == 'salir':
        break
    elif tw == '':
        print('No se permiten publicaciones vacias')
    elif len(tw) > 20:
        print('Sobrepasa los 20 caracteres')
    else:
        print(f"""Tu Twitt ha sido publicado\n{tw}""")
