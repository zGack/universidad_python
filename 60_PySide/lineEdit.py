from PySide6.QtWidgets import QLineEdit, QMainWindow, QApplication
import sys

class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Line Edit')

        # Line Edit
        linea_texto = QLineEdit()

        # Maximo de chars
        linea_texto.setMaxLength(20)

        # Placeholder
        linea_texto.setPlaceholderText('Introduce tu nombre')

        # Solo lectura
        #linea_texto.setReadOnly(True)

        # Validacion (mask)
        linea_texto.setInputMask('000-000-0000')

        # Evento ENTER, cambio seleccion de texto, cambio texto
        linea_texto.returnPressed.connect(self.enter_presionado)
        linea_texto.selectionChanged.connect(self.cambio_seleccion)
        linea_texto.textChanged.connect(self.cambio_texto)

        # Mostrar Componente
        self.setCentralWidget(linea_texto)

    def enter_presionado(self):
        print('Se presiono el enter')
        self.centralWidget().setText('Sebas Mena')

    def cambio_seleccion(self):
        print('Cambio seleccion texto')
        print(self.centralWidget().selectedText())

    def cambio_texto(self, texto):
        print(f'Cambio de texto {texto}')

if __name__ == '__main__':
    app = QApplication()
    ventana = Componentes()
    ventana.show()
    sys.exit(app.exec())