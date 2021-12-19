import tkinter as tk
from tkinter import messagebox

class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('400x450')
        self.resizable(0,0)
        self.title('Calculadora')
        self.iconbitmap('calculadora.ico')
        
        # Attr
        self.expresion = ''

        self.entrada = None
        self.entrada_texto = tk.StringVar()

        self._creacion_componentes()

    def _creacion_componentes(self):
        # Frame para la caja de texto
        entrada_frame = tk.Frame(self, width=400, height=50, bg='grey')
        entrada_frame.pack(side=tk.TOP)

        # Caja de texto
        entrada = tk.Entry(entrada_frame, font=('arial', 18, 'bold'), textvariable=self.entrada_texto, width=30, justify=tk.RIGHT)
        entrada.grid(row=0, column=0, ipady=10)

        # Frame para los botones
        btn_frame = tk.Frame(self, width=400, height=450, bg='grey')
        btn_frame.pack(fill='both', padx=3)

        # SEGUNDA FILA
        # Boton AC
        btn_clear = tk.Button(btn_frame, text='AC', width=13, height=3, 
                    bd=0, bg='#eee', cursor='hand2', command=self._evento_limpiar)
        btn_clear.grid(row=0, column=0, padx=1, pady=1)

        # Boton borrar
        btn_borrar = tk.Button(btn_frame, text='Borrar', width=13, height=3,
                        bd=0, bg='#eee', cursor='hand2', command=self._evento_borrar)
        btn_borrar.grid(row=0, column=1, padx=1, pady=1)

        # Boton porcentaje
        btn_porcentaje = tk.Button(btn_frame, text='%', width=13, height=3,
                            bd=0, bg='#eee', cursor='hand2', command=self._evento_porcentaje)
        btn_porcentaje.grid(row=0, column=2, pady=1, padx=1)

        # Boton dividir
        btn_dividir = tk.Button(btn_frame, text='/', width=13, height=3, 
                        bd=0, bg='#eee', cursor='hand2', command=lambda: self._evento_click('/'))
        btn_dividir.grid(row=0, column=3, pady=1, padx=1)

        # TERCERA FILA
        # Boton 7
        btn_siete = tk.Button(btn_frame, text='7', width=13, height=3, 
                    bd=0, bg='#fff', cursor='hand2', command=lambda: self._evento_click('7'))
        btn_siete.grid(row=1, column=0, padx=1, pady=1)

        # Boton 8
        btn_ocho = tk.Button(btn_frame, text='8', width=13, height=3, 
                    bd=0, bg='#fff', cursor='hand2', command=lambda: self._evento_click('8'))
        btn_ocho.grid(row=1, column=1, padx=1, pady=1)

        # Boton 9
        btn_nueve = tk.Button(btn_frame, text='9', width=13, height=3, 
                    bd=0, bg='#fff', cursor='hand2', command=lambda: self._evento_click('9'))
        btn_nueve.grid(row=1, column=2, padx=1, pady=1)

        # Boton multiplicacion
        btn_multiplicacion = tk.Button(btn_frame, text='*', width=13, height=3, 
                        bd=0, bg='#eee', cursor='hand2', command=lambda: self._evento_click('*'))
        btn_multiplicacion.grid(row=1, column=3, pady=1, padx=1)

        # CUARTA FILA
        # Boton 4
        btn_cuatro = tk.Button(btn_frame, text='4', width=13, height=3, 
                    bd=0, bg='#fff', cursor='hand2', command=lambda: self._evento_click('4'))
        btn_cuatro.grid(row=2, column=0, padx=1, pady=1)

        # Boton 5
        btn_cinco = tk.Button(btn_frame, text='5', width=13, height=3, 
                    bd=0, bg='#fff', cursor='hand2', command=lambda: self._evento_click('5'))
        btn_cinco.grid(row=2, column=1, padx=1, pady=1)

        # Boton 6
        btn_seis = tk.Button(btn_frame, text='6', width=13, height=3, 
                    bd=0, bg='#fff', cursor='hand2', command=lambda: self._evento_click('6'))
        btn_seis.grid(row=2, column=2, padx=1, pady=1)

        # Boton resta
        btn_resta = tk.Button(btn_frame, text='-', width=13, height=3, 
                        bd=0, bg='#eee', cursor='hand2', command=lambda: self._evento_click('-'))
        btn_resta.grid(row=2, column=3, pady=1, padx=1)

        # CUARTA FILA
        # Boton 1
        btn_uno = tk.Button(btn_frame, text='1', width=13, height=3, 
                    bd=0, bg='#fff', cursor='hand2', command=lambda: self._evento_click('1'))
        btn_uno.grid(row=3, column=0, padx=1, pady=1)

        # Boton 2
        btn_dos = tk.Button(btn_frame, text='2', width=13, height=3, 
                    bd=0, bg='#fff', cursor='hand2', command=lambda: self._evento_click('2'))
        btn_dos.grid(row=3, column=1, padx=1, pady=1)

        # Boton 3
        btn_tres = tk.Button(btn_frame, text='3', width=13, height=3, 
                    bd=0, bg='#fff', cursor='hand2', command=lambda: self._evento_click('3'))
        btn_tres.grid(row=3, column=2, padx=1, pady=1)

        # Boton suma
        btn_suma = tk.Button(btn_frame, text='+', width=13, height=3, 
                        bd=0, bg='#eee', cursor='hand2', command=lambda: self._evento_click('+'))
        btn_suma.grid(row=3, column=3, pady=1, padx=1)

        # QUINTA FILA
        # Boton 0
        btn_cero = tk.Button(btn_frame, text='0', width=27, height=3, 
                    bd=0, bg='#fff', cursor='hand2', command=lambda: self._evento_click('0'))
        btn_cero.grid(row=4, column=0, padx=1, pady=1, columnspan=2)

        # Boton .
        btn_decimal = tk.Button(btn_frame, text='.', width=13, height=3, 
                    bd=0, bg='#eee', cursor='hand2', command=lambda: self._evento_click('.'))
        btn_decimal.grid(row=4, column=2, padx=1, pady=1)

        # Boton igual
        btn_igual = tk.Button(btn_frame, text='=', width=13, height=3, 
                    bd=0, bg='#eee', cursor='hand2', command=self._evento_evaluar)
        btn_igual.grid(row=4, column=3, padx=1, pady=1)

    def _evento_limpiar(self):
        self.expresion = ''
        self.entrada_texto.set(self.expresion)

    def _evento_borrar(self):
        self.expresion = self.entrada_texto.get()[:-1] 
        self.entrada_texto.set(self.expresion)

    def _evento_porcentaje(self):
        pass
    
    def _evento_click(self, elemento):
        self.expresion = f'{self.expresion}{elemento}'
        self.entrada_texto.set(self.expresion)

    def _evento_evaluar(self):
        try:
            if self.expresion:
                resultado = str(eval(self.expresion))
                self.entrada_texto.set(resultado)
        except Exception as e:
            messagebox.showerror('Error', f'Ocurrio un error: {e}')
            self.entrada_texto.set('') 
            self.expresion = ''

if __name__ == '__main__':
    calculadora = Calculadora()
    calculadora.mainloop()