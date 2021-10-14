from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

print("Creacion Objeto Cuadrado".center(50,'-'))
cuadrado1 = Cuadrado(5, 'rojo')
print(f'{cuadrado1} Area: {cuadrado1.calcular_area()}')

print("Creacion Objeto Rectangulo".center(50,'-'))
rectangulo1 = Rectangulo(5, 3, 'amarillo')
print(f'{rectangulo1} Area: {rectangulo1.calcular_area()}')
