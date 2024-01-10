# -*- coding: utf-8 -*-
"""
Created on Sun May  1 20:03:20 2022

@author: Kewwsito
"""

class planahorro:
    __codigo=int
    __modelo=''
    __version=''
    __valorv=float
    __cantcplan=0
    __cantcpag=0
    
    def __init__(self,codigo,modelo,version,valorv,cantcplan,cantcpag):
        self.__codigo=codigo
        self.__modelo=modelo
        self.__version=version
        self.__valorv=valorv
        self.cantcplan=cantcplan
        self.cantcpag=cantcpag
        
    def getactualizaValor(self,nuevovalor):
        self._valorv=nuevovalor
        return print("Valor actualizado!!! \n El nuevo valor es:",self.__valorv)
    
    def getimportecuota(self):
        valorcuota=((self.__valorv/self.cantcplan) + self.__valorv * 0.10)
        return (valorcuota)
    def __str__(self):
        return print("Codigo:" ,self.__codigo,"Modelo:",self.__modelo,"Version:",self.__version,"Valor:",self.__valorv)
    def getcod(self):
        return self.__codigo
    def getmodel(self):
        return self.__modelo
    def getver(self):
        return self.__version
    def getvalor(self):
        return self.__valorv
    def getMonto(self):
        return float(self.__cantcpag*self.getvalor())
        
    @classmethod
    def getCantCPag(cls):
       return cls.__cantcplan
    @classmethod
    def modificar(cls,x):
        cls.__cantcpag=int(x)

    