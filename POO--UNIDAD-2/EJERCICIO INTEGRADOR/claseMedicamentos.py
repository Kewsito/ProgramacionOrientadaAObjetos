class Medicamento:
    __idCama: int
    __idMedicamento: int
    __nomComercial:str
    __monodroga:str
    __presentacion:str
    __cant_ap:str
    __precioTot:float

    def __init__(self,idCama,idMedicamento,nomComercial,monodroga,presentacion,cant_ap,precioTot):
        self.__idCama=int(idCama)
        self.__idMedicamento=int(idMedicamento)
        self.__nomComercial=str(nomComercial)
        self.__monodroga=str(monodroga)
        self.__presentacion=str(presentacion)
        self.__cant_ap=str(cant_ap)
        self.__precioTot=float(precioTot)
    
    def getIdCama(self):
        return self.__idCama
    
    def getIdMedicamento(self):
        return self.__idMedicamento
    
    def getNomComercial(self):
        return self.__nomComercial
    
    def getmonodroga(self):
        return self.__monodroga
    
    def getpresentacion(self):
        return self.__presentacion
    
    def getCantap(self):
        return self.__cant_ap
    
    def getPrecioTot(self):
        return self.__precioTot
    
    def __str__(self):
        return ("Id. Cama: {} || Id. Medicamento: {} || Nombre Comercial: {} || Monodroga: {} || Presentacion: {} || Cantidad Aplicada: {} || Precio total: {}".format(self.__idCama,self.__idMedicamento,self.__nomComercial,self.__monodroga,self.__presentacion,self.__cant_ap,self.__precioTot))
    