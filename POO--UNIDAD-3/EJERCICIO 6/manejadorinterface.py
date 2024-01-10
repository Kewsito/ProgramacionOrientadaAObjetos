from ClaseInterface import ClaseInterface
from ClaseLista import Lista
from ObjectEncoder import ObjectEncoder

class ManejadorInterface:
    __controlEncoder: ObjectEncoder

    def __init__(self):
        self.__controlEncoder = ObjectEncoder()

    def invocarinter(self, clista: ClaseInterface, op):

        if op == 1:
            pos = int(input("Ingrese la posicion: "))
            tipo = input("Ingrese un tipo de aparato: ")
            objeto = self.__controlEncoder.retornarobjeto(tipo) #obtengo el objeto
            if objeto is not None:
                clista.insertarelemento(pos, objeto) #interfaz de insertar en cualquier posicion
            else:
                print("El elemento a insertar no es un objeto")

        if op == 2:
            tipo = input("Ingrese un tipo de aparato: ")
            objeto = self.__controlEncoder.retornarobjeto(tipo) #obtengo el objeto
            if objeto is not None:
                clista.agregarelementofinal(objeto) #interfaz de agregaralfinal
            else:
                print("El elemento a insertar no es un objeto")

        if op == 3:
            pos = int(input("Ingrese una posicion de la lista: "))
            dato = clista.mostrarelemento(pos) #interfaz de mostrar
            if dato is not None:
                print(repr(dato))
            else:
                print("Posicion incorrecta")

    def llamarinterfaces(self, claselista,op):
        self.invocarinter(ClaseInterface(claselista), op)
