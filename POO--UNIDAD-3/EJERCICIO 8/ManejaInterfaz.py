from ClaseInterfaz import Interfaz
from IDirector import IDirector
from ITesorero import ITesorero
from ObjectEncoder import ObjectEncoder
class ManejaInterface:
    __controlador: ObjectEncoder

    def __init__(self):
        self.__controlador = ObjectEncoder()

    def opcionesGeneral (self,Ilista: Interfaz,op):
        if op == 2:
            tipo = input("Ingrese el tipo de agente(Docente-Investigador-Personal Apoyo-Docente Investigador): ")
            obj = self.__controlador.retornarObjeto(tipo.lower())
            pos = int(input("Ingrese la posicion a insertar el objeto: "))
            if obj != None:
                Ilista.insertarElemento(pos,obj)
            else:
                print("Intenta insertar un elemento que no es un objeto de tipo aparato")
        elif op == 3:
            tipo = input("Ingrese el tipo de agente(Docente-Investigador-Personal Apoyo-Docente Investigador): ")
            obj = self.__controlador.retornarObjeto(tipo.lower())
            if obj != None:
                Ilista.insertarFinal(obj)
            else:
                print("Intenta insertar un elemento que no es un objeto de tipo aparato")
        elif op == 4:
            pos = int(input("Ingrese una posicion de la lista: "))
            dato = Ilista.tipodeObjeto(pos)
            if dato != None:
                print("Tipo de agente: {}".format(dato.getTipoAgente()))
            else:
                print("Posicion incorrecta")
        else:
            print("No se encuentra la opcion ingresada")

    def opcionesDirector(self, Ilista: IDirector,op):
        if op == "A":
            cuil = input("Ingrese el CUIL del Agente: ")
            imp = float(input("Ingrese el nuevo sueldo basico: "))
            Ilista.modificarBasico(cuil,imp)
        elif op == "B":
            cuil = input("Ingrese el CUIL del Agente: ")
            por = float(input("Ingrese el nuevo porcentaje: "))
            Ilista.modificarPorcentajeporcargo(cuil,por)
        elif op == "C":
            cuil = input("Ingrese el CUIL del Agente: ")
            por = float(input("Ingrese el nuevo porcentaje: "))
            Ilista.modificarPorcentajeporcargo(cuil,por)
        elif op == "D":
            cuil = input("Ingrese el CUIL del Agente: ")
            imp = float(input("Ingrese el nuevo importe extra: "))
            Ilista.modificarImporteExtra(cuil,imp)
        else:
            print("Opcion incorrecta")
    def opcionesTesorero(self,Ilista: ITesorero,op):
        if op == "A":
            cuil = input("Ingrese el CUIL del Agente: ")
            Ilista.gastosSueldoPorEmpleado (cuil)
        else:
            print("Opcion incorrecta")

    def llamaInterface(self,lista,op,user="general"):
        if user.lower() == "general":
            self.opcionesGeneral(Interfaz(lista),op)
        elif user.lower() == "director":
            self.opcionesDirector(IDirector(lista),op)
        elif user.lower() == "tesorero":
            self.opcionesTesorero(ITesorero(lista),op)