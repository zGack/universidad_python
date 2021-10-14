class Persona:
    def __init__(self, nombre, apellido, edad, *valor, **termios):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.valor = valor
        self.termios = termios

    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad} {self.valor} {self.termios}')

def __main__():
    person1 = Persona('Sebas', 'Mena', 22, '6577344', 2, 3, 5, f='fresa', l='limon')
    person1.mostrar_detalle()

    person2 = Persona('Valen', 'Lozada', 20)
    person2.mostrar_detalle()

__main__()

