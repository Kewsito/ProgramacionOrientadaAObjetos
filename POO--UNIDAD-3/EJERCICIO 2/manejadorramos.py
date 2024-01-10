from ManejadorFlores import ManejaFlores
from ramos import ramos
class ManejadorRamos:
    __lista: list[ramos]
    __instancia: ManejaFlores
    def __init__(self):
        self.__lista=[]
        self.__instancia=ManejaFlores()
    def agregar_Venta(self):
        tamanos=["Pequeño","Mediano","Grande"]
        t=int(input("Ingrese un tamaño de ramo: 1 - Pequeño, 2 - Mediano, 3 - Grande: "))
        R=Ramo(tamanos[t-1])
        self.__instancia.mostrar_flores()
        F = int(input("Ingrese un numero de flor 0 para terminar: "))
        while F != 0:
            if F > -1 and F <= self.__instancia.get_Ct():
                R.agregar_flor(self.__instancia.get_flor(F-1))
            else:
                print("Numero incorrecto ingrese nuevamente")
            F = int(input("Ingrese un numero de flor 0 para terminar: "))
        self.__lista.append(R)
    def calcula_Max(self):
        for i in range(len(self.__lista)):
            flores=self.__lista[i].getFlores()
            datos={}
            for flor in flores:
                if flor.getNom() not in datos:
                    datos[flor.getNom()]=1
                else:
                    datos[flor.getNom()]+=1
            datos=sorted(datos.items(),key=lambda x:x[1],reverse=True)
            try:
                print("----5 Flores mas pedidas para el ramo {} de tamaño: {}----".format(i+1,self.__lista[i].getTam()))
                for i in range(5):
                    print("Top: {}, Nombre: {}, Cantidad: {}".format(i+1,datos[i][0],datos[i][1]))
            except Exception:
                print("Al parecer no hay 5 tipos de flores distintas en este ramo, por lo tanto no es posible realizar el top de manera correcta")
    def tipoDeRamo(self):
        tip=input("Ingrese un tipo de ramo(Pequeño-Mediano-Grande): ").lower()
        print("Flores vendidas en los ramos de tipo: {}".format(tip))
        for i in range(len(self.__lista)):
            if self.__lista[i].getTam().lower() == tip:
                print("------Ramo: {}, Tamaño: {}------".format(i + 1, tip))
                print("--Flores--")
                self.__lista[i].flores_porTam()
