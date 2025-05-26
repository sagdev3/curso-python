from abc import ABC, abstractmethod


class Inventario(ABC):
    def __init__(self, nombre, activo_fijo, numero_serie, marca, modelo):
        self.nombre = nombre
        self.activo_fijo = activo_fijo
        self.numero_serie = numero_serie
        self.marca = marca
        self.modelo = modelo
        self.baja = False

    @abstractmethod
    def dar_baja(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class InventarioEquipo(Inventario):
    def __init__(self, nombre, activo_fijo, numero_serie, marca, modelo):
        super().__init__(nombre, activo_fijo, numero_serie, marca, modelo)

    def dar_baja(self):
        self.baja = True
