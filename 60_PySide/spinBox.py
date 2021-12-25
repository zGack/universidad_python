from PySide6.QtWidgets import QDoubleSpinBox, QMainWindow, QApplication, QSpinBox
import sys

class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Spin Box')

        # SpinBox (Valores numericos)
        numero = QSpinBox()

        # DoubleSpinBox (Valores flotantes)
        #numero = QDoubleSpinBox

        # Establecer valor minimo y valor maximo
        #numero.setMinimum(-5)
        #numero.setMaximum(5)
        numero.setRange(-5000, 5000)

        # Establecer prefijo y sufijo
        numero.setPrefix('$ ')
        numero.setSuffix(' COP')

        # Salto (step)
        numero.setSingleStep(1000)

        # Evento cambio de valor
        # Valor numerico
        numero.valueChanged.connect(self.cambio_valor)

        # valor en texto
        numero.textChanged.connect(self.cambio_texto)

        # Mostrar componente
        self.setCentralWidget(numero)

    def cambio_valor(self, nuevo_valor):
        print(f'Nuevo valor: {nuevo_valor}')

    def cambio_texto(self, nuevo_texto):
        print(f'Nuevo texto {nuevo_texto}')

if __name__ == '__main__':
    app = QApplication()
    ventana = Componentes()
    ventana.show()
    sys.exit(app.exec())