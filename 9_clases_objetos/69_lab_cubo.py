class Cubo:
    def __init__(self, ancho, alto, profundidad):
        self.ancho = ancho
        self.alto = alto
        self.profundidad = profundidad

    def calcular_cubo(self):
        return self.ancho * self.alto * self.profundidad

def __main__():
    ancho = int(input("Proporcione el ancho: "))
    alto = int(input("Proporcione el alto: "))
    profundidad = int(input("Proporcione el profundidad: "))
    
    cubo1 = Cubo(ancho, alto, profundidad)

    print(f'Volumen cubo: {cubo1.calcular_cubo()}')
    

__main__()
