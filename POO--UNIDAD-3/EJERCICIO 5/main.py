from zope.interface import Interface


class Interfaz(Interface):
    def insertarElem(self, objeto):
        pass

    def agregarElem(self, elemento):
        pass

    def mostrarElem(self, pos):
        pass
