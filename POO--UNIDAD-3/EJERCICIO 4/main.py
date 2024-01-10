from ManejadorCalefactores import manejadorcalefactores

if __name__ == "__main__":
    m = manejadorcalefactores()
    m.CargaCalefactorAGas()
    m.CargaCalefactorElectrico()
    m.mostrar()
    opc = int(input(
        "Ingrese una opcion \n\t 1- Ingresar por teclado el  costo por m3 y cantidad que se estima consumir en m3 y mostrar marca y modelo del calefactor a gas natural de menor costo de consumo. \n\t 2- Ingresar por teclado el costo de el kilowatt/h, la cantidad que se estima consumir por hora y mostrar  marca  y modelo del calefactor eléctrico de menor consumo.\n\t 3- Teniendo en cuenta los dos ítems anteriores, muestre: tipo de calefactor y todos los datos del calefactor de menor consumo. \n\t"))
    while opc != 0:
        if opc == 1:
            costo = int(input("Ingrese costo por m3 \n"))
            consumo = int(input("ingrese cantidad a consumir \n"))
            posgas=m.itemd1(costo, consumo)
        elif opc == 2:
            costo = int(input("Ingrese costo por m3 \n"))
            consumo = int(input("ingrese cantidad a consumir \n"))
            posel=m.itemd2(costo, consumo)
        elif opc == 3:
            m.mostrarcalefactor(posel,posgas)
        opc = int(input(
            "Ingrese una opcion \n\t 1- Ingresar por teclado el  costo por m3 y cantidad que se estima consumir en m3 y mostrar marca y modelo del calefactor a gas natural de menor costo de consumo. \n\t 2- Ingresar por teclado el costo de el kilowatt/h, la cantidad que se estima consumir por hora y mostrar  marca  y modelo del calefactor eléctrico de menor consumo.\n\t 3- Teniendo en cuenta los dos ítems anteriores, muestre: tipo de calefactor y todos los datos del calefactor de menor consumo. \n\t"))
