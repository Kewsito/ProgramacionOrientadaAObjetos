import csv
import numpy as np
from flores import flores
class ManejaFlores:
    __arreglo: np.array
    def __init__(self):
        self.__arreglo=self.carga_arr()
    def carga_arr(self):
        with open('Flores.csv', 'r', encoding='utf8') as archivo:
            lista=[]
            reader=csv.reader(archivo,delimiter=";")
            for fila in reader:
                F=flores(fila[0],fila[1],fila[2],fila[3])
                lista.append(F)
            arr=np.array(lista)
            archivo.close()
            return arr
    def getlong(self):
        return len(self.__arreglo)
    def mostrar(self):
        print(len(self.__arreglo))
        for i in range(len(self.__arreglo)):
            print(self.__arreglo[i])
    def mostrarflor(self,pos):
        print("--Nombre: {}, Numero: {}, Color: {}--".format(self.__arreglo[pos].getNom(),self.__arreglo[pos].getNum(),self.__arreglo[pos].getCol()))
    def getflor(self,pos):
        return self.__arreglo[pos]
