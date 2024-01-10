"""""
Se necesita desarrollar una aplicación que procese la información de las variables meteorológicas temperatura, humedad y presión atmosférica. El registro de estas variables se hace cada una hora durante todos los días del mes. Esto se guarda en un archivo de texto separado con coma que contiene los siguientes datos: número de día, hora, valor de la variable temperatura, valor de la variable humedad y valor de la variable presión atmosférica. Se genera un archivo por cada mes.
Defina la clase “Registro” que posea como atributos los valores de las tres variables meteorológicas que se registran.
Implemente un programa que:
1.    Defina una lista bidimensional en la que se almacene el registro de las variables meteorológicas (instancia de la clase Registro) para cada día del mes, por cada hora.
2.    Almacene en la lista bidimensional los datos registrados en el archivo.
3.    Presente un menú de opciones permita realizar las siguientes tareas:

3.1.        Mostrar para cada variable el día y hora de menor y mayor valor.

3.2.        Indicar la temperatura promedio mensual por cada hora.

3.3.        Dado un número de día listar los valores de las tres variables para cada hora del día dado. El listado debe tener el siguiente formato.
"""""
#from atexit import register

from menu import Menu1
from claseRegistro import Registro
import csv
def mayorTemp(lista):
    max=-9999
    for i in lista:
        for j in lista[i]:
            if lista[i][j].gettemp()>max:
                max=lista[i][j].gettemp()
                dia= i
                hora= j
    print("Dia:",dia+1,"Hora:",hora+1,"Temperatura:",max)
def mostrarlista(lista):
    for i in range(30):
        print("Dia:",i+1)
        for j in range(24):
            print("Hora:",j+1)
            print ("Humedad:",lista[i][j].gethum()," Presion:",lista[i][j].getpres()," Temperatura:",lista[i][j].gettemp())
        print("------------------------------------------------------------------------")
if __name__=="__main__":
    lista = []
    archivo=open("VariablesdelMes.csv")
    reader=csv.reader(archivo,delimiter=",")
    next(reader) #PUNTERO?

    for i in range(30): #Agrego 30 filas
        lista.append([Registro(0,0,0)]*24) #Agrego 24 columnas?
    for fila in reader:
        dia=int(fila[0])
        hora=int(fila[1])
        p=Registro(fila[2],fila[3],fila[4])
        lista[dia-1][hora-1]=p
    mostrarlista(lista)
    #Comienzo modulo menu.py
    Menu1(lista)