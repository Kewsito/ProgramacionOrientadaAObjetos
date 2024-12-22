from claseProvincias import Provincias
from ObjectEncoder import ObjectEncoder
from VistaWeather import NewProvincia
import requests

API_KEY = "your-token"


class Manejador:
    __listaprov: list
    __provac: tuple
    __contr: ObjectEncoder

    def __init__(self, decodificador, vista):
        self.__contr = decodificador
        self.__listaprov = self.__contr.decoDiccionario
        self.vista = vista

    def setDATOS(self, provac):
        try:
            response = requests.get(
                f'https://api.openweathermap.org/data/2.5/weather?units=metric&q={provac.getNombre()}&appid={API_KEY}')
            data = response.json()
            provac.setTemperatura(data['main']['temp'])
            provac.setHumedad(data['main']['humidity'])
            provac.setSensacionT(data['main']['feels_like'])
        except:
            raise ValueError("NO SE PUDIERON OBTERNER LOS DATOS DEL CLIMA")

    def SeleccionarP(self,index):
        self.__provac=(index,self.__listaprov[index])
        self.setDATOS(self.__provac[1])
        self.vista.verProvinciaenForm(self.__provac[1])

    def borrarP(self):
        self.__listaprov.pop(self.__provac[0])
        self.vista.borrarP(self.__provac[0])
        self.grabardatos()

    def agregarP(self):
        nuevaP = NewProvincia(self.vista).show()
        if nuevaP:
            self.setDATOS(nuevaP)
            self.__listaprov.append(nuevaP)
            self.grabardatos()

    def toJSON(self):
        lista_aux = []
        for p in self.__lista_provs:
            lista_aux.append(p.toJSON())
        return lista_aux

    def grabardatos(self):
        self.__contr.guardarJSONArchivo(self.toJSON())

    def start(self):
        for i in self.__listaprov:
            self.vista.agregarP(i)
        self.vista.mainloop()
