"""
Defina una clase “Email” con los siguientes atributos: idCuenta, dominio, tipo de dominio y contraseña (todos estos datos se ingresan por teclado). Y los siguientes métodos:
a- El constructor.
b- Método “retornaEmail()” que construye una dirección e-mail con los valores de los atributos de Email. Por ejemplo:

idCuenta.: alumnopoo
dominio: gmail
tipoDominio: com
Resultado devuelto por retornaEmail: alumnopoo@gmail.com

c- Método “getDominio()”, que retorna el dominio.

d- Método “crearCuenta(), crea una cuenta a partir de una dirección de correo que recibe como parámetro.

Implemente un programa que permita:

1- Ingresar el nombre de una persona y de su cuenta de correo, el identificador de cuenta, dominio y tipo de dominio (crear una instancia de la clase Email) y luego imprima el siguiente mensaje:

Estimado <nombre> te enviaremos tus mensajes a la dirección <dirección de correo>.

2- Para la instancia creada en el ítem anterior, modificar la contraseña, teniendo en cuenta que se debe ingresar la contraseña actual, y ésta debe ser igual a la registrada en la instancia. Luego se debe ingresar la nueva contraseña y realizar la modificación correspondiente.

3- Crear un objeto de clase Email, a partir de una dirección de correo, por ejemplo: informatica.fcefn@gmail.com, juanLiendro1957@yahoo.com, etc.

4- Leer de un archivo separado por comas 10 direcciones de e-mail, crear instancias de la clase Email; luego ingresar un identificador de cuenta e indicar si está repetido o no."""

from claseEmail import Email
from fun4 import fun4

if __name__=='__main__':
    p = Email (input ("Ingrese identificador de cuenta \n"),input ("Ingrese el dominio de la cuenta \n"),input ("Ingrese tipo de dominio de la cuenta \n"),input("Ingrese la contraseña \n")) #INGRESO DE DATOS
    nombre = input("Ingrese NOMBRE \n")
    
    p.retornaEmail(nombre)
    cuenta = Email ("","","","")
    cuenta.crearCuenta(input ("Ingrese cuenta de correo de la persona \n"))
    archivo = open("texto1.csv")
    direcciones = archivo.read().split(";")
    fun4(direcciones)
    archivo.close()
    
