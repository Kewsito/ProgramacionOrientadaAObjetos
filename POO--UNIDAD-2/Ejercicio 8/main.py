
'''Sobrecarga de operadores

Defina una clase “Conjunto” que represente un conjunto matemático de números enteros.

Implemente un programa que presente un menú de opciones que permita lo siguiente:

1- La unión de dos conjuntos, para ello sobrecargue el operador binario suma (+). Teniendo en cuenta que la unión es un nuevo conjunto que posee los elementos de ambos conjuntos, en caso de haber elementos repetidos solo aparecen una vez en el resultado. Ejemplo: Sea A={1,2,3,4} y B= {3,6,9}, A+B = {1,2,3,4,6,9}

2- La diferencia de dos conjuntos, para ello sobrecargue el operador binario resta (-). Teniendo en cuenta que el resultado de la diferencia de conjuntos es un nuevo conjunto que posee los elementos del primer operando que no se encuentren en el segundo operando. Ejemplo: Sea A={1,2,3,4} y B= {3,6,9}, A-B = {1,2}

3- Verificar si dos conjuntos son iguales, para ello sobrecargue el operador “==” teniendo en cuenta que dos conjuntos se consideran iguales si tienen la misma cantidad de elementos y sus valores son iguales (sin importar el orden de los elementos).'''

from claseConjunto import Conjunto
if __name__=='__main__':
    A=Conjunto([1,2,3,4])
    B=Conjunto([1,2,3,4])
    print("Conjunto A: \n {}".format(A))
    print("Conjunto B: \n {}".format(B))
    opc=int(input("INGRESE UNA OPCION \n 1- Union de conjuntos \n 2- Diferencia de conjuntos.\n 3- Igualdad de conjuntos \n 0- Salir \n"))
    while opc != 0:
        if opc==1:
            print("A + B = {}".format(A+B))
        elif opc==2:
            print("A - B = {}".format(A-B))
        elif opc==3:
            print("A == B = {}".format(A==B))
        opc=int(input("INGRESE UNA OPCION \n 1- Union de conjuntos \n 2- Diferencia de conjuntos.\n 3- Igualdad de conjuntos \n 0- Salir \n"))
        
