class calefactor:
    __marca: str
    __modelo: str

    def __init__(self, mar, mod):
        self.__marca = mar
        self.__modelo = mod

    def getmar(self):
        return self.__marca

    def getmod(self):
        return self.__modelo
