# from abc import ABC, abstractmethod


# class Model(ABC):
#     @abstractmethod
#     def guardar(self):
#         pass


class Usuario():
    def guardar(self):
        print("Guardando en BBD")


class Sesion():
    def guardar(self):
        print("Guardando en archivo")


def guardar(entidades):
    for entidad in entidades:
        entidad.guardar()


usuario = Usuario()
sesion = Sesion()
guardar([sesion, usuario])
