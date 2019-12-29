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
        print("hola", file=sys.stderr)
        player = self.arbitro.jugadorTurno
        print(player, file=sys.stderr)
        tablero = self.tablero
        print(tablero, file=sys.stderr)
        acabado = self.arbitro.estaAcabado()
        print(acabado, file=sys.stderr)
        return player, tablero, acabado
