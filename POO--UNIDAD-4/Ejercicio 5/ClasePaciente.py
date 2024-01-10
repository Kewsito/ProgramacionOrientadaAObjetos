import re


class Paciente:
    emailRegex = re.compile(r"[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}")
    telefonoRegex = re.compile(r"\([0-9]{3}\)[0-9]{7}")
    __nombre: str
    __apellido: str
    __telefono: str
    __email: str
    __altura: float
    __peso: float

    def __init__(self, apellido, nombre, email, telefono, altura, peso):
        self.__nombre = self.requerido(nombre, "El nombre es requerido")
        self.__apellido = self.requerido(apellido, "El apellido es requerido")
        self.__telefono = self.formatoValido(telefono, Paciente.telefonoRegex, 'Telefono no tiene formato correcto')
        self.__email = self.formatoValido(email, Paciente.emailRegex,'Email no tiene formato correcto')
        self.__altura = self.requerido(altura, "La altura es requerida")
        self.__peso = self.requerido(peso, "El peso es requerido")



    def getNombre(self):
        return self.__nombre

    def getApellido(self):
        return self.__apellido

    def getTel(self):
        return self.__telefono

    def getEmail(self):
        return self.__email

    def getAltura(self):
        return self.__altura

    def getPeso(self):
        return self.__peso


    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                    apellido=self.__apellido,
                    nombre=self.__nombre,
                    email=self.__email,
                    telefono=self.__telefono,
                    altura=self.__altura,
                    peso=self.__peso,
                    )
            )
        return d


    def requerido(self, valor, mensaje):
        if not valor:
            raise ValueError(mensaje)
        return valor

    def formatoValido(self, valor, regex, mensaje):
        if not valor or not regex.match(valor):
            raise ValueError(mensaje)
        return valor


    def calcularIMC(self):
        peso = float(self.__peso)
        altura = float(self.__altura)
        IMC = round(peso / altura**2, 2)
        if IMC < 18.5:
            mensaje = "Peso inferior al normal - IMC: {}".format(IMC)
        elif 18.5 <= IMC < 25:
            mensaje = "Peso normal - IMC: {}".format(IMC)
        elif 25 <= IMC < 30:
            mensaje = "Peso superior al normal - IMC: {}".format(IMC)
        else:
            mensaje = "Obesidad - IMC:{}".format(IMC)
        return mensaje
