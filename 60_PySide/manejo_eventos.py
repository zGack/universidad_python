# Signals y slots
from PySide6.QtWidgets import QApplication, QLabel, QLineEdit, QMainWindow, QPushButton, QVBoxLayout, QWidget
import sys

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Signals y Slots')
        self.setFixedSize(400, 200)
        # Componentes
        self.label = QLabel()
        self.entry_txt = QLineEdit()
        # Conectar el entry_txt con label
        # la señal es textChanged, el slot es setText
        self.entry_txt.textChanged.connect(self.label.setText)
        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.entry_txt)
        layout.addWidget(self.label)
        # Contenedor
        container = QWidget()
        container.setLayout(layout)
        # Se publica el contenedor
        self.setCentralWidget(container)

if __name__ == '__main__':
    # Obj app
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()

    sys.exit(app.exec())