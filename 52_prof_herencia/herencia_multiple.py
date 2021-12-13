# MRO - Method Resolution Order 
# Ejemplo

class Clase1():
    def __init__(self):
        print('Clase1.__init__()')

    def metodo(self):
        return f'Metodo Clase1'

class Clase2(Clase1):
    def __init__(self):
        print('Clase2.__init__()')

    def metodo(self):
        print('Metodo Clase2')

class Clase3(Clase1):
    def __init__(self):
        print('Clase3.__init__()')

    def metodo(self):
        print('Metodo Clase3')

class Clase4(Clase2, Clase3):
    def metodo(self):
        print('Metodo clase4')

if __name__ == '__main__':
    clase4 = Clase4()
    print(Clase4.__bases__)
    print(Clase4.__mro__)
    clase4.metodo()