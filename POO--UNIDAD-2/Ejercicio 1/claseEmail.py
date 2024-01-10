class Email:
    __idCuenta = ''
    __dominio = ''
    __tipoDominio = ''
    __contraseña = ''

    def __init__(self,idCuenta,dominio,tipoDominio,contraseña):
        self.idCuenta=idCuenta
        self.dominio=dominio
        self.tipoDomionio=tipoDominio
        self.contraseña=contraseña
    
    def getDominio(self):
        return self.__dominio

    def retornaEmail(self,name):
        return print("Estimado",name.upper(), "te enviaremos tus mensajes a la dirección: \n",self.idCuenta+"@"+self.dominio+"."+self.tipoDomionio)
        #variable + . + upper = CONVIERTE AL STRING EN MAYUSCULA
    def crearCuenta(self,correo):
        id=correo.split("@")
        dom=id[1].split(".")
        self.idCuenta=id[0]
        self.dominio=dom[0]
        self.tipoDomionio=dom[1]
        print("Email generado")
    def modcontra(self,oldpass):
        if self.__contraseña == oldpass:
            self.__contraseña= input("Ingrese nueva contraseña:")
            print("Su contraseña se modifico a: "+self.__contraseña)
        else:
            print("Contraseña incorrecta")
        