class Monitor:
    contador_monitor = 0

    def __init__(self, marca, size):
        Monitor.contador_monitor += 1
        self._id_monitor = Monitor.contador_monitor
        self._marca = marca
        self._size = size

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size

    def __str__(self):
        return f'Monitor: Id: {self._id_monitor} marca: {self._marca}, size: {self._size} pulgadas'
