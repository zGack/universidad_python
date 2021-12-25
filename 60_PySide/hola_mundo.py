import sys
from PySide6.QtWidgets import QApplication, QMainWindow

# Clase base de Qt (PySide)
# Se encarga de procesar los eventos (event loop)
app = QApplication()

# Objeto ventana
ventana = QMainWindow()

# Cambiar el titulo
ventana.setWindowTitle('Hola Mundo con PySide')

ventana.resize(600, 400)

# Mostrar la ventana
ventana.show()

# Se ejecut la aplicacion
sys.exit(app.exec())