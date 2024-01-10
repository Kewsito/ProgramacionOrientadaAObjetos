

class Provincias:
    __nombre: str
    __capital: str
    __cantHabitantes: int
    __cantDep: int
    __temp: float
    __sensacionT: float
    __humedad: float

    def __init__(self, nombre, capital, cantHabitantes, cantDep, temp="", sensacionT="", humedad=""):
        self.__cantHabitantes = self.validacion(cantHabitantes, "Cantidad de habitantes es un dato requerido")
        self.__nombre = self.validacion(nombre, "Nombre es un dato requerido")
        self.__capital = self.validacion(capital, "Capital es un dato requerido")
        self.__cantDep = self.validacion(cantDep, "Cantidad de habitantes es un dato requerido")
        self.__temp = temp
        self.__sensacionT = sensacionT
        self.__humedad = humedad

    def getNombre(self):
        return self.__nombre

    def getCapital(self):
        return self.__capital

    def getCantHabitantes(self):
        return self.__cantHabitantes

    def getCantDep(self):
        return self.__cantDep

    def getTemp(self):
        return self.__temp

    def getSensacion(self):
        return self.__sensacionT

    def getHumedad(self):
        return self.__humedad

    def setTemp(self, valor):
        self.__temp = self.validacion(valor, "ERROR DE TEMP")

    def setSensacion(self, valor):
        self.__sensacionT = self.validacion(valor, "ERROR DE SENSACION")

    def setHumedad(self, valor):
        self.__humedad = self.validacion(valor, "ERROR DE HUMEDAD")

    def validacion(self, x, msj):
        if not x:
            raise ValueError(msj)
        return x

    def toJSON(self):
        d = dict(__class__=self.__class__.__name__,
                 __atributos__=dict(nombre=self.__nombre, capital=self.__capital, cantHabitantes=self.__cantHabitantes,
                                    cantDep=self.__cantDep, temp=self.__temp, sensacionT=self
                                    .__sensacionT, humedad=self.__humedad))
        return d
