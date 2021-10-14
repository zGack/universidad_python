from Empleado import Empleado
from Gerente import Gerente

def imprimir_detalles(objeto):
    #print(objeto)
    print(type(objeto))
    print(objeto.mostrar_detalle())
    if isinstance(objeto, Gerente):
        print(objeto.departamento)

empleado = Empleado('Sebas', 5000)
imprimir_detalles(empleado)

gerente = Gerente('Valen', 15000, 'Marketing')
imprimir_detalles(gerente)

