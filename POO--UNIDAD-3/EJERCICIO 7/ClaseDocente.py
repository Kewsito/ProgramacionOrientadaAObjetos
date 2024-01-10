from ClasePersonal import Personal

class Docente(Personal):
    __carrera = ""
    __cargo = ""
    __catedra = ""

    def __init__(self, **kwargs):
        self.__carrera = kwargs["carrera"]
        self.__cargo = kwargs["cargo"]
        self.__catedra = kwargs["catedra"]
        super().__init__(**kwargs)

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

    def getCarrera(self):
        return self.__carrera

    def getCargo(self):
        return self.__cargo

    def getCatedra(self):
        return self.__catedra

    def getTipoAgente(self):
        return self.__class__.__name__

    def calculaSueldo(self):
        total = self.getSueldo()
        total = total + (total*self.getAnti()/100)
        if self.__cargo == "simple":
            total = total + (total*0.10)
        elif self.__cargo == "semiexclusivo":
            total = total + (total*0.20)
        elif self.__cargo == "exclusivo":
            total = total + (total*0.30)
        self.setSueldo(total)

    def getSueldoDocente(self):
        return self.getSueldo()
