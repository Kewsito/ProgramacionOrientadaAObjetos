from pathlib import Path
from ClaseDocente import Docente
from ClaseInvestigador import Investigador
from ClasePersonalApoyo import PersonalApoyo
from ClaseDocenteInvestigador import DocenteInvestigador
import json
class ObjectEncoder(object):

    def decodificarDiccionario(self,lista):
        diccionario = self.leerJSONArchivo("Personal.json")
        for elem in diccionario:
            if '__class__' not in elem:
                print("No se encuentra el diccionario")
            else:
                class_name=elem['__class__']
                class_=eval(class_name)
                if class_name == "Docente":
                    atributos = elem['__atributos__']
                    H = class_(**atributos)
                    lista.insertarFinal(H)
                elif class_name == "Investigador":
                    atributos = elem['__atributos__']
                    T = class_(**atributos)
                    lista.insertarFinal(T)
                elif class_name == "DocenteInvestigador":
                    atributos = elem['__atributos__']
                    T = class_(**atributos)
                    lista.insertarFinal(T)
                elif class_name == "PersonalApoyo":
                    atributos = elem['__atributos__']
                    L = class_(**atributos)
                    lista.insertarFinal(L)

    def cargaJson(self):
        objeto1 = Docente(cuil="20-3454506-8", apellido="Perez", nombre="Nicolas", sueldo=89000, anti=3,carrera="LCC", cargo="JTP", catedra="Sistemas de Informacion")
        objeto2 = Investigador(cuil="15-324235-5", apellido="Dominguez", nombre="Juan", sueldo=120000, anti=2,area="Computacional", tipo="Cientifica")
        objeto3 = PersonalApoyo(cuil="12-456543-4", apellido="Castro", nombre="Maria", sueldo=140000, anti=2,categoria="I")
        objeto4 = DocenteInvestigador(programa="I", importe=25000, cuil="18-3446706-8", apellido="Lopez",nombre="Marcos", sueldo=89000, anti=3, catedra="EyFCI", carrera="LCC",cargo="Jefe de Catedra", area="Estructuras", tipo="Teorica")
        d = objeto1.toJson()
        d1 = objeto2.toJson()
        d2 = objeto3.toJson()
        d3 = objeto4.toJson()
        lista = [d, d1, d2, d3]
        self.guardarJSONArchivo(lista, "Personal.json")
    def retornarObjeto(self, tipo):
        if tipo == "docente":
            objeto = Docente(cuil="15-1823791-2", apellido="Ortiz", nombre="Juan", sueldo=50000, anti=10, carrera="LSI",cargo="exclusivo", catedra="Programacion Orientada a Objetos")
        elif tipo == "investigador":
            objeto = Investigador(cuil="20-1923192-3", apellido="Dominguez", nombre="Carlos", sueldo=120000, anti=2,area="Computacional", tipo="Cientifica")
        elif tipo == "personal apoyo":
            objeto = PersonalApoyo(cuil="12-456543-4", apellido="Pereyra", nombre="Maria", sueldo=70000, anti=1,categoria=17)
        elif tipo == "docente investigador":
            objeto = DocenteInvestigador(programa="II", importe=25000, cuil="18-3446706-8", apellido="Lopez", nombre="Juan Cruz", sueldo=90000, anti=4, catedra="EyFCI", carrera="LCC",cargo="semiexclusivo", area="Estructuras", tipo="Teorica")
        else:
            objeto = None

        return objeto
    def guardarJSONArchivo(self, diccionario, archivo):
        with Path(archivo).open("w", encoding="UTF-8") as destino:
            json.dump(diccionario, destino, indent=4)
            destino.close()
    def leerJSONArchivo(self,archivo):
        with Path(archivo).open(encoding="UTF-8") as fuente:
            diccionario = json.load(fuente)
            fuente.close()
            return diccionario

    def convertirTextoADiccionario(self, texto):
        return json.loads(texto)