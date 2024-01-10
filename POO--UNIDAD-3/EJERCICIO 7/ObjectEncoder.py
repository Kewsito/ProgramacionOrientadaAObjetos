import json
from pathlib import Path
from ClaseInvestigador import Investigador
from ClaseDocente import Docente
from ClasePersonalApoyo import PersonalApoyo
from ClaseDocenteInvestigador import DocenteInvestigador

class ObjectEncoder:

    def cargaJson(self,jsonF):
        objeto1 = Docente(cuil="20-3454506-8",apellido="Perez",nombre="Nicolas",sueldo=89000,anti=3,carrera="LCC",cargo="JTP",catedra="Sistemas de Informacion")
        objeto2 = Investigador(cuil="15-324235-5",apellido="Dominguez",nombre="Juan",sueldo=120000,anti=2,area="Computacional",tipo="Cientifica")
        objeto3 = PersonalApoyo(cuil="12-456543-4",apellido="Castro",nombre="Maria",sueldo=140000,anti=2,categoria="12")
        objeto4 = DocenteInvestigador(programa="I",importe=25000, cuil="18-3446706-8",apellido="Lopez",nombre="Marcos",sueldo=89000,anti=3,catedra="EyFCI",carrera="LCC",cargo="Simple",area="Estructuras",tipo="Teorica")


        #print(objeto4.getcuil())
        #print(objeto4.getimporte())
        d1 = objeto1.toJson()
        d2 = objeto2.toJson()
        d3 = objeto3.toJson()
        d4 = objeto4.toJson()
        #print(d0)
        lista = [d1, d2, d3, d4]
        self.guardarJSONArchivo(lista, "personal.json")



    def guardarJSONArchivo(self, lista, archivo):
        with Path(archivo).open("w", encoding="UTF-8") as destino:
            json.dump(lista, destino, indent=4)
            destino.close()


    #para decodificar el archivo json
    def leerJSON(self, archivo):
        with Path(archivo).open(encoding="UTF-8") as fuente:
            diccionario=json.load(fuente)
            fuente.close()
            return diccionario


    def cargarobjeto(self, claselista):
        listadicc = self.leerJSON("personal.json")
        print(len(listadicc))
        for elem in listadicc:
            if "__class__" not in elem:
                print("No se encuentra la clase")
            else:
                class_name = elem["__class__"]
                class_ = eval(class_name)
                print(class_name)

                if class_name == "Docente":
                    atributos = elem["__atributos__"]
                    D = class_(**atributos)
                    claselista.agregarPersona(D)
                elif class_name == "Investigador":
                    atributos = elem['__atributos__']
                    I = class_(**atributos)
                    claselista.agregarPersona(I)
                elif class_name == "PersonalApoyo":
                    atributos = elem['__atributos__']
                    P = class_(**atributos)
                    claselista.agregarPersona(P)
                elif class_name == "DocenteInvestigador":
                    atributos = elem['__atributos__']
                    DI = class_(**atributos)
                    claselista.agregarPersona(DI)


    def retornarobjeto(self, tipo):
        if tipo == "Docente":
            objeto = Docente(cuil="15-1823791-2",apellido="Ortiz",nombre="Juan",sueldo=50000,anti=10,carrera="LSI",cargo="JTP",catedra="Programacion Orientada a Objetos")
        elif tipo == "Investigador":
            objeto = Investigador(cuil="20-1923192-3",apellido="Dominguez",nombre="Carlos",sueldo=120000,anti=2,area="Computacional",tipo="Cientifica")
        elif tipo == "Personal Apoyo":
            objeto = PersonalApoyo(cuil="12-456543-4",apellido="Pereyra",nombre="Maria",sueldo=70000,anti=1,categoria="I")
        elif tipo == "Docente Investigador":
            objeto = DocenteInvestigador(programa="I",importe=25000, cuil="18-3446706-8",apellido="Lopez",nombre="Juan Cruz",sueldo=90000,anti=4,catedra="EyFCI",carrera="LCC",cargo="Jefe de Catedra",area="Estructuras",tipo="Teorica")
        else:
            objeto = None

        return objeto



