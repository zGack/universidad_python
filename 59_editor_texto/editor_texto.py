import tkinter as tk
from tkinter.filedialog import askopenfile, asksaveasfilename

class Editor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Editor de texto')
        # Conf tamaño min de la ventana
        self.rowconfigure(0, minsize=600, weight=1)
        # Conf min de la segunda columna
        self.columnconfigure(1, minsize=600, weight=1)
        # Atributo de campo de texto
        self.campo_texto = tk.Text(self, wrap=tk.WORD)
        # Atributo de archivo
        self.archivo = None
        # Atributo para saber si ya se abrio un archivo anterormete
        self.archivo_abierto = False
        # Creacon de componentes
        self._crear_componentes()
        self._crear_menu()

    def _crear_componentes(self):
        frame_btns = tk.Frame(self, relief=tk.RAISED, bd=2)
        btn_abrir = tk.Button(frame_btns, text='Abrir', command=self._abrir_archivo)
        btn_guardar = tk.Button(frame_btns, text='Guardar', command=self._guardar)
        btn_guardar_como = tk.Button(frame_btns, text='Guardar Como...', command=self._guardar_como)

        # Se expanden los btns de manera horizontal
        btn_abrir.grid(row=0, column=0, sticky='we', padx=5, pady=5)
        btn_guardar.grid(row=1, column=0, sticky='we', padx=5, pady=5)
        btn_guardar_como.grid(row=2, column=0, sticky='we', padx=5, pady=5)

        # Se expande el frame de NS
        frame_btns.grid(row=0, column=0, sticky='ns')
        
        # Campo de texto
        self.campo_texto.grid(row=0, column=1, sticky='NSWE')

    def _crear_menu(self):
        # Menu desplegable
        menu_app = tk.Menu(self)
        self.config(menu=menu_app)

        # Opcs del menu
        # Archivo
        menu_archivo = tk.Menu(menu_app, tearoff=False)
        menu_app.add_cascade(label='Archivo', menu=menu_archivo)
        menu_archivo.add_command(label='Abrir', command=self._abrir_archivo)
        menu_archivo.add_command(label='Guardar', command=self._guardar)
        menu_archivo.add_command(label='Guardar Como..', command=self._guardar_como)
        menu_archivo.add_separator()
        menu_archivo.add_command(label='Salir', command=self.quit)

    def _abrir_archivo(self):
        # Abrir el archivo
        self.archivo_abierto = askopenfile(mode='r+')

        # Se elimina el texto anterior
        self.campo_texto.delete(1.0, tk.END)

        # Se revisa si hay un archivo
        if not self.archivo_abierto:
            return 

        # Se abre el archivo en modo lectura/escritura
        with open(self.archivo_abierto.name, 'r+') as self.archivo:
            # Se lee el contenido
            texto = self.archivo.read()
            # Se inserta el contenido del archivo en el campo de texto
            self.campo_texto.insert(1.0, texto)
            # Se modifica el titulo de la aplicacion
            self.title(f'*Editor Texto - {self.archivo.name}')

    def _guardar(self):
        # Si ya se abrio un archivo, se sobreescribe
        if self.archivo_abierto:
            with open(self.archivo_abierto.name, 'w') as self.archivo:
                # Se lee el contenido de la caja de texto
                text = self.campo_texto.get(1.0, tk.END)
                # Se escribe el contenido al mismo archivo
                self.archivo.write(text)
                # Se cambia el titulo de la app
                self.title(f'Editor Texto - {self.archivo.name}')
        else:
            self._guardar_como()
    
    def _guardar_como(self):
        # Se guarda el archivo actual como nuevo archivo
        self.archivo = asksaveasfilename(
            defaultextension='txt',
            filetypes=[('Archivos de Texto', '*.txt'), ('Todo los Archivos', '*.*')]
        )
        if not self.archivo:
            return
        # Abrimos el archivo en modo escritura (write)
        with open(self.archivo, 'w') as archivo:
            # Se lee el contenido de la caje de texto
            texto = self.campo_texto.get(1.0, tk.END)
            # Se escribe el contenido al nuevo archivo 
            archivo.write(texto)
            # Se cambia el nombre del archivo
            self.title(f'Editor Texto - {archivo.name}')
            self.archivo_abierto = archivo

if __name__ == '__main__':
    editor = Editor()
    editor.mainloop()