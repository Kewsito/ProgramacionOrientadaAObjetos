import tkinter as tk
from tkinter import messagebox
from claseProvincias import Provincias


# CLASE CON EL LISTADO DE PROVINCIAS
class ProvinciaList(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master)
        self.lb = tk.Listbox(self, **kwargs)
        scroll = tk.Scrollbar(self, command=self.lb.yview)
        self.lb.config(yscrollcommand=scroll.set)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.lb.pack(side=tk.RIGHT, fill=tk.BOTH, expand=1)

    # AGREGA PROVINCIA A LA LISTA
    def insertar(self, provincia, index=tk.END):
        text = "{}".format(provincia.getNombre())
        self.lb.insert(index, text)

    # BORRAR PROVINCIA DE LA LISTA
    def borrar(self, index):
        self.lb.delete(index, index)

    # MUESTRA PROVINCIA CON DOBLE CLICK
    def bind_doble_click(self, callback):
        handler = lambda _: callback(self.lb.curselection()[0])
        self.lb.bind("<Double-Button-1>", handler)


# CLASE CON FORMULARIO DE PROVINCIA
class ProvinciaForm(tk.LabelFrame):
    fields = {"NOMBRE", "CAPITAL", "CANTIDAD DE HABITANTES", "CANTIDAD DE DEPARTAMENTOS/PARTIDOS", "TEMPERATURA",
              "SENSACION TERMICA", "HUMEDAD"}

    def __init__(self, master, **kwargs):
        super().__init__(master, text="PROVINCIA", padx=10, pady=10, **kwargs)
        self.frame = tk.Frame(self)
        self.entries = list(map(self.crearCampo, enumerate(self.fields)))
        self.frame.pack()

    # MUESTRA DATOS DE LA PROVINCIA
    def crearCampo(self, field):
        position, text = field
        label = tk.Label(self.frame, text=text)
        entry = tk.Label(self.frame, width=20)
        label.grid(row=position, column=0, pady=5)
        entry.grid(row=position, column=1, pady=5)
        return entry

    # OBTIENE DATOS DE FORMULARIO

    def mostrarestadoPenForm(self):
        values = [e.get() for e in self.entries]
        prov = None
        try:
            prov = Provincias(*values)
        except ValueError as e:
            messagebox.showerror("Error de validacion", str(e), parent=self)
        self.limpiar()
        return prov

    # LIMPIAR CAMPOS DE FORMULARIO
    def limpiar(self):
        for entry in self.entries:
            entry.delete(0, tk.END)


# CLASE PARA CREAR UNA PROVINCIA
class ProvinciaCreateForm(tk.LabelFrame):
    fields = ("Nombre", "Capital", "Cantidad de Habitantes", "Cantidad de departamentos/partidos")

    def __init__(self, master, **kwargs):
        super().__init__(master, text="Provincia", padx=10, pady=10, **kwargs)
        self.frame2 = tk.Frame(self)
        self.entries = list(map(self.crearCampo, enumerate(self.fields)))
        self.frame2.pack()

    # Defino los campos del formulario para luego mostrar los datos de la provincia
    def crearCampo(self, field):
        position, text = field
        label = tk.Label(self.frame2, text=text)
        entry = tk.Entry(self.frame2, width=25)
        label.grid(row=position, column=0, pady=5)
        entry.grid(row=position, column=1, pady=5)
        return entry

    # obtiene los valores de los campos del formulario para crear una nueva provincia
    def crearProvinciaDesdeFormulario(self):
        values = [e.get() for e in self.entries]
        weather = None
        try:
            weather = Provincias(*values)
        except ValueError as e:
            messagebox.showerror("Error de Validación", str(e), parent=self)
        self.limpiar()
        return weather

    def limpiar(self):
        for entry in self.entries:
            entry.delete(0, tk.END)


# CREA PROVINCIA EN UNA VENTANA EMERGENTE
class NewProvincia(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.Weather = None
        self.form = ProvinciaForm(self)
        self.btn_add = tk.Button(self, text="CONFIRMAR", command=self.confirmar)
        self.form.pack(padx=10, pady=10)
        self.btn_add.pack(pady=10)

    # CONFIRMA CREACION DE PROVINCIA
    def confirmar(self):
        self.Provincia = self.form.crearProvinciaDesdeFormulario()
        if self.Provincia:
            messagebox.showinfo("AVISO", str("Provincia añadida correctamente"), parent=self)
            self.destroy()

    # Funcion para obtener la provincia creada
    def show(self):
        self.grab_set()  # Ventana emergente que permite interactuar con ella sin actuar sobre la principal
        self.wait_window()
        return self.Provincia

    # VISTA GENERAL DE PROVNCIAS


class ProvinciaView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Lista de Weathers")
        self.list = ProvinciaList(self, height=15)
        self.form = ProvinciaForm(self)
        self.list.pack(side=tk.LEFT, padx=10, pady=10)
        self.form.pack(padx=10, pady=10)

        self.btn_new = tk.Button(self, text="AGREGAR PROVINCIA")
        self.btn_new.pack(side=tk.BOTTOM, pady=5)

        self.btn_new2 = tk.Button(self, text="ELIMINAR PROVINCIA")
        self.btn_new2.pack(side=tk.BOTTOM, pady=5)

    def setControlador(self, ctrl):
        self.ctrl = ctrl
        self.btn_new.config(command=self.ctrl.SeleccionarP)
        self.list.bind_doble_click(self.ctrl.SeleccionarP)
        self.btn_new2.config(command=self.ctrl.borrarP)
        self.btn_new2.config(state=tk.DISABLED)

    def agregarProvincia(self, Weather):
        self.list.insertar(Weather)

    def borrarProvincia(self, index):
        self.form.limpiar()
        self.list.borrar(index)
        self.btn_new2.config(state=tk.DISABLED)
        messagebox.showinfo("AVISO", str("PROVINCIA ELIMINADA CORRECTAMENTE"), parent=self)

    def verProvinciaEnForm(self, Weather):
        self.btn_new2.config(state=tk.NORMAL)
        self.form.mostrarestadoPenForm(Weather)
