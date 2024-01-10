import os
from ObjectEncoder import ObjectEncoder
from ManejaInterfaz import ManejaInterface
from ClaseLista import Lista
class Menu:
    __claseLista: Lista

    def __init__(self):
        self.__claseLista=Lista()
        try:
            jsonF = ObjectEncoder()
            jsonF.decodificarDiccionario(self.__claseLista)
            manejaInterfaz = ManejaInterface()
        except:
            print("Necesita crearse el archivo, puede ingresar la opcion 1 (GENERAL) del programa")

    def mostrar(self):
        print("--OPCIONES GENERALES--")
        print("1 - Crear archivo .json si es que no existe")
        print("2 - Insertar un agente en la colección en una posición determinada.\n3 - Agregar un agente a la colección.")
        print("4 - Dada una posición de la lista: Mostrar por pantalla que tipo de agente se encuentra almacenado en dicha posición.")
        print("5 - Ingresar por teclado el nombre de una carrera y generar un listado ordenado por nombre con todos los datos de los agentes que se desempeñan como docentes investigadores.")
        print("6 - Dada un área de investigación, contar la cantidad de agentes que son docente    investigador, y la cantidad de investigadores que trabajen en ese área.\n7 - Recorrer la colección y generar un listado que muestre nombre y apellido, tipo de Agente y sueldo de todos los agentes, ordenado por apellido.")
        print("8. Calcular importe extra de categoria de investigacion")
        print("9 - Almacenar los datos de todos los agentes en el archivo “Personalnew.json” ")

    def menuOp(self):
        self.mostrar()
        op=int(input("Ingrese una opcion (0 PARA SALIR DEL MENU GENERAL): "))

        while op != 0:
            os.system('cls')

            if op == 1:
                jsonF.cargaJson()
                jsonF.decodificarDiccionario(self.__claseLista)
                manejaInterfaz = ManejaInterface()

            elif op == 2:
                manejaInterfaz.llamaInterface(self.__claseLista,op)

            elif op == 3:
                manejaInterfaz.llamaInterface(self.__claseLista,op)

            elif op == 4:
                manejaInterfaz.llamaInterface(self.__claseLista,op)

            elif op == 5:
                self.__claseLista.listado_ordenado_porNombre()

            elif op == 6:
                self.__claseLista.cuentaAgenteInvestigadores()

            elif op == 7:
                self.__claseLista.listadoOrdenado()

            elif op == 8:
                self.__claseLista.listadoporCategoria()

            elif op == 9:
                self.__claseLista.almacenaJson(jsonF)

            else:
                print("Opcion incorrecta intente nuevamente")
            self.mostrar()
            op=int(input("Ingrese una opcion (0 PARA SALIR DEL MENU GENERAL): "))
            os.system('cls')

    def muestraDirector(self):
        print("A. Modificar sueldo")
        print("B. Modificar porcentaje docente")
        print("C. Modificar porcentaje personal apoyo")
        print("D. Modificar porcentaje docente investigador")
    def menuDirector(self,user):
        manejaInterfaz = ManejaInterface()
        self.muestraDirector()
        op = input("Ingrese una opcion (X para volver al menu principal o 0 para terminar): ")
        while op != "0":
            if op == "A":
                manejaInterfaz.llamaInterface(self.__claseLista,op,user)
            elif op == "B":
                manejaInterfaz.llamaInterface(self.__claseLista,op,user)
            elif op == "C":
                manejaInterfaz.llamaInterface(self.__claseLista,op,user)
            elif op == "D":
                manejaInterfaz.llamaInterface(self.__claseLista,op,user)
            elif op == "X":
                self.menuOp()
            else:
                print("Opcion incorrecta intente nuevamente")
            self.muestraDirector()
            op = input("Ingrese una opcion (X para volver al menu principal o 0 para terminar): ")

    def menuTesorero(self,user):
        manejaInterfaz = ManejaInterface()
        print("A. Consultar sueldos")
        op = input("Ingrese una opcion (X para volver al menu principal o 0 para terminar): ")
        while op != "0":
            if op == "A":
                manejaInterfaz.llamaInterface(self.__claseLista,op,user)
            elif op == "X":
                self.menuOp()
            else:
                print("Opcion incorrecta intente nuevamente")
            print("A. Consultar sueldos")
            op = input("Ingrese una opcion (X para volver al menu principal o 0 para terminar): ")