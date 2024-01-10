from Menu import Menu
if __name__ == "__main__":
    m = Menu()
    bandera = True
    usuario = (input("Ingrese el usuario (Director/Tesorero) - (FIN para terminar): ")).lower()
    while bandera is True:
        contra = input("Ingrese la contraseña: ")
        if usuario == "tesorero" and contra == "uTesoreso/ag@74ck":
            m.menuTesorero(usuario)
        elif usuario == "director" and contra == "uDirector/ufC77#!1":
            m.menuDirector(usuario)
        else:
            print("Contraseña/Usuario Incorrecto o intenta salir del programa al inicio del mismo")
        usuario = input("Ingrese el usuario (Director/Tesorero) - (FIN para terminar): ")
        if usuario.lower() == "fin":
            bandera = False