from zope.interface import Interface
class Interfaz(Interface):
    def insertarElemento(self,pos,objeto):
        pass

    def insertarFinal(self,objeto):
        pass

    def tipodeObjeto(self, pos):
        pass