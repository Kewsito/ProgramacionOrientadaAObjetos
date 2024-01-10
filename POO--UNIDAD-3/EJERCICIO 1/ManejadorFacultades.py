
from Facultad import facultad
from carrera import Carrera
import csv
class ManejadorFacultad:
    __listaf: list

    def __init__(self):
        self.__listaf = self.cargarobjetos()

    def cargarobjetos(self):
        listaf=[]
        archivo = open("Facultades.csv","r",encoding="utf8")
        reader = csv.reader(archivo, delimiter=",")
        fila=next(reader)
        bandera = True

        while bandera:
            print("-"*100)
            print("|||[Facultad]|||")
            print(fila)
            print("-"*100)
            print("|||[Carreras]|||")
            filaCarrera=next(reader)
            f = facultad(fila[0], fila[1], fila[2], fila[3], fila[4])
            listaf.append(f)
            while bandera and fila[0] == filaCarrera[0]:
                print(filaCarrera)
                try:
                    c = Carrera(filaCarrera[1], filaCarrera[2], filaCarrera[3], filaCarrera[4], filaCarrera[5])
                    f.agregarcarre(c)
                    filaCarrera=next(reader)
                except StopIteration:
                    bandera=False

            fila=filaCarrera

        archivo.close()
        return listaf

    def mostrarfacultades(self,cod):
        i=0
        b=True
        while i< len(self.__listaf) and b:
            if cod==self.__listaf[i].getcod():
                print("Nombre Facultad: {} \n".format(self.__listaf[i].getnom()))
                for j in range(self.__listaf[i].longcarre()):
                    print("CARRERA: {} || DURACION: {} ".format(self.__listaf[i].getnomcarre(j),self.__listaf[i].getdurcarre(j)))
                b=False
            else:
                i+=1

    def buscarnom(self,nomcarrera):
        i=0
        b=True
        while i< len(self.__listaf) and b:
            for j in range(self.__listaf[i].longcarre()):
                if self.__listaf[i].getnomcarre(j)==nomcarrera:
                    print("Codigo de facultad: {} Codigo de carrera: {} \n Nombre: {} Localidad: {},{} ".format(self.__listaf[i].getcod(),self.__listaf[i].getcodcarre(j),self.__listaf[i].getnomcarre(j),self.__listaf[i].getdire(),self.__listaf[i].getloc()))
                b=False
            else:
                i+=1