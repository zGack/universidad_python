class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalle(self):
        print(f'Persona: {self._nombre} {self._apellido} {self._edad}')

def __main__():
    person1 = Persona('Sebas', 'Mena', 22)
    person1.mostrar_detalle()

__main__()
