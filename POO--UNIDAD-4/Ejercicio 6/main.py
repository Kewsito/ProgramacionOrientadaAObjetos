from ManejadorWeather import Manejador
from VistaWeather import ProvinciaView
from ObjectEncoder import ObjectEncoder

if __name__ == '__main__':
    conn = ObjectEncoder("weather.json")
    vista = ProvinciaView()
    ManejadorClima = Manejador(conn, vista)
    vista.setControlador(ManejadorClima)
    ManejadorClima.start()
