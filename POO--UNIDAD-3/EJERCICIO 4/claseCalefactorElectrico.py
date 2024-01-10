from ClaseCalefactor import calefactor


class calefactorelectrico(calefactor):
    __potencia: int

    def __init__(self, mar, mod, po):
        self.__potencia = int(po)
        super().__init__(mar, mod)

    def __str__(self):
        return ("Calefactor electrico: \n\t Marca: {} Modelo: {} Potencia: {}".format(super().getmar(),super().getmod(),self.__potencia))

    def getpot(self):
        return self.__potencia

    def setcalefactorE(self):
        cadena = "Calefactor Electrico"
        return cadena
