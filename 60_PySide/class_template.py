from PySide6.QtWidgets import QMainWindow, QApplication
import sys

class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Componente')

        # Mostrar componente
        self.setCentralWidget()

if __name__ == '__main__':
    app = QApplication()
    ventana = Componentes()
    ventana.show()
    sys.exit(app.exec())