

from itertools import accumulate


class Viajero:
    __nviajero =int
    __dni = ""
    __nom = ""
    __ap = ""
    __ma = int

    def __init__(self,nviajero,dni,nombre,apellido,millas_acum):
        self.__nviajero=nviajero
        self.__dni=dni
        self.__nom=nombre
        self.__ap=apellido
        self.__ma=millas_acum
    
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
    
    def __gt__(self,Otro):
        if type(Otro) == Viajero:
            return self.__ma>Otro.__ma
        if type(Otro)==int:
            return self.__ma>Otro
    def __add__(self,Otro):
        return (self.__ap,self.__dni,self.__nom,self.__ap,self.__ma+Otro)
    def __sub__(self,Otro):
        return (self.__ap,self.__dni,self.__nom,self.__ap,self.__ma-Otro)