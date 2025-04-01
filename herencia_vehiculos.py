class Vehicle:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.is_available = True

    def sell(self):
        if self.is_available:
            self.is_available = False
            print(
                f'El vehiculo {self.brand} {self.model} con un valor de ${self.price}')
        else:
            print('El Vehiculo no esta disponible')

    def check_available(self):
        return self.is_available

    def get_price(self):
        return self.price

    def start_engine(self):
        raise NotImplementedError(
            "Este metodo debe ser implementado por la subclase")

    def stop_engine(self):
        raise NotImplementedError(
            "Este metodo debe ser implementado por la subclase")


class Car(Vehicle):
    def start_engine(self):
        if not self.is_available:
            return f"El motor del coche {self.brand} esta en marcha"
        else:
            return f'El coche {self.brand} no esta disponible'

    def stop_engine(self):
        if self.is_available:
            return f'El motor del coche {self.brand} se ha detenido'
        else:
            return f'El coche {self.brand} No esta disponible'


class Bike(Vehicle):
    def start_engine(self):
        if not self.is_available:
            return f'La Bicicleta {self.brand} esta en marcha'
        else:
            return f'La bicicleta {self.brand} no esta disponible'

    def stop_engine(self):
        if self.is_available:
            return f'LA Bicicleta {self.brand} se ha detenido'
        else:
            return f'La Bicicleta {self.brand} No esta disponible'


class Truck(Vehicle):
    def start_engine(self):
        if not self.is_available:
            return f"El motor del Camion {self.brand} esta en marcha"
        else:
            return f'El Camion {self.brand} no esta disponible'

    def stop_engine(self):
        if self.is_available:
            return f'El motor del Camion {self.brand} se ha detenido'
        else:
            return f'El Camion {self.brand} No esta disponible'


class Customer:
    def __init__(self, name):
        self.name = name
        self.purchased_vehicles = []

    def buy_vehicles(self, vehicle: Vehicle):
        if vehicle.check_available():
            vehicle.sell()
            self.purchased_vehicles.append(vehicle)
        else:
            print(f'Lo siento el vehiculo {vehicle.brand} no esta disponible')

    def inquire_vehicle(self, vehicle: Vehicle):
        if vehicle.check_available():
            availablity = 'Disponible'
        else:
            availablity = 'No Disponible'
        print(
            f'El {vehicle.brand} esta {availablity} y cuesta {vehicle.get_price()}')


class Dealerchip:
    def __init__(self):
        self.inventory = []
        self.customers = []

    def add_vehicles(self, vehicles: Vehicle):
        self.inventory.append(vehicles)
        print(f'El vehiculo {vehicles.brand} ha sido agregado al inventario')

    def register_customers(self, customer: Customer):
        self.customers.append(customer)
        print(f'El Cliente {customer.name} ha sido Registrado')

    def show_available_vehicles(self):
        print("Vehiculos Disponibles")
        for vehicle in self.inventory:
            if vehicle.check_available():
                print(
                    f"Vehiculo {vehicle.brand} - {vehicle.model} - {vehicle.get_price()}")


car1 = Car("Toyota", "Corolla", 25545)
bike1 = Bike("Yamaha", "MT-07", 4546)
truck1 = Truck("Volvo", "FH16", 200000)

customer1 = Customer('Santiago')

dealership = Dealerchip()

dealership.add_vehicles(car1)
dealership.add_vehicles(bike1)
dealership.add_vehicles(truck1)

dealership.register_customers(customer1)

dealership.show_available_vehicles()

customer1.inquire_vehicle(car1)

customer1.buy_vehicles(car1)


dealership.show_available_vehicles()
