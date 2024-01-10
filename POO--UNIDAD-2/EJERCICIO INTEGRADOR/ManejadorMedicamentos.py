from claseMedicamentos import Medicamento
import csv
class manejadorMedicamentos:
    __arreglo: list
    
    def __init__(self):
        self.__arreglo=self.CrearMedicamento()
        
    def CrearMedicamento(self):
        lista=[]
        archivo= open("medicamentos.csv")
        reader=csv.reader(archivo,delimiter=";")
        next(reader,None)
        for fila in reader:
            c=Medicamento(fila[0], fila[1],fila[2],fila[3],fila[4],fila[5],fila[6])
            lista.append(c)
        archivo.close()
        return lista
    
    def getMedicamentos(self,idcama):
        acu=0
        print("Medicamento/monodroga \t Presentacion \t Cantidad \t\t Precio")        
        for i in range(len(self.__arreglo)):
            if idcama==self.__arreglo[i].getIdCama():
                print("{}/{} \t\t\t {} \t\t {} \t\t\t {}".format(self.__arreglo[i].getIdMedicamento(),self.__arreglo[i].getmonodroga(),self.__arreglo[i].getpresentacion(),self.__arreglo[i].getCantap(),self.__arreglo[i].getPrecioTot()))
                acu+=self.__arreglo[i].getPrecioTot()
        print("Total adeudado: \t\t\t\t\t\t\t\t\t\t |[{}]|".format(acu))        
        
    def show(self):
        for i in range(len(self.__arreglo)):
            print(self.__arreglo[i])
            print("-"*30)
    