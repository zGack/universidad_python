from PySide6.QtWidgets import QComboBox, QMainWindow, QApplication
import sys

class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('ComboBox')
        
        # Combobox (drop down list)
        combobox = QComboBox()

        # Agregar elementos
        combobox.addItem('Uno')
        combobox.addItems(['Dos', 'Tres'])

        # Elemento seleccionado
        combobox.currentIndexChanged.connect(self.cambio_indice)
        combobox.currentTextChanged.connect(self.cambio_texto)

        # Combobox editable
        combobox.setEditable(True)

        # POLITICAS DE INSERCION

        # No permitir agregar
        #combobox.setInsertPolicy(QComboBox.NoInsert)

        # Insertar al inicio
        #combobox.setInsertPolicy(QComboBox.InsertAtTop)
        
        # Modificar item 
        #combobox.setInsertPolicy(QComboBox.InsertAtCurrent)

        # Insertar al final
        #combobox.setInsertPolicy(QComboBox.InsertAtBottom)
    
        # Insertar antes el item actual
        #combobox.setInsertPolicy(QComboBox.InsertBeforeCurrent)

        # Insertar despues el item actual
        #combobox.setInsertPolicy(QComboBox.InsertAfterCurrent)

        # Insertar alfabeticamente
        combobox.setInsertPolicy(QComboBox.InsertAlphabetically)

        # Limitar numero de items
        combobox.setMaxCount(5)

        # Publicar componente
        self.setCentralWidget(combobox)

    def cambio_indice(self, indice):
        print(f'Indice seleccionado: {indice}')
        
    def cambio_texto(self, texto):
        print(f'Texto seleccionado: {texto}')

if __name__ == '__main__':
    app = QApplication([])
    ventana = Componentes()
    ventana.show()
    sys.exit(app.exec())

