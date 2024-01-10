


class Viajero:
    __nviajero : int
    __dni = ""
    __nom = ""
    __ap = ""
    __ma : int

    def __init__(self,nviajero,dni,nombre,apellido,millas_acum):
        self.__nviajero=int(nviajero)
        self.__dni=dni
        self.__nom=nombre
        self.__ap=apellido
        self.__ma=int(millas_acum)
    
    def __str__(self):
        return self.__nviajero

    def getnumviajero(self):
        return self.__nviajero
    
    def cantMa(self):
        return self.__ma
    
    def acumularMillas(self,cant):
        self.__ma+=cant
        return self.__ma
    
    def canjearMillas(self,mcanje):
        millas=0
        if mcanje <= self.__ma:
            millas= mcanje-self.__ma
            return millas
        else:
            print("ERROR EN LA OPERACION \n")
    def mostrar(self):
        print("Nro:{}, DNI: {}, Nombre: {}, Apellido: {}, Millas: {}".format(self.__nviajero,self.__dni,self.__nom,self.__ap,self.__ma))
    #Mayor que
    def __gt__(self,Otro):
        if type(Otro) == Viajero:
            return self.__ma>Otro.__ma
        if type(Otro)==int:
            return self.__ma>Otro
    
    #Igual que
    def __eq__(self, Otro) -> bool:
        if type(self.__ma)==Viajero:
            return self.__ma==Otro
        elif type(Otro)==Viajero:
            return Otro.__ma==self.__ma
    #Suma: Sobrecarga por derecha
    def __radd__(self,Otro):
        return Viajero(self.__ap,self.__dni,self.__nom,self.__ap,self.__ma+Otro)
    #Resta: Sobrecarga por derecha
    def __rsub__(self,Otro):
        return Viajero(self.__ap,self.__dni,self.__nom,self.__ap,self.__ma-Otro)
