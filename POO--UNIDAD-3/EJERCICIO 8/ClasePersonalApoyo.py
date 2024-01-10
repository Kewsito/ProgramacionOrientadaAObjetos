from ClasePersonal import Personal
class PersonalApoyo(Personal):
    __categoria: int
    __porcentaje: float

    def __init__(self, **kwargs):
        self.__categoria = kwargs["categoria"]
        self.__porcentaje = self.obtenerPorcentaje()
        super().__init__(**kwargs)

    def __repr__(self):
        return repr(__class__)

    def getTipoAgente(self):
        return (self.__class__.__name__)

    def getCategoria(self):
        return self.__categoria

    def obtenerPorcentaje(self):
        porcentaje = 0
        if self.__categoria >= 1 or self.__categoria <= 10:
            porcentaje = 0.10
        elif self.__categoria >= 11 or self.__categoria <= 20:
            porcentaje = 0.20
        elif self.__categoria == 21 or self.__categoria == 22:
            porcentaje = 0.30
        return porcentaje

    def calculaSueldo(self):
        total = self.getSueldo()
        sueldo = total + (total * self.getAnti()/100) + (total * self.__porcentaje)
        self.setSueldo(sueldo)

    def setPorcentaje(self,por: float):
        self.__porcentaje = por


    def toJson(self):
            d = dict(
                __class__=self.__class__.__name__,
                __atributos__=dict(
                    cuil= self.getCuil(),
                    apellido= self.getApellido(),
                    nombre= self.getNombre(),
                    sueldo= self.getSueldo(),
                    anti= self.getAnti(),
                    categoria = self.__categoria
                )
            )
            return d