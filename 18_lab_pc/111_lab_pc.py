from Raton import Raton
from Teclado import Teclado
from Monitor import Monitor
from Computadora import Computadora
from Orden import Orden

teclado1 = Teclado('Kalley','USB')
raton1 = Raton('Logitech', 'USB')
monitor1 = Monitor('HP', 15)
computadora1 = Computadora('ACER',monitor1, teclado1, raton1)

teclado2 = Teclado('HP','Bluetooh')
raton2 = Raton('Acer','Bluetooh')
monitor2 = Monitor('Samsung', '32')
computadora2 = Computadora('LENOVO',monitor2, teclado1, raton2)

teclado3 = Teclado('Logitech','USB')
raton3 = Raton('Razer','Bluetooh')
monitor3 = Monitor('LG', '31')
computadora3 = Computadora('Corsair',monitor3, teclado3, raton3)

computadoras = [computadora1, computadora2, computadora3]
orden1 = Orden(computadoras)

print(orden1)


orden2 = Orden([computadora2, computadora3])
print(orden2)
