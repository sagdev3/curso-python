class Alquiler:
    def __init__(self, marca, modelo, year, color, puertas, placa, precio):
        self.marca = marca
        self.modelo = modelo
        self.year = year
        self.color = color
        self.puertas = puertas
        self.placa = placa
        self.precio = precio
        self.disponible = True

    def alquiler(self):
        if self.disponible:
            self.disponible = False
            print(
                f'El auto {self.marca} {self.modelo} color {self.color} con placas {self.placa} ha sido alquilado a un valor de ${self.precio}')
        else:
            print(f'El auto con placa {self.placa} ya no esta disponible')

    def devolucion(self):
        self.disponible = True
        print(f'El auto con placas {self.placa} ha sido devuelto')


class Ventas:
    def __init__(self, marca, modelo, year, color, puertas, chasis, precio):
        self.marca = marca
        self.modelo = modelo
        self.year = year
        self.color = color
        self.puertas = puertas
        self.chasis = chasis
        self.precio = precio
        self.disponible = True

    def venta(self):
        if self.disponible:
            self.disponible = False
            print(
                f'El auto {self.marca} {self.modelo} color {self.color} ha sido vendido a un valor de ${self.precio}')
        else:
            print(
                f'El auto {self.marca} {self.modelo} color {self.color} ya no esta disponible')


class Clientes:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula
        self.autos_alquilados = []
        self.autos_comprados = []

    def alquiler_auto(self, auto):
        if auto.disponible:
            auto.alquiler()
            self.autos_alquilados.append(auto)
        else:
            print(
                f'El auto {auto.marca} {auto.modelo} con placas {auto.placa} no esta disponible')

    def devolucion_auto(self, auto):
        if auto in self.autos_alquilados:
            auto.devolucion()
            self.autos_alquilados.remove(auto)
        else:
            print(
                f'El auto {auto.marca} {auto.modelo} no esta en la lista de alquilados')

    def comprar_auto(self, auto):
        if auto.disponible:
            auto.venta()
            self.autos_comprados.append(auto)
        else:
            print(
                f'El auto {auto.marca} {auto.modelo} del año {auto.year} con precio de ${auto.precio}')


class Concesionaria:
    def __init__(self):
        self.autos_para_alquilar = []
        self.autos_para_vender = []
        self.clientes = []

    def add_autos_alquiler(self, auto):
        self.autos_para_alquilar.append(auto)
        print(
            f'El auto {auto.marca} {auto.modelo} con placas {auto.placa} color {auto.color} con {auto.puertas} se ha comprado para alquiler a un valor de ${auto.precio}')

    def registrar_cliente(self, cliente):
        self.clientes.append(cliente)
        print(f'El cliente {cliente.nombre} ha sido agregado')

    def mostrar_autos_para_alquilar(self):
        print('Autos para Alquilar: ')
        for auto in self.autos_para_alquilar:
            if auto.disponible:
                print(
                    f'{auto.marca} {auto.modelo} color {auto.color} {auto.puertas} puertas, con placas {auto.placa} precio ${auto.precio}')

    def add_autos_ventas(self, auto):
        self.autos_para_vender.append(auto)
        print(
            f'El auto {auto.marca} {auto.modelo} del año {auto.year} ha sido agregado en un valor de ${auto.precio}')

    def mostrar_autos_en_ventas(self):
        for auto in self.autos_para_vender:
            if auto.disponible:
                print('Autos en ventas: ')
                print(
                    f'{auto.marca} {auto.modelo} color {auto.color} {auto.puertas} puertas del año {auto.year} precio ${auto.precio}')


auto1 = Alquiler('Chevrolet', 'Spark', '2015', 'rojo', '4', 'PEF-4554', 8000)
auto2 = Alquiler('Hiundai', 'Q10', '2020', 'blanco', '4', 'MAF-3564', 14000)

cliente1 = Clientes('Santiago', "13111411787")
cliente2 = Clientes('Dayana', '1724554665')

consecionaria = Concesionaria()

consecionaria.add_autos_alquiler(auto1)
consecionaria.add_autos_alquiler(auto2)

consecionaria.mostrar_autos_para_alquilar()

cliente1.alquiler_auto(auto1)

consecionaria.mostrar_autos_para_alquilar()
cliente2.alquiler_auto(auto2)

cliente1.devolucion_auto(auto1)
consecionaria.mostrar_autos_para_alquilar()


auto3 = Ventas('Chevrolet', 'Family', '2023', 'gris', '4', '134315245', 16000)
auto4 = Ventas('Chevrolet', 'Camaro', '2007',
               'Azul', '3', '314342523454', 30000)
consecionaria.add_autos_ventas(auto3)
consecionaria.add_autos_ventas(auto4)

consecionaria.mostrar_autos_en_ventas()

cliente1.comprar_auto(auto4)
consecionaria.mostrar_autos_en_ventas()
