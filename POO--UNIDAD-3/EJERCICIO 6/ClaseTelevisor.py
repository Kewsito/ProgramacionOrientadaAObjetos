from ClaseAparatos import Aparatos


class Televisor(Aparatos):
    __tipopan: str
    __pulgadas: float
    __tipodedef: str
    __conexionint: bool

    def __init__(self, mar, mod, col, pais, pre, tippan, pulg, tipodedef, conexionint):
        self.__tipodedef = str(tipodedef)
        self.__conexionint = bool(conexionint)
        self.__pulgadas = float(pulg)
        self.__tipopan = str(tippan)
        super().__init__(mar, mod, col, pais, pre, tippan, pulg, tipodedef, conexionint)

    def __str__(self):
        return ("Aparato: Televisor \n\t Marca: {} Modelo: {} Color: {} Pais de Fabricacion: {} Precio Base: {} Tipo de Pantalla: {} Pulgadas: {} Tipo de definicion: {} Conexion a Internet: {}".format(super().getmar(),super().getmod(),super().getcol(),super().getpais(),super().getpreciob(),
                self.__tipopan, self.__pulgadas, self.__tipodedef, self.__conexionint))

    def gettdef(self):
        return self.__tipodedef

    def getconexion(self):
        return self.__conexionint

    def getpulg(self):
        return self.__pulgadas

    def gettipopan(self):
        return self.__tipopan

    def gettipo(self):
        return ("Televisor")

    def toJson(self):
        d = dict(__class__=self.__class__.__name__, __atributos__=dict(
            mar=self.getmar(), mod=self.getmod(), col=self.getcol(), pais=self.getpais(), pre=self.getpreciob(),
            tippan=self.__tipopan, pulg=self.__pulgadas, tipodedef=self.__tipodedef, conexionint=self.__conexionint
        )
                 )
        return d
