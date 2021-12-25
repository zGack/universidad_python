from PySide6.QtCore import QSize
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys

class VentanaPySide(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('POO con PySide')
        #self.resize(600, 400)
        self.setFixedSize(QSize(600, 400))

        # Componentes
        self._agregar_componentes()

    def _agregar_componentes(self):
        # Agregar menu
        menu = self.menuBar()
        menu_archivo = menu.addMenu('Archivo')
        # Aregar opciones al menu
        accion_nuevo = QAction('Nuevo', self)
        menu_archivo.addAction(accion_nuevo)
        # Agregar texto a la barra de estado
        accion_nuevo.setStatusTip('Nuevo Archivo')
        # Agregar mensaje a la barra de estado
        self.statusBar().showMessage('Informacion de la barra estado...')
        # Boton
        btn = QPushButton('Nuevo boton')
        # Se agrega el boton en la ventana
        self.setCentralWidget(btn)

if __name__ == '__main__':
    app = QApplication([])
    # Obj tipo ventana
    ventana = VentanaPySide()
    ventana.show()

    sys.exit(app.exec())