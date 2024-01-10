import os
from ClaseLista import Lista
from ObjectEncoder import ObjectEncoder
from ClaseManejadorInterface import ManejadorInterface

class Menu:
    __op: int
    __ClaseLista: Lista
    __controlEncoder: ObjectEncoder
    __ManejadorInterface: ManejadorInterface


    def __init__(self):
        self.__op=0
        self.__ClaseLista = Lista()
        self.__controlEncoder = ObjectEncoder()
        self.__ManejadorInterface = ManejadorInterface()


    def mostrar(self):
        centinela=None
        while(centinela!=0):
            self.__op=int(input("""
            **Menu**
--------------------------------------------------        
Opcion ->[1] : Cargar Aparatos en archivo .json
Opcion ->[2] : Cargar Objetos en la Lista
--------------------------------------------------
----------------Funcionalidades-------------------
Opcion ->[3] : Insertar en cualquier posicion
Opcion ->[4] : Insertar al final
Opcion ->[5] : Dada una posición de la Lista: Mostrar por pantalla qué tipo de objeto se encuentra almacenado en dicha posición.
Opcion ->[6] : Mostrar la cantidad de heladeras, lavarropas y televisores cuya marca sea phillips.
Opcion ->[7] : Mostrar la marca de todos los lavarropas que tienen carga superior.
Opcion ->[8] : Mostrar para todos los aparatos que la empresa tiene a la venta, marca, país de fabricación e importe de venta.
Opcion ->[9] : Almacenar los objetos de la colección Lista en el archivo “aparatoselectronicos.json”.
Opcion ->[0] : [Finalizar]
Ingrese Opcion-> """))

            if(self.__op==1):
               self.opcion1()

            elif(self.__op==2):
                self.opcion2()

            elif(self.__op==3):
                self.opcion3()

            elif(self.__op==4):
                self.opcion4()

            elif(self.__op==5):
                self.opcion5()

            elif(self.__op==6):
                self.opcion6()

            elif(self.__op==7):
                self.opcion7()

            elif(self.__op==8):
                self.opcion8()

            elif(self.__op==9):
                self.opcion9()

            elif(self.__op==0):
                centinela=0
            else:
                print("Error")


    def opcion1(self):
        os.system("cls")
        self.__controlEncoder.cargarAparato()

    def opcion2(self):
        os.system("cls")
        self.__controlEncoder.cargarobjeto(self.__ClaseLista)

    def opcion3(self):
        os.system("cls")
        self.__ManejadorInterface.llamarinterfaces(self.__ClaseLista,1)

    def opcion4(self):
        os.system("cls")
        self.__ManejadorInterface.llamarinterfaces(self.__ClaseLista,2)

    def opcion5(self):
        os.system("cls")
        self.__ManejadorInterface.llamarinterfaces(self.__ClaseLista,3)

    def opcion6(self):
        os.system("cls")
        self.__ClaseLista.mostrarcantidades()

    def opcion7(self):
        os.system("cls")
        self.__ClaseLista.mostrarcargasup()

    def opcion8(self):
        self.__ClaseLista.mostrartodos()
        os.system("cls")

    def opcion9(self):
        os.system("cls")
        self.__ClaseLista.guardarjson(self.__controlEncoder)
