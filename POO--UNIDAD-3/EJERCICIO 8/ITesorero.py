from zope.interface import Interface

class ITesorero (Interface):

    def gastosSueldoPorEmpleado (self, dni):
        pass