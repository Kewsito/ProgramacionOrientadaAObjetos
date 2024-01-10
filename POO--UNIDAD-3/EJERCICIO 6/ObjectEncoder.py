from pathlib import Path
from ClaseHeladera import Heladera
from ClaseLavarropas import Lavarropas
from ClaseTelevisor import Televisor

import json


class ObjectEncoder:

    def cargarAparato(self):
        lista = []

        op = None
        while op != 0:
            op = int(input("""
Ingrese [1]: Cargar Heladeras
Ingrese [2]: Cargar Televisor
Ingrese [3]: Cargar Lavarropa
Ingrese [0]: Para Finalizar
Ingrese Opcion-> """
                           ))
            if op != 0:
                marca = input("Ingrese la marca: ")
                modelo = input("Ingrese el modelo: ")
                color = input("Ingrese el color: ")
                paisfab = input("Ingrese el pais de fabricacion: ")
                precio = float(input("Ingrese el precio: "))

            if op == 1:  # cargar Heladera
                capl = float(input("Ingrese la capacidad en litros: "))
                tipo = input("Ingrese el tipo: ")
                if tipo == "Freezer":
                    freezer = True
                    ciclica = False
                elif tipo == "Ciclica":
                    ciclica = True
                    freezer = False
                else:
                    freezer = False
                    ciclica = False

                h = Heladera(marca, modelo, color, paisfab, precio, capl, freezer, ciclica).toJSON()
                lista.append(h)

            elif op == 2:  # cargar televisor
                tipop = input("Ingrese tipo de pantalla: ")
                pulg = input("Ingrese las pulgadas: ")
                tipod = input("Ingrese el tipo de definicion: ")
                valor = input("Tiene conexion a internet (Si/No): ")
                if valor == "Si":
                    conex = True
                else:
                    conex = False

                t = Televisor(modelo, color, paisfab, precio, tipop, pulg, tipod, conex, marca).toJSON()
                lista.append(t)

            elif op == 3:  # cargar lavarropa
                caplav = input("Ingrese la capacidad de lavado: ")
                velcent = input("Ingrese la velocidad de centrifugado: ")
                cantp = input("Ingrese la cantidad de programas: ")
                tipop = input("Ingrese el tipo de carga: ")

                l = Lavarropas(marca, modelo, color, paisfab, precio, caplav, velcent, cantp, tipop).toJSON()
                lista.append(l)
            elif op == 0:
                op = 0
                print("Fin")

        self.guardarJSONArchivo(lista, "aparatos2.json")

    def guardarJSONArchivo(self, lista, archivo):
        with Path(archivo).open("w", encoding="UTF-8") as destino:
            json.dump(lista, destino, indent=4)
            destino.close()

    # para decodificar el archivo json
    def leerJSON(self, archivo):
        with Path(archivo).open(encoding="UTF-8") as fuente:
            diccionario = json.load(fuente)
            fuente.close()
            return diccionario

    def cargarobjeto(self, claselista):
        listadicc = self.leerJSON("aparatos.json")

        for elem in listadicc:
            if "__class__" not in elem:
                print("No se encuentra la clase")
            else:
                class_name = elem["__class__"]
                class_ = eval(class_name)
                print(class_name)

                if class_name == "Heladera":
                    atributos = elem["__atributos__"]
                    H = class_(**atributos)
                    claselista.agregarAparato(H)
                elif class_name == "Televisor":
                    atributos = elem['__atributos__']
                    T = class_(**atributos)
                    claselista.agregarAparato(T)
                elif class_name == "Lavarropa":
                    atributos = elem['__atributos__']
                    L = class_(**atributos)
                    claselista.agregarAparato(L)

    def retornarobjeto(self, tipo):

        marca = input("Ingrese la marca: ")
        modelo = input("Ingrese el modelo: ")
        color = input("Ingrese el color: ")
        pais = input("Ingrese el pais de fabricacion: ")
        precio = float(input("Ingrese el precio: "))

        if tipo == "Heladera":
            capl = float(input("Ingrese la capacidad en litros: "))
            tipo = input("Ingrese el tipo: ")
            if tipo == "Freezer":
                freezer = True
                ciclica = False
            elif tipo == "Ciclica":
                ciclica = True
                freezer = False
            else:
                freezer = False
                ciclica = False

            objeto = Heladera(marca, modelo, color, pais, precio, capl, freezer, ciclica)
        elif tipo == "Lavarropa":
            caplav = input("Ingrese la capacidad de lavado: ")
            velcent = input("Ingrese la velocidad de centrifugado: ")
            cantp = input("Ingrese la cantidad de programas: ")
            tipop = input("Ingrese el tipo de carga: ")

            objeto = Lavarropas(marca, modelo, color, pais, precio, caplav, velcent, cantp, tipop)
        elif tipo == "Televisor":
            tipop = input("Ingrese tipo de pantalla: ")
            pulg = input("Ingrese las pulgadas: ")
            tipod = input("Ingrese el tipo de definicion: ")
            valor = input("Tiene conexion a internet (Si/No): ")
            if valor == "Si":
                conex = True
            else:
                conex = False

            objeto = Televisor(marca, modelo, color, pais, precio, tipop, pulg, tipod, conex)
        else:
            objeto = None
            print("El tipo ingresado es incorrecto")

        return objeto
