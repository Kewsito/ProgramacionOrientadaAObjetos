from clasecalefactoragas import CalefactorAGas
from claseCalefactorElectrico import calefactorelectrico
from ClaseCalefactor import calefactor
import csv
import numpy as np


class manejadorcalefactores:
    __calefactores: np.array

    def __init__(self):
        self.__calefactores = np.empty(0, dtype=calefactor)

    def agregarcalefactor(self, calefactor):
        self.__calefactores = np.append(self.__calefactores, calefactor)

    def CargaCalefactorElectrico(self):
        with open("calefactoraelectrico.csv", "r", encoding="utf8") as archivo:
            reader = csv.reader(archivo, delimiter=";")
            next(reader, None)
            for fila in reader:
                Ce = calefactorelectrico(fila[0], fila[1], fila[2])
                self.agregarcalefactor(Ce)

    def CargaCalefactorAGas(self):
        with open("calefactoragas.csv", "r", encoding="utf8") as arch:
            reader = csv.reader(arch, delimiter=";")
            next(reader, None)
            for fila in reader:
                Cg = CalefactorAGas(fila[0], fila[1], fila[2], fila[3])
                self.agregarcalefactor(Cg)

    def mostrar(self):
        for i in range(len(self.__calefactores)):
            print(self.__calefactores[i])

    def mostrarpos(self, pos):
        print("El calefactor con menor consumo es: Marca: {} Modelo: {}".format(self.__calefactores[pos].getmar(),
                                                                                self.__calefactores[pos].getmod()))

    def itemd1(self, costo, consumo):
        i = 0
        min = 9999999
        while i < len(self.__calefactores):
            if type(self.__calefactores[i]) is CalefactorAGas:
                co = (self.__calefactores[i].getcalorias() / 1000) * costo * consumo
                if co < min:
                    min = co
                    pos = i
                i += 1
            else:
                i += 1
        self.mostrarpos(pos)
        return pos

    def itemd2(self, costo, consumo):
        i = 0
        min = 99999
        while i < len(self.__calefactores):
            if type(self.__calefactores[i]) is calefactorelectrico:
                cos = (self.__calefactores[i].getpot() / 1000) * costo * consumo
                if cos < min:
                    min = cos
                    pos = i
                i += 1
            else:
                i += 1
        self.mostrarpos(pos)
        return pos

    def mostrarcalefactor(self, posel, posgas):
        if type(self.__calefactores[posel]) is calefactorelectrico:
            print("Tipo de calefactor: {} Marca: {} Modelo: {} Potencia: {}".format(
                self.__calefactores[posel].setcalefactorE(), self.__calefactores[posel].getmar(),
                self.__calefactores[posel].getmod(), self.__calefactores[posel].getpot()))
        elif type(self.__calefactores[posgas]) is CalefactorAGas:
            print("Tipo de calefactor: {} Marca: {} Modelo: {} Matricula: {} Calorias: {}".format(
                self.__calefactores[posgas].setcalefactorG(), self.__calefactores[posgas].getmar(),
                self.__calefactores[posgas].getmod(), self.__calefactores[posgas].getmatricula(),
                self.__calefactores[posgas].getcalorias()))
