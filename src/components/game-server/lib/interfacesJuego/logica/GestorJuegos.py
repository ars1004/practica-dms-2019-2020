from lib.interfacesJuego.datos.ListaJugadores import ListaJugadores
from lib.interfacesJuego.logica.JuegoDamas import JuegoDamas
from lib.interfacesJuego.logica.JuegoEnRaya import JuegoEnRaya
import sys


class GestorJuegos:
    """ Contiene una lista de juegos que se pueden juegar.
    Cada juego esta en un diccionario donde la clave es el nombre y el
    valor es la clase del juego.
    Para añadir un juego a la lista se importa la clase que hereda de logica.Juego
    y se añade al diccionario con el nombre del juego.
    Ejemplo:
        'from logica.JuegoGo import JuegoGo'


        'self.dict_juegos = {
        ...
        "Go": JuegoGo,
        ...
        }'

    """

    def __init__(self):
        self.dict_juegos = {
            "Damas": JuegoDamas,
            "Tres en raya": JuegoEnRaya
        }
        self.juego = None
        self.jugadores = ListaJugadores()

    def obtener_juegos(self):
        """ Obtiene la lista de juegos disponibles.
        """
        return list(self.dict_juegos.keys())

    def seleccionar_juego(self, juego):
        """ Selecciona uno de los juegos para jugar.
        """
        juego = self.dict_juegos[juego]
        self.juego = juego([1, 2])
        self.jugadores.vaciar()

    def añadir_jugador(self, token):
        jugador = self.juego.crearJugador()
        self.jugadores.añadir_jugador(token, jugador)
        return jugador.returnId()

    def hacer_movimiento(self, movimiento, token):
        jugador = self.jugadores.obtener_jugador(token)
        self.juego.hacer_movimiento(movimiento, jugador.returnId())

    def obtener_estado(self):
        return self.juego.obtener_estado()
