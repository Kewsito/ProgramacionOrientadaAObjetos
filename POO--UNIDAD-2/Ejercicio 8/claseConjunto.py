class Conjunto:
    __lista=list

    def __init__(self, lista):
        self.__lista=lista

    def __str__(self):
        return str(self.__lista)

    def __add__(self, otro):
        a=[]
        for elemento in self.__lista:
            a.append(elemento)
        for elemento in otro.__lista:
            if elemento not in a:
                a.append(elemento)
        return Conjunto(a)
    def __sub__(self, otro):
        a=[]
        for element in self.__lista:
            if element not in otro.__lista:
                a.append(element)
        return Conjunto(a)
    def __eq__(self,otro):
        b=False
        if len(self.__lista)==len(otro.__lista):
            b=True
            for element in self.__lista:
                if element not in otro.__lista:
                    b=False
        return b
