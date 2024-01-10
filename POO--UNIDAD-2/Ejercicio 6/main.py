from claseViajero import Viajero
from manejador import Manejador_Viajeros
import csv

if __name__ == '__main__':
        viajero= Manejador_Viajeros()
        viajero.CargaLista()
        num= input("Ingrese un numero de un Viajero Frecuente: ")
        r= viajero.BuscarViajero(num)
        if r == -1:
            print('Numero de viajero incorrecto')
        else:
            print ('1. Consultar Cantidad de Millas \n')
            print ('2. Acumular Millas \n')
            print ('3. Canjear Millas \n')
            print ('0. Salir \n')
        
        opcion=input('Ingrese una opcion: ')
        while opcion != 0:
               
            if opcion==1:
                    print('Cantidad total de millas recorridas ', format(viajero.Op1(r)))
                   
            elif opcion==2:
                    mi= input('Ingrese cantidad de millas ')
                    print('Millas acumuladas: ', format(viajero.Op2(r)))
                    
            elif opcion==3:
                    canje= input ('Ingrese millas a canjear')
                    if canje !=0:
                        print('Nueva cantidad de millas= ', format(viajero.canjearMillas))
            else: 
                print('Opcion Incorrecta')
        
        opcion= input('Ingrese una opcion: ')