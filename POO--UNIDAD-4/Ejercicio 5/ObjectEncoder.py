from ClasePaciente import Paciente
import json
from pathlib import Path

class ObjectEncoder:
    __lista: list
    __archivo : str

    def __init__(self, archivo):
        self.__lista = []
        self.__archivo = archivo


    def decodificarDiccionario(self):
        diccionario = self.leerJSONArchivo()
        for elem in diccionario:
            if '__class__' not in elem:
                raise TypeError('Diccionario no válido')
            else:
                class_name=elem['__class__']
                class_=eval(class_name)
                objeto = class_(**elem["__atributos__"])
                self.__lista.append(objeto)
        return self.__lista



    def guardarJSONArchivo(self, diccionario):
        with Path(self.__archivo).open("w", encoding="UTF-8") as destino:
            json.dump(diccionario, destino, indent=4)
            destino.close()

    def leerJSONArchivo(self):
        with Path(self.__archivo).open(encoding="UTF-8") as fuente:
            diccionario = json.load(fuente)
            fuente.close()
            return diccionario

    def convertirTextoADiccionario(self, texto):
        return json.loads(texto)
