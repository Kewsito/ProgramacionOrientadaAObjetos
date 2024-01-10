from ManejadorEquipo import ManejadorEquipo
from ManejadorJugador import ManejadorJugador
from ManejadorContrato import ManejadorContrato
import os

class Menu:
    __intanciaequipos = None
    __intanciajugador = None
    __intanciacontrato = None

    def __init__(self):
        self.__intanciacontrato = ManejadorContrato()
        self.__intanciajugador = ManejadorJugador()
        self.__intanciaequipos = ManejadorEquipo()

    def op(self):
        print("1. Cargar los datos de los Equipos en la clase Manejador de Equipos, a partir de los datos registrados en el archivo.\n2:Crear un contrato para un jugador en un equipo: Se genera un contrato para un jugador en un equipo.\n3. Consultar jugadores Contratados: Ingresar el DNI de un jugador, si está contratado, mostrar el nombre del Equipo en el que fue contratado, y la fecha de finalización de contrato.\n4. Consultar Contratos: Ingresar el identificador de un Equipo y listar los datos de los Jugadores cuyo contrato vence en 6 meses.\n5. Obtener importe de contratos: Para un nombre de equipo leído desde teclado, determinar el importe total de los contratos que posee con los jugadores del equipo.\n6. Guardar Contratos: Generar un nuevo archivo que contenga los siguientes datos de los contratos: DNI del jugador, Nombre del equipo, fecha de inicio, fecha de fin, y el pago mensual.")
        opcion = int(input("Ingrese una opcion (finalice con 0):"))

        while opcion != 0:
            os.system('cls')
            if opcion == 1:
                self.__intanciaequipos.CargaEquipo()
                self.__intanciajugador.CargaJugador()
            elif opcion == 2:
                self.__intanciacontrato.CargaContrato(self.__intanciaequipos.getarrayE(), self.__intanciajugador.getListaJ())
                self.__intanciacontrato.mostrarcontrato()
            elif opcion == 3:
                dni = int(input("Ingrese el DNI de un jugador:"))
                self.__intanciacontrato.consJContratado(dni)
            elif opcion == 4:
                self.__intanciacontrato.ConsulCon(input("Ingrese el identficador de un equipo"))
            elif opcion == 5:
                equipo = input("Ingrese el nombre de un equipo:")
                total = self.__intanciacontrato.ObtImpCon(equipo)
                if total == -1:
                    print("El equipo ingresado no existe")
                else:
                    print("El total del el equipo {} es {}".format(equipo,total))

            elif opcion == 6:
                self.__intanciacontrato.GeneArchi()
            else:
                print("La opcion Ingresada no Existe")
            print("1. Cargar los datos de los Equipos en la clase Manejador de Equipos, a partir de los datos registrados en el archivo.\n2:Crear un contrato para un jugador en un equipo: Se genera un contrato para un jugador en un equipo.\n3. Consultar jugadores Contratados: Ingresar el DNI de un jugador, si está contratado, mostrar el nombre del Equipo en el que fue contratado, y la fecha de finalización de contrato.\n4. Consultar Contratos: Ingresar el identificador de un Equipo y listar los datos de los Jugadores cuyo contrato vence en 6 meses.\n5. Obtener importe de contratos: Para un nombre de equipo leído desde teclado, determinar el importe total de los contratos que posee con los jugadores del equipo.\n6. Guardar Contratos: Generar un nuevo archivo que contenga los siguientes datos de los contratos: DNI del jugador, Nombre del equipo, fecha de inicio, fecha de fin, y el pago mensual.")
            opcion = int(input("Ingrese una opcion (finalice con 0)"))
            os.system('cls')
