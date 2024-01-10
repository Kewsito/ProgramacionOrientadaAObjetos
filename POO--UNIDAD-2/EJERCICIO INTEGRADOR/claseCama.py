class Cama:
    __idCama: int
    __habitacion: str
    __estado: bool = None
    __nomyap : str
    __diag : str
    __fechaint: str
    __fechaalt: str = None

    def __init__(self,idCama,habitacion,estado,nomyap,diag,fechaint,fechaalt):
        self.__idCama=int(idCama)
        self.__habitacion=str(habitacion)
        self.__estado=bool(estado)
        self.__nomyap=str(nomyap)
        self.__diag=str(diag)
        self.__fechaint=str(fechaint)
        self.__fechaalt=str(fechaalt)

    def __str__(self):
        return ("Id. Cama: {} || Habitacion: {} || NyA: {} || Diagnostico: {} || Fecha de internacion: {}".format(self.__idCama,self.__habitacion,self.__nomyap,self.__diag,self.__fechaint))
    
    def getIdCama(self):
        return self.__idCama
    
    def getRoom(self):
        return self.__habitacion
    
    def getEstado(self):
        return self.__estado
    
    def getNomyap(self):
        return self.__nomyap
    
    def getDiag(self):
        return self.__diag
    
    def getFechaInt(self):
        return self.__fechaint
    
    def getFechaAlta(self):
        return self.__fechaalt
    def setAlta(self,fecha):
        self.__fechaalt=fecha
        self.__estado=False
