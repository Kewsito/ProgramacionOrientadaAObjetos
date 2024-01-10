from ClaseCalefactor import calefactor

class CalefactorAGas(calefactor):
    __matricula:str
    __calorias:int

    def __init__(self,mar,mod,matr,calorias):
        self.__calorias=int(calorias)
        self.__matricula=str(matr)
        super().__init__(mar,mod)

    def __str__(self):
        return ("Calefactor a Gas: \n\t Marca: {} Modelo: {} Matricula: {} Calorias: {}".format(super().getmar(),super().getmod(),self.__matricula,self.__calorias))

    def getmatricula(self):
        return self.__matricula

    def getcalorias(self):
        return self.__calorias

    def setcalefactorG(self):
        cadena="Calefactor a Gas"
        return cadena

