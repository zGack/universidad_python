from PySide6.QtWidgets import QListWidget, QMainWindow, QApplication
import sys

class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('ListWidget')

        # QListWidget
        lista = QListWidget()

        # Agregar elementos
        lista.addItem('Uno')
        lista.addItems(['Dos', 'Tres'])

        # Elemento seleccionado
        lista.currentItemChanged.connect(self.cambio_elemento)
        lista.currentTextChanged.connect(self.cambio_texto)

        # Mostrar wideget
        self.setCentralWidget(lista)

    def cambio_elemento(self, elemento):
        print(f'Nuevo elemento: {elemento.text()}')

    def cambio_texto(self, texto):
        print(f'Nuevo texto: {texto}')

if __name__ == '__main__':
    app = QApplication()
    ventana = Componentes()
    ventana.show()
    sys.exit(app.exec())