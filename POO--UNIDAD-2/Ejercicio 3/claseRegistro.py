
class Registro:
    __temp=""
    __hume=""
    __pres=""
    def __init__(self,temp,hume,pres):
        self.__temp=float(temp)
        self.__hume=int(hume)
        self.__pres=int(pres)

    def gettemp(self):
        return self.__temp
    
    def gethum(self):
        return self.__hume
    
    def getpres(self):
        return self.__pres
