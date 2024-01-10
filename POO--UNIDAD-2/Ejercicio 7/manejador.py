from claseViajero import Viajero
import csv
class Manejador_Viajeros:
    __lista= []
    
    def __init__(self):
        self.__lista=[]
    
    def CargaLista (self):
        archivo= open('archivo.csv')
        reader= csv.reader(archivo,delimiter=',')
      
        for fila in reader : 
            objeto = Viajero(fila[0], fila[1], fila[2], fila[3], fila[4])
            self.__lista.append(objeto)
            
    def BuscarViajero (self, num):
        retorno= -1
        i=0
        ban= False
        while(i < len(self.__lista) and (ban == False)):
            if num == self.__lista[i].getnumviajero():
                ban= True
                retorno= i
            else:
                i+=1
        return retorno
    
    def Op1  (self, retorno):
        self.__lista[retorno].cantMa
        
    def Op2 (self, retorno):
        c= int(input('Ingrese cantidad de millas para acumular: '))
        self.__lista[retorno].acumularMillas(c)
    
    def Op3 (self, retorno):
        canje= int(input('Ingrese millas a canjear: '))
        n= self.__lista.canjearMillas(canje)
        if n!= 0:
            print('Cantidad de millas= {}', n)
        else:
            print("Error")
    def Sobrecarga123(self):
        v = self.__lista[0]
        print("Por izquierda: \n {} == 2500".format(v))
        print(v==2500)
        print("Por derecha: \n 2500 == {}".format(v))
        print(2500==v)
        print("Comparacion entre objetos: \n {} == {}".format(v,self.__lista[1]))
        print(v==self.__lista[1])
        print("Entre otros objetos: \n {} == {}" .format(v,self.__lista[2]))
        print(v==self.__lista[2])
        print("--Apartado 2 y 3--")
        v.mostrar()
        v=1000 + v
        print("Se acumulan nuevas millas")
        v.mostrar()
        print("Se realiza un canje de millas")
        v = 2500 - v
        v.mostrar()
        
        v.mostrar()
        
        