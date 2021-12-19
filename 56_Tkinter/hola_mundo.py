# GUI - Graphical User Interface
# Tkinter
import tkinter as tk
from tkinter import ttk

# Se crea un objeto usando la clase tk
ventana = tk.Tk()

# Tamaño de ventana
ventana.geometry('600x400')

# Nombre de la ventana
ventana.title('Ventana')

# Establecer icono de la aplcacionn
ventana.iconbitmap('icono.ico')

# Metodo evento_click
def evento_click():
    btn1.config(text='Boton presionado')
    print('Ejucucion del evento_click')
    # Se crea un nuevo componente
    btn2 = ttk.Button(ventana, text='Nuevo boton')
    btn2.pack()

# Creacion de boton (widget)
# El obj padre es la ventana
btn1 = ttk.Button(ventana, text='Dar Click', command=evento_click)

# Pack layout manager (para mostrar el btn en la ventana)
btn1.pack()

# Se imprime la ventana (solo al final)
ventana.mainloop()