from ClaseNodo import Nodo
from zope.interface import implementer
from ClaseDocenteInvestigador import DocenteInvestigador
from ClaseInvestigador import Investigador
from ClaseInterfaz import Interfaz
from IDirector import IDirector
from ITesorero import ITesorero
@implementer(Interfaz)
@implementer(IDirector)
@implementer(ITesorero)
class Lista:
    __comienzo = None
    __actual = None
    __indice = 0
    __tope = 0

    def __init__(self):
        self.__comienzo=None
        self.__actual=None

    def __iter__(self):
        return self

    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual=self.__comienzo
            self.__indice=0
            raise StopIteration
        else:
            self.__indice+=1
            dato=self.__actual.getDato()
            self.__actual=self.__actual.getSiguiente()
            return dato

    def agregarPersona(self,persona):
        nodo=Nodo(persona)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo=nodo
        self.__actual=nodo
        self.__tope+=1

    def insertarElemento(self,pos,objeto):
        cont = 1
        cabeza = self.__comienzo
        if self.__comienzo is None:
            nodo = Nodo(objeto)
            nodo.setSiguiente(self.__comienzo)
            self.__comienzo = nodo
            self.__actual = nodo
            self.__tope += 1
        else:
            while cont < pos - 1  and cabeza is not None:
                cont += 1
                cabeza = cabeza.getSiguiente()
            if pos == 1:
                nuevoNodo = Nodo(objeto)
                nuevoNodo.setSiguiente(cabeza)
                self.__comienzo = nuevoNodo
                self.__actual = nuevoNodo
            else:
                nuevoNodo = Nodo(objeto)
                nuevoNodo.setSiguiente(cabeza.getSiguiente())
                cabeza.setSiguiente(nuevoNodo)
            self.__tope+=1

    def insertarFinal(self,objeto):
        if self.__comienzo is None:
            nodo = Nodo(objeto)
            nodo.setSiguiente(self.__comienzo)
            self.__comienzo = nodo
            self.__actual = nodo
        else:
            cabeza = self.__comienzo
            while cabeza.getSiguiente() is not None:
                cabeza = cabeza.getSiguiente()
            nodo = Nodo(objeto)
            cabeza.setSiguiente(nodo)
        self.__tope+=1

    def tipodeObjeto(self, pos):
        dato = None
        cont = 1
        if self.__comienzo is None and pos != 1:
            dato = None
        cabeza = self.__comienzo
        while cabeza.getSiguiente() is not None and cont < pos:
            cont += 1
            cabeza = cabeza.getSiguiente()
        if cont == pos:
            dato = cabeza.getDato()
        return dato

    def listado_ordenado_porNombre(self):
        nom = input("Ingrese el nombre de la carrera: ")
        lista = []
        cabeza = self.__comienzo
        while cabeza is not None:
            dato = cabeza.getDato()
            if  type(dato) is DocenteInvestigador:
                if dato.getCarrera().lower() == nom.lower():
                    lista.append(dato)
            cabeza = cabeza.getSiguiente()
        lista = sorted(lista)
        for elemento in lista:
            print("Apellido y Nombre: {}, Carrera: {}".format(elemento.getApellido() + " " + elemento.getNombre(),elemento.getCarrera()))

    def cuentaAgenteInvestigadores(self):
        area = input("Ingrese el area de investigacion: ")
        ct1 = 0
        ct2 = 0
        cabeza = self.__comienzo
        while cabeza is not None:
            dato = cabeza.getDato()
            if type(dato) is DocenteInvestigador:
                if dato.getArea().lower() == area.lower():
                    ct1 += 1
            elif type(dato) is Investigador:
                if dato.getArea().lower() == area.lower():
                    ct2 += 1
            cabeza = cabeza.getSiguiente()
        print("Para el area de investigacion {}, la cantidad de docentes investigadores es de {} y de investigadores es {}".format(area,ct1,ct2))

    def listadoOrdenado(self):
        lista = []
        cabeza = self.__comienzo

        while cabeza is not None:
            dato = cabeza.getDato()
            dato.calculaSueldo()
            lista.append(dato)
            cabeza = cabeza.getSiguiente()

        listaord = sorted(lista)
        for elem in listaord:
            print("Nombre y apellido: {}, Tipo de agente: {}, Sueldo:{}".format(elem.getNombre() + " " + elem.getApellido(), elem.getTipoAgente(), elem.getSueldo()))

    def listadoporCategoria(self):
        cat = (input("Ingrese una categoria: ")).lower()
        print(cat)
        total = 0
        cabeza = self.__comienzo
        while cabeza is not None:
            dato = cabeza.getDato()
            if type(dato) is DocenteInvestigador and dato.getIncentivo().lower() == cat:
                print("Nombre: {}, Apellido: {}, Importe Extra: ${}".format(dato.getNombre(),dato.getApellido(),dato.getImporteEx()))
                total += dato.getImporteEx()
            cabeza = cabeza.getSiguiente()
        print("El Ministerio deberá abonar un total de: ${}".format(total))

    def almacenaJson(self,objectEncoder):
        lista = []
        cabeza = self.__comienzo
        while cabeza is not None:
            dato = cabeza.getDato()
            dicc = dato.toJson()
            lista.append(dicc)
            cabeza = cabeza.getSiguiente()
        objectEncoder.guardarJSONArchivo(lista, "NuevosAparatos.json")
        print("--Archivo guardado correctamente--")

    def modificarBasico(self, cuil, nuevoBasico):
        cabeza = self.__comienzo
        band = False
        while cabeza is not None and band is False:
            if cabeza.getDato().getCuil() == cuil:
                cabeza.getDato().setSueldo(nuevoBasico)
                print("Sueldo basico modificado correctamente")
                band = True
            cabeza = cabeza.getSiguiente()
        if band == False:
            print("Agente no encontrado o CUIL ingresado de manera incorrecta")

    def modificarPorcentajeporcargo(self,cuil,nuevoPorcentaje):
        cabeza = self.__comienzo
        band = False
        while cabeza is not None and band is False:
            if cabeza.getDato().getCuil() == cuil and cabeza.getDato().getTipoAgente().lower() == "docente":
                cabeza.getDato().setPorcentaje(nuevoPorcentaje)
                print("Porcentaje modificado correctamente")
                band = True
            elif cabeza.getDato().getCuil() == cuil and cabeza.getDato().getTipoAgente().lower() == "personalapoyo":
                cabeza.getDato().setPorcentaje(nuevoPorcentaje)
                print("Porcentaje modificado correctamente")
                band = True
            cabeza = cabeza.getSiguiente()
        if band == False:
            print("Agente no encontrado o CUIL ingresado de manera incorrecta")
    """
    def modificarPorcentajeporcategoria(self,cuil, nuevoPorcentaje):
        cabeza = self.__comienzo
        band = False
        while cabeza is not None and band is False:
            if cabeza.getDato().getCuil() == cuil and cabeza.getDato().getTipoAgente().lower() == "personalapoyo":
                cabeza.getDato().setPorcentaje(nuevoPorcentaje)
                print("Porcentaje modificado correctamente")
                band = True
            cabeza = cabeza.getSiguiente()
        if band == False:
            print("Agente no encontrado o DNI ingresado de manera incorrecta")
    """
    def modificarImporteExtra(self, cuil, nuevoImporteExtra):
        cabeza = self.__comienzo
        band = False
        while cabeza is not None and band is False:
            if cabeza.getDato().getCuil() == cuil and cabeza.getDato().getTipoAgente().lower() == "docenteinvestigador":
                cabeza.getDato().setImporteExtr(nuevoImporteExtra)
                print("Importe extra modificado correctamente")
                band = True
            cabeza = cabeza.getSiguiente()
        if band == False:
            print("Agente no encontrado o CUIL ingresado de manera incorrecta")

    def gastosSueldoPorEmpleado (self, cuil):
        cabeza = self.__comienzo
        band = False
        while cabeza is not None and band is False:
            if cabeza.getDato().getCuil() == cuil:
                print("Empleado: {}, Sueldo: {}".format(cabeza.getDato().getApellido() + " " + cabeza.getDato().getNombre(),cabeza.getDato().getSueldo()))
                band = True
            cabeza = cabeza.getSiguiente()
        if band == False:
            print("Agente no encontrado o CUIL ingresado de manera incorrecta")