celcius = int(input("Introduce la temperatura en grados Celsius: "))

fahrenheit = (celcius * 9/5) + 32
kelvin = celcius + 273.15

mensaje = f"""Ingresaste {celcius} °C. 🌡️
La temperatura en Fahrenheit es: {fahrenheit} °F
La temperatura en Kelvin es: {kelvin} K
"""
print(mensaje)
