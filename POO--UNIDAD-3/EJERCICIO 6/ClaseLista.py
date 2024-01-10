from ClaseHeladera import Heladera
from ClaseLavarropas import Lavarropas
from ClaseTelevisor import Televisor
from ClaseNodo import Nodo
from zope.interface import implementer
from Interfaz import Interfaz


@implementer(Interfaz)
class Lista:
    __comienzo: None
    __actual: None
    __ind: None
    __tope: None

    def __init__(self):
        self.__comienzo = None
        self.__actual = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            valor = self.__actual.getvalor()
            self.__actual = self.__actual.getsiguiente()
            return valor

    def agregarAparato(self, aparato):
        nodo = Nodo(aparato)
        nodo.setsiguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__actual = nodo
        self.__tope += 1
        print("Tope: {}".format(self.__tope))

    #INTERFACES

    def InsElem(self, pos, obj):
        cont = 1
        cabeza = self.__comienzo
        if self.__comienzo is None:
            nodo = Nodo(obj)
            nodo.setsiguiente(self.__comienzo)
            self.__comienzo = Nodo
            self.__actual = Nodo
            self.__tope += 1
        while cont < pos and cabeza is not None:
            cont += 1
            cabeza = cabeza.getsiguiente()
        if pos == 1:
            nuevonodo = Nodo(obj)
            nuevonodo.setsiguiente(cabeza)
            self.__comienzo = nuevonodo
            self.__actual = nuevonodo
        else:
            nuevonodo = Nodo(obj)
            nuevonodo.setsiguiente(cabeza.getSiguiente())
            cabeza.setSiguiente(nuevonodo)
        self.__tope += 1

    def AgrElem(self, obj):
        print("Insertando al final")
        if self.__comienzo is None:
            nuevonodo = Nodo(obj)
            nuevonodo.setsiguiente(self.__comienzo)
            self.__comienzo = nuevonodo
            self.__actual = nuevonodo
        else:
            cabeza = self.__comienzo
            while cabeza.getsiguiente() is not None:
                cabeza = cabeza.getsiguiente()
            nuevonodo = Nodo(obj)
            cabeza.setSiguiente(nuevonodo)
        self.__tope += 1

    def mostrarelemento(self, pos):
        dato = None
        cont = 1
        if self.__comienzo is None and pos != 1:
            dato = None
        cabeza = self.__comienzo
        while cabeza.getSiguiente() is not None and cont < pos:
            cont += 1
            cabeza = cabeza.getSiguiente()
        if cont == pos:
            dato = cabeza.getDato()

        return dato

    #FUNCIONALIDADES
    def mostrarcant(self):
        cantL=0
        cantH=0
        cantT=0
        cabeza = self.__comienzo
        while cabeza is not None:
            if type(cabeza.getDato()) is Heladera and cabeza.getDato().getmar() == "Phillips":
                cantH += 1
            elif type(cabeza.getDato()) is Lavarropas and cabeza.getDato().getmar() == "Phillips":
                cantL += 1
            elif type(cabeza.getDato()) is Televisor and cabeza.getDato().getmar() == "Phillips":
                cantT += 1
            cabeza = cabeza.getsiguiente()
        print("Cantidad de Heladeras Phillips: {}".format(cantH))
        print("Cantidad de Lavarropas Phillips: {}".format(cantL))
        print("Cantidad de Televisores Phillips: {}".format(cantT))

    def mostrarcarga(self):
        cabeza=self.__comienzo
        while cabeza is not None:
            print("Aparatos de la Empresa")
            print("Marca: {} Pais de Fabricacion: {} Importe de venta: {} ".format(cabeza.getDato().getmar(),cabeza.getDato().getpais(),cabeza.getDato().getimp()))
            cabeza = cabeza.getsiguiente()

    def guardarjson(self, ObjectEncoder):
        lista = []
        cabeza = self.__comienzo
        while cabeza is not None:
            dato = cabeza.getDato()
            dicc = dato.toJson()
            lista.append(dicc)
            cabeza = cabeza.getsiguiente()
        ObjectEncoder.guardarjsonarch(lista,"nuevosaparatos.json")
        print("Archivo JSON creado correctamente!")
