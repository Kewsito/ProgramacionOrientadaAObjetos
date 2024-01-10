

class Personal:
    __cuil = ""
    __apellido = ""
    __nombre = ""
    __sueldob = float
    __anti = int

    def __init__(self, **kwargs):
        self.__cuil = kwargs["cuil"]
        self.__apellido = kwargs["apellido"]
        self.__nombre = kwargs["nombre"]
        self.__sueldob = kwargs["sueldo"]
        self.__anti = kwargs["anti"]

    def getCuil(self):
        return self.__cuil

    def getApellido(self):
        return self.__apellido

    def getNombre(self):
        return self.__nombre

    def getSueldo(self):
        return self.__sueldob

    def getAnti(self):
        return self.__anti


    def __gt__(self, other):
        band = False
        if self.__apellido != other.__apellido and self.__apellido > other.__apellido:
            band = True
        if self.__apellido == other.__apellido and self.__nombre > other.__nombre:
            band = True
        return band

    #polimorfismo
    def getTipoAgente(self):
        pass

    def calculaSueldo(self):
        pass
    def setSueldo(self, valor : float):
        self.__sueldob = valor
