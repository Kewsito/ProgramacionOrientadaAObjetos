from tkinter import *
from tkinter import ttk, messagebox, Tk
import json
from numpy import double
import requests


class Aplicacion():
    __ventana = None
    __dolar = None
    __resultado = None
    __conversor = None

    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.title("Conversor de Moneda")
        self.__ventana.geometry("300x150")
        self.__resultado = StringVar()
        self.__dolar = DoubleVar()
        self.__conversor = DoubleVar()
        self.__dolar.trace('w', self.calculo)

        mainframe = ttk.Frame(self.__ventana, padding="5 2 5 2")

        mainframe.grid(column=0, row=0, sticky=(N, W, E, S), columnspan=10)
        mainframe.columnconfigure(0, weight=2)
        mainframe.rowconfigure(0, weight=2)
        mainframe['borderwidth'] = 2
        mainframe['relief'] = 'sunken'

        ttk.Label(mainframe, text='Dolares').grid(column=2, row=1, sticky=W)

        self.dolar = ttk.Entry(mainframe, textvariable=self.__dolar, width=10)
        self.dolar.grid(column=1, row=1, sticky=(W))  # type:ignore

        ttk.Label(mainframe, text='Es equivalente a ').grid(column=0, row=2)
        self.resultado = ttk.Label(mainframe, textvariable=self.__resultado).grid(column=1, row=2,
                                                                                  sticky=(W))  # type:ignore
        ttk.Label(mainframe, text='pesos').grid(column=2, row=2)

        self.botonS = ttk.Button(mainframe, text='Salir', command=self.__ventana.destroy).grid(row=3, column=1)
        self.run()
        self.__ventana.mainloop()

    def run(self):
        response = requests.get('https://www.dolarsi.com/api/api.php?type=dolar')
        data = response.json()
        i = 0
        b = False
        while i < len(data) and b == False:
            if data[i]['casa']['nombre'] == 'Oficial':
                b = True
                self.__conversor = float(data[i]['casa']['venta'].replace(',', '.'))

            i += 1

    def calculo(self, *args):
        a = self.dolar.get()
        if a != '':
            try:
                valor = float(self.dolar.get())
                print(self.__conversor)
                self.__resultado.set(float(valor) * float(self.__conversor))
            except ValueError:
                messagebox.showerror('Error', 'Debe ingresar un valor numerico')
                self.__dolar.set('')
                self.dolar.focus()
        else:
            self.__resultado.set(0.0)


if __name__ == "__main__":
    app = Aplicacion()
