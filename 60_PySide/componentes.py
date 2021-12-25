from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QCheckBox, QLabel, QMainWindow
from PySide6.QtCore import Qt
import sys

class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Componentes')
        # Checkbox
        checkbox = QCheckBox('Este es un checkbox')
        # Tercer estado
        #checkbox.setTristate(True)
        # Señal de cambio de componente
        checkbox.stateChanged.connect(self.mostrar_estado)

        """"
        # Etiqueta
        label = QLabel('Hola')
        # Cargar imagen
        label.setPixmap(QPixmap('layla.jpg'))
        # ajustar escala de la imagen
        label.setScaledContents(True)
        """

        """
        # Modicar valor inicial
        label.setText('Saludos')
        # Modificar fuente
        fuente = label.font()
        fuente.setPointSize(25)
        label.setFont(fuente)
        # Modificar alineacion de la etiqueta
        label.setAlignment(Qt.AlignCenter)
        #label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        """
        # Publicar componente
        self.setCentralWidget(checkbox)

    def mostrar_estado(self, estado):
        print(f'Estado del checkbox: {estado}')

        if estado == Qt.Checked:
            print('Checkbox encendido')
        elif estado == Qt.PartiallyChecked:
            print('Checkbox sin estado o parcialmente checado')
        elif estado == Qt.Unchecked:
            print('Checkbox apagado')
        else:
            print('Checkbox con estado invalido')

if __name__ == '__main__':
    app = QApplication([])
    ventana = Componentes()
    ventana.show()
    sys.exit(app.exec())

