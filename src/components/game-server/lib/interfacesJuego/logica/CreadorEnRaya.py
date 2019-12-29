"""
Creador del juego Tres en Raya
Se encarga de llevar el tablero y crear el arbitro
"""
from lib.interfacesJuego.logica.Creador import Creador
from lib.interfacesJuego.datos.TableroEnRaya import TableroEnRaya
from lib.interfacesJuego.logica.ArbitroEnRaya import ArbitroEnRaya
import sys


class CreadorEnRaya(Creador):

    def __init__(self, tamaño, jugadores):
        self.adjudicarTamaño(tamaño)
        self.tablero = self.crearTablero(self.tamaño)
        self.jugadores = jugadores
        self.arbitro = ArbitroEnRaya(self.board, self.jugadores)

    def adjudicarTamaño(self, size):
        super().adjudicarTamaño(size)

    def crearTablero(self, tamaño):
        self.board = TableroEnRaya(tamaño)
        grid = self.board.devolverTablero()
        return grid

    def obtenerEstado(self):
        player = self.arbitro.jugadorTurno
        tablero = self.tablero
        acabado = self.arbitro.estaAcabado()
        return player, tablero, acabado
