from ClaseAparatos import Aparatos


class Lavarropas(Aparatos):
    __capLav: str
    __vel: int
    __cantProg: int
    __tipodeCarga: str

    def __init__(self, mar, mod, col, pais, pre, cap, vel, cant, tipc):
        self.__capLav = str(cap)
        self.__vel = int(vel)
        self.__cantProg = int(cant)
        self.__tipodeCarga = str(tipc)
        super().__init__(mar, mod, col, pais, pre)

    def __str__(self):
        return (
            "Aparato: Lavarropas \n\t Marca: {} Modelo: {} Color: {} Pais de Fabricacion: {} Precio Base: {} Capacidad de Lavado: {} Velocidad de Centrifugado {} Cantidad de programas: {} Tipo de Carga: {}".format(
                super().getmar(), super().getmod(), super().getcol(), super().getpais(), super().getpreciob(),
                self.__capLav, self.__vel, self.__cantProg, self.__tipodeCarga))

    def getcaplav(self):
        return self.__capLav

    def getvel(self):
        return self.__vel

    def getcantProg(self):
        return self.__cantProg

    def gettipodeCarga(self):
        return self.__tipodeCarga

    def gettipoL(self):
        return "Lavarropas"

    def toJson(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(mar=self.getmar(), mod=self.getmod(), col=self.getmod(), pais=self.getpais(),
                               pre=self.getpreciob(), cap=self.__capLav, vel=self.__vel, cant=self.__cantProg,
                               tipc=self.__tipodeCarga,
                               )
        )
        return d
