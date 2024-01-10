from ManejadorCamas import ManejadorCamas
from ManejadorMedicamentos import manejadorMedicamentos
if __name__=='__main__':
    camas=ManejadorCamas()
    camas.CrearCamas()
    medicamento=manejadorMedicamentos()
    medicamento.CrearMedicamento()
    op=int(input("Ingrese una opcion\n 1 - Mostrar pacientes \n 2 - Mostrar Medicamentos \n 3 - Listar datos de pacientes y medicamentos que debe devolver \n 4 - Datos de pacientes internados dado un diagnostico \n 0 - Salir \n"))
    while op!=0:
        if op==1:
            camas.show()
        elif op==2:
            medicamento.show()                    
        elif op==3:
            nap=str(input("Ingrese nombre y apellido del paciente \n"))
            i=camas.op3(nap)
            fecha=str(input("Ingrese la fecha de alta del paciente \n"))
            camas.AltaPaciente(fecha, i)
            print("||[DATOS DEL PACIENTE]|| \n")
            idcama=camas.mostrarDatos(i)
            medicamento.getMedicamentos(idcama)
        elif op==4:
            op4=str(input("Ingrese el diagnostico \n"))
            print("{}".format(op4))
            camas.PacientesDiag(op4)
        op=int(input("Ingrese una opcion\n 1 - Mostrar pacientes \n 2 - Mostrar Medicamentos \n 3 - Listar datos de pacientes y medicamentos que debe devolver \n 4 - Datos de pacientes internados dado un diagnostico \n 0 - Salir \n"))
        
