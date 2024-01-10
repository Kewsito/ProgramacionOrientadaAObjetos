from ClaseDocente import Docente
from ClaseInvestigador import Investigador
class DocenteInvestigador(Docente,Investigador):
    __progIncen: str
    __importeEx: float

    def __init__(self, **kwargs):
        self.__progIncen = kwargs["programa"]
        self.__importeEx = kwargs["importe"]
        super().__init__(**kwargs)

    def getTipoAgente(self):
        return (self.__class__.__name__)

    def getIncentivo(self):
        return self.__progIncen

    def getImporteEx(self):
        return self.__importeEx

    def calculaSueldo(self):
        total = self.getSueldoDocente()
        total += self.__importeEx
        self.setSueldo(total)

    def setImporteExtr(self,valor : float):
        self.__importeEx = valor

    def toJson(self):
            d = dict(
                __class__=self.__class__.__name__,
                __atributos__=dict(
                    cuil= self.getCuil(),
                    apellido= self.getApellido(),
                    nombre= self.getNombre(),
                    sueldo= self.getSueldo(),
                    anti= self.getAnti(),
                    carrera = self.getCarrera(),
                    cargo = self.getCargo(),
                    catedra = self.getCatedra(),
                    area = self.getArea(),
                    tipo = self.getTipo(),
                    programa = self.__progIncen,
                    importe = self.__importeEx
                )
            )
            return d