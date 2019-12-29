from lib.interfacesJuego.datos.ListaJugadores import ListaJugadores
from lib.interfacesJuego.datos.ListaJuegos import ListaJuegos
import sys


class GestorJuegos:
    
    def __init__(self):
        self.juego = None
        self.jugadores = ListaJugadores()
        self.juegos = ListaJuegos()

    def obtener_juegos(self):
        return self.juegos.obtener_juegos()

    def seleccionar_juego(self, juego):
        """ Selecciona uno de los juegos para jugar.
        """
        juego = self.juegos.obtener_juego(juego)
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
