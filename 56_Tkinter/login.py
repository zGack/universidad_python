import tkinter as tk
from tkinter import ttk, messagebox

class Login(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('300x130')
        self.title('Login')
        self.resizable(0, 0)
        # Grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        self._user_var = tk.StringVar()
        self._passw_var = tk.StringVar()


        self._crear_widgets()

    # Definir el metodo crear _comonentes
    def _crear_widgets(self):
        # Widgets
        user_label = ttk.Label(self, text='Usuario:')
        passw_label = ttk.Label(self, text='Password:')

        user_entry = ttk.Entry(self, width=30, textvariable=self._user_var)
        passw_entry = ttk.Entry(self, width=30, show='*', textvariable=self._passw_var)

        login_btn = ttk.Button(self, text='Login', command=self._login)

        user_label.grid(row=0, column=0, sticky='e', padx=5, pady=5)
        user_entry.grid(row=0, column=1, pady=5, sticky='w', padx=5)

        passw_label.grid(row=1, column=0, sticky='e', padx=5, pady=5)
        passw_entry.grid(row=1, column=1, pady=5, sticky='w', padx=5)

        login_btn.grid(row=2, column=0, columnspan=2)


    def _login(self):
        usuario = self._user_var.get()
        password = self._passw_var.get()

        if usuario and password:
            messagebox.showinfo(title='Datos Login', message=f'Usuario: {usuario}, Password: {password}')
            self._user_var = ''
            self._passw_var = ''



if __name__ == '__main__':
    login = Login()    
    login.mainloop()