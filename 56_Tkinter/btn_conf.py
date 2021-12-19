import tkinter as tk
from tkinter import ttk
from tkinter.constants import COMMAND

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejo de Grid')
ventana.iconbitmap('icono.ico')

# Configuracion Grid
ventana.rowconfigure(0, weight=1)
ventana.rowconfigure(1, weight=5)
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=5)

# Metodos de los eventos
def evento_1():
    btn1.config(text='Boton 1 presionado')

def evento_2():
    btn2.config(text='Boton 2 presionado')

def evento_4():
    btn4.config(text='Boton 4 presionado', fg='blue', relief=tk.GROOVE, bg='yellow')

# Botonees
btn1 = ttk.Button(ventana, text='Boton1', command=evento_1)
# PADX - PADY = MARGIN | IPADX - IPADY
btn1.grid(row=0, column=0, sticky='NSWE', padx=40, pady=30, ipady=50, columnspan=2)

# N, E, S, W
btn2 = ttk.Button(ventana, text='Boton 2', command=evento_2)
btn2.grid(row=1, column=0, sticky='NSWE')

btn3 = ttk.Button(ventana, text='Boton 3')
#btn3.grid(row=0, column=1, sticky='NSWE')

btn4 = tk.Button(ventana, text='Boton 4', command=evento_4)
btn4.grid(row=1, column=1, sticky='NSWE')

ventana.mainloop()