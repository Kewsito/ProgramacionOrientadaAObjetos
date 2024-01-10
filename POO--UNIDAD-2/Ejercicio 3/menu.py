import claseRegistro
def mayorTemp(lista):
     maximo= -9999
     for i in range(30):
         for j in range(24):
             if lista[i][j].gettemp() > maximo:
                 maximo = lista[i][j].gettemp()
     return print("Temperatura= {}, del dia {} y hora {}" .format(maximo, i, j))
 
def menorTemp(lista):
     minimo= 9999
     for i in range(30):
         for j in range(24):
             if minimo > lista[i][j].gettemp():
                 minimo = lista[i][j].gettemp()
     return print(" Temperatura= {}, del dia {} y hora {}" .format(minimo, i, j))

def mayorHum(lista):
     max= -9999
     for i in range(30):
         for j in range(24):
             if max< lista[i][j].gethum():
                 max= lista[i][j].gethum()
     return print("Maxima Humedad= {}, del dia {} y hora {}" .format(max, i, j))
def menorHum(lista):
     min= 9999
     for i in range(30):
         for j in range(24):
             if min> lista[i][j].gethum():
                 min= lista[i][j].gethum()
     return print("Maxima Humedad= {}, del dia {} y hora {}" .format(min, i, j))
 
def mayorPres(lista):
     max= -9999
     for i in range(30):
         for j in range(24):
             if max< lista[i][j].getpres():
                 max= lista[i][j].getpres()
     return print("Maxima Presion= {}, del dia {} y hora {}" .format(max, i, j))
 
def menorPres(lista):
     min= 9999
     for i in range(30):
         for j in range(24):
             if min> lista[i][j].getpres():
                 min= lista[i][j].getpres()
     return print("Maxima Presion= {}, del dia {} y hora {}" .format(min, i, j))
 
def promedio(lista):
 
     for i in range(30):
         p=0
         for j in range(24):
             p += lista[i][j].gettemp()
         print("En la hora {}, el promedio es {:.2f}" .format(j, p/30))
 
def ejer3(lista):
     d= int(input('Ingrese dia: '))
     for j in range(24):
         print('HORA, tTEMPERATURA, tHUMEDAD, tPRESION' )
         print('t{}, t{}, t{}, t{} ' .format(j+1, lista[d-1][j].gettemp(), lista[d-1][j].gethum(), lista[d-1][j].getpres()))
     
def Menu1(lista):
    print ('\n 1. Mostrar \n\n 2. Temperatura Promedio\n \n 3. Listar valores \n \n 0. SALIR \n')
    op= int(input('Ingrese una opcion: '))
    while op!=0:
        if op == 1:
            print('TEMPERATURA \n')
            print('Maxima= \n {} \n Minima{} \n' .format(mayorTemp(lista), menorTemp(lista)))
            print('HUMEDAD \n')
            print('Maxima= \n {} \n Minima{} \n' .format(mayorHum(lista), menorHum(lista)))
            print('PRESION \n')
            print('Maxima= \n {} \n Minima{} \n' .format(mayorPres(lista), menorPres(lista)))       
        elif op== 2:
            promedio(lista)
        elif op== 3:
            ejer3(lista)
            
        print ('\n 1. Mostrar \n\n 2. Temperatura Promedio\n \n 3. Listar valores \n \n 0. SALIR \n')
        op= int(input('Ingrese una opcion: '))