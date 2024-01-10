from ClasePersonal import Personal
class Docente(Personal):
    __carrera: str
    __cargo: str
    __catedra: str
    __porcentaje: float

    def __init__(self, **kwargs):
        self.__carrera = kwargs["carrera"]
        self.__cargo = kwargs["cargo"]
        self.__catedra = kwargs["catedra"]
        self.__porcentaje = self.obtenerPorcentaje()
        super().__init__(**kwargs)


    def getTipoAgente(self):
        return (self.__class__.__name__)

    def getCarrera(self):
        return self.__carrera

    def getCargo(self):
        return self.__cargo

    def getCatedra(self):
        return self.__catedra

    def obtenerPorcentaje(self):
        porcent = 0
        if self.__cargo == "simple":
            porcent = 0.10
        elif self.__cargo == "semiexclusivo":
            porcent = 0.20
        elif self.__cargo == "exclusivo":
            porcent = 0.30
        return porcent

    def calculaSueldo(self):
        sueldo = self.getSueldo()
        total = sueldo + (sueldo * self.getAnti() / 100) + (sueldo * self.__porcentaje)
        self.setSueldo(total)

    def setPorcentaje(self,por: float):
        self.__porcentaje = por

    def getSueldoDocente(self):
        self.calculaSueldo()
        return self.getSueldo()

    def toJson(self):
            d = dict(
                __class__=self.__class__.__name__,
                __atributos__=dict(
                    cuil= self.getCuil(),
                    apellido= self.getApellido(),
                    nombre= self.getNombre(),
                    sueldo= self.getSueldo(),
                    anti= self.getAnti(),
                    carrera = self.__carrera,
                    cargo = self.__cargo,
                    catedra = self.__catedra,
                )
            )
            return d
