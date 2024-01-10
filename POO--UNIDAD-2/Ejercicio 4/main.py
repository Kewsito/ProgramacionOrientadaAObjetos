"""""
Métodos y Constructores con valores por defecto
Defina una clase Ventana con los siguientes atributos: título, valor de las coordenadas x e y del vértice superior izquierdo y valor de las coordenadas x e y del vértice inferior derecho. Implemente los métodos necesarios, para que pueda ejecutarse el programa dado.
Reglas de negocio:
El menor valor para las coordenadas del vértice superior izquierdo es 0 para cada una.
El mayor valor para las coordenadas del vértice inferior derecho es 500 para cada una.
El desplazamiento por defecto de una ventana es en una unidad en la dirección correspondiente.
El valor de x del vértice superior izquierdo siempre debe ser menor al valor de x del vértice inferior derecho.
El valor de y del vértice superior izquierdo siempre debe ser menor al valor de y del vértice inferior derecho.
"""
from re import X
import xdrlib
from claseVentana import Ventana

if __name__ ==  '__main__':

    print('==== Ventana Inicio ====')

    ventanaInicio= Ventana('Inicio')

    ventanaInicio.mostrar()

    print('Ventana: {} Alto: {} Ancho: {}'.format(ventanaInicio.getTitulo(),ventanaInicio.alto(),ventanaInicio.ancho()))

    print('==== Ventana Cargar ====')

    ventanaCargar= Ventana('Cargar',10,20)

    ventanaCargar.mostrar()

    print('*** Mueve a la derecha ***')

    ventanaCargar.moverDerecha(10)

    ventanaCargar.mostrar()

    print('*** Mueve a la izquierda ***')

    ventanaCargar.moverIzquierda(10)

    ventanaCargar.mostrar()

    print('*** Bajar ***')

    ventanaCargar.bajar(10)

    ventanaCargar.mostrar()

    print('==== Ventana Borrar ====')

    ventanaBorrar = Ventana('Borrar', 10,20,100,200)

    ventanaBorrar.mostrar()

    print('*** Subir ***')

    ventanaBorrar.subir(5)   

    ventanaBorrar.mostrar()

    print('*** Subir ***')

    ventanaBorrar.subir()

    ventanaBorrar.mostrar()

    print('*** Bajar ***')

    ventanaBorrar.bajar()

    ventanaBorrar.mostrar()
