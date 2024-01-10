class Fraccion:
    __numerador: int
    __denominador: int

    def __init__(self, num, den=1):
        self.__numerador= int(num)
        self.__denominador= int(den)
        self.simplificar()
    
    def simplificar(self):
        for i in range(2, self.__numerador):
            if self.__numerador % i == 0 and self.__denominador % i == 0:
                print(i)
                self.numerador = self.numerador // i
                self.denominador = self.denominador // i
        
    
    def __str__(self):
        num=0
        if self.__numerador!=num:
            numero= str(self.__numerador) + '/' + str(self.__denominador)
        if self.__denominador==1:
            numero= str(self.__numerador)

        
        return numero

    def __add__(self, otro):
        self.__numerador= self.__numerador* otro.__denominador + self.__denominador*otro.__numerador
        self.__denominador= self.__denominador*otro.__denominador
        self.simplificar()
        return self

    def __sub__(self, otro):
        self.__numerador= self.__numerador* otro.__denominador - self.__denominador*otro.__numerador
        self.__denominador= self.__denominador*otro.__denominador
        self.simplificar()
        return self
    
    def __mul__(self, otro):
        self.__numerador= self.__numerador*otro.__numerador
        self.__denominador= self.__denominador*otro.__denominador
        self.simplificar()
        return self
    
    def __truediv__(self, otro):
        self.__numerador= self.__numerador * otro.__denominador
        self.__denominador= self.__denominador * otro.__numerador
        self.simplificar()
        return self
    
    def getnumerador(self):
        return self.__numerador
    
    def getdenominador(self):
        return self.__denominador



    