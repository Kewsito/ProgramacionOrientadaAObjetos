import os
from ObjectEncoder import ObjectEncoder
from ClaseLista import Lista
from ClaseManejadorInterface import ManejadorInterface

class Menu:
    __op: int
    __ObjectEncoder: ObjectEncoder
    __controlLista: Lista
    __ManejadorInterface: ManejadorInterface


    def __init__(self):
        self.__op=0
        self.__ObjectEncoder = ObjectEncoder()
        self.__controlLista = Lista()
        self.__ManejadorInterface = ManejadorInterface()


    def mostrar(self):
        centinela=None
        while(centinela!=0):
            self.__op=int(input("""
            **Menu**
Opcion ->[12] : Crear Archivo .json
Opcion ->[13] : Cargar Objetos en Lista
----------------------------------------
Opcion ->[1] : Insertar a agentes a la colección.
Opcion ->[2] : Agregar agentes a la colección.
Opcion ->[3] : Dada una posición de la lista: Mostrar por pantalla que tipo de agente se encuentra almacenado en dicha posición.
Opcion ->[4] : Ingresar por teclado el nombre de una carrera y generar un listado ordenado por nombre con todos los datos de los agentes que se desempeñan como docentes investigadores.
Opcion ->[5] : Dada un área de investigación, contar la cantidad de agentes que son docente    investigador, y la cantidad de investigadores que trabajen en ese área.
Opcion ->[6] : Recorrer la colección y generar un listado que muestre nombre y apellido, tipo de Agente y sueldo de todos los agentes, ordenado por apellido.
Opcion ->[7] : Dada una categoría de investigación (I, II, III, IV o V), leída desde teclado, listar apellido, nombre e importe extra por docencia e investigación, de todos los docentes investigadores que poseen esa categoría, al final del listado deberá mostrar el total de dinero que la Secretaría de Investigación debe solicitar al Ministerio en concepto de importe extra que cobran los docentes investigadores de la categoría solicitada.
Opcion ->[8] : Almacenar los datos de todos los agentes en el archivo “personal.json”   
Opcion ->[0] : [Finalizar]

Ingrese Opcion-> """))

            if(self.__op==12):
               self.opcion12()

            elif(self.__op==13):
               self.opcion13()

            elif(self.__op==1):
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

            elif(self.__op==0):
                centinela=0
            else:
                print("Error")


    def opcion12(self):
        os.system("cls")
        self.__ObjectEncoder.cargaJson("personal.json")

    def opcion13(self):
        os.system("cls")
        self.__ObjectEncoder.cargarobjeto(self.__controlLista)

    def opcion1(self):
        os.system("cls")
        self.__ManejadorInterface.llamarinterfaces(self.__controlLista,1)

    def opcion2(self):
        os.system("cls")
        self.__ManejadorInterface.llamarinterfaces(self.__controlLista,2)

    def opcion3(self):
        os.system("cls")
        self.__ManejadorInterface.llamarinterfaces(self.__controlLista,3)

    def opcion4(self):
        os.system("cls")
        carrera = input("Ingrese el nombre de la carrera: ")
        self.__controlLista.mostrardocenteinv(carrera)

    def opcion5(self):
        os.system("cls")
        area = input("Ingrese el area de investigacion: ")
        self.__controlLista.contar(area)

    def opcion6(self):
        os.system("cls")
        self.__controlLista.listadoOrdenado()

    def opcion7(self):
        os.system("cls")
        categ = input("Ingrese una categoria de investigacion (I, II, III, IV o V): ")
        self.__controlLista.mostrarlistadoinv(categ)

    def opcion8(self):
        os.system("cls")
        listaguardar = self.__controlLista.obtenerlista()
        self.__ObjectEncoder.guardarJSONArchivo(listaguardar, "nuevospersonal.json")

