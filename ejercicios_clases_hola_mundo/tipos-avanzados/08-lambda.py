usuarios = [["Santiago", 4], ["Dayana", 1], ["Dani", 5]]

usuarios.sort(key=lambda el: el[1], reverse=True)
print(usuarios)
