from flores import flores


class ramos:
    __tam: str
    __flores: list[flores]

    def __init__(self, tam):
        self.__tam = tam
        self.__flores = []

    def gettamaño(self):
        return self.__tam

    def agregarflor(self, obj):
        self.__flores.append(obj)
