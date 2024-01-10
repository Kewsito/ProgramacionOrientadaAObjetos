import datetime
from Contrato import Contrato
import numpy as np


class ManejadorContrato:
    __arrayC = None

    def __init__(self):
        self.__arrayC = np.empty(0, dtype=Contrato)

    def agregarContrato(self, contrato):
        self.__arrayC = np.append(self.__arrayC, contrato)

    def mostrarcontrato(self):
        for i in range(len(self.__arrayC)):
            print(self.__arrayC[i])

    def CargaContrato(self, arrayE, listaJ):
        for i in range(len(listaJ)):
            Finicio = input("Ingrese una fecha de inicio de contrato para el jugador {}".format(listaJ[i].getnombre()))
            Ffin = input("Ingrese una fecha de finalizacion de contrato para el jugador {}".format(listaJ[i].getnombre()))
            Pago = float(input("Ingrese pago mensual para el jugador".format(listaJ[i].getnombre())))
            equipo = input("Ingrese el equipo en el que va estar ")
            j = 0
            while j < len(arrayE) and equipo != arrayE[j].getnombre():
                j += 1
            if j < len(arrayE):
                contrato = Contrato(Finicio, Ffin, Pago)
                contrato.setequipoC(arrayE[j])
                contrato.setjugadorC(listaJ[i])
                self.agregarContrato(contrato)
                print("-------------")
            else:
                contrato = Contrato(Finicio, Ffin, Pago)
                contrato.setequipoC(None)
                contrato.setjugadorC(None)
                self.agregarContrato(contrato)
                print("El equipo ingresado no existe")
                print("-------------")

    def consJContratado(self, dni):
        i = 0
        while i < len(self.__arrayC) and self.__arrayC[i].getjugadorE().getdni() != dni:
            i += 1
        if i < len(self.__arrayC):
            if self.__arrayC[i].getjugadorE().getnombre() == None:
                print("Este jugador no esta contratado")
            else:
                print("Nombre del equipo:{} , Fecha de Finalizacion:{}".format(self.__arrayC[i].getequipoC().getnombre(), self.__arrayC[i].getffin()))
        else:
            print("El DNI ingresado no existe")

    def ConsulCon(self, iden):
        i = 0
        vence = datetime.datetime.today() + datetime.timedelta(days=365/2)
        while i < len(self.__arrayC) and self.__arrayC[i].getequipoC().getnombre() != iden:
            i += 1
        if i < len(self.__arrayC):
            for j in range(len(self.__arrayC)):
                if (self.__arrayC[j].getffin() > self.__arrayC[j].getfinicio()) and vence == self.__arrayC[j].getffin().month:
                    print("El contrato del jugador {} vence en 6 meses".format(self.__arrayC[j].getjugadorE().getnombre()))
                elif self.__arrayC[j].getffin() < self.__arrayC[j].getfinicio():
                    print("El contrato del jugador {} vencio hace {} ".format(self.__arrayC[j].getjugadorE().getnombre(), self.__arrayC[j].getfinicio().month - self.__arrayC[j].getffin().month))
                else:
                    print("El contrato del jugador {} vence en {} mes/meses".format(self.__arrayC[j].getjugadorE().getnombre(), self.__arrayC[j].getffin().month - self.__arrayC[j].getfinicio().month))

    def ObtImpCon(self,equipo):
        i = 0
        retornatot = 0
        while i < len(self.__arrayC) and self.__arrayC[i].getequipoC().getnombre() != equipo:
            i += 1
        if i < len(self.__arrayC):
            for j in range(len(self.__arrayC)):
                if self.__arrayC[j].getequipoC().getnombre() == equipo:
                    retornatot += self.__arrayC[j].getpmensual()
        else:
            retornatot = -1
        return retornatot

    def GeneArchi(self):
        with open("Contrato.txt", "w") as file:
            file.write("FechaInicio;FechaFin;PagoMensual;NombreEquipo;DNIjugador\n")
            for i in range(len(self.__arrayC)):
                file.write(str(self.__arrayC[i].getfinicio())+";")
                file.write(str(self.__arrayC[i].getffin())+";")
                file.write(str(self.__arrayC[i].getpmensual())+";")
                file.write(self.__arrayC[i].getequipoC().getnombre()+";")
                file.write(str(self.__arrayC[i].getjugadorE().getdni())+"\n")

    def getarrayC(self):
        return self.__arrayC

    def getposarrayC(self, pos):
        return self.__arrayC[pos]
