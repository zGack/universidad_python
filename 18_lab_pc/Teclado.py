from DispositivoEntrada import DispositivoEntrada as in_device

class Teclado(in_device):
    contador_teclados = 0

    def __init__(self, tipo_entrada, marca):
        super().__init__(tipo_entrada, marca)
        Teclado.contador_teclados += 1
        self._id_teclado = Teclado.contador_teclados

    def __str__(self):
        return f'Teclado: Id: {self._id_teclado} {super().__str__()}'
