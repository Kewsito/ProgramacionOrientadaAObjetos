import csv
from Jugador import Jugador


class ManejadorJugador:
    __listaJ = None

    def __init__(self):
        self.__listaJ = []

    def CargaJugador(self):
        archivo = open("Jugador.csv")
        reader = csv.reader(archivo, delimiter=";")
        for fila in reader:
                jugador = Jugador(int(fila[0]), str(fila[1]), str(fila[2]), str(fila[3]), fila[4])
                self.__listaJ.append(jugador)

    def getListaJ(self):
        return self.__listaJ

    def getposLisJ(self, pos):
        return self.__listaJ[pos]


