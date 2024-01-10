class Aparatos:
    __marca: str
    __modelo: str
    __color: str
    __pais: str
    __preciob: float

    def __init__(self,mar,mod,col,pais,pre):
        self.__pais=str(pais)
        self.__preciob=float(pre)
        self.__color=str(col)
        self.__marca=str(mar)
        self.__modelo=str(mod)

    def __str__(self):
        return ("Marca: {} Modelo: {} Color: {} Pais: {} Precio Base: {}".format(self.__marca, self.__modelo, self.__color, self.__pais, self.__preciob))

    def getmar(self):
        return self.__marca

    def getmod(self):
        return self.__modelo

    def getcol(self):
        return self.__color

    def getpais(self):
        return self.__pais

    def getpreciob(self):
        return self.__preciob
