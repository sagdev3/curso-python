usuarios = {
    "usuario": "sagsilver",
    "pass": "123456"
}

print("Ingresa tus Credenciales")
print('------------------------')

user = input('Usuario: ')
passw = input('Clave: ')

if user != usuarios["usuario"] and passw != usuarios["pass"]:
    print('❌ Error: Usuario y contraseña incorrectos.')
elif user != usuarios["usuario"]:
    print("❌ Error: El usuario no es correcto.")
elif passw != usuarios["pass"]:
    print("❌ Error: La contraseña no es correcta.")
else:
    print("✅ ¡Felicidades! Datos correctos.")
