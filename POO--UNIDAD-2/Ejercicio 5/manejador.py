# -*- coding: utf-8 -*-
"""
Created on Sun May  1 20:34:17 2022

@author: Kewwsito
"""
import csv
from clasePlanAhorro import planahorro
class manejador:
    __lista=[]
    
    def __init__(self):
        self.__lista=[]
    
    def cargaLista(self):
        archivo = open("planes.csv")
        reader = csv.reader(archivo,delimiter=';')

        for fila in reader:
            obj=planahorro(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5])
            self.__lista.append(obj)
    def buscarVehiculo(self, valor):
        retorno=-1
        i=0
        bander=False
        while(i<len(self.__lista) and (bander==False)):
            if self.__lista[i].getimportecuota<valor:
                retorno=i
                bander=True
            else:
                i=+i
            return retorno
    def buscarCodigo(self,cod):
        r=-1
        b=False
        i=0
        while (i<len(self.__lista) and (b==False)):
            if cod==self.__lista[i].getcod:
                r=i
                b=True
            else:
                i+=i                
        return r
        
    #a.      Actualizar el valor del vehículo de cada plan. Para esto se muestra el código del plan, el modelo y versión del vehículo, luego se ingresa el valor actual del vehículo y se modifica el atributo correspondiente.
    def Opa(self):
        for i in len(self.__lista):
            print("Codigo:",self.__lista[i].getcod()," Modelo:",self.__lista[i].getmodel()," Version:",self.__lista[i].getver()," Valor:",self.__lista[i].getvalorv())
            nuevovalor=input("Ingrese su nuevo valor")
            self.__lista.getactualizarValor(nuevovalor)
            
    #b.      Dado un valor, mostrar código del plan, modelo y versión del vehículo, cuyo valor de la cuota sea inferior al valor dado.
    def Opb(self):
        val=input("Ingrese valor")
        i=self.__lista.buscarVehiculo(val)
        if i!=-1:
            print("Codigo de plan:",self.__lista[i].getcod,"|| Modelo:",self.__lista[i].getmodel,"|| Version:",self.__lista[i].getver)
        else:
            print("No se encontro el vehiculo")
    
    #c.       Mostrar el monto que se debe haber pagado para licitar el vehículo (cantidad de cuotas para licitar * importe de la cuota).
    def Opc(self):
        for i in len(self.__lista):
            print("Monto: ",self.__lista.getMonto())
    #d.      Dado el código de un plan, modificar la cantidad cuotas que debe tener pagas para licitar.
    def Opd(self):
        cod=input("Ingrese codigo del plan")
        i=self.__lista.buscarCodigo(cod)
        self.__lista[i].modificar(input("Ingrese la cantidad de cuotas que debe tener para licitar"))
        
        
