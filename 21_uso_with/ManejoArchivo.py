class ManejoRecursos:
    def __init__(self, nombre):
        self.nombre = nombre

    def __enter__(self):
        print('Obtenemos el recurso'.center(50, '-'))
        self.nombre = open(self.nombre, 'r', encoding='utf8')
        return self.nombre

    def __exit__(self, tipo_excep, valor_excep, traceback):
        print('Cerrar el recurso'.center(50, '-'))

        if self.nombre:
            self.nombre.close()


