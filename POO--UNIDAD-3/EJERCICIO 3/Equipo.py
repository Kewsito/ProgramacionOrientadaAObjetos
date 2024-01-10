class Equipo:
    __nombre = None
    __ciudad = None

    def __init__(self, nom, ciu):
        self.__nombre = nom
        self.__ciudad = ciu
        self.__cantidad = 0

    def __str__(self):
        return "Nombre:{} Ciudad:{}".format(self.__nombre,self.__ciudad)

    def setcantidad(self, cantidad):
        self.__cantidad = cantidad

    def getnombre(self):
        return self.__nombre

    def getciudad(self):
        return self.__ciudad

    def getcantidad(self):
        return self.__cantidad
