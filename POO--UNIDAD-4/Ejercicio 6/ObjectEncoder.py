import json
from pathlib import Path


class ObjectEncoder:
    __lista: list
    __arch: str

    def __init__(self, arch):
        self.__lista = []
        self.__arch = arch

    def decoDiccionario(self):
        dicc = self.leerJSONArchivo()
        print(dicc)
        for elem in dicc:
            if "__class__" not in elem:
                print("NO SE ENCUENTRA EL DICCIONARIO")
            else:
                class_name = elem['__class__']
                class_ = eval(class_name)
                objeto = class_(**elem(['__atributos__']))
                self.__lista.append(objeto)
            return self.__lista

    def guardarJSONArchivo(self, dicc):
        with Path(self.__arch).open("w", encoding="UTF-8") as destino:
            json.dump(dicc, destino, indent=4)
            destino.close()

    def leerJSONArchivo(self):
        with Path(self.__arch).open(encoding="UTF-8") as fuente:
            dicc = json.load(fuente)
            fuente.close()
            return dicc
