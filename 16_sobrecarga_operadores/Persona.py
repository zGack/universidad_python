class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def __add__(self, other):
        return f'{self.nombre} {other.nombre}'


perosona1 = Persona('Sebas')
perosona2 = Persona('Valen')

print(perosona1 + perosona2)
#obj1 + obj2
