from Raton import Raton
from Monitor import Monitor
from Teclado import Teclado

class Computadora:
    contador_computadora = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contador_computadora += 1
        self._id_computadora = Computadora.contador_computadora
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def monitor(self):
        return self._monitor

    @monitor.setter
    def monitor(self, monitor):
        self._monitor = monitor

    @property
    def teclado(self):
        return self._teclado

    @teclado.setter
    def teclado(self, teclado):
        self._teclado = teclado

    @property
    def raton(self):
        return self._raton

    @raton.setter
    def raton(self, raton):
        self._raton = raton

    def __str__(self):
        return f'''
        {self._nombre}: {self._id_computadora}
        Monitor: {self._monitor}
        Teclado: {self._teclado}
        Raton: {self._raton}
        '''

if __name__ == '__main__':
    teclado1 = Teclado('Kalley','USB')
    raton1 = Raton('Logitech', 'USB')
    monitor1 = Monitor('HP', 15)
    computadora1 = Computadora('ACER',monitor1, teclado1, raton1)
    print(computadora1)
    teclado2 = Teclado('HP','Bluetooh')
    raton2 = Raton('Acer','Bluetooh')
    monitor2 = Monitor('Samsung', '32')
    computadora2 = Computadora('ACER',monitor2, teclado1, raton2)
    print(computadora2)


