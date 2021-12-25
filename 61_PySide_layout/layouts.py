from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QApplication, QHBoxLayout, QMainWindow, QVBoxLayout, QWidget
import sys

class Color(QWidget):
    def __init__(self, nuevo_color):
        super().__init__()

        # Color de fondo
        self.setAutoFillBackground(True)
        paletaColores = self.palette()

        # Componente color
        paletaColores.setColor(QPalette.Window, QColor(nuevo_color))

        # Nuevo color al componente
        self.setPalette(paletaColores)

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Layouts en PySide')

        # Layout vertical
        #layout = QVBoxLayout()

        # Layout horizontal
        #layout = QHBoxLayout()

        # Layouts anidados
        h_layout = QHBoxLayout()
        v_layout = QVBoxLayout()

        # Agregar widgets al v_layout
        v_layout.addWidget(Color('red'))
        v_layout.addWidget(Color('green'))
        v_layout.addWidget(Color('yellow'))
        

        h_layout.addWidget(Color('Blue'))

        # Se agrega el v_layout al h_layout
        h_layout.addLayout(v_layout)
        
        # Agregar widgets al h_layout
        h_layout.addWidget(Color('Black'))

        # Widget
        componente = QWidget()
        componente.setLayout(h_layout)

        self.setCentralWidget(componente)

if __name__ == '__main__':
    app = QApplication()
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())