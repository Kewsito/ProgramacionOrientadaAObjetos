

class flores:
    __num: int
    __nom: str
    __color:str
    __desc:str
    
    def __init__(self,num,nom,col,desc):
        self.__color=str(col)
        self.__nom=str(nom)
        self.__num=int(num)
        self.__desc=str(desc)
    
    def __str__(self):
        return (f"Nombre: {} Numero: {} Color: {} Descripcion: {}".format(self.__nom,self.__num,self.__color,self.__desc))
        