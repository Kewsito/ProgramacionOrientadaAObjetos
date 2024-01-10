from carrera import Carrera #se importa la clase continente
class facultad:
    __cod: int
    __nom: str
    __dire:str
    __loc:str
    __tel:str
    __carreras: list #Agregacion por composicion
    def __init__(self,cod,nom,dire,loc,tel):
        self.__cod=int(cod)
        self.__nom=str(nom)
        self.__dire=str(dire)
        self.__loc=str(loc)
        self.__tel=str(tel)
        self.__carreras=[] #SE AGREGA UNA LISTA VACIA
    
    def agregarcarre(self,obj): #Guarda las carreras en self.__carreras en forma de lista
        self.__carreras.append(obj)
    
    def getcod(self):
        return self.__cod
    
    def getnom(self):
        return self.__nom
    
    def getloc(self):
        return self.__loc
    
    def getdire(self):
        return self.__dire
    #CARRERAS
    def longcarre(self):
        return len(self.__carreras)
    
    def getnomcarre(self,p):
        return self.__carreras[p].getnom()
    
    def getdurcarre(self,p):
        return self.__carreras[p].getdur()
    
    def getcodcarre(self,p):
        return self.__carreras[p].getcod()
    
    def getloccarre(self,p):
        return self.__carreras[p].getloc()
