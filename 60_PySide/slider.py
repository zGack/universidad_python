from PySide6.QtGui import Qt
from PySide6.QtWidgets import QDial, QMainWindow, QApplication, QSlider
import sys

class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Slider')

        # Slider
        #slider = QSlider()
        #slider = QSlider(Qt.Horizontal)

        # Dial
        dial = QDial()

        # Establecer rango min y max
        #dial.setMinimum(-5)
        #dial.setMaximum(5)
        dial.setRange(-5, 5)
        
        # Signals
        dial.valueChanged.connect(self.cambio_valor)
        dial.sliderMoved.connect(self.slider_cambio_valor)
        dial.sliderPressed.connect(self.slider_presionado)
        dial.sliderReleased.connect(self.slider_liberado)

        # Mostrar componente
        self.setCentralWidget(dial)

    def cambio_valor(self, nuevo_valor):
        print(f'Nuevo valor: {nuevo_valor}')

    def slider_cambio_valor(self, nueva_posicion):
        print(f'Nueva posicion: {nueva_posicion}')

    def slider_presionado(self):
        print('Dial presionado')

    def slider_liberado(self):
        print('Dial liberado')


if __name__ == '__main__':
    app = QApplication()
    ventana = Componentes()
    ventana.show()
    sys.exit(app.exec())