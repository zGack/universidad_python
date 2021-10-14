from DispositivoEntrada import DispositivoEntrada as in_device

class Raton(in_device):
    contador_ratones = 0

    def __init__(self, tipo_entrada, marca):
        super().__init__(tipo_entrada, marca)
        Raton.contador_ratones += 1
        self.idRaton = Raton.contador_ratones

    def __str__(self):
        return f'Raton:  Id: {self.idRaton} {super().__str__()}'

