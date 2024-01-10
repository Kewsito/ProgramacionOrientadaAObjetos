class Ventana:
    __titulo=''
    __XvsI=0
    __YvsI=0
    __XvinfD=0
    __YvinfD=0

    def __init__(self,titulo,XI=0,YI=0,XD=500,YD=500):
        self.__titulo=titulo
        self.__XvsI=XI
        self.__YvsI=YI
        self.__XvinfD=XD
        self.__YvinfD=YD
        if XI < 0 or YI<0 or XD > 500 or YD > 500 or XI>=XD or YI >= YD:
            print("ERROR AL CARGAR LOS DATOS")

    def mostrar(self):
        return print("Titulo:",self.__titulo," \n Vertice Superior Izquierdo: VI = (",self.__XvsI,",",self.__YvsI,") \n Vertice Inferior Derecho: VD = (",self.__XvinfD,",",self.__YvinfD,")")
    def moverDerecha(self,pos=1):
        if self.__XvinfD+pos>=0:
            self.__XvinfD+=pos
        if self.__XvsI+pos<=500:
            self.__XvsI+=pos
    def moverIzquierda(self,pos=-1):
        if self.__XvinfD-pos>=0:
            self.__XvinfD-=pos
        if self.__XvsI-pos<=500:
            self.__XvsI-=pos
    def subir(self,pos=1):
        if self.__YvinfD+pos>=0:
            self.__YvinfD+=pos
        if self.__YvsI+pos<=500:
            self.__YvinfD+=pos
    def bajar(self, pos=-1):
        if self.__YvinfD-pos>=0:
            self.__YvinfD-=pos
        if self.__YvsI-pos>=500:
            self.__YvsI-=pos
    def alto(self):
        return self.__YvinfD-self.__YvsI
    def ancho(self):
        return self.__XvinfD-self.__XvsI
    def getTitulo(self):
        return print("Titulo:",self.__titulo)
