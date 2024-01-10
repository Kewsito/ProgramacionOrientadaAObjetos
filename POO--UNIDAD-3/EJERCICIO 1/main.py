from ManejadorFacultades import ManejadorFacultad
if __name__=="__main__":
    m=ManejadorFacultad()
    m.cargarobjetos()
    op=int(input("Ingrese una opcion: \n\t 1-Ingresar el código  de una facultad y mostrar nombre de la facultad, nombre  y duración de cada una de las carreras que se dictan en esa facultad. \n\t 2-Dado el nombre de una carrera, mostrar código (se conforma con número de código de Facultad y código de carrera), nombre y localidad de la facultad donde esta se dicta.\n"))
    while op!=0:
        if op==1:
            m.mostrarfacultades(int(input("INGRESE CODIGO DE FACULTAD \n")))
        elif op==2:
            m.buscarnom(str(input("INGRESE NOMBRE DE LA CARRERA \n")))
            
        op=int(input("Ingrese una opcion: \n\t 1-Ingresar el código  de una facultad y mostrar nombre de la facultad, nombre  y duración de cada una de las carreras que se dictan en esa facultad. \n\t 2-Dado el nombre de una carrera, mostrar código (se conforma con número de código de Facultad y código de carrera), nombre y localidad de la facultad donde esta se dicta.\n"))
    