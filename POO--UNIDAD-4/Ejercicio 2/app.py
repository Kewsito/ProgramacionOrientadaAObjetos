from tkinter import *
from tkinter import ttk, messagebox
import tkinter


class Aplicacion():
    __ventana = None
    __precioBase = None
    __resultado = None

    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.title("Calculo de IVA")
        self.__ventana.geometry("425x150")
        self.__precioBase = StringVar()
        self.__resultado = StringVar()
        self.valor= tkinter.IntVar()
        self.__iva= StringVar()
        mainframe = ttk.Frame(self.__ventana, padding="5 2 5 2")

        mainframe.grid(column=0, row=0, sticky=(N, W, E, S), columnspan=10)
        mainframe.columnconfigure(0, weight=2)
        mainframe.rowconfigure(0, weight=2)
        mainframe['borderwidth']= 2
        mainframe['relief']= 'sunken'
        ttk.Label(mainframe, text= 'Precio sin IVA').grid(column=0, row= 1)
        self.precio= ttk.Entry(mainframe, textvariable=self.__precioBase, width=20)
        self.precio.grid(column=1, row=1, sticky=W, columnspan=1)

        #Radio button
        ttk.Radiobutton(mainframe, text= 'IVA 21%', value=0, variable= self.valor).grid(column=1, row=2, columnspan=1, sticky=W)
        ttk.Radiobutton(mainframe, text= 'IVA 10.5%', value=1, variable= self.valor).grid(column=1, row=3, columnspan=1, sticky=W)

        ttk.Label(mainframe, text= 'IVA').grid(column=0, row= 4)
        self.iva= ttk.Label(mainframe, textvariable=self.__iva, width=20)
        self.iva.grid(column=1, row=4, sticky=W, columnspan=3)

        ttk.Label(mainframe, text= 'Precio con IVA').grid(column=0, row= 5)
        self.resultado= ttk.Label(mainframe, textvariable=self.__resultado, width=20)
        self.resultado.grid(column=1, row=5, sticky=W, columnspan=3)

        self.botonC= ttk.Button(mainframe, text= 'Calcular', command= self.calculariva)
        self.botonC.grid(row=6, column= 1)
        self.botonS= ttk.Button(mainframe, text= 'Salir', command= self.__ventana.destroy)
        self.botonS.grid(row=6, column= 2)

        self.valor.set(-1)
        self.__ventana.mainloop()

    def calculariva(self, *args):
        a= float(self.precio.get())
        if a!='':
            try:
                if self.valor.get()== 0:
                    #a= a*1.21 sirve para calcular el porcentaje con suma
                    b= a*(21/100)
                    a+= (a*0.21)
                    self.__iva.set(b)
                    self.__resultado.set(a)
                
                elif self.valor.get()== 1:
                    b= a*0.105
                    a+= a*0.105
                    self.__iva.set(b)
                    self.__resultado.set(a)
            except ValueError:
                messagebox.showerror(title='Error', message='Debe ingresar precio Base')
                self.__precioBase.set('')
                self.precio.focus()
        else:
            self.__precioBase.set('')




if __name__ == "__main__":
    app = Aplicacion()