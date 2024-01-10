from tkinter import *
from tkinter import ttk, messagebox


class Aplicacion():
    __ventana = None
    __altura = None
    __peso = None
    __resultado = None
    __tippeso = None

    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.title("CALCULADORA DE IMC")
        self.__ventana.geometry("425x150")
        self.__altura = StringVar()
        self.__peso = StringVar()
        self.__tippeso = StringVar()
        self.__resultado = StringVar()
        mainframe = ttk.Frame(self.__ventana, padding="5 2 5 2")

        # CONFIGURACION FILA 1
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S), columnspan=3)
        mainframe.columnconfigure(0, weight=2)
        mainframe.rowconfigure(0, weight=2)
        mainframe['borderwidth'] = 2
        mainframe['relief'] = 'sunken'
        ttk.Label(mainframe, text='ALTURA: ').grid(column=0, row=1)
        self.altura = ttk.Entry(mainframe, textvariable=self.__altura, width=30)
        self.altura.grid(column=1, row=1, sticky=W, columnspan=3)
        ttk.Label(mainframe, text='m').grid(column=2, row=1, sticky=W)

        # CONFIGURACION FILA 2

        ttk.Label(mainframe, text="PESO:").grid(column=0, row=3)
        self.peso = ttk.Entry(mainframe, textvariable=self.__peso, width=30)
        self.peso.grid(column=1, row=3, sticky=W)
        ttk.Label(mainframe, text='kg').grid(column=2, row=3, sticky=W)

        # CONFIGURACION BOTONES

        self.boton1 = ttk.Button(mainframe, text="CALCULAR", command=self.calcular)
        self.boton1.grid(row=6, column=0)
        self.boton2 = ttk.Button(mainframe, text="LIMPIAR", command=self.limpiar)
        self.boton2.grid(row=6, column=1)

        # CONFIGURACION RESULTADOS

        ttk.Label(mainframe, text="TU INDICE CORPORAL (IMC) es:").grid(row=8, column=0)
        ttk.Label(mainframe, textvariable=self.__resultado).grid(row=8, column=1)
        ttk.Label(mainframe, text="Kg/m").grid(row=8, column=2)
        ttk.Label(mainframe, textvariable=self.__tippeso).grid(row=9, column=1)
        self.__ventana.mainloop()

    def calcular(self, *args):
        a = float(self.altura.get())
        b = float(self.peso.get())
        if a != '' and b != '':
            try:
                valor = float(b / a)
                if valor < 18.5:
                    self.__resultado.set(valor)
                    self.__tippeso.set("Peso inferior al normal")
                elif 18.5 < valor < 24.9:
                    self.__resultado.set(valor)
                    self.__tippeso.set("NORMAL")
                elif 25 < valor < 29.9:
                    self.__resultado.set(valor)
                    self.__tippeso.set("PESO SUPERIOR AL NORMAL")
                elif valor > 30:
                    self.__resultado.set(valor)
                    self.__tippeso.set("OBESIDAD")
            except ValueError:
                messagebox.showerror(title="Error de tipo", message="Debe ingresar un valor numerico")
                self.__altura.set('')
                self.__peso.set('')
                self.altura.focus()
        else:
            self.__altura.set('')
            self.__peso.set('')

    def limpiar(self):
        self.__altura.set("")
        self.__peso.set('')
        self.__tippeso.set('')
        self.__resultado.set("")
        self.altura.focus()


if __name__ == "__main__":
    app = Aplicacion()
