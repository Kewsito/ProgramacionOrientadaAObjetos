from zope.interface import Interface

class ClaseInterface(Interface):
    def insertarelemento(self, posicion, elemento):
        pass

    def agregarelementofinal(self, elemento):
        pass

    def mostrarelemento(self, posicion):
        pass

