if __name__ != "__main__":
    print("tarea de mantenimiento")
    # from ..gestion.crud import guardar #Import relativo
    from usuario.gestion.crud import guardar  # Import absoluto

    print(__name__)

    def pagar_impuestos():
        print('Impuestos pagados')
        guardar()

if __name__ == "__main__":
    print("tarea de mantenimiento")
