import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from time import sleep

class Componentes(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('600x400')
        self.title('Widgets')
        self.resizable(0,0)

        self.crear_tabs()

    def crear_tabs(self):
        # Tab control
        control_tabulador = ttk.Notebook(self)

        # Frame
        tab_1 = ttk.Frame(control_tabulador)
        control_tabulador.add(tab_1, text='Tabulador 1')

        # Mostrar tabulador
        control_tabulador.pack(fill='both')

        # widgets tabulador 1
        self.crear_widgets_t1(tab_1)

        # Segundo tabulador
        tab_2 = ttk.LabelFrame(control_tabulador, text='Contenido')
        control_tabulador.add(tab_2, text='Tabulador 2')

        # widgets tabulador 2
        self.crear_widgets_t2(tab_2)

        # tercer tabulador
        tab_3 = ttk.Frame(control_tabulador)
        control_tabulador.add(tab_3, text='Tabulador 3')

        self.crear_widgets_t3(tab_3)

        # cuarto tabulador
        tab_4 = ttk.LabelFrame(control_tabulador, text='Imagen')
        control_tabulador.add(tab_4, text='Tabulador 4')

        self.crear_widgets_t4(tab_4)

        # quinto tabulador
        tab_5 = ttk.LabelFrame(control_tabulador, text='Progress Bar')
        control_tabulador.add(tab_5, text='Tabulador 5')

        self.crear_widgets_t5(tab_5)



    def crear_widgets_t1(self,tab):
        # Se agrega widgets
        label_1 = ttk.Label(tab, text='Nombre:')
        label_1.grid(row=0, column=0, sticky='e')

        entry_1 = ttk.Entry(tab, width=30)
        entry_1.grid(row=0, column=1, padx=5, pady=5)

        def enviar():
            messagebox.showinfo('Mensaje ', entry_1.get())

        btn_1 = ttk.Button(tab, text='Enviar', command=enviar)
        btn_1.grid(row=0, column=2, padx=5)

    def crear_widgets_t2(self, tab):
        contenido = 'Este es mi texto con el contenido'
        # Creamos el componente de scroll
        scroll = scrolledtext.ScrolledText(tab, width=50, height=10, wrap=tk.WORD)
        scroll.insert(tk.INSERT, contenido)

        # Se muestra el widget
        scroll.grid(row=0, column=0)

    def crear_widgets_t3(self, tab):
        # dataList
        datos = [x+1 for x in range(10)]
        combobox = ttk.Combobox(tab, width=15, values=datos)
        combobox.grid(row=0, column=0, padx=10, pady=10)
        # Elemento por default
        combobox.current(4)
        # Boton
        def mostrar_valor():
            messagebox.showinfo(title='Valor seleccionado', message=f'Valor seleccionado {combobox.get()}')

        btn1 = ttk.Button(tab, text='Mostrar valor seleccionado', command=mostrar_valor)
        btn1.grid(row=0, column=1)

    def crear_widgets_t4(self, tab):
        imagen = tk.PhotoImage(file='python-logo.png')

        def mostrar_titulo():
            messagebox.showinfo(title='Mas info imagen',  message= f'Nombre imagen: {imagen.cget("file")}')

        btn1 = ttk.Button(tab, image=imagen, command=mostrar_titulo)
        btn1.grid(row=0, column=0)

    def crear_widgets_t5(self, tab):
        barra_progreso = ttk.Progressbar(tab, orient='horizontal', length=550)
        barra_progreso.grid(row=0, column=0, padx=10, pady=10, columnspan=4)

        def ejecutar_barra():
            barra_progreso['maximum'] = 100
            for valor in range(101):
                sleep(0.05)

                barra_progreso['value'] = valor
                barra_progreso.update()

            barra_progreso['value'] = 0

        def ejecutar_ciclo():
            barra_progreso.start()

        def detener():
            barra_progreso.stop()

        def detener_despues():
            esperar_ms = 1000
            self.after(esperar_ms, barra_progreso.stop)
        

        btn_inicio = ttk.Button(tab, text='Ejecutar barra de progreso', command=ejecutar_barra)
        btn_inicio.grid(row=1, column=0)
        btn_ciclo = ttk.Button(tab, text='Ejecutar ciclo', command=ejecutar_ciclo)
        btn_ciclo.grid(row=1, column=1)
        btn_detener = ttk.Button(tab, text='Detener ejecucin', command=detener)
        btn_detener.grid(row=1, column=2)
        btn_despues = ttk.Button(tab, text='Detener ejecucion despues', command=detener_despues)
        btn_despues.grid(row=1, column=3)

    
if __name__ == '__main__':
    widgets = Componentes()
    widgets.mainloop()