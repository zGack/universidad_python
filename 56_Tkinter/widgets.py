import sys
import tkinter as tk
from tkinter import READABLE, Menu, messagebox, ttk
from tkinter.constants import CENTER, DISABLED

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejo de Grid')
ventana.iconbitmap('icono.ico')

# Etiqueta (label)
label1 = tk.Label(ventana, text='Etiqueta 1')
label1.grid(row=1, column=0, columnspan=2)

# Variable que se modifca posteriormente (set) (get) 
entry_var = tk.StringVar(value='Valor por default')

entry1 = ttk.Entry(ventana, width=30, textvariable=entry_var)
entry2 = ttk.Entry(ventana, width=30, justify=CENTER, show='*')
entry1.grid(row=0, column=0)
#entry2.grid(row=1, column=0)

# Insert 
#entry1.insert(0, 'Cromatica')
entry2.insert(0, 'Escriba su contraseña')
entry2.insert(tk.END,': ')

# Config
#entry1.config(state='readonly')

def enviar():
    # Obtener contenido
    # print(entry1.get())
    # btn1.config(text=entry_var.get())

    # Modificacion usando la variable de texto y el metodo set
    #entry_var.set('Cambio...')

    # Modificar el texto del label
    label1.config(text=entry_var.get())

    # Obtener contenido
    print(entry_var.get())

    # Seleccionar contenido
    # entry1.select_range(0, tk.END)
    # entry1.focus()

    # Eliminar contenido
    #entry1.delete(0, tk.END)

    # Ventana de alerta
    msg = entry_var.get()
    if msg:
        messagebox.showinfo('Mensaje Informativo', 'Menssaje informativo ' + msg)
        # messagebox.showwarning('Mensaje Informativo', 'Menssaje de alerta ' + msg)
        # messagebox.showerror('Mensaje Informativo', 'Menssaje de error ' + msg)

def salir():
    ventana.quit()
    ventana.destroy()
    sys.exit()

def crear_menu():
    # Configurar el menu principal 
    menu_princial = Menu(ventana)

    # tearoff = False
    submenu_archivo = Menu(menu_princial, tearoff=False)
    submenu_ayuda = Menu(menu_princial, tearoff=False)

    # Agregar opcion
    submenu_archivo.add_command(label='Nuevo')
    submenu_ayuda.add_command(label='Acerca de')

    # Separador
    submenu_archivo.add_separator()

    # Opcion salir
    submenu_archivo.add_command(label='Salir', command=salir)

    # Se agrega el submenu al principal
    menu_princial.add_cascade(menu=submenu_archivo, label='Archivo')
    menu_princial.add_cascade(menu=submenu_ayuda, label='Ayuda')
    
    # Se muestra el menu en la ventana princial
    ventana.config(menu=menu_princial)

# Boton
btn1 = ttk.Button(ventana, text='Enviar', command=enviar)
btn1.grid(row=0, column=1)

crear_menu()
ventana.mainloop()