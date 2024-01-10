from ClasePersonal import Personal

class PersonalApoyo(Personal):
    __categoria = ""

    def __init__(self, **kwargs):
        self.__categoria = int(kwargs["categoria"])
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
                    categoria = self.__categoria
                )
            )
        return d

    def getCategoria(self):
        return self.__categoria

    def calculaSueldo(self):
        total = self.getSueldo()
        total = total + (total*self.getAnti()/100)
        if self.__categoria >= 1 or self.__categoria <= 10:
            total = total + (total*0.10)
        elif self.__categoria >= 11 or self.__categoria <= 20:
            total = total + (total*0.20)
        elif self.__categoria == 21 or self.__categoria == 22:
            total = total + (total*0.30)
        self.setSueldo(total)

    def getTipoAgente(self):
        return self.__class__.__name__
