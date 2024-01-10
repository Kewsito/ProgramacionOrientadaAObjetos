from ClaseAparatos import Aparatos


class Heladera(Aparatos):
    __caplit: int
    __freezer: bool
    __ciclica: bool

    def __init__(self, mar, mod, col, pais, pre, cap, fre, cicli):
        self.__ciclica = bool(cicli)
        self.__freezer = bool(fre)
        self.__caplit = int(cap)
        super().__init__(mar, mod, col, pais, pre)

    def __str__(self):
        return (
            "Aparato: Heladera \n\t Marca: {} Modelo: {} Color: {} Pais de Fabricacion: {} Precio Base: {} Capacidad en Litros: {} Freezer: {} Ciclica: {}".format(
                super().getmar(), super().getmod(), super().getcol(), super().getpais(), super().getpreciob(),
                self.__caplit, self.__freezer, self.__ciclica))

    def getfre(self):
        return self.__freezer

    def getciclica(self):
        return self.__ciclica

    def getcaplit(self):
        return self.__caplit

    def gettipoH(self):
        return "Heladera"

    def toJson(self):
        d = dict(
            __class=self.__class__.__name__, __atributos__=dict(
                mar=self.getmar(), mod=self.getmod(), col=self.getcol(), pais=self.getpais(), pre=self.getpreciob(),
                cap=self.__caplit, fre=self.__freezer, cicli=self.__ciclica,
            )
        )
        return d
