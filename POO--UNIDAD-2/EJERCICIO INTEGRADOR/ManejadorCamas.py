from claseCama import Cama
import numpy as np
from numpy import array
import csv
class ManejadorCamas:
    __arreglo: array
    def __init__(self):
        self.__arreglo=self.CrearCamas()
    
    def CrearCamas(self):
        l=[]
        archivo= open("camas.csv")
        reader = csv.reader(archivo,delimiter=";")
        next(reader, None)
        for fila in reader:
            c=Cama(fila[0], fila[1],fila[2],fila[3],fila[4],fila[5],fila[6])
            l.append(c)
        archivo.close()
        arreglo=np.array(l)
        return arreglo
    
    def op3(self,nombre):
        for i in range(len(self.__arreglo)):
            if nombre == self.__arreglo[i].getNomyap():
                b=i
        print("INDEX:{}".format(b))
        return b
    
    def AltaPaciente(self,fecha,pos):
        self.__arreglo[pos].setAlta(fecha)
        
    def mostrarDatos(self,pos):
        print("Paciente: {} \t Cama: {} \t Habitacion: {} \n Diagnostico: {} \t Fecha de internacion: {} \n Fecha de alta: {} \n".format(self.__arreglo[pos].getNomyap(),self.__arreglo[pos].getIdCama(),self.__arreglo[pos].getRoom(),self.__arreglo[pos].getDiag(),self.__arreglo[pos].getFechaInt(),self.__arreglo[pos].getFechaAlta()))
        return self.__arreglo[pos].getIdCama()
    
    def PacientesDiag(self,diag):
        for i in range(len(self.__arreglo)):
            if self.__arreglo[i].getEstado()==True:
                print("Entra diag: {}".format(self.__arreglo[i].getDiag()))
                if str(self.__arreglo[i].getDiag())==diag:
                    print(self.__arreglo[i])
                    
    def getIdcama(self,pos):
        return self.__arreglo[pos].getIdCama()
    
    def show(self):
        for i in range(len(self.__arreglo)):
            print (self.__arreglo[i])
            print("-"*30)
        
    