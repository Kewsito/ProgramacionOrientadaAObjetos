from claseEmail import Email
def fun4(adress):
    lista=[]
    for i in range(len(adress)):
        ad=Email("","","","")
        ad.crearCuenta(adress[i])
        lista.append(ad) 
    busca = input("Ingrese ID a buscar:")
    b=0
    for ad in lista:
        #print(ad.retornarEmail()) 
        if  ad.idCuenta == busca:
            b=1
    if b==1:
        print ("El ID ingresado se encuentra repetido")
    else: 
        print ("No se encuentra el ID ingresado")