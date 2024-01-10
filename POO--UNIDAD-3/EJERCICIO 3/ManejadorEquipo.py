from Equipo import Equipo
import csv
import numpy as np


class ManejadorEquipo:
    __arrayE = None

    def __init__(self):
        self.__arrayE = np.empty(0, dtype=Equipo)

    def agregarEquipo(self, equipo):
        self.__arrayE = np.append(self.__arrayE, equipo)

    def CargaEquipo(self):
        archivo = open("Equipo.csv")
        reader = csv.reader(archivo, delimiter=";")
        bandera=True
        for fila in reader:
            if bandera:
                 bandera = not bandera
            else:
                equipo = Equipo(str(fila[0]), str(fila[1]))
                self.agregarEquipo(equipo)
        print(len(self.__arrayE))
        archivo.close()

    def getarrayE(self):
        return self.__arrayE

    def getposarrayE(self, pos):
        return self.__arrayE[pos]

    def getnombreE(self, pos):
        return self.__arrayE[pos].getnombre()
